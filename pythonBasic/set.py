s= set()
#print(type(s))
#l=[1,2,3,4]
#s_from_set= set(l)
#print(s_from_set)
s.add(1)
s.add(2)
s1= s.union({1,2,3})
s2= s.intersection({1,2,3})
print(s, s1, s2)
print(len(s))
