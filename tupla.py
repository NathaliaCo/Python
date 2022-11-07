# crea una tupla llamada t con 3 elementos, 1 lista y 1 conjunto
t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe')

# imprime la tupla t
print (t)

# indica la cantidad de caracteres dentro de la tupla (5)
print (len(t))

# imprime los signos dentro de las comillas creando un espacio
print ('=====================================')

# imprime el caracter en la posición 0 (23)
print (t[0])

# imprime el caracter en la posición 3 ["perrito, "gatito]
print (t[3])

# imprime desde el caracter en la posición 1 hasta el caratcer en la posición 2
print (t[1:3])

# imprime el elemento en la posición 1 del caracter en la posición 3
print (t[3][1])

# imprime los signos dentro de las comillas creando un espacio
print ('====================================')

# imprime el caracter en la posición 3 ["perrito, "gatito]
print (t[3])

# con el método append se agrega un elemento ('lorito') a la lista (caracter) que se encuentra en la posicón 3 de la tupla
t[3].append('lorito')

# imprime la tupla con la modificación
print (t)

# imprime los signos dentro de las comillas creando un espacio
print ('====================================')

# se recorre e imprime los elementos de la tupla t 
for elemento in t:
    print (elemento)

# imprime los signos dentro de las comillas creando un espacio
print ('====================================')

# recorre e imprime los caracteres empezando en 0 y acabando en la cantidad de caracteres de la tupla (5)
for index in range(0,len(t)):
    print (t[index])

# imprime los signos dentro de las comillas creando un espacio
print ('====================================')

#recorre el elemento 'a' dentro del interable (tupla) e imprime "El elemento 'a' esta en la tupla"
if 'a' in t:
    print ("El elemento 'a' esta en la tupla")

# imprime los signos dentro de las comillas creando un espacio
print ('====================================')

# crea una lista de la tupla y determina que el caracter en la posición 1 de la lista es 'A' e imprime la lista
lista=list(t)
lista[1]='A'
print (lista)

# crea una tupla de la lista e imprime la tupla creada
tupla=tuple(lista)
print (tupla)

# imprime los signos dentro de las comillas creando un espacio
print ('====================================')

# crea una lista llamada l con 5 caracteres 
l = [(1,1), (2,4), (3,9), (4,16), (5,25)]

# recorre los elementos x de la lista y ejecuta que se imprima el primer elemento de cada conjunto (caracteres) seguido de : y el segundo elemento del conjunto
for x, y in l:
    print (x, ':', y)
