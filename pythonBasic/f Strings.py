# F strings
import math
me = "harry"
a1=3
# a = "this is %s %s" %(me, a1)
# a= "This is {1} {0}"
# b=a.format(me, a1)
# print(a)
# print(b)
a = f"This is {me} {a1} {4*450} {math.cos(90)}"
print(a)

