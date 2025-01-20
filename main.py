#creating sets
A={1,2,3,4,5,6}
B={5,6,7,8,4,2}
#union of sets
print(A|B)
print(A.union(B))
#intersection of sets
print(A&B)
print(A.intersection(B))
#difference of sets
print(A-B)
#conversion of list to set
my_list=[1,2,3,4]
my_set = set(my_list)
print(my_set)
#symmetric difference
print(A.symmetric_difference(B))
print(A^B)
#adding element to empty set
numset=set([])
numset.add(6)
numset.add(8)
numset.add(7)
numset.add(3)
print(numset)
#removing an element from the set
numset.remove(6)
numset.discard(8)
print(numset)