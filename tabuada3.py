numero = int(input("DIGITE UM NUMERO: ")) 
valor = int(input("DIGITE QUALQUER NUMERO ONDE VC QUER PARA,LEMBRE DE DIGITAR SEMPRE UM NUMERO A MAIS! : "))
i = int(input("DIGITE QUAL NUMERO ONDE VC QUER COMEÇAR: ")) 

for i in range(i, valor + 1): 
    print(f"{i} * {numero} = { i * numero}") 