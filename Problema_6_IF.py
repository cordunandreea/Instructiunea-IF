#Andrei primeşte într-o zi trei note, nu toate bune. Se hotărăşte ca, dacă ultima notă este cel puţin 8, să le spună părinţilor toate
#notele primite iar dacă este mai mică decât 8, să le comunice doar cea mai mare notă dintre primele două. Introduceţi notele
#luate şi afişaţi notele pe care le va comunica părinţilor. Exemple : Date de intrare 6 9 9 Date de ieşire 6 9 9 ; Date de
#intrare 8 5 7 Date de ieşire 8.
n1=int(input('prima nota='))
n2=int(input('a doua nota='))
n3=int(input('a treia nota='))
if 0 > n1 > 10 or 0 > n2 > 10 or 0 > n3 > 10:
    print('nota invalida')
else:
 if n3>=8:
     print(n1, n2, n3)
 if n3<8:
     if n1 > n2:
         print(n1)
     else:
         print(n2)
