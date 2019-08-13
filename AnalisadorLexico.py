#ler arquivo TXT
arquivo = open('teste.txt', 'r')

conteudo = arquivo.readlines()
arq = str(conteudo).strip('[]')

print(arq.split(";",2))

#com o split no conteudo do arquivo, deve-se identificar cada token

#Inserir código
