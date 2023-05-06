vk_form=['x=x0+sx   y=y0+sy','sx=x-x0   sy=y-y0','s=√(Sx^2+Sy^2)  jeb  s= √((x-x0)^2+(y-y0)^2 )','x=x0+v∙t','x=x0+v0∙t+(a∙t^2)/2','a=(v-v0)/t',]
vk=['x - pārvietojuma vektora galapunkts x koordināte // x0 - pārvietojuma v. x sākumpunkts k. // sx - pārvietojuma v. projekcija x k. ///' + ' y - pārvietojuma vektora galapunkts y koordināte // y0 - pārvietojuma v. y sākumpunkts k. // sy - pārvietojuma v. projekcija y k.',
    'x - pārvietojuma vektora galapunkts x koordināte // x0 - pārvietojuma v. x sākumpunkts k. // sx - pārvietojuma v. projekcija x k. ///' + ' y - pārvietojuma vektora galapunkts y koordināte // y0 - pārvietojuma v. y sākumpunkts k. // sy - pārvietojuma v. projekcija y k.',
    's - pārvietojums // sx - pārvietojuma vektora projekcija x koordināte // sy - pārvietojuma v. projekcija y k. ///' + ' x - pārvietojuma vektora galapunkts x koordināte // x0 - pārvietojuma v. x sākumpunkts k. // y - pārvietojuma vektora galapunkts y koordināte // y0 - pārvietojuma v. y sākumpunkts k.',
    'x – pārvietojuma vektora galapunkts x koordināte // x0 – pārvietojuma v. x sākumpunkts k. // v – ātrums, m/s // t – laiks, s',
    'x – pārvietojuma vektora galapunkts x koordināte // x0 – pārvietojuma v. x sākumpunkts k. // v0 – sākuma ātrums, m/s // t - laiks, s // a - paātrinājums, m/s^2',
    'a – paātrinājums, m/s^2 // v – ātrums, m/s // v0 – sākuma ātrums, m/s // t – laiks, s']

ed_form=['A=F∙l∙cosa  jeb  A=∆E','Ek=(m∙v^2)/2','Ep=m∙g∙h','E=Ek+Ep  jeb  E=(m∙v^2)/2+m∙g∙h','Ep(d)=(k∙(∆x)^2)/2']
ed=["A – darbs, J // F – spēks, N // l - ceļš, m // a - leņķis starp pārvietojuma un spēka pielikšanas virzieniem ///" + ' A – darbs, J // ∆E - enerģijas izmaiņa, J',
    "Ek – kinetiskā enerģija, J // m – masa, kg // v - ātrums, m/s",
    "Ep – potenciālā enerģija, J // m – masa, kg // g – brīvās krišanas paātrinājums, m/s^2 // h - augstums, m",
    "E - pilnā mehāniskā enerģija, J // Ek – kinetiskā enerģija, J // Ep – potenciālā enerģija, J ///" + ' E - pilnā mehāniskā enerģija, J // m – masa, kg // v - ātrums, m/s // g – brīvās krišanas paātrinājums. m/s^2 // h - augstums, m',
    "Ep(d) – deformēta ķermeņa potenciālā enerģija, J // k – elastības (stinguma) koeficients // ∆x – pagarinājums, m"]

sm_form=['F=m∙a','F1=F2','F=m∙g','μ=Fv/(m∙g) jeb μ=Fb/Fr','Fr=m∙g vai Fr=Fs' ,'Fb=μ∙Fr','Fv=Fb vai Fv=μ∙m∙g']
sm=['F – spēks, N // m – ķermeņa masa, kg // a - paātrinājums, m/s^2',
    'F1 – pirmajam ķermenim pieliektais spēks, N // F2 – otrajam ķermenim pieliktais spēks, N',
    'F – spēks, N // m – ķermeņa masa, kg // g – brīvās krišanas paātrinājums, m/s^2',
    'μ - berzes koeficients // Fv – vilcējspēks, N // m – ķermeņa masa, kg // g - brīvās krišanas paātrinājums, m/s^2 /// Fb – berzes spēks, N // Fr – balsta reakcijas spēks, N',
    'Fr - balsta reakcijas spēks, N // m – ķermeņa masa, kg // g - brīvās krišanas paātrinājums, m/s^2 /// Fs – smaguma spēks, N',
    'Fb – berzes spēks, N // μ - berzes koeficients // Fr – balsta reakcijas spēks, N',
    'Fv – vilcējspēks, N // Fb – berzes spēks, N // μ - berzes koeficients // m – ķermeņa masa, kg // g - brīvās krišanas paātrinājums, m/s^2']

