#y = ax³+ bx²+cx +d
x = 0
essais = 0
choix1 = int(input("""
1 = polynome de degrès 3 :
2 = polynome de degrès 2 :
3 = ajustement afine :
               """))
if choix1 == 1:
    choix = input('tu veut calculer le x ou le y ?')
    if choix == 'x' :
        print("le mode de précision est de 3 = 0.00 ,  2 = 0.000 et le 1 = 0.00000000000 (le mode de précision influencie grandement la vitesse de calcul)")
        p = int(input("choisie le 1 si tu veut beaucoup de présision choisie 2 si tu veut la moitier et 3 si tu veut pas de précision ?"))
        y = int(input("quelle est la hauteur que tu as ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        d = int(input("quelle est le d"))
        if p == 1 :
            xr = x+0.00001
        if p == 2 :
            xr = x+0.001
        if p == 3 :
            xr = x+0.01
        calcul =  a*x**3 + b*x**2+c*x+d   #pour modifier le + ou le  -
        while calcul<y :
            calcul =  a*x**3 + b*x**2+c*x+d      #pour modifier le + ou le  -
            x+= xr
            essais += 1
        x = 1
        while calcul>y :
            calcul =  a*x**3 + b*x**2+c*x+d #pour modifier le + ou le  -
            x-=xr
            essais += 1

        print(f"{y} = {a}*{x}³+{b}*{x}²+{c}*{x}+{d}  au bout de {essais} essais") #pour modifier le + ou le  -

    elif choix == 'y' :
        x = int(input("quelle est la largeur que tu a ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        d = int(input("quelle est le d"))
        calcul =  a*x**3 + b*x**2+c*x+d  #pour modifier le + ou le  -
        print(f" {calcul} = {a}*{x}³+{b}*{x}²+{c}*{x}+{d} ") #pour modifier le + ou le  -
elif choix1 == 2 :
    choix2 = input('tu veut calculer le x ou le y ?')
    if choix2 == 'x' :
        print("le mode de précision est de 3 = 0.00 ,  2 = 0.000 et le 1 = 0.00000000000 (le mode de précision influencie grandement la vitesse de calcul)")
        p = int(input("choisie le 1 si tu veut beaucoup de présision choisie 2 si tu veut la moitier et 3 si tu veut pas de précision ?"))
        y = int(input("quelle est la hauteur que tu as ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        if p == 1 :
            xr = x+0.00001
        if p == 2 :
            xr = x+0.001
        if p == 3 :
            xr = x+0.01
        calcul = a*x**2 + b*x+c   #pour modifier le + ou le  -
        while calcul <y :
            calcul =  a*x**2 + b*x+c  #pour modifier le + ou le  -
            x+=xr
            essais += 1
        x = 1
        while calcul>y :
            calcul =  a*x**2 + b*x+c    #pour modifier le + ou le  -
            essais += 1
        print(f"{y} = {a}*{x}²+{b}*{x}+{c}")   #pour modifier le + ou le  -
    elif choix2 == 'y' :
        x = int(input("quelle est la largeur que tu a ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        calcul =  a*x**2 + b*x+c   #pour modifier le + ou le  -
        print(f" {calcul} = {a}*{x}²+{b}*{x}+{c} ")   #pour modifier le + ou le  -
# y = ax² + bx + c
if choix1 == 3:#y = ax+b
    choix3 = input('tu veut calculer le x ou le y ?')
    if choix3 == 'x' :
        print("le mode de précision est de 3 = 0.00 ,  2 = 0.000 et le 1 = 0.00000000000 (le mode de précision influencie grandement la vitesse de calcul)")
        p = int(input("choisie le 1 si tu veut beaucoup de présision choisie 2 si tu veut la moitier et 3 si tu veut pas de précision ?"))
        y = int(input("quelle est la hauteur que tu as ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        if p == 1 :
            xr = x+0.00001
        if p == 2 :
            xr = x+0.001
        if p == 3 :
            xr = x+0.01
        x = 0
        calcul = a*x+b   #pour modifier le + ou le  -
        while calcul <y :
            calcul = a*x+b  #pour modifier le + ou le  -
            x+=0.0001
            essais += 1
        x = 1
        while calcul>y :
            calcul =  a*x+b   #pour modifier le + ou le  -
            x-=0.00001
            essais += 1
        print(f"{y} = {a}*{x}+{b} tu a obtenue ce resultat au bout de {essais} essais")  #pour modifier le + ou le  -
    elif choix3 == 'y' :
        x = int(input("quelle est la largeur que tu a ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        calcul = a*x+b  #pour modifier le + ou le  -
        print(f"{calcul} = {a}*{x}+{b}")  #pour modifier le + ou le  -