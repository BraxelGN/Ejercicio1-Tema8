
f=open('placas.txt','r')
datos=f.read()
f.close()
print(datos)

f=open('placas.txt','w')
lista=[
    'un auto',
    'dos autos',
    'tres autos',
]
f.writelines(lista)
f.close()








