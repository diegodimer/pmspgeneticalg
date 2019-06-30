Invalid option '-tmlim'; try glpsol --help
GLPSOL: GLPK LP/MIP Solver, v4.65
Parameter(s) specified in the command line:
 --tmlim 3600 -m formulacao_PMSP.mod -d 80on12Rp50Rs50_1 -o 80on12Rp50Rs50_1.sol
Reading model section from formulacao_PMSP.mod...
50 lines were read
Reading data section from 80on12Rp50Rs50_1...
78911 lines were read
Generating tempoMaior...
Generating r1...
Generating r2...
Generating r3...
Generating r4...
Generating r5...
Generating r7...
Model has been successfully generated
GLPK Integer Optimizer, v4.65
7614 rows, 78802 columns, 322082 non-zeros
78802 integer variables, 78720 of which are binary
Preprocessing...
7612 rows, 77841 columns, 321040 non-zeros
77841 integer variables, 77760 of which are binary
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  1.000e+06  ratio =  1.000e+06
GM: min|aij| =  8.643e-01  max|aij| =  1.157e+00  ratio =  1.339e+00
EQ: min|aij| =  7.470e-01  max|aij| =  1.000e+00  ratio =  1.339e+00
2N: min|aij| =  5.000e-01  max|aij| =  1.000e+00  ratio =  2.000e+00
Constructing initial basis...
Size of triangular part is 7612
Solving LP relaxation...
GLPK Simplex Optimizer, v4.65
7612 rows, 77841 columns, 321040 non-zeros
      0: obj =   0.000000000e+00 inf =   1.244e+05 (83)
    468: obj =   9.838685198e+05 inf =   6.401e-12 (0) 2
