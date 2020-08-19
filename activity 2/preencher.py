import csv
import numpy as np
print("Por favor digite o nome do CSV a ser testado")
nome=input()
#nome='crx.data'
with open(nome, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
for i in range(0,len(data[0])):
	moda={}
	falta=0
	max=-1
	for j in range (0,len(data)):
		if(data[j][i]=="?"):
			flag=1
			continue
		elif (data[j][i] in moda):
			moda[data[j][i]]=moda[data[j][i]]+1
		else:
			moda[data[j][i]]=1	
		if(moda[data[j][i]]>max):
			max=moda[data[j][i]]
			elem=data[j][i]
	if(flag==1):
		for j in range (0,len(data)):
			if(data[j][i]=="?"):
				data[j][i]=elem

np.savetxt("resultado.csv", data, delimiter=",", fmt='%s')
