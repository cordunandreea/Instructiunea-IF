#La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
#fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
#afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
#numărul de boabe de porumb. Exemplu: Date de intrare 100 4050 Date de ieşire: Curcanul mai mult cu 10 boabe.
a=int(input('nr de gaini='))
b=int(input('nr de boabe de porumb='))
c=b//a
d=b-c*a
if c < d:
    print('Curcanul mai mult cu',d-c, 'boabe')
if c > d:
    print('Gainile mai mult cu',c-d, 'boabe')
if c == d:
    print('egalitate')