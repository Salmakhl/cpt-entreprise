from class_produit import*
from class_composition import*
from class_elementaire import*
from class_compose import*

p1 = elementaie("produit1","code", 234)
p2 = elementaie("produit2","code",345)
print(p1)

c1 = compose("name","code",28 ,[p1,p2])
print(c1)
co = composition(p1,3435)
print(co)