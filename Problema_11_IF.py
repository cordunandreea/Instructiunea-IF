#Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau
#IMPAR. Exemplu : Date de intrare : 45 3 24 Date de ieşire : 45 impar 3 impar 24 par.
n1=int(input('primul nr='))
n2=int(input('al doilea nr='))
n3=int(input('al treilea nr='))
r1=n1%2
r2=n2%2
r3=n3%2
if r1==0:
    print(n1)
    print('par')
else:
    print(n1)
    print('impar')
if r2==0:
    print(n2)
    print('par')
else:
    print(n2)
    print('impar')
if r3==0:
    print(n3)
    print('par')
else:
    print(n3)
    print('impar')