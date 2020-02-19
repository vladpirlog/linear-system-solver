"""
        Functia 'program' primeste ca argument un fisier ce contine, pe prima linie, numarul de ecuatii si cel
    de necunoscute, iar pe urmatoarele linii, matricea sistemului (nr_ecuatii linii, fiecare cu cate
    nr_necunoscute valori, separate prin spatiu).
        Functia intoarce o lista de tupluri, reprezentand sistemul fundamental de solutii al sistemului omogen
    asociat matricii date. De asemenea, se scriu in fisier necunoscutele principale in functie de cele secundare.
"""


# Functie de afisare pentru o matrice.

def print_matrix(m):
    for line in m:
        for el in line:
            print(str(el).ljust(12), end='')
        print()
    print()


def program(file):
    # matrix = matricea coeficientilor
    # nr_ecuatii = numarul de ecuatii
    # nr_necunoscute = numarul de necunoscute
    matrix = []
    with open(file, 'r') as f:
        nr_ecuatii, nr_necunoscute = map(int, f.readline().split())
        for line in f:
            matrix.append(list(map(float, line.split())))

    # In cazul in care nu exista ecuatii sau necunoscute, se returneaza None.

    if nr_necunoscute == 0 or nr_ecuatii == 0:
        return None

    # Se aduce sistemul la forma Gauss (se creeaza zerouri sub diagonala principala).

    for i in range(nr_necunoscute):
        for j in range(i, nr_ecuatii):
            if matrix[j][i] != 0:
                temp = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = temp
                break
        for j in range(i + 1, nr_ecuatii):
            if matrix[j][i] != 0 and matrix[i][i] != 0:
                rap = matrix[j][i] / matrix[i][i]
                for k in range(nr_necunoscute):
                    matrix[j][k] = matrix[j][k] - (rap * matrix[i][k])

    # Se creeaza o noua matrice fara liniile ce contin doar zerouri.

    new_matrix = [line for line in matrix if any(line)]

    if len(new_matrix) == 0:

        # Daca lungimea noii matrici este 0, atunci orice solutie reala este acceptata.

        return [tuple(['x[{}]'.format(x + 1) for x in range(nr_necunoscute)])]
    elif len(new_matrix) == nr_necunoscute:

        # Daca lungimea noii matrici este egala cu nr de necunoscute, atunci singura solutie acceptata
        # este solutia nula (sistemul este compatibil determinat).

        return [tuple([0] * nr_necunoscute)]
    else:
        # Necunoscutele principale sunt cele ce vor fi scrise in functie de celelalte necunoscute.

        nr_necunoscute_principale = len(new_matrix)

        # ind_nec_princ = lista indicilor necunoscutelor principale; aceasta reprezinta, de asemenea, indicii coloanelor
        #                 ce compun minorul principal, despre care stim sigur ca are determinantul nenul
        # ind_nec_sec = lista indicilor necunoscutelor secundare (cele ce nu se scriu in functie de celalte necunoscute)

        ind_nec_princ = []
        for k in range(nr_necunoscute):
            if new_matrix[-1][k] != 0:
                ind_nec_princ = list(
                    range(k - nr_necunoscute_principale + 1, k + 1))
                break

        ind_nec_sec = [elem for elem in range(
            nr_necunoscute) if elem not in ind_nec_princ]

        # Se scrie fiecare necunoscuta principala doar in functie de cele secundare;
        # in acest moment, coeficientii necunoscutelor pot avea orice valoare.

        for i in ind_nec_princ:
            for j in range(i - ind_nec_princ[0]):
                if new_matrix[i - ind_nec_princ[0]][i] != 0:
                    div = -new_matrix[j][i] / \
                        new_matrix[i - ind_nec_princ[0]][i]
                    for k in range(nr_necunoscute):
                        new_matrix[j][k] = new_matrix[i -
                                                      ind_nec_princ[0]][k] * div + new_matrix[j][k]

        # Coeficientul necunoscutelor principale se aduce la valoarea -1; astfel, se pot citi coeficientii
        # necunoscutei de pe linia corespunzatoare din matrice.

        # De exemplu, pentru linia [-1, 0, 0, 2, 3] se deduce faptul ca -x[1] + 2 * x[4] + 3 * x[5] = 0, de unde
        # rezulta ca x[1] = 2 * x[4] + 3 * x[5].

        for i in ind_nec_princ:
            div = -new_matrix[i - ind_nec_princ[0]][i]
            for k in range(nr_necunoscute):
                if div != 0:
                    new_matrix[i - ind_nec_princ[0]][k] = round(
                        new_matrix[i - ind_nec_princ[0]][k] / div, 4)

        # Se inlocuiesc valorile de -0.0 din matrice cu 0.0.

        for i in range(len(new_matrix)):
            for j in range(nr_necunoscute):
                if new_matrix[i][j] == 0:
                    new_matrix[i][j] = 0.0

        # Se scriu in fisier solutiile de forma x[n] = ... + a[k] * x[k] + a[k + 1] * x[k + 1] + ...

        with open(str(file).replace('.in', '.out').replace('input', 'output'), 'w') as g:
            for i in ind_nec_princ:
                res = ''
                for j in ind_nec_sec:
                    if matrix[i - ind_nec_princ[0]][j] > 0:
                        res += ' + {} * x[{}]'.format(
                            matrix[i - ind_nec_princ[0]][j], j + 1)
                    elif matrix[i - ind_nec_princ[0]][j] < 0:
                        res += ' - {} * x[{}]'.format(-matrix[i -
                                                              ind_nec_princ[0]][j], j + 1)
                if res == '':
                    res = ' 0 '
                g.write('x[{}] ='.format(i + 1) + res + '\n')

        # Pentru fiecare necunoscuta secundara, se adauga la new_matrix linii ce contin 1 la indicele necunoscutei
        # respective si 0 in rest. Aceste linii ajuta la extragerea sistemului fundamental de solutii din matrice.

        # De exemplu, pentru necunoscuta secundara x[4], se va adauga linia [0, 0, 0, 1, 0].

        for i in ind_nec_sec:
            line_to_add = [0.0] * nr_necunoscute
            line_to_add[i] = 1.0
            new_matrix.insert(i, line_to_add)

        # sol = lista de tupluri ce reprezinta sistemul fundamental de solutii

        sol = []
        for i in ind_nec_sec:
            sol.append(tuple([line[i] for line in new_matrix]))

        return sol
