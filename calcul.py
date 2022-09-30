#y = ax³+ bx²+cx +d
choix1 = input('tu veut faire un polynome de degrès 2 ou un polynome de degrès 3 ? ou un afine ? ')
if choix1 == 'polynome de degrès 3' or choix1 == 'polynome de degres 3':
    choix = input('tu veut calculer le x ou le y ?') 
    if choix == 'x' :
        y = int(input("quelle est la hauteur que tu as ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        d = int(input("quelle est le d"))
        x=0
        calcul =  a*x**3 + b*x**2+c*x+d 
        while calcul<y :
            calcul =  a*x**3 + b*x**2+c*x+d
            x+=0.0001
        x = 1
        while calcul>y :
            calcul =  a*x**3 + b*x**2+c*x+d
            x-=0.00001

        if calcul<y :
            print(f"{y} = {a}*{x}³+{b}*{x}²+{c}*{x}+{d}")
        if calcul>y :
            print(f"{y} = {a}*{x}³+{b}*{x}²+{c}*{x}+{d}")

    elif choix == 'y' :
        x = int(input("quelle est la largeur que tu a ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        d = int(input("quelle est le d"))
        calcul =  a*x**3 + b*x**2+c*x+d
        print(f" {calcul} = {a}*{x}³+{b}*{x}²+{c}*{x}+{d} ")
elif choix1 == 'polynome de degrès 2' or choix1 == 'polynome de degres 2' :
    choix2 = input('tu veut calculer le x ou le y ?')
    if choix2 == 'x' :
        y = int(input("quelle est la hauteur que tu as ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        x = 0
        calcul = a*x**2 + b*x+c
        while calcul <y :
            calcul =  a*x**2 + b*x+c
            x+=0.0001
        x = 1
        while calcul>y :
            calcul =  a*x**2 + b*x+c
            x-=0.00001
        print(f"{y} = {a}*{x}²+{b}*{x}+{c}")
    elif choix2 == 'y' :
        x = int(input("quelle est la largeur que tu a ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        c = int(input("quelle est le c"))
        calcul =  a*x**2 + b*x+c
        print(f" {calcul} = {a}*{x}²+{b}*{x}+{c} ")
# y = ax² + bx + c
if choix1 == 'afine' :#y = ax+b
    choix3 = input('tu veut calculer le x ou le y ?')
    if choix3 == 'x' :
        y = int(input("quelle est la hauteur que tu as ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        x = 0
        calcul = a*x+b
        while calcul <y :
            calcul = a*x+b
            x+=0.0001
            x = 1
        while calcul>y :
            calcul =  a*x+b
            x-=0.00001
        print(f"{y} = {a}*{x}+{b}")
    elif choix3 == 'y' :
        x = int(input("quelle est la largeur que tu a ?"))
        a = int(input("quelle est le a"))
        b = int(input("quelle est le b"))
        calcul = a*x+b
        print(f"{calcul} = {a}*{x}+{b}")