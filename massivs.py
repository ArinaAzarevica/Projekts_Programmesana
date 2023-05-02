ed_form=['A=F∙S∙cosa','A=E','Ek=(m∙v^2)/2','Ep=m∙g∙h','Ep=m∙g∙h','Ep(d)=(k∙(∆x)^2)/2','∆Ep(d)=A','Fe=k∙|∆x|','A=F∆x','E=Ek+Ep']
ed=["0-Darbs; 1-Darbs; 1-Kinētiskā enerģija; 3-Potenciala energija - "]
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
    c=int(input("0-Darbs; 1-Darbs; 2-Kinētiskā enerģija; 3-Potenciala energija - "))
    if 0<=c<4:
        print(ed_form[c])
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