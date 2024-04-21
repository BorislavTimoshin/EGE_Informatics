s = """71	14	76	87	97	18	31	50	81	45	81	89	48	23	100	98	57	18	68
80	71	18	76	95	49	42	50	56	53	45	91	27	80	88	69	36	80	99
37	54	69	31	34	16	92	47	73	28	86	99	14	30	96	44	48	69	34
86	96	24	39	93	44	11	18	64	90	70	79	24	88	31	49	91	44	56
92	15	61	39	18	61	40	68	97	77	73	75	36	33	65	40	72	69	32
16	49	39	94	15	38	68	75	73	65	29	32	87	50	19	24	87	20	85
25	31	53	21	20	98	34	76	39	34	44	59	93	100	42	51	35	67	38
51	63	68	17	87	87	10	77	31	32	71	27	40	52	85	73	15	43	62
18	10	50	92	27	58	58	13	29	82	88	43	30	19	13	44	35	44	21
24	99	99	96	23	72	28	19	47	97	96	99	98	90	37	80	76	37	36
23	30	50	64	62	87	66	59	91	56	95	84	64	90	69	76	25	19	42
91	67	41	79	80	19	97	48	66	40	25	46	50	40	64	86	18	40	95
52	62	50	74	13	54	39	21	37	17	63	54	13	68	63	14	70	79	65
88	28	96	89	22	35	80	12	53	27	75	62	40	31	59	88	59	19	17
10	15	89	78	21	41	71	38	40	89	11	25	50	20	64	24	16	47	83
13	21	82	44	15	35	60	78	10	27	53	78	93	21	99	18	87	47	15
89	32	42	94	70	20	60	94	50	10	79	84	65	30	29	83	59	70	38
57	89	100	15	81	33	13	76	97	40	21	79	61	11	30	94	71	55	59
16	80	86	26	49	98	90	49	92	36	50	60	54	51	92	24	91	77	10
""".split()

s = list(map(int, s))
matrix = []
for i in range(0, 19 * 19, 19):
    matrix.append(s[i:i + 19])

inaccessible_cells_for_down = [
    (10, 2), (10, 3), (10, 4), (10, 5),
    (5, 4), (5, 5), (5, 6), (5, 7),
    (2, 8), (2, 9), (2, 10), (2, 11),
    (13, 7), (13, 8), (13, 9), (13, 10),
    (9, 13), (9, 14), (9, 15), (9, 16)
]
inaccessible_cells_for_right = [
    (10, 6), (11, 6), (12, 6), (13, 6),
    (5, 8), (6, 8), (7, 8), (8, 8),
    (2, 12), (3, 12), (4, 12), (5, 12),
    (9, 17), (10, 17), (11, 17), (12, 17),
    (13, 11), (14, 11), (15, 11), (16, 11)
]
inaccessible_cells_for_diagonal = inaccessible_cells_for_down + [
    (11, 6), (12, 6), (13, 6), (14, 6),
    (6, 8), (7, 8), (8, 8), (9, 8),
    (3, 12), (4, 12), (5, 12), (6, 12),
    (10, 17), (11, 17), (12, 17), (13, 17),
    (14, 11), (15, 11), (16, 11), (17, 11)
]
min_sum = 1e12
min_lenght = 1e12


def rec(y, x, summa, lenght):
    global min_sum, min_lenght
    if summa > min_sum:
        return
    if y == 18 and x == 18:
        if summa < min_sum:
            min_sum = summa
            min_lenght = lenght
        elif summa == min_sum:
            if lenght < min_lenght:
                min_lenght = lenght
        return
    if x == 18:
        if (y + 1, x) not in inaccessible_cells_for_down:
            rec(y + 1, x, summa + matrix[y + 1][x], lenght + 1)
        return
    if y == 18:
        if (y, x + 1) not in inaccessible_cells_for_right:
            rec(y, x + 1, summa + matrix[y][x + 1], lenght + 1)
        return
    if (y, x + 1) not in inaccessible_cells_for_right:
        rec(y, x + 1, summa + matrix[y][x + 1], lenght + 1)
    if (y + 1, x) not in inaccessible_cells_for_down:
        rec(y + 1, x, summa + matrix[y + 1][x], lenght + 1)
    if (y + 1, x + 1) not in inaccessible_cells_for_diagonal:
        rec(y + 1, x + 1, summa + matrix[y + 1][x + 1], lenght + 1)


rec(0, 0, matrix[0][0], 1)
print(min_sum, min_lenght)
