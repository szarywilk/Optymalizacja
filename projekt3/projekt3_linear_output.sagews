# ten sam algorytm, co w projekt3.sagews, tylko zamiast rozwiązania wypisuje program liniowy 

import numpy as np
import parser

# dodanie pracownika do bossa
def add_empl(tree,employee,boss):
    if tree.get(boss) is None:
        tree[boss] = set()
    tree[boss].add(employee)

# dodanie bossa do pracownika
def add_boss(tree,boss,employee):
    tree[employee] = boss

# tworzenie drzewa wszystkich pracowników bossa
def empl_tree(tree):
    out_tree = {}
    for employee,_ in tree.iteritems():
        boss = tree.get(employee)
        while boss is not None:
            add_empl(out_tree,employee,boss)
            boss = tree.get(boss)
    return out_tree

# sprawdzenie, czy i jest bossem j
def is_boss(tree, i, j):
    if i == j:
        return True
    if tree.get(i) is not None:
        return j in tree.get(i)
    return False

tree_w = {}
tree_u = {}

f = open(raw_input('Podaj nazwe pliku: '))

N = int(f.readline())

# sczytywanie linijek
lista=[]
for i in xrange(N):
    lista.append(map(int,f.readline().split()))

# tworzenie macierzy A:
# 0 i 1 kolumna: numery bossów danego pracownika w WSA i Union 
# 2 i 3 kolmna: wymagana liczba osób w departamencie zarządzanym przez daną osobę
A = []
for i in lista:
    A.append(i)

# tworzenie drzew pracowników obu organizacji:
for i in xrange(N):
    if i != A[i][0]:
        add_boss(tree_w,A[i][0],i)
    if i != A[i][1]:
        add_boss(tree_u,A[i][1],i)

tree_w = empl_tree(tree_w)
tree_u = empl_tree(tree_u)

# tworzenie wektorów ograniczeń: b1 i b2
c1=[]
for i in xrange(N):
    c1.append(A[i][2])
c2=[]
for i in xrange(N):
    c2.append(A[i][3])

b1 = np.transpose(c1)
b2 = np.transpose(c2)

# wypisywanie problemu liniowego

with open('output.sagews', 'w') as outfile:
    outfile.write('N = ' + str(N) + '\n')
    outfile.write('p = MixedIntegerLinearProgram(maximization=False)\n'
                 'v = p.new_variable(real=False)\n')   

    s = ''
    for i in xrange(N):
        s = s + 'v[' + str(i) + '] + '
    s = s[:-3]
    outfile.write('p.set_objective(' + s + ')\n')

    for i in xrange(N):
        s = ''
        if b1[i] != 0:
            for j in xrange(N):
                if is_boss(tree_w, i, j):
                    s = s + 'v[' + str(j) + '] + '
            s = s[:-3]
            s = s + ' >= ' + str(b1[i])
            outfile.write('p.add_constraint('+ s +')\n')

    for i in xrange(N):
        s = ''
        if b2[i] != 0:
            for j in xrange(N):
                if is_boss(tree_u, i, j):
                    s = s + 'v[' + str(j) + '] + '
            s = s[:-3]
            s = s + ' >= ' + str(b2[i])
            outfile.write('p.add_constraint('+ s +')\n')


    outfile.write('for i in xrange(N):\n' '    p.add_constraint(0 <= v[i] <=1)\n')
    outfile.write('print(\'Liczba wszystkich osob to:\')\n'
                 'print(N)\n'
                 'print(\'Maksymalna liczba osob, ktore mozna zwolnic to:\')\n'
                 'print(N - p.solve())\n')

    outfile.write('print(\'Nalezy zwolnic osoby o numerach:\')\n')

    outfile.write('for i in xrange(N):\n' + '    if p.get_values(v[i]) == 0: \n' + '        print(i)\n' + 'print(\'(indeksujac od 0)\')')

f.close()
outfile.close()
