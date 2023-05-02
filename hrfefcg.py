a=int(input("Izvēlies formulu - "))
if a==1:
    b=int(input("1-Projekciju aprēķināšana; 2-Vektora moduļa aprēķināšana - "))
    if b==1:
        print("sx=x-x0")
    elif b==2:
        print("√(S^2+Sy^2)")
    else:
        print('fhd')
elif a==2:
    print("Izvēlies formulu - ")
    c=int(input("1-Darbs; 2-Kinētiskā enerģija; - "))
    if c==1:
        print("A=F ∙S ∙cosa")
        print('vai ir vaj for apz - ')
        s=int(input('ja 1, ne 2 - '))
        if s==1:
            print('gshdx')
        elif s==2:
            print('nekas')
        else:
            print('megini velreiz')
            s=int(input('ja 1 ne 2 - '))
else:
    print('megini velreiz')
    a=int(input("Izvēlies formulu - "))