#“Mă iubeşte un pic, mult, cu pasiune, la nebunie, deloc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă
#iubeşte …. Exemplu: Date de intrare: x=10 Date de ieşire: … deloc.
x=int(input('margareta are:'))
if x%2==0:
    print('mult')
if x%3==0:
    print('cu pasiune')
if x%4==0:
    print('la nebunie')
if x%5==0:
    print('deloc')
else:
    print('un pic')