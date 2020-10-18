#La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
#secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
#rosie. 
x=int(input('x='))
if x > 0 and x<=25:
    print('alb')
if x > 25 and x<=50:
    print('rosu')
if x > 50 and x<=75:
    print('albastru')
if x > 75 and x <=100:
    print('negru')