vpk_form=['y=h-((g∙t^2)/2)   v=g∙t    h=(g∙t^2)/2','v=v0+g∙t   h=v0t+g∙t   h=(v0^2)/(2∙g)  tp=v0/g   h=v0∙t-(g∙t^2/2)','T=t/N vai T=1/v', 'ϑ=N/t vai ϑ=1/T', 'v=(2π∙R)/T=2π∙R∙ϑ']
vpk=['y - koordināta // h - augstums, m // g – brīvās krišanas paātrinājums, m/s^2 // t - laiks, s // v - ātrums, m/s',
     'v - ātrums, m/s // v0 – sākuma ātrums, m/s // g - brīvās krišanas paātrinājums, m/s^2 // t - laiks, s // h - augstums, m // tp - pacelšanās laiks, s',
     'v - ātrums, m/s // v0 – sākuma ātrums, m/s // vy – ātrums uz y ass, m/s', 
     'T - periods, s // t - laiks, s // N – apgriezienu skaits // v - ātrums, m/s',
     'ϑ - frekvence, Hz // N – apgriezienu skaits // t – laiks, s // T - periods, s',
     'v - ātrums, m/s // R – riņķa līnijas rādiuss, m // T - periods, s // ϑ  - frekvence, Hz']

print("Ievadiet temu -")
a=int(input("1-Vektori un kustība; 2-Enerģija un darbs; 3-Spēks un mijiedarbība; 4-Vienmērīgi paātrināta kustība -" ))
while a<1 or a>4:
    print('Tādas tēmas nav, ievadiet vēlreiz - ')
    a=int(input("1-Vektori un kustība; 2-Enerģija un darbs; 3-Spēks un mijiedarbība; 4-Vienmērīgi paātrināta kustība -" ))
if a==1:
    print("Izvēlieties formulu - ")
    c=int(input("0-Vektora gala punktu koordinātu noteikšanai; 1-Projekciju aprēķināšana; 2-Vektora moduļa aprēķināšana; 3-Kustības koordinātes vienādojums; 4-Vienmērīgi paātrinātas Taisnlīnijas kustības pilnais koordinātas vienādojums; 5-Paātrinājums - "))
    if 0<=c<6:
        print(vk_form[c])
        print('Vai ir nepieciešams izvadīt formulas lielumu apzīmējumus- ')
        s=int(input('Jā- 1, Nē- 2 - '))
        if s==1:
            print(vk[c])
        elif s==2:
            print(' ')                
elif a==2:
    print("Izvēlieties formulu - ")
    c=int(input("0-Darbs; 1-Kinētiskā enerģija; 2-Potenciālā enerģija; 3-Pilnā mehāniskā enerģija; 4-Deformēta ķermeņa potenciālā enerģija - "))
    if 0<=c<4:
        print(ed_form[c])
        print('Vai ir nepieciešams izvadīt formulas lielumu apzīmējumus- ')
        s=int(input('Jā- 1, Nē- 2 - '))
        if s==1:
            print(ed[c])
        elif s==2:
            print(' ')          
      
elif a==3:
    print("Izvēlieties formulu - ")
    c=int(input("0-Otrais Ņūtona likums; 1-Trešais Ņūtona likums; 2-Zemes pievilkšanas spēks; 3-Berzes koeficients; 4-Balsta reakcijas spēks; 5-Slīdes berzes spēks; 6-Vilcējspēks - "))
    if 0<=c<7:
        print(sm_form[c])   
        print('Vai ir nepieciešams izvadīt formulas lielumu apzīmējumus - ')
        s=int(input('Jā- 1, Nē- 2 - '))
        if s==1:
            print(sm[c])
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
            print(vpk[c])
        elif s==2:
            print(' ')          
           

    
    
    