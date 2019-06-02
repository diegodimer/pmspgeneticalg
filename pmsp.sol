Problem:    pmsp
Rows:       23
Columns:    15 (15 integer, 11 binary)
Non-zeros:  53
Status:     INTEGER OPTIMAL
Objective:  tempoMaior = 0 (MINimum)

   No.   Row name        Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 tempoMaior                  0
     2 escalon[1,1]                0                          -0
     3 escalon[2,1]                0                          -0
     4 r1[1]                       1             1             =
     5 r1[2]                       1             1             =
     6 r2[0,1]                     0            -0             =
     7 r2[1,1]                     0            -0             =
     8 r2[2,1]                     0            -0             =
     9 TC[1,0]          1.00000e+009                      1e+009
    10 TC[1,1]                     0                      1e+009
    11 TC[1,2]                     0                      1e+009
    12 TC[2,0]                     0                      1e+009
    13 TC[2,1]          1.00000e+009                      1e+009
    14 TC[2,2]                     0                      1e+009
    15 r4[0]                       0                          -0
    16 r4[1]                       0                          -0
    17 r4[2]                       0                          -0
    18 r5[1]                       1             1             =
    19 r7[1]                       1             1             =
    20 r6                          0            -0             =
    21 r10[0]                      0            -0
    22 r10[1]                      0            -0
    23 r10[2]                      0            -0

   No. Column name       Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 c[0]         *              0             0
     2 c[1]         *              0             0
     3 c[2]         *              0             0
     4 cmax         *              0             0
     5 x[1,0,1]     *              1             0             1
     6 x[1,2,1]     *              0             0             1
     7 x[2,0,1]     *              0             0             1
     8 x[2,1,1]     *              1             0             1
     9 x[0,1,1]     *              0             0             1
    10 x[0,2,1]     *              1             0             1
    11 x[1,1,1]     *              0             0             1
    12 x[2,2,1]     *              0             0             1
    13 x[0,0,1]     *              0             0             1
    14 esc[1,1]     *              1             0             1
    15 esc[2,1]     *              1             0             1

Integer feasibility conditions:

INT.PE: max.abs.err. = 0.00e+000 on row 0
        max.rel.err. = 0.00e+000 on row 0
        High quality

INT.PB: max.abs.err. = 7.00e+001 on row 13
        max.rel.err. = 7.00e-008 on row 13
        Medium quality

End of output
