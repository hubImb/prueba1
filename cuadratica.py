import math
coef_a=float(input("Ingrese el coefciente a: "))
coef_b=float(input("Ingrese el coefciente b: "))
coef_c=float(input("Ingrese el coefciente c: "))
x1=0
x2=0
determinante=coef_b**2-4*coef_a*coef_c
if determinante>=0:
  if coef_a==0:
    x1=(-coef_c)/(coef_b)
    print(x1)
  else:
    if determinante==0:
      x1=-coef_b/(2*coef_a)
      print(x1)
    else:
      x1=(-coef_b+math.sqrt(determinante))/(2*coef_a)
      x2=(-coef_b-math.sqrt(determinante))/(2*coef_a)
      print(x1)
      print(x2)
else:
  print("La ecuacion no tiene soluciones reales")