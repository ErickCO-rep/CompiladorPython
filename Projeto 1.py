from tokenizer import tokenize, TOK
from beautifultable import BeautifulTable

arquivo = open("teste.txt","r")
ler = arquivo.read()

l = 0
r = ['auto','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while']
pot = ['.',';',',','(',')',':','+','<','>','-','*','%','=']
poc = ['++','--','>=','<=','+=','-=','/=','%=','*=', '!=']
num = ['0','1','2','3','4','5','6','7','8','9']


table = BeautifulTable()
table.column_headers = ["Linha", "Token", "Símbolo"]

for token in tokenize(ler):

    print(u"{0}: '{1}' {2}".format(
        TOK.descr[token.kind],
        token.txt or "-",
        token.val or ""))
    
    if(token.txt == 'None'):
        l = l+1

    for reser in r:
        if(token.txt == reser):
            tk = token.txt
            sib = "Palavra Reservada"
            table.append_row([l, tk, sib])
            
    for pont in pot:
        if(token.txt == pont):
            tk = token.txt
            sib = "Símbolo Especial"
            table.append_row([l, tk, sib])

    for ponc in poc:
        if(token.txt == ponc):
            tk = token.txt
            sib = "Símbolo Composto"
            table.append_row([l, tk, sib])
                        
    for nume in num:
        if(token.txt == nume):
            tk = token.txt
            sib = "Constante Inteiro"
            table.append_row([l, tk, sib])
            
    if((token.txt != r) and (token.txt != pot) and (token.txt != poc) and (token.txt != num)):
        tk = token.txt
        sib = "Variável"
        table.append_row([l, tk, sib])
                                    
print (table)
