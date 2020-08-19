import csv
import numpy as np

def calculate_avg(coluna):
	soma = 0
	cont = 0
	for i in range(0,len(data[0])):
		if (data[coluna][i]!="?"):
			soma+=data[coluna][i]
			cont+=1

	return soma/cont

def calculate_moda(coluna):
	moda={}
	max=-1
	for j in range(0,len(data)):
		if (data[j][coluna]=="?"):
			continue
		elif (data[j][coluna] in moda):
			moda[data[j][coluna]]=moda[data[j][i]]+1
		else:
			moda[data[j][coluna]]=1	
		if (moda[data[j][coluna]]>max):
			max=moda[data[j][coluna]]
			elem=data[j][coluna]
	return elem

def substitute(coluna, valor):
	print("Substituindo a coluna ", coluna, " com o valor ", valor)
	for j in range (0,len(data)):
		if (data[j][coluna] == "?"):
			data[j][coluna] = valor

#print("Por favor digite o nome do CSV a ser testado")
#nome=input()
nome='crx.csv'
with open(nome, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for i in range(0,len(data[0])):
	temFaltante = False
	eMedia = False
	for j in range (0,len(data)):
		if (data[j][i]=="?"):
			temFaltante = True
		if (isinstance(data[j][i],float)):
			eMedia = True
		if (temFaltante and eMedia):
			break
	
	if (temFaltante):
		if (eMedia):
			substituinte = calculate_avg(i)
		else :
		  substituinte = calculate_moda(i)  
		substitute(i, substituinte)
	

np.savetxt("resultado.csv", data, delimiter=",", fmt='%s')
