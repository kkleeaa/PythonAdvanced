my_set= {1,2,3}
my_set= set([4,5,6])
print(my_set)

A={34,1,2,54,90,42,87}
B={5,63,29,1,2,90,66,43}

unioni=A.union(B)
print(unioni)

prerje=A.intersection(B)
print(prerje)

diferenca=A.difference(B)
print(diferenca)

A.add(100)
A.remove(100)
A.clear()
print(len(A))
my_list=[3,4,5,3,5,2]
unique_set=set(my_list)
print(unique_set)
colors={'red','green''blue'}
color= "red"
print(color in colors)
print(color not in colors)
