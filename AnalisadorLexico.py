from tabulate import tabulate
from beautifultable import BeautifulTable

#ler arquivo TXT
arquivo = open('teste.txt', 'r')
ler = arquivo.read()

#Ler palavras reservadas
r = ['auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while']

table = BeautifulTable()
table.column_headers = ["PALAVRAS RESERVADAS DA LINGUAGEM C"]

c = ""
for l in ler:
    if(l != ' '):
        c += l
    else:
        for reser in r:
            if((c == reser) and (c != ' ')):
                table.append_row([c])
            else:
                c = ""
                break
        
print (table)
