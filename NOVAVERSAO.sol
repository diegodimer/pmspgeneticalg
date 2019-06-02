Problem:    NOVAVERSAO
Rows:       17
Columns:    12 (12 integer, 8 binary)
Non-zeros:  36
Status:     INTEGER OPTIMAL
Objective:  tempoMaior = 30 (MINimum)

   No.   Row name        Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 tempoMaior                 30
     2 r1[1]                       1             1             =
     3 r1[2]                       1             1             =
     4 r2[1,1]                     0            -0             =
     5 r2[2,1]                     0            -0             =
     6 r3[0,1]                  9999                        9999
     7 r3[0,2]                   -30                        9999
     8 r3[1,1]                     0                        9999
     9 r3[1,2]                  9999                        9999
    10 r3[2,1]                    20                        9999
    11 r3[2,2]                     0                        9999
    12 r4[1]                     -20                          -0
    13 r4[2]                       0                          -0
    14 r5[1]                       1             1             =
    15 r6[1]                      10            -0
    16 r6[2]                      30            -0
    17 r7                          0            -0             =

   No. Column name       Activity     Lower bound   Upper bound
------ ------------    ------------- ------------- -------------
     1 x[0,1,1]     *              1             0             1
     2 x[2,1,1]     *              0             0             1
     3 x[0,2,1]     *              0             0             1
     4 x[1,2,1]     *              1             0             1
     5 x[1,0,1]     *              0             0             1
     6 x[2,0,1]     *              1             0             1
     7 x[1,1,1]     *              0             0             1
     8 x[2,2,1]     *              0             0             1
     9 c[0]         *              0             0
    10 c[1]         *             10             0
    11 c[2]         *             30             0
    12 cmax         *             30             0

Integer feasibility conditions:

INT.PE: max.abs.err. = 0.00e+000 on row 0
        max.rel.err. = 0.00e+000 on row 0
        High quality

INT.PB: max.abs.err. = 0.00e+000 on row 0
        max.rel.err. = 0.00e+000 on row 0
        High quality

End of output
