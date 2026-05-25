def pergunta_sim_nao(prompt):
    while True:
        resposta = input(prompt).strip().lower()
        if resposta in ("sim"):
            return True
        if resposta in ("nao"):
            return False
        print("Por favor, responda com 'sim' ou 'nao' .")

def maior_que(valor):
    return pergunta_sim_nao(f"O número escolhido é MAIOR que {valor}? ")

def encontrar_intervalo():
    # Pergunta base para definir a direção (positivos ou negativos)
    if maior_que(0):
        low, high = 0, 10
        while maior_que(high):
            low = high
            high *= 10
        return low, high
    else:
        high, low = 0, -10
        while not maior_que(low):
            high = low
            low *= 10
        return low, high
#Implementacao de algoritimo de busca binaria
def busca_binaria():
    low, high = encontrar_intervalo()
    while low + 1 < high:
        mid = (low + high) // 2 
        
        if maior_que(mid):
            low = mid
        else:
            high = mid
            
    return high

def main():
    print("Pense em um número inteiro. Eu vou tentar adivinhá-lo usando perguntas.")
    numero = busca_binaria()
    print(f"\nJá sei! O número escolhido é {numero}.")

if __name__ == "__main__":
    main()
