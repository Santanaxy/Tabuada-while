numero = int(input("DIGITE UM NUMERO: ")) 
valor = int(input("DIGITE QUAL NUMERO VC QUER PARAR: "))
i = int(input("DIGITE QUAL NUMERO ONDE VC QUER COMEÇAR: ")) 

while i <= (valor): 
    print(f"{i} * {numero} = {i * numero}")
    i+=1  
    