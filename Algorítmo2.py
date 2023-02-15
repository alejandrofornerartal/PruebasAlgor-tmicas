import os, sys

print("Prueba algorítmica 2")
print(" ")

mujeresmayores = 0
hombresmayores = 0
personasmayores = 0
personasmenores = 0
porcentaje_de_mayores = 0
porcentaje_de_menores = 0
for i in range (1, 51):
	print ('Persona ' + repr (i))
	edad = int (input ('Escribe la edad de la persona: : '))
	print ('¿ Qué sexo tiene la persona ?.')
	print ('\t1.- Hombre')
	print ('\t2.- Mujer')
	sys.stdout.write ('\t')
	sexo = 0
	while sexo<1 or sexo>2:
		sexo = int (input (': '))
		if sexo<1 or sexo>2:
			sys.stdout.write ('Error, elige un número 1 o 2.')
	if sexo==1 and edad>=18:
		masculinos_mayores=hombresmayores+1
	if sexo==2 and edad<18:
		femeninasmenores=mujeresmayores+1
	if edad<18:
		personasmenores=personasmenores+1
	else:
		personasmayores=personasmayores+1
	print ()

