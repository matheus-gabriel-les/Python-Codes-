import random
numero_escolhido = ""
MED = random.randint(1,5000)
count = 0
while numero_escolhido!= "sim":
    tentativa = input("O numero escolido e maior que "+str(MED)+ "?")
    if tentativa == "sim":
        MED = random.randint(MED,MED*2)
        numero_escolhido = input("O numero escolido e "+str(MED)+"?")
    elif tentativa == "nao":
        MED = random.randint(MED//2,MED)
        numero_escolhido = input("O numero escolido e "+str(MED)+"?")
    count += 1
print("O numero escolhido e "+str(MED)+" e o numero de tentativas foi: "+str(count))  
