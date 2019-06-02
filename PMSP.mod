# Dados
# Jobs
set I; # i = 1, ... n;
set J; # j = 0, ... n;

# Máquinas
set K;

# Tempo de processamento em cada máquina
param G {i in I, j in J, k in K};
param V; # valor muito grande 


# Variáveis
# tempo em que o job j foi completo
var c {j in J} >= 0 integer;
# job com maior tempo para completar
var cmax >= 0 integer;
# 1 se job j é escalonado diretamente depois do job i na máquina k, 0 caso contrário
var x {i in J, j in J, k in K} binary;

# 1 se job i foi escalonado em maq K
var esc {i in I, k in K} binary;

# Função objetivo.
minimize tempoMaior: cmax;

# faz esc ser 1 onde o job é escaloando
s.t. escalon{i in I, k in K}: (sum  {j in J: i!=j} x[i,j,k]) <= esc[i,k];

# todos os jobs tem que ser feitos
s.t. r1 {j in I} : ( sum {k in K, i in J: i!=j} (x[i,j,k])  ) = 1;
#s.t. r12 {j in J} : -1 * ( sum {i in I: i!=j} (sum {k in K}(x[i,j,k]) ) ) <= -1;

#todo job é precedido e sucedido por outro job
s.t. r2 {h in J, k in K}: (sum {i in J: i!=h} x[i,h,k]) - (sum {j in J: j!=h} x[h,j,k]) = 0;
#s.t. r21 {h in J, k in K}: -1 * (sum {i in I: i!=h} x[i,h,k]) - (sum {j in J: j!=h} x[h,j,k]) <= 0;

# cada job é o tempo dele ser completo + o tempo do anterior ser completo
s.t. TC {i in I, j in J}: (c[i] + (sum {k in K} ( x[i,j,k] * G[i,j,k] ) ) + V * ( ( sum {k in K} x[i,j,k] ) -1  ) ) - c[j] <= 0;



# máximo
s.t. r4 {j in J}: c[j] <= cmax;

# cada máquina começa com no max 1 job
s.t. r5 {k in K}: (sum {j in J} x[0,j,k]) = 1; 
#s.t. r51 {k in K}: -1 * (sum {j in J} x[0,j,k]) <= -1; 

# cada máquina começa com no max 1 job
s.t. r7 {k in K}: (sum {j in J} x[j,0,k]) = 1; 
#s.t. r71 {k in K}: -1 * (sum {j in J} x[j,0,k]) <= -1; 

#dummy job (pra soma no r3 começar em 0+t1)
s.t. r6 : c[0] = 0;
s.t. r10{j in J}: c[j]>=0;
end; 

