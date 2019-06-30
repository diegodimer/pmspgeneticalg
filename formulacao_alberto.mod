#!/usr/bin/env glpsol

set K; #conjunto de máquinas K = 1...m

set I; # i = 0, ... n; # conjunto de tarefas
set J; # j = 1, ... n;

param P {j in J, k in K};         # Processing time of job j on machine k
param S {i in I, j in J, k in K}; # Sequence-dependent setup time to process job j after job i on machine k

# @alberto Troquei o "j in I" para "j in J",
# assim fica uniforme com o resto do modelo.
param G {i in I, j in J, k in K} := P[j,k] + S[i,j,k];  

param V := 1000000; # valor muito grande

var x {i in I, j in I, k in K} binary; # 1 se job j é escalonado diretamente depois do job i na máquina k, 0 caso contrário

var c {j in I} >= 0 integer; # tempo em que o job j foi completo

var cmax >= 0 integer; # job com maior tempo para completar


minimize tempoMaior: cmax; # Função objetivo.

s.t. r1 {j in J} : ( sum {k in K, i in I: i!=j} (x[i,j,k])  ) = 1; # todos os jobs tem que ser feitos

s.t. r2 {h in J, k in K}: (sum {i in I: i!=h} x[i,h,k]) - (sum {j in I: j!=h} x[h,j,k]) = 0; #todo job é precedido e sucedido por outro job

# @alberto Ajustei as iterações sobre j.
# Também não precisa pôr na forma padrão
#s.t. r3 {i in I, j in J}: (c[i] + (sum {k in K} ( x[i,j,k] * G[i,j,k] ) ) + V * ( ( sum {k in K} x[i,j,k] ) -1  ) ) <= c[j];
s.t. r3 {i in I, j in J}: c[j] >= c[i] + sum {k in K} G[i,j,k] * x[i,j,k] + V * (sum {k in K} x[i,j,k] - 1); 

s.t. r4 {j in J}: c[j] <= cmax; # máximo

# @alberto Correção: cada máquina começa com a tarefa artificial 0,
# e a tarefa 0 deve ter alguma outra tarefa como sucessora.
s.t. r5 {k in K}: (sum {j in J} x[0,j,k]) = 1; # cada máquina começa com no max 1 job

# @alberto Não precisa, já foi descrito que c[j] >= 0
# quando declarou as variáveis.
#s.t. r6 {j in J}: c[j] >=0;

# @alberto Tarefa artificial não gasta tempo de processamento.
s.t. r7 : c[0] = 0;

# Fim do bloco de modelo.

end;
