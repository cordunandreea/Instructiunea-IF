#Se consideră trei numere întregi. Dacă toate sunt pozitive, să se afişeze numărul mai mare dintre al doilea şi al treilea număr, în
#caz contrar să se calculeze suma primelor două numere. Exemple: Date de intrare 45 23 100 date de ieşire 100 ; Date de
#intrare 34 -25 10 Date de ieşire 9.
n1=int(input('primul nr='))
n2=int(input('al doilea nr='))
n3=int(input('al treilea nr='))
if n1 > 0 and n1 > 0 and n3 > 0:
    if n2 > n3:
        print(n2)
    if n2 < n3:
        print(n3)
else:
    print(n1+n2)    