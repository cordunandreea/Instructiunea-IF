#Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
#câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
#numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
#Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
#bilelor: 17 Mari: 11 bile Verzi: 7 bile .
#bile mici - a
#bile mari - b
aa=int(input('bile mici albe='))
ba=int(input('bile mari albe='))
ar=int(input('bile mici rosii='))
br=int(input('bile mari rosii='))
av=int(input('bile mici verzi='))
bv=int(input('bile mari verzi='))
total=aa+ba+ar+br+av+bv
print('totalul bilelor:', total)
atotal=aa+ar+av
btotal=ba+br+bv
if btotal > atotal:
    print('mari:',btotal)
else:
    print('mici:', atotal)
a=aa+ba
r=ar+br
v=av+bv
if a > r and a > v:
    print('albe:',a)
if r > a and r > v:
    print('rosii:',r)
if v > a and v > r:
    print('verzi:',v)