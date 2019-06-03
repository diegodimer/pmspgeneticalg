

set K; #conjunto de máquinas K = 1...m

set I; # i = 0, ... n; # conjunto de tarefas
set J; # j = 1, ... n;

param G {i in I, j in I, k in K}; # Sequence-dependent setup time to process job j after job i on machine k
param V; # valor muito grande


var x {i in I, j in I, k in K} binary; # 1 se job j é escalonado diretamente depois do job i na máquina k, 0 caso contrário

var c {j in I} >= 0 integer; # tempo em que o job j foi completo

var cmax >= 0 integer; # job com maior tempo para completar


minimize tempoMaior: cmax; # Função objetivo.


s.t. r1 {j in J} : ( sum {k in K, i in I: i!=j} (x[i,j,k])  ) = 1; # todos os jobs tem que ser feitos

s.t. r2 {h in J, k in K}: (sum {i in I: i!=h} x[i,h,k]) - (sum {j in I: j!=h} x[h,j,k]) = 0; #todo job é precedido e sucedido por outro job

s.t. r3 {i in I, j in J}: (c[i] + (sum {k in K} ( x[i,j,k] * G[i,j,k] ) ) + V * ( ( sum {k in K} x[i,j,k] ) -1  ) ) <= c[j];

s.t. r4 {j in J}: c[j] <= cmax; # máximo

s.t. r5 {k in K}: (sum {j in J} x[0,j,k]) = 1; # cada máquina começa com no max 1 job

s.t. r6 {j in J}: c[j] >=0;

s.t. r7 : c[0] = 0;




# Fim do bloco de modelo.

end;
