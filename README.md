# orca-scripts
Some of my ORCA 5.0 scripts for automated analysis of DFT calculations. Feel free to use, steal some code or do whatever you like with it. 😉

## orca_states.py
Parses the states of a ORCA 5.0 TD-DFT Calculation to as csv file

use:
```Shell
python orca_states.py FILE.out -t [THRESHOLD]
```
Parameters
* `FILE.out` > ORCA 5.0 output file
* `-t`/`--threshold` minimum rate to be included 1 being 100%

## orca_pop.py
Parses Population Analysis to .txt file

use:
```Shell
python orca_pop.py FILE.out -p [POPULATION] -m [METAL]
```
Parameters:
* `FILE.out` > ORCA 5.0 output file
* `-p`/`--population` Population Method, values: (`mulliken` (default), `loewdin`) (optional)
* `-m`/`--metal` Metal Atom e.g. Hg, Au, La, ... (optional)

Example Output:
<details>

```
#	Sym	Charge	Pop
0	H	0.254273	0.000272
1	Ni	-0.107624	0.005352
2	N	-0.172276	-0.012352
3	N	-0.111769	0.086219
4	N	-0.130648	0.086136
5	N	-0.180918	-0.013780
6	N	-0.209544	0.002165
7	C	-0.227174	0.124466
8	C	-0.228493	-0.014463
9	H	0.152022	-0.000202
10	C	-0.177105	0.084100
11	H	0.161446	-0.003997
12	C	0.022514	0.027617
13	C	0.166352	0.095768
14	C	0.156976	0.019557
15	C	-0.264479	-0.042452
16	H	0.165535	0.002176
17	C	-0.199369	0.049116
18	H	0.161973	-0.001502
19	C	0.077265	-0.084299
20	C	0.119779	0.287380
21	C	0.176976	-0.086449
22	C	-0.271683	0.058499
23	H	0.165434	-0.001684
24	C	-0.197861	-0.048022
25	H	0.162736	0.002184
26	C	0.069496	0.032887
27	C	0.157860	0.085380
28	C	0.121923	0.033472
29	C	-0.261826	0.084049
30	H	0.162587	-0.003698
31	C	-0.180679	-0.011020
32	H	0.155658	-0.000450
33	C	-0.197986	0.126101
34	C	1.581959	-0.007770
35	C	0.095851	-0.007368
36	C	-0.223020	0.003606
37	H	0.138383	-0.000212
38	C	-0.134834	-0.001335
39	H	0.138606	0.000143
40	C	-0.127800	0.003882
41	C	-0.134188	-0.000555
42	H	0.138204	0.000178
43	C	-0.245447	0.006461
44	H	0.147906	-0.000423
45	C	0.096494	-0.018311
46	C	-0.222799	0.015818
47	H	0.138694	-0.000579
48	C	-0.134879	-0.006106
49	H	0.137820	0.000544
50	C	-0.129441	0.012962
51	C	-0.135055	-0.006315
52	H	0.137692	0.000693
53	C	-0.247872	0.016263
54	H	0.150125	-0.000576
55	C	0.092262	-0.005451
56	C	-0.240678	0.004773
57	H	0.152577	-0.000195
58	C	-0.136814	-0.001569
59	H	0.138458	0.000249
60	C	-0.126834	0.004056
61	C	-0.134315	-0.000470
62	H	0.138237	0.000081
63	C	-0.224465	0.005747
64	H	0.139516	-0.000239
65	C	-0.256941	-0.006730
66	C	-0.254505	0.003409
67	H	0.136991	0.000412
68	C	-0.111260	-0.000194
69	H	0.136630	-0.000025
70	C	-0.143151	-0.000531
71	C	-0.165278	0.000601
72	H	0.135078	-0.000021
73	C	-0.155327	0.000443
74	H	0.160979	0.000069
75	C	-0.269032	0.018060
76	C	-0.323791	-0.002071
77	H	0.140175	-0.000245
78	C	-0.183559	0.001716
79	H	0.133077	0.000278
80	C	-0.149073	-0.000966
81	H	0.157422	0.000283
82	H	0.139930	-0.000208
83	H	0.136508	0.000083
84	H	0.139369	-0.000676
85	H	0.140046	-0.000194
Sum of charges: 0.0
Sum of populations: 1.0
Sum of Non-Metal-Charges: 0.1076
Sum of Non-Metal-Populations: 0.9946
Metal-Charge: -0.1076
Metal-Population: 0.0054
```

</details>

## orca_energies.py
Parses Energies of all calculations (containing a frequency calculation) from *`_property.txt`-file and writes it to a csv file

use:
```Shell
python orca_energies.py FOLDER
```

Parameters:
* `FOLDER` Path to folder

## suborca5.py
creates new shell script based on template file `orca5_submit.sh` and starts an orca 5.0 calculation on our slurm system

use:
```Shell
python suborca5.py PATH.inp [PARTITION]
```
Parameters 
* `PATH.inp` > ORCA 5.0 input file
* `PARTITION` (optional), values: (NONE, `mem`, `hdd`)

e.g.
```Shell
python suborca5.py H2_opt_b3lyp.inp mem
```
