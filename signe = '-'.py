a = int(input("quelle est le a ?"))
b = int(input("quelle est le b ?"))
c = int(input("quelle est le c?"))
d = int(input("quelle est le d ?"))
x = int(input("quelle est la largeur que tu veut ?"))
signe = input('quelle est le signe que tu veut entre le a et b ? : ')
if signe == '-' :
    calcul = a*x**3 - b*x**2
elif signe == '+' :
    calcul = a*x**3 + b*x**2
signe2 = input('quelle est le signe que tu veut entre b et c ? :  ')
if signe2 == '+' :
    calcul = calcul+c*x
if signe2 == '-' :
    calcul = calcul-c*x
signe3 = input('quelle est le signe que tu veut entre c et d ? :  ')
if signe3 == '+' :
    calcul = calcul+d
if signe3 == '-' :
    calcul = calcul-d
print(f"{calcul} = {a}*{x}**3{signe}{b}*{x}**2{signe2}{c}*{x}{signe3}{d}")

