vk_form=['x=x0+sx   y=y0+sy','sx=x-x0   sy=y-y0','s=√(Sx^2+Sy^2) jeb s= √((x-x0)^2+(y-y0)^2 )','x=x0+vxt','x=x0+v0∙t+(a∙t^2)/2','a=(v-v0)/t',]
vk=['Vektora gala punktu koordinātu noteikšanai','Projekciju aprēķināšana','Vektora moduļa aprēķināšana','Kustības koordinātes vienādojums','Vienmērīgi paātrinātas Taisnlīnijas kustības pilnais koordinātas vienādojums','Paātrinājums']
ed_form=['A=F∙S∙cosa','Ek=(m∙v^2)/2','Ep=m∙g∙h','E=Ek+Ep','Ep(d)=(k∙(∆x)^2)/2']
ed=["0-Darbs; 1-Darbs; 1-Kinētiskā enerģija; 3-Potenciala energija; Pilnā mehāniskā enerģija - "]
sm_form=['F=m∙a','F1=F2','F=m∙g','μ=Fv/(m∙g) jeb μ=Fb/Fr','Fr=m∙g vai Fr=Fs∙m' ,'Fb=μ∙Fr vai Fb=m∙a','Fv=Fb vai Fv=μ∙m∙g']
sm=['Otrais Ņūtona likums','Trešais Ņūtona likums','Zemes pievilkšanas spēks','Berzes koeficients','Balasta reakcijas spēks','Slīdes berzes spēks','Vilcējspējs']
vpk_form=['y=h-((g∙t^2)/2)   v=g∙t    h=(g∙t^2)/2','v=v0+g∙t   h=v0t+g∙t   h=(v0^2)/(2∙g)  tp=v0/g   h=v0∙t-(g∙t^2/2)','v=√(v0^2+vy^2)','vp=v0∙sina  vh=v0∙cosa   ts=(2∙vp)/g   h=vp^2/(2∙g)   l=(2∙vp∙vh)/g','T=t/N vai T=1/v', 'ϑ=N/t vai ϑ=1/T', 'v=(2π∙R)/T=2π∙R∙ϑ']
vkp=['Brīvais kritiens','Vertikāls sviediens','Horizontāls sviediens', 'Slīps sviediens', 'Periods','Frekvence','Kustības lineārais ātrums']

print("Ievadiet temu -")
a=int(input("1-Vektori un kustiba; 2-Energija un darbs; 3-Speks un mijiedarbiba; 4-Vienmerigi paaatrinata kustiba -" ))
if a==1:
    print("Izvēlieties formulu - ")
    c=int(input("0-Vektora gala punktu koordinātu noteikšanai; 1-Projekciju aprēķināšana; 2-Vektora moduļa aprēķināšana; 3-Kustības koordinātes vienādojums; 4-Vienmērīgi paātrinātas Taisnlīnijas kustības pilnais koordinātas vienādojums; 5-Paātrinājums - "))
    if 0<=c<6:
        print(vk_form[c])
        print('Vai ir nepieciešams izvadīt formulas lielumu apzīmējumus- ')
        s=int(input('Jā- 1, Nē- 2 - '))
        if s==1:
            print('gshdx')
        elif s==2:
            print(' ')                
elif a==2:
    print("Izvēlieties formulu - ")
    c=int(input("0-Darbs; 1-Kinētiskā enerģija; 2-Potenciala energija; 3-Pilnā mehāniskā enerģija; 4-Deformēta ķermeņa potenciālā enerģija - "))
    if 0<=c<4:
        print(ed_form[c])
        print('Vai ir nepieciešams izvadīt formulas lielumu apzīmējumus- ')
        s=int(input('Jā- 1, Nē- 2 - '))
        if s==1:
            print('gshdx')
        elif s==2:
            print(' ')          
      
elif a==3:
    print("Izvēlieties formulu - ")
    c=int(input("0-Otrais Ņūtona likums; 1-Trešais Ņūtona likums; 2-Zemes pievilkšanas spēks; 3-Berzes koeficients; 4-Balasta reakcijas spēks; 5-Slīdes berzes spēks; 6-Vilcējspējs - "))
    if 0<=c<7:
        print(sm_form[c])   
        print('Vai ir nepieciešams izvadīt formulas lielumu apzīmējumus - ')
        s=int(input('Jā- 1, Nē- 2 - '))
        if s==1:
            print('gshdx')
        elif s==2:
            print(' ')          
         
elif a==4:
    print("Izvēlieties formulu - ")
    c=int(input("0-Brīvais kritiens; 1-Vertikāls sviediens; 2-Horizontāls sviediens; 3-Slīps sviediens; 4-Periods; 5-Frekvence; 6-Kustības lineārais ātrums' - "))
    if 0<=c<7:
        print(vpk_form[c])  
        print('Vai ir nepieciešams izvadīt formulas lielumu apzīmējumus - ')
        s=int(input('Jā 1, Nē 2 - '))
        if s==1:
            print('gshdx')
        elif s==2:
            print(' ')          
           

    
    
    
