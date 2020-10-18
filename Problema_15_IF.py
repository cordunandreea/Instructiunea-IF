#Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
#ce clasa va fi repartizat (A, B, C, D sau E)?. Exemplu : date de intrare : x=73 date de ieşire : C.
x=int(input('x='))
if x > 0 and x<=25:
    print('A')
if x > 25 and x<=50:
    print('B')
if x > 50 and x<=75:
    print('C')
if x > 75 and x<=100:
    print('D')
if x > 100 and x<=125:
    print('E')