*   940: obj =   9.688129520e-09 inf =   1.406e-12 (0) 2
OPTIMAL LP SOLUTION FOUND
Integer optimization begins...
Long-step dual simplex will be used
+   940: mip =     not found yet >=              -inf        (1; 0)
+  1060: mip =     not found yet >=   9.828665053e-09        (3; 0)
+  1244: mip =     not found yet >=   9.828665053e-09        (5; 0)
+  1411: mip =     not found yet >=   9.828665053e-09        (7; 0)
+  1542: mip =     not found yet >=   9.828665053e-09        (9; 0)
+  1662: mip =     not found yet >=   9.828665053e-09        (11; 0)
+  1762: mip =     not found yet >=   9.828665053e-09        (13; 0)
+  1877: mip =     not found yet >=   9.828665053e-09        (15; 0)
Time used: 61.9 secs.  Memory used: 132.1 Mb.
+  1994: mip =     not found yet >=   9.828665053e-09        (17; 0)
+  2080: mip =     not found yet >=   9.828665053e-09        (19; 0)
+  2212: mip =     not found yet >=   9.828665053e-09        (21; 0)
+  2282: mip =     not found yet >=   9.828665053e-09        (23; 0)
+  2447: mip =     not found yet >=   9.828665053e-09        (25; 0)
+  2584: mip =     not found yet >=   9.828665053e-09        (27; 0)
+  2650: mip =     not found yet >=   9.828665053e-09        (29; 0)
+  2786: mip =     not found yet >=   9.828665053e-09        (31; 0)
Time used: 125.4 secs.  Memory used: 132.8 Mb.
+  2949: mip =     not found yet >=   9.828665053e-09        (33; 0)
+  3135: mip =     not found yet >=   9.828665053e-09        (35; 0)
+  3338: mip =     not found yet >=   9.828665053e-09        (37; 0)
+  3497: mip =     not found yet >=   9.828665053e-09        (39; 0)
+  3604: mip =     not found yet >=   9.828665053e-09        (41; 0)
+  3787: mip =     not found yet >=   9.828665053e-09        (43; 0)
+  4050: mip =     not found yet >=   9.828665053e-09        (45; 0)
+  4353: mip =     not found yet >=   9.828665053e-09        (47; 0)
Time used: 187.4 secs.  Memory used: 133.3 Mb.
+  4623: mip =     not found yet >=   9.828665053e-09        (49; 0)
+  4890: mip =     not found yet >=   9.828665053e-09        (51; 0)
+  5128: mip =     not found yet >=   9.828665053e-09        (53; 0)
+  5345: mip =     not found yet >=   9.828665053e-09        (55; 0)
+  5633: mip =     not found yet >=   9.828665053e-09        (57; 0)
+  5965: mip =     not found yet >=   9.828665053e-09        (59; 0)
+  6322: mip =     not found yet >=   9.828665053e-09        (61; 0)
+  6675: mip =     not found yet >=   9.828665053e-09        (63; 0)
+  7112: mip =     not found yet >=   9.828665053e-09        (65; 0)
Time used: 249.9 secs.  Memory used: 134.0 Mb.
+  7411: mip =     not found yet >=   9.828665053e-09        (67; 0)
+  7693: mip =     not found yet >=   9.828665053e-09        (69; 0)
+  7918: mip =     not found yet >=   9.828665053e-09        (70; 1)
+  8120: mip =     not found yet >=   9.828665053e-09        (72; 1)
+  8203: mip =     not found yet >=   9.828665053e-09        (74; 1)
+  8305: mip =     not found yet >=   9.828665053e-09        (75; 1)
+  8439: mip =     not found yet >=   9.828665053e-09        (77; 1)
+  8629: mip =     not found yet >=   9.828665053e-09        (79; 1)
Time used: 313.0 secs.  Memory used: 134.5 Mb.
+  8748: mip =     not found yet >=   9.828665053e-09        (81; 1)
+  8858: mip =     not found yet >=   9.828665053e-09        (82; 1)
+  9036: mip =     not found yet >=   9.828665053e-09        (84; 1)
+  9169: mip =     not found yet >=   9.828665053e-09        (86; 1)
+  9355: mip =     not found yet >=   9.828665053e-09        (88; 1)
+  9526: mip =     not found yet >=   9.828665053e-09        (90; 1)
+  9623: mip =     not found yet >=   9.828665053e-09        (92; 1)
Time used: 375.1 secs.  Memory used: 135.0 Mb.
+  9772: mip =     not found yet >=   9.828665053e-09        (94; 1)
+  9963: mip =     not found yet >=   9.828665053e-09        (96; 1)
+ 10223: mip =     not found yet >=   9.828665053e-09        (98; 1)
+ 10538: mip =     not found yet >=   9.828665053e-09        (100; 1)
+ 10659: mip =     not found yet >=   9.828665053e-09        (102; 1)
+ 10881: mip =     not found yet >=   9.828665053e-09        (104; 1)
+ 11027: mip =     not found yet >=   9.828665053e-09        (106; 1)
Time used: 437.8 secs.  Memory used: 135.6 Mb.
+ 11206: mip =     not found yet >=   9.828665053e-09        (107; 1)
+ 11520: mip =     not found yet >=   9.828665053e-09        (109; 1)
+ 11719: mip =     not found yet >=   9.828665053e-09        (111; 1)
+ 11965: mip =     not found yet >=   9.828665053e-09        (113; 1)
+ 12253: mip =     not found yet >=   9.828665053e-09        (115; 1)
+ 12511: mip =     not found yet >=   9.828665053e-09        (117; 1)
+ 12798: mip =     not found yet >=   9.828665053e-09        (119; 1)
+ 13126: mip =     not found yet >=   9.828665053e-09        (120; 1)
Time used: 498.1 secs.  Memory used: 136.1 Mb.
+ 13458: mip =     not found yet >=   9.828665053e-09        (122; 1)
+ 13752: mip =     not found yet >=   9.828665053e-09        (124; 1)
+ 13966: mip =     not found yet >=   9.828665053e-09        (126; 1)
+ 14339: mip =     not found yet >=   9.828665053e-09        (128; 1)
+ 14669: mip =     not found yet >=   9.828665053e-09        (130; 1)
+ 14957: mip =     not found yet >=   9.828665053e-09        (131; 1)
+ 15237: mip =     not found yet >=   9.828665053e-09        (133; 1)
+ 15525: mip =     not found yet >=   9.828665053e-09        (135; 1)
+ 15706: mip =     not found yet >=   9.828665053e-09        (137; 1)
+ 16293: mip =     not found yet >=   9.828665053e-09        (139; 1)
Time used: 559.4 secs.  Memory used: 136.8 Mb.
+ 16626: mip =     not found yet >=   9.828665053e-09        (141; 1)
+ 17103: mip =     not found yet >=   9.828665053e-09        (143; 1)
+ 17491: mip =     not found yet >=   9.828665053e-09        (146; 1)
+ 18203: mip =     not found yet >=   9.828665053e-09        (149; 1)
+ 18750: mip =     not found yet >=   9.828665053e-09        (151; 1)
+ 19267: mip =     not found yet >=   9.828665053e-09        (154; 1)
+ 20100: mip =     not found yet >=   9.828665053e-09        (157; 1)
+ 20771: mip =     not found yet >=   9.828665053e-09        (160; 1)
+ 21472: mip =     not found yet >=   9.828665053e-09        (163; 1)
+ 21594: mip =     not found yet >=   9.828665053e-09        (164; 2)
Time used: 621.1 secs.  Memory used: 137.5 Mb.
+ 21687: mip =     not found yet >=   9.828665053e-09        (166; 2)
+ 21748: mip =     not found yet >=   9.828665053e-09        (168; 2)
+ 21838: mip =     not found yet >=   9.828665053e-09        (169; 3)
+ 21898: mip =     not found yet >=   9.828665053e-09        (171; 3)
+ 21965: mip =     not found yet >=   9.828665053e-09        (173; 3)
+ 22078: mip =     not found yet >=   9.828665053e-09        (175; 3)
+ 22203: mip =     not found yet >=   9.828665053e-09        (177; 3)
Time used: 682.6 secs.  Memory used: 137.8 Mb.
+ 22280: mip =     not found yet >=   9.828665053e-09        (179; 3)
+ 22422: mip =     not found yet >=   9.828665053e-09        (181; 3)
+ 22664: mip =     not found yet >=   9.828665053e-09        (183; 3)
+ 22787: mip =     not found yet >=   9.828665053e-09        (185; 3)
+ 22990: mip =     not found yet >=   9.828665053e-09        (187; 3)
+ 23122: mip =     not found yet >=   9.828665053e-09        (189; 3)
+ 23266: mip =     not found yet >=   9.828665053e-09        (191; 3)
Time used: 744.3 secs.  Memory used: 138.5 Mb.
+ 23398: mip =     not found yet >=   9.828665053e-09        (193; 3)
+ 23603: mip =     not found yet >=   9.828665053e-09        (195; 3)
+ 23738: mip =     not found yet >=   9.828665053e-09        (197; 3)
+ 23927: mip =     not found yet >=   9.828665053e-09        (199; 3)
+ 24049: mip =     not found yet >=   9.828665053e-09        (201; 3)
+ 24293: mip =     not found yet >=   9.828665053e-09        (203; 3)
+ 24530: mip =     not found yet >=   9.828665053e-09        (205; 3)
Time used: 808.9 secs.  Memory used: 138.9 Mb.
+ 24623: mip =     not found yet >=   9.828665053e-09        (207; 3)
+ 24806: mip =     not found yet >=   9.828665053e-09        (209; 3)
+ 24988: mip =     not found yet >=   9.828665053e-09        (211; 3)
+ 25143: mip =     not found yet >=   9.828665053e-09        (213; 3)
+ 25318: mip =     not found yet >=   9.828665053e-09        (215; 3)
+ 25446: mip =     not found yet >=   9.828665053e-09        (217; 3)
+ 25697: mip =     not found yet >=   9.828665053e-09        (219; 3)
Time used: 872.7 secs.  Memory used: 139.3 Mb.
+ 26018: mip =     not found yet >=   9.828665053e-09        (221; 3)
+ 26230: mip =     not found yet >=   9.828665053e-09        (223; 3)
+ 26298: mip =     not found yet >=   9.828665053e-09        (225; 3)
+ 26509: mip =     not found yet >=   9.828665053e-09        (227; 3)
+ 26807: mip =     not found yet >=   9.828665053e-09        (229; 3)
+ 26899: mip =     not found yet >=   9.828665053e-09        (231; 3)
+ 27093: mip =     not found yet >=   9.828665053e-09        (233; 3)
+ 27302: mip =     not found yet >=   9.828665053e-09        (235; 3)
+ 27497: mip =     not found yet >=   9.828665053e-09        (237; 3)
Time used: 935.2 secs.  Memory used: 139.8 Mb.
+ 27725: mip =     not found yet >=   9.828665053e-09        (239; 3)
+ 27977: mip =     not found yet >=   9.828665053e-09        (241; 3)
+ 28194: mip =     not found yet >=   9.828665053e-09        (243; 3)
+ 28579: mip =     not found yet >=   9.828665053e-09        (245; 3)
+ 28942: mip =     not found yet >=   9.828665053e-09        (247; 3)
+ 29169: mip =     not found yet >=   9.828665053e-09        (249; 3)
+ 29436: mip =     not found yet >=   9.828665053e-09        (251; 3)
+ 29872: mip =     not found yet >=   9.828665053e-09        (253; 3)
+ 30282: mip =     not found yet >=   9.828665053e-09        (255; 3)
Time used: 996.8 secs.  Memory used: 140.3 Mb.
+ 30611: mip =     not found yet >=   9.828665053e-09        (257; 3)
+ 31082: mip =     not found yet >=   9.828665053e-09        (259; 3)
+ 31531: mip =     not found yet >=   9.828665053e-09        (262; 3)
+ 31973: mip =     not found yet >=   9.828665053e-09        (265; 3)
+ 32471: mip =     not found yet >=   9.828665053e-09        (268; 3)
+ 32964: mip =     not found yet >=   9.828665053e-09        (271; 3)
+ 33351: mip =     not found yet >=   9.828665053e-09        (274; 3)
+ 33885: mip =     not found yet >=   9.828665053e-09        (277; 3)
+ 34382: mip =     not found yet >=   9.828665053e-09        (280; 3)
+ 34711: mip =     not found yet >=   9.828665053e-09        (283; 3)
Time used: 1058.5 secs.  Memory used: 140.9 Mb.
+ 35234: mip =     not found yet >=   9.828665053e-09        (287; 3)
+ 35675: mip =     not found yet >=   9.828665053e-09        (291; 3)
+ 36080: mip =     not found yet >=   9.828665053e-09        (292; 4)
+ 36168: mip =     not found yet >=   9.828665053e-09        (294; 4)
+ 36255: mip =     not found yet >=   9.828665053e-09        (296; 4)
+ 36388: mip =     not found yet >=   9.828665053e-09        (298; 4)
+ 36563: mip =     not found yet >=   9.828665053e-09        (300; 4)
+ 36713: mip =     not found yet >=   9.828665053e-09        (302; 4)
+ 36782: mip =     not found yet >=   9.828665053e-09        (303; 4)
Time used: 1120.6 secs.  Memory used: 141.8 Mb.
+ 36897: mip =     not found yet >=   9.828665053e-09        (305; 4)
+ 36985: mip =     not found yet >=   9.828665053e-09        (307; 4)
+ 37051: mip =     not found yet >=   9.828665053e-09        (309; 4)
+ 37215: mip =     not found yet >=   9.828665053e-09        (311; 4)
+ 37390: mip =     not found yet >=   9.828665053e-09        (313; 4)
+ 37517: mip =     not found yet >=   9.828665053e-09        (314; 4)
+ 37671: mip =     not found yet >=   9.828665053e-09        (316; 4)
Time used: 1184.1 secs.  Memory used: 142.1 Mb.
+ 37752: mip =     not found yet >=   9.828665053e-09        (317; 4)
+ 37836: mip =     not found yet >=   9.828665053e-09        (318; 4)
+ 37942: mip =     not found yet >=   9.828665053e-09        (319; 4)
+ 38136: mip =     not found yet >=   9.828665053e-09        (321; 4)
+ 38211: mip =     not found yet >=   9.828665053e-09        (322; 4)
+ 38401: mip =     not found yet >=   9.828665053e-09        (324; 4)
+ 38562: mip =     not found yet >=   9.828665053e-09        (325; 4)
+ 38719: mip =     not found yet >=   9.828665053e-09        (327; 4)
+ 38851: mip =     not found yet >=   9.828665053e-09        (329; 4)
Time used: 1247.8 secs.  Memory used: 142.2 Mb.
+ 39033: mip =     not found yet >=   9.828665053e-09        (331; 4)
+ 39290: mip =     not found yet >=   9.828665053e-09        (333; 4)
+ 39474: mip =     not found yet >=   9.828665053e-09        (334; 4)
+ 39792: mip =     not found yet >=   9.828665053e-09        (336; 4)
+ 40096: mip =     not found yet >=   9.828665053e-09        (338; 4)
+ 40492: mip =     not found yet >=   9.828665053e-09        (340; 4)
+ 40740: mip =     not found yet >=   9.828665053e-09        (342; 4)
Time used: 1308.3 secs.  Memory used: 143.0 Mb.
+ 40929: mip =     not found yet >=   9.828665053e-09        (344; 4)
+ 41090: mip =     not found yet >=   9.828665053e-09        (346; 4)
+ 41440: mip =     not found yet >=   9.828665053e-09        (347; 5)
+ 41521: mip =     not found yet >=   9.828665053e-09        (349; 5)
+ 41636: mip =     not found yet >=   9.828665053e-09        (351; 5)
+ 41738: mip =     not found yet >=   9.828665053e-09        (352; 5)
+ 41910: mip =     not found yet >=   9.828665053e-09        (354; 5)
+ 41992: mip =     not found yet >=   9.828665053e-09        (355; 5)
Time used: 1372.4 secs.  Memory used: 143.7 Mb.
+ 42113: mip =     not found yet >=   9.828665053e-09        (357; 5)
+ 42222: mip =     not found yet >=   9.828665053e-09        (358; 5)
+ 42389: mip =     not found yet >=   9.828665053e-09        (360; 5)
+ 42507: mip =     not found yet >=   9.828665053e-09        (361; 5)
+ 42610: mip =     not found yet >=   9.828665053e-09        (363; 5)
+ 42805: mip =     not found yet >=   9.828665053e-09        (365; 5)
+ 43015: mip =     not found yet >=   9.828665053e-09        (367; 5)
Time used: 1435.0 secs.  Memory used: 144.5 Mb.
+ 43257: mip =     not found yet >=   9.828665053e-09        (369; 5)
+ 43480: mip =     not found yet >=   9.828665053e-09        (371; 5)
+ 43623: mip =     not found yet >=   9.828665053e-09        (373; 5)
+ 43823: mip =     not found yet >=   9.828665053e-09        (375; 5)
+ 44183: mip =     not found yet >=   9.828665053e-09        (377; 5)
+ 44483: mip =     not found yet >=   9.828665053e-09        (379; 5)
+ 44648: mip =     not found yet >=   9.828665053e-09        (379; 6)
+ 44729: mip =     not found yet >=   9.828665053e-09        (380; 6)
+ 44840: mip =     not found yet >=   9.828665053e-09        (382; 6)
+ 44894: mip =     not found yet >=   9.828665053e-09        (383; 6)
Time used: 1499.7 secs.  Memory used: 145.4 Mb.
+ 44991: mip =     not found yet >=   9.828665053e-09        (385; 6)
+ 45069: mip =     not found yet >=   9.828665053e-09        (387; 6)
+ 45170: mip =     not found yet >=   9.828665053e-09        (389; 6)
+ 45238: mip =     not found yet >=   9.828665053e-09        (391; 6)
+ 45282: mip =     not found yet >=   9.828665053e-09        (393; 6)
+ 45346: mip =     not found yet >=   9.828665053e-09        (395; 6)
+ 45493: mip =     not found yet >=   9.828665053e-09        (397; 6)
Time used: 1562.8 secs.  Memory used: 145.7 Mb.
+ 45701: mip =     not found yet >=   9.828665053e-09        (399; 6)
+ 45819: mip =     not found yet >=   9.828665053e-09        (401; 6)
+ 45940: mip =     not found yet >=   9.828665053e-09        (403; 6)
+ 46072: mip =     not found yet >=   9.828665053e-09        (405; 6)
+ 46281: mip =     not found yet >=   9.828665053e-09        (407; 6)
+ 46403: mip =     not found yet >=   9.828665053e-09        (409; 6)
+ 46512: mip =     not found yet >=   9.828665053e-09        (411; 6)
+ 46641: mip =     not found yet >=   9.828665053e-09        (413; 6)
Time used: 1625.2 secs.  Memory used: 146.2 Mb.
+ 46796: mip =     not found yet >=   9.828665053e-09        (415; 6)
+ 46905: mip =     not found yet >=   9.828665053e-09        (417; 6)
+ 47073: mip =     not found yet >=   9.828665053e-09        (419; 6)
+ 47198: mip =     not found yet >=   9.828665053e-09        (421; 6)
+ 47342: mip =     not found yet >=   9.828665053e-09        (423; 6)
+ 47455: mip =     not found yet >=   9.828665053e-09        (425; 6)
+ 47611: mip =     not found yet >=   9.828665053e-09        (427; 6)
+ 47863: mip =     not found yet >=   9.828665053e-09        (429; 6)
+ 48059: mip =     not found yet >=   9.828665053e-09        (431; 6)
Time used: 1686.9 secs.  Memory used: 146.5 Mb.
+ 48170: mip =     not found yet >=   9.828665053e-09        (433; 6)
+ 48387: mip =     not found yet >=   9.828665053e-09        (435; 6)
+ 48693: mip =     not found yet >=   9.828665053e-09        (437; 6)
+ 48748: mip =     not found yet >=   9.828665053e-09        (438; 7)
+ 48850: mip =     not found yet >=   9.828665053e-09        (440; 7)
+ 48911: mip =     not found yet >=   9.828665053e-09        (442; 7)
+ 49077: mip =     not found yet >=   9.828665053e-09        (444; 7)
+ 49184: mip =     not found yet >=   9.828665053e-09        (446; 7)
Time used: 1748.0 secs.  Memory used: 147.1 Mb.
+ 49356: mip =     not found yet >=   9.828665053e-09        (448; 7)
+ 49518: mip =     not found yet >=   9.828665053e-09        (450; 7)
+ 49693: mip =     not found yet >=   9.828665053e-09        (452; 7)
+ 49867: mip =     not found yet >=   9.828665053e-09        (454; 7)
+ 49984: mip =     not found yet >=   9.828665053e-09        (456; 7)
+ 50184: mip =     not found yet >=   9.828665053e-09        (458; 7)
+ 50300: mip =     not found yet >=   9.828665053e-09        (460; 7)
Time used: 1810.1 secs.  Memory used: 147.8 Mb.
+ 50487: mip =     not found yet >=   9.828665053e-09        (462; 7)
+ 50644: mip =     not found yet >=   9.828665053e-09        (464; 7)
+ 50836: mip =     not found yet >=   9.828665053e-09        (466; 7)
+ 51003: mip =     not found yet >=   9.828665053e-09        (468; 7)
+ 51190: mip =     not found yet >=   9.828665053e-09        (470; 7)
+ 51442: mip =     not found yet >=   9.828665053e-09        (472; 7)
+ 51679: mip =     not found yet >=   9.828665053e-09        (474; 7)
+ 51846: mip =     not found yet >=   9.828665053e-09        (476; 7)
Time used: 1872.2 secs.  Memory used: 148.0 Mb.
+ 52052: mip =     not found yet >=   9.828665053e-09        (478; 7)
+ 52157: mip =     not found yet >=   9.828665053e-09        (480; 7)
+ 52336: mip =     not found yet >=   9.828665053e-09        (482; 7)
+ 52728: mip =     not found yet >=   9.828665053e-09        (484; 7)
+ 53224: mip =     not found yet >=   9.828665053e-09        (486; 7)
+ 53490: mip =     not found yet >=   9.828665053e-09        (488; 7)
+ 53728: mip =     not found yet >=   9.828665053e-09        (490; 7)
+ 54131: mip =     not found yet >=   9.828665053e-09        (492; 7)
+ 54504: mip =     not found yet >=   9.828665053e-09        (494; 7)
Time used: 1933.1 secs.  Memory used: 148.8 Mb.
+ 54898: mip =     not found yet >=   9.828665053e-09        (496; 7)
+ 55012: mip =     not found yet >=   9.828665053e-09        (499; 7)
+ 55387: mip =     not found yet >=   9.828665053e-09        (501; 7)
+ 55693: mip =     not found yet >=   9.828665053e-09        (503; 7)
+ 56013: mip =     not found yet >=   9.828665053e-09        (505; 7)
+ 56258: mip =     not found yet >=   9.828665053e-09        (507; 7)
+ 56555: mip =     not found yet >=   9.828665053e-09        (509; 7)
+ 56989: mip =     not found yet >=   9.828665053e-09        (511; 7)
+ 57508: mip =     not found yet >=   9.828665053e-09        (514; 7)
+ 58073: mip =     not found yet >=   9.828665053e-09        (517; 7)
Time used: 1994.3 secs.  Memory used: 149.3 Mb.
+ 58707: mip =     not found yet >=   9.828665053e-09        (520; 7)
+ 59249: mip =     not found yet >=   9.828665053e-09        (523; 7)
+ 59953: mip =     not found yet >=   9.828665053e-09        (526; 7)
+ 60785: mip =     not found yet >=   9.828665053e-09        (529; 7)
+ 61531: mip =     not found yet >=   9.828665053e-09        (532; 7)
+ 62447: mip =     not found yet >=   9.828665053e-09        (533; 7)
+ 63387: mip =     not found yet >=   9.828665053e-09        (536; 7)
+ 64193: mip =     not found yet >=   9.828665053e-09        (539; 7)
+ 64948: mip =     not found yet >=   9.828665053e-09        (543; 7)
+ 65996: mip =     not found yet >=   9.828665053e-09        (546; 7)
Time used: 2054.8 secs.  Memory used: 149.8 Mb.
+ 66707: mip =     not found yet >=   9.828665053e-09        (550; 7)
+ 67608: mip =     not found yet >=   9.828665053e-09        (553; 7)
+ 68595: mip =     not found yet >=   9.828665053e-09        (555; 7)
+ 69441: mip =     not found yet >=   9.828665053e-09        (559; 7)
+ 70542: mip =     not found yet >=   9.828665053e-09        (562; 7)
+ 71623: mip =     not found yet >=   9.828665053e-09        (566; 7)
+ 72758: mip =     not found yet >=   9.828665053e-09        (569; 7)
+ 74126: mip =     not found yet >=   9.828665053e-09        (572; 7)
+ 74981: mip =     not found yet >=   9.828665053e-09        (577; 7)
+ 75548: mip =     not found yet >=   9.828665053e-09        (580; 7)
+ 76611: mip =     not found yet >=   9.828665053e-09        (583; 7)
Time used: 2115.5 secs.  Memory used: 150.2 Mb.
+ 76963: mip =     not found yet >=   9.828665053e-09        (585; 8)
+ 77056: mip =     not found yet >=   9.828665053e-09        (587; 8)
+ 77144: mip =     not found yet >=   9.828665053e-09        (589; 8)
+ 77227: mip =     not found yet >=   9.828665053e-09        (591; 8)
+ 77274: mip =     not found yet >=   9.828665053e-09        (593; 8)
+ 77321: mip =     not found yet >=   9.828665053e-09        (595; 8)
+ 77459: mip =     not found yet >=   9.828665053e-09        (597; 8)
+ 77639: mip =     not found yet >=   9.828665053e-09        (599; 8)
Time used: 2177.9 secs.  Memory used: 150.7 Mb.
+ 77727: mip =     not found yet >=   9.828665053e-09        (601; 8)
+ 77831: mip =     not found yet >=   9.828665053e-09        (603; 8)
+ 77969: mip =     not found yet >=   9.828665053e-09        (605; 8)
+ 78111: mip =     not found yet >=   9.828665053e-09        (607; 8)
+ 78283: mip =     not found yet >=   9.828665053e-09        (609; 8)
+ 78431: mip =     not found yet >=   9.828665053e-09        (611; 8)
+ 78522: mip =     not found yet >=   9.828665053e-09        (613; 8)
Time used: 2239.4 secs.  Memory used: 151.2 Mb.
+ 78658: mip =     not found yet >=   9.828665053e-09        (615; 8)
+ 78790: mip =     not found yet >=   9.828665053e-09        (617; 8)
+ 79019: mip =     not found yet >=   9.828665053e-09        (619; 8)
+ 79170: mip =     not found yet >=   9.828665053e-09        (621; 8)
+ 79359: mip =     not found yet >=   9.828665053e-09        (623; 8)
+ 79578: mip =     not found yet >=   9.828665053e-09        (625; 8)
+ 79917: mip =     not found yet >=   9.828665053e-09        (627; 8)
+ 80230: mip =     not found yet >=   9.828665053e-09        (629; 8)
+ 80474: mip =     not found yet >=   9.828665053e-09        (631; 8)
Time used: 2301.6 secs.  Memory used: 151.9 Mb.
+ 80800: mip =     not found yet >=   9.828665053e-09        (633; 8)
+ 81077: mip =     not found yet >=   9.828665053e-09        (635; 8)
+ 81306: mip =     not found yet >=   9.828665053e-09        (637; 8)
+ 81467: mip =     not found yet >=   9.828665053e-09        (639; 8)
+ 81853: mip =     not found yet >=   9.828665053e-09        (641; 8)
+ 82053: mip =     not found yet >=   9.828665053e-09        (643; 8)
+ 82267: mip =     not found yet >=   9.828665053e-09        (645; 8)
+ 82588: mip =     not found yet >=   9.828665053e-09        (647; 8)
+ 82933: mip =     not found yet >=   9.828665053e-09        (649; 8)
+ 83195: mip =     not found yet >=   9.828665053e-09        (651; 8)
Time used: 2362.5 secs.  Memory used: 152.5 Mb.
+ 83607: mip =     not found yet >=   9.828665053e-09        (653; 8)
+ 84075: mip =     not found yet >=   9.828665053e-09        (656; 8)
+ 84829: mip =     not found yet >=   9.828665053e-09        (659; 8)
+ 85346: mip =     not found yet >=   9.828665053e-09        (662; 8)
+ 85828: mip =     not found yet >=   9.828665053e-09        (665; 8)
+ 86217: mip =     not found yet >=   9.828665053e-09        (668; 8)
+ 86748: mip =     not found yet >=   9.828665053e-09        (671; 8)
+ 87029: mip =     not found yet >=   9.828665053e-09        (673; 8)
+ 87313: mip =     not found yet >=   9.828665053e-09        (676; 8)
+ 87879: mip =     not found yet >=   9.828665053e-09        (678; 8)
+ 88391: mip =     not found yet >=   9.828665053e-09        (680; 8)
Time used: 2424.4 secs.  Memory used: 153.2 Mb.
+ 89099: mip =     not found yet >=   9.828665053e-09        (683; 8)
+ 89606: mip =     not found yet >=   9.828665053e-09        (685; 8)
+ 90221: mip =     not found yet >=   9.828665053e-09        (688; 8)
+ 90651: mip =     not found yet >=   9.828665053e-09        (691; 8)
+ 91295: mip =     not found yet >=   9.828665053e-09        (695; 8)
+ 91615: mip =     not found yet >=   9.828665053e-09        (699; 8)
+ 92315: mip =     not found yet >=   9.828665053e-09        (703; 8)
+ 93032: mip =     not found yet >=   9.828665053e-09        (707; 8)
+ 93885: mip =     not found yet >=   9.828665053e-09        (712; 8)
+ 95111: mip =     not found yet >=   9.828665053e-09        (715; 9)
Time used: 2485.1 secs.  Memory used: 153.9 Mb.
+ 95155: mip =     not found yet >=   9.828665053e-09        (716; 9)
+ 95220: mip =     not found yet >=   9.828665053e-09        (717; 9)
+ 95276: mip =     not found yet >=   9.828665053e-09        (718; 9)
+ 95296: mip =     not found yet >=   9.828665053e-09        (719; 9)
+ 95344: mip =     not found yet >=   9.828665053e-09        (720; 9)
+ 95431: mip =     not found yet >=   9.828665053e-09        (722; 9)
+ 95507: mip =     not found yet >=   9.828665053e-09        (724; 9)
+ 95570: mip =     not found yet >=   9.828665053e-09        (726; 9)
+ 95648: mip =     not found yet >=   9.828665053e-09        (727; 9)
Time used: 2549.4 secs.  Memory used: 154.3 Mb.
+ 95770: mip =     not found yet >=   9.828665053e-09        (729; 9)
+ 95833: mip =     not found yet >=   9.828665053e-09        (730; 9)
+ 95914: mip =     not found yet >=   9.828665053e-09        (732; 9)
+ 95989: mip =     not found yet >=   9.828665053e-09        (734; 9)
+ 96086: mip =     not found yet >=   9.828665053e-09        (736; 9)
+ 96169: mip =     not found yet >=   9.828665053e-09        (737; 9)
+ 96245: mip =     not found yet >=   9.828665053e-09        (738; 9)
+ 96320: mip =     not found yet >=   9.828665053e-09        (739; 9)
+ 96466: mip =     not found yet >=   9.828665053e-09        (740; 9)
Time used: 2609.8 secs.  Memory used: 154.6 Mb.
+ 96593: mip =     not found yet >=   9.828665053e-09        (742; 9)
+ 96661: mip =     not found yet >=   9.828665053e-09        (743; 9)
+ 96763: mip =     not found yet >=   9.828665053e-09        (744; 9)
+ 96824: mip =     not found yet >=   9.828665053e-09        (745; 9)
+ 97010: mip =     not found yet >=   9.828665053e-09        (747; 9)
+ 97149: mip =     not found yet >=   9.828665053e-09        (749; 9)
+ 97255: mip =     not found yet >=   9.828665053e-09        (751; 9)
+ 97441: mip =     not found yet >=   9.828665053e-09        (753; 9)
Time used: 2673.9 secs.  Memory used: 155.1 Mb.
+ 97591: mip =     not found yet >=   9.828665053e-09        (754; 9)
+ 97878: mip =     not found yet >=   9.828665053e-09        (756; 9)
+ 97996: mip =     not found yet >=   9.828665053e-09        (758; 9)
+ 98172: mip =     not found yet >=   9.828665053e-09        (760; 9)
+ 98323: mip =     not found yet >=   9.828665053e-09        (762; 9)
+ 98523: mip =     not found yet >=   9.828665053e-09        (763; 9)
+ 98773: mip =     not found yet >=   9.828665053e-09        (765; 9)
+ 99102: mip =     not found yet >=   9.828665053e-09        (767; 9)
Time used: 2737.0 secs.  Memory used: 155.7 Mb.
+ 99423: mip =     not found yet >=   9.828665053e-09        (769; 9)
+ 99816: mip =     not found yet >=   9.828665053e-09        (771; 9)
+100281: mip =     not found yet >=   9.828665053e-09        (773; 9)
+100589: mip =     not found yet >=   9.828665053e-09        (775; 9)
+100915: mip =     not found yet >=   9.828665053e-09        (777; 9)
+101201: mip =     not found yet >=   9.828665053e-09        (779; 9)
+101698: mip =     not found yet >=   9.828665053e-09        (781; 9)
Time used: 2798.1 secs.  Memory used: 156.1 Mb.
+102028: mip =     not found yet >=   9.828665053e-09        (783; 9)
+102521: mip =     not found yet >=   9.828665053e-09        (785; 9)
+102743: mip =     not found yet >=   9.828665053e-09        (787; 9)
+103417: mip =     not found yet >=   9.828665053e-09        (788; 9)
+103796: mip =     not found yet >=   9.828665053e-09        (790; 9)
+104193: mip =     not found yet >=   9.828665053e-09        (792; 9)
+104722: mip =     not found yet >=   9.828665053e-09        (794; 9)
+105303: mip =     not found yet >=   9.828665053e-09        (797; 9)
+106100: mip =     not found yet >=   9.828665053e-09        (799; 9)
+106745: mip =     not found yet >=   9.828665053e-09        (802; 9)
Time used: 2859.5 secs.  Memory used: 156.7 Mb.
+107469: mip =     not found yet >=   9.828665053e-09        (805; 9)
+107789: mip =     not found yet >=   9.828665053e-09        (808; 9)
+108408: mip =     not found yet >=   9.828665053e-09        (811; 9)
+108912: mip =     not found yet >=   9.828665053e-09        (815; 9)
+109388: mip =     not found yet >=   9.828665053e-09        (818; 9)
+110167: mip =     not found yet >=   9.828665053e-09        (822; 9)
+111532: mip =     not found yet >=   9.828665053e-09        (824; 9)
+112516: mip =     not found yet >=   9.828665053e-09        (829; 9)
+113389: mip =     not found yet >=   9.828665053e-09        (834; 9)
+114232: mip =     not found yet >=   9.828665053e-09        (839; 9)
+115189: mip =     not found yet >=   9.828665053e-09        (845; 9)
Time used: 2919.7 secs.  Memory used: 157.6 Mb.
+115737: mip =     not found yet >=   9.828665053e-09        (850; 9)
+116013: mip =     not found yet >=   9.828665053e-09        (852; 10)
+116065: mip =     not found yet >=   9.828665053e-09        (853; 10)
+116136: mip =     not found yet >=   9.828665053e-09        (854; 10)
+116231: mip =     not found yet >=   9.828665053e-09        (856; 10)
+116322: mip =     not found yet >=   9.828665053e-09        (858; 10)
+116456: mip =     not found yet >=   9.828665053e-09        (860; 10)
+116646: mip =     not found yet >=   9.828665053e-09        (862; 10)
Time used: 2981.5 secs.  Memory used: 158.1 Mb.
+116712: mip =     not found yet >=   9.828665053e-09        (864; 10)
+116854: mip =     not found yet >=   9.828665053e-09        (866; 10)
+116967: mip =     not found yet >=   9.828665053e-09        (868; 10)
+117140: mip =     not found yet >=   9.828665053e-09        (870; 10)
+117348: mip =     not found yet >=   9.828665053e-09        (872; 10)
+117474: mip =     not found yet >=   9.828665053e-09        (874; 10)
+117590: mip =     not found yet >=   9.828665053e-09        (876; 10)
Time used: 3042.2 secs.  Memory used: 158.6 Mb.
+117797: mip =     not found yet >=   9.828665053e-09        (878; 10)
+117978: mip =     not found yet >=   9.828665053e-09        (880; 10)
+118169: mip =     not found yet >=   9.828665053e-09        (882; 10)
+118415: mip =     not found yet >=   9.828665053e-09        (884; 10)
+118593: mip =     not found yet >=   9.828665053e-09        (886; 10)
+118756: mip =     not found yet >=   9.828665053e-09        (888; 10)
+118972: mip =     not found yet >=   9.828665053e-09        (890; 10)
Time used: 3103.8 secs.  Memory used: 158.9 Mb.
+119176: mip =     not found yet >=   9.828665053e-09        (892; 10)
+119313: mip =     not found yet >=   9.828665053e-09        (894; 10)
+119502: mip =     not found yet >=   9.828665053e-09        (896; 10)
+119760: mip =     not found yet >=   9.828665053e-09        (898; 10)
+119962: mip =     not found yet >=   9.828665053e-09        (900; 10)
+120140: mip =     not found yet >=   9.828665053e-09        (902; 10)
+120491: mip =     not found yet >=   9.828665053e-09        (904; 10)
Time used: 3164.5 secs.  Memory used: 159.3 Mb.
+120782: mip =     not found yet >=   9.828665053e-09        (906; 10)
+121008: mip =     not found yet >=   9.828665053e-09        (908; 10)
+121191: mip =     not found yet >=   9.828665053e-09        (910; 10)
+121347: mip =     not found yet >=   9.828665053e-09        (912; 10)
+121509: mip =     not found yet >=   9.828665053e-09        (914; 10)
+121812: mip =     not found yet >=   9.828665053e-09        (915; 10)
+122000: mip =     not found yet >=   9.828665053e-09        (917; 10)
+122234: mip =     not found yet >=   9.828665053e-09        (919; 10)
+122410: mip =     not found yet >=   9.828665053e-09        (921; 10)
Time used: 3225.3 secs.  Memory used: 159.6 Mb.
+122627: mip =     not found yet >=   9.828665053e-09        (923; 10)
+122775: mip =     not found yet >=   9.828665053e-09        (925; 10)
+122949: mip =     not found yet >=   9.828665053e-09        (927; 10)
+123208: mip =     not found yet >=   9.828665053e-09        (929; 10)
+123382: mip =     not found yet >=   9.828665053e-09        (931; 10)
+123637: mip =     not found yet >=   9.828665053e-09        (933; 10)
+123859: mip =     not found yet >=   9.828665053e-09        (935; 10)
+124000: mip =     not found yet >=   9.828665053e-09        (937; 10)
+124260: mip =     not found yet >=   9.828665053e-09        (939; 10)
+124381: mip =     not found yet >=   9.828665053e-09        (941; 10)
Time used: 3285.4 secs.  Memory used: 159.9 Mb.
+124843: mip =     not found yet >=   9.828665053e-09        (943; 10)
+125232: mip =     not found yet >=   9.828665053e-09        (945; 10)
+125471: mip =     not found yet >=   9.828665053e-09        (947; 10)
+125869: mip =     not found yet >=   9.828665053e-09        (949; 10)
+126281: mip =     not found yet >=   9.828665053e-09        (951; 10)
+126473: mip =     not found yet >=   9.828665053e-09        (954; 10)
+126862: mip =     not found yet >=   9.828665053e-09        (956; 10)
+127196: mip =     not found yet >=   9.828665053e-09        (959; 10)
+127761: mip =     not found yet >=   9.828665053e-09        (962; 10)
+128327: mip =     not found yet >=   9.828665053e-09        (965; 10)
Time used: 3347.1 secs.  Memory used: 160.6 Mb.
+128822: mip =     not found yet >=   9.828665053e-09        (969; 10)
+129429: mip =     not found yet >=   9.828665053e-09        (973; 10)
+130077: mip =     not found yet >=   9.828665053e-09        (979; 10)
+130813: mip =     not found yet >=   9.828665053e-09        (985; 10)
+132123: mip =     not found yet >=   9.828665053e-09        (992; 10)
+132551: mip =     not found yet >=   9.828665053e-09        (998; 10)
+132715: mip =     not found yet >=   9.828665053e-09        (1003; 11)
+132784: mip =     not found yet >=   9.828665053e-09        (1004; 11)
+132853: mip =     not found yet >=   9.828665053e-09        (1006; 11)
+132902: mip =     not found yet >=   9.828665053e-09        (1007; 11)
Time used: 3407.2 secs.  Memory used: 161.3 Mb.
+132995: mip =     not found yet >=   9.828665053e-09        (1009; 11)
+133034: mip =     not found yet >=   9.828665053e-09        (1010; 11)
+133110: mip =     not found yet >=   9.828665053e-09        (1011; 11)
+133203: mip =     not found yet >=   9.828665053e-09        (1012; 11)
+133270: mip =     not found yet >=   9.828665053e-09        (1013; 11)
+133327: mip =     not found yet >=   9.828665053e-09        (1014; 11)
+133398: mip =     not found yet >=   9.828665053e-09        (1015; 11)
+133429: mip =     not found yet >=   9.828665053e-09        (1016; 11)
+133488: mip =     not found yet >=   9.828665053e-09        (1017; 11)
+133538: mip =     not found yet >=   9.828665053e-09        (1018; 11)
+133558: mip =     not found yet >=   9.828665053e-09        (1019; 11)
Time used: 3470.9 secs.  Memory used: 161.6 Mb.
+133629: mip =     not found yet >=   9.828665053e-09        (1020; 11)
+133657: mip =     not found yet >=   9.828665053e-09        (1021; 11)
+133792: mip =     not found yet >=   9.828665053e-09        (1023; 11)
+133920: mip =     not found yet >=   9.828665053e-09        (1025; 11)
+134088: mip =     not found yet >=   9.828665053e-09        (1027; 11)
+134144: mip =     not found yet >=   9.828665053e-09        (1028; 11)
+134281: mip =     not found yet >=   9.828665053e-09        (1030; 11)
+134387: mip =     not found yet >=   9.828665053e-09        (1032; 11)
Time used: 3534.0 secs.  Memory used: 162.3 Mb.
+134556: mip =     not found yet >=   9.828665053e-09        (1034; 11)
+134759: mip =     not found yet >=   9.828665053e-09        (1036; 11)
+134903: mip =     not found yet >=   9.828665053e-09        (1038; 11)
+135093: mip =     not found yet >=   9.828665053e-09        (1040; 11)
+135336: mip =     not found yet >=   9.828665053e-09        (1042; 11)
+135488: mip =     not found yet >=   9.828665053e-09        (1044; 11)
+135762: mip =     not found yet >=   9.828665053e-09        (1046; 11)
Time used: 3597.3 secs.  Memory used: 162.7 Mb.
+135844: mip =     not found yet >=   9.828665053e-09        (1047; 11)
TIME LIMIT EXCEEDED; SEARCH TERMINATED
Time used:   3604.5 secs
Memory used: 178.6 Mb (187305712 bytes)
Writing MIP solution to '80on12Rp50Rs50_1.sol'...
