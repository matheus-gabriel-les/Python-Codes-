import random
numero_escolhido = ""
MED = 500
AUX = 0
count = 0
while numero_escolhido!= "sim":
    tentativa = input("O numero escolido e maior que "+str(MED)+ "?")
    if tentativa == "sim":
        AUX = MED + 1
        MED = random.randint(MED,AUX)
    elif tentativa == "nao":
        MED = MED - 1
        MED = random.randint(AUX,MED)
    numero_escolhido = input("O numero escolido e "+str(MED)+"?")
    count += 1
print("O numero escolhido e "+str(MED)+" e o numero de tentativas foi: "+str(count))  