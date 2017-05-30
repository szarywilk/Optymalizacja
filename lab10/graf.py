#znajdujemy najmniejsze pokrycie wierzchołkowe danego grafu

p = MixedIntegerLinearProgram(maximization=False)
y = p.new_variable(real=True)

#każdemu wierzchołkowi y[i] przypisujemy taką samą wagę (równą 1)

p.set_objective(y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7]+y[8]+y[9]+y[10]+y[11]+y[12]+y[13])

#uwzględniamy wszystkie krawędzie (dla każdej krawędzi co najmniej jeden z jej końców należy do najmniejszego pokrycia)
 
p.add_constraint(y[0]+y[7]>=1)
p.add_constraint(y[0]+y[9]>=1)
p.add_constraint(y[0]+y[12]>=1)
p.add_constraint(y[1]+y[7]>=1)
p.add_constraint(y[1]+y[10]>=1)
p.add_constraint(y[2]+y[8]>=1)
p.add_constraint(y[2]+y[9]>=1)
p.add_constraint(y[2]+y[11]>=1)
p.add_constraint(y[3]+y[7]>=1)
p.add_constraint(y[3]+y[10]>=1)
p.add_constraint(y[3]+y[13]>=1)
p.add_constraint(y[4]+y[8]>=1)
p.add_constraint(y[4]+y[13]>=1)
p.add_constraint(y[5]+y[8]>=1)
p.add_constraint(y[5]+y[11]>=1)
p.add_constraint(y[5]+y[12]>=1)
p.add_constraint(y[6]+y[9]>=1)
p.add_constraint(y[6]+y[13]>=1)

#problem zrelaksowany (dla całkowitoliczbowego 1/0 oznacza przynależność wierzchołka do pokrycia)

for i in (0, 14):
    p.add_constraint(0<=y[i]<=1)

p.solve()

v = p.get_values(y)
print(v)
