proc = [10, 5, 8, 3, 5, 6, 7, 9]
bit_ref = [0] * len(proc)
ponteiro = 0# Ponteiro para o algoritmo do relógio

def access(value):
    idx = proc.index(value)# Marca o acesso à página, definindo o bit de referência para 1
    bit_ref[idx] = 1# Exibe o acesso e o estado do bit de referência
    print(f"Acesso: {value} -> bit_ref[{idx}] = 1")
# Simulando acessos a páginas
access(5)
access(7)
access(9)

print("\nIniciando substituição de páginas:\n")
while proc and len(proc) > 3:
    print(f"Ponteiro em posição {ponteiro}: página {proc[ponteiro]} (bit={bit_ref[ponteiro]})")
    
    if bit_ref[ponteiro] == 1:# Se o bit de referência for 1, dá uma "segunda chance" à página, reseta o bit e avança o ponteiro
        print(f"  Bit=1 (Segunda chance): Reseta bit para 0 e avança o ponteiro.")
        bit_ref[ponteiro] = 0
        ponteiro = (ponteiro + 1) % len(proc)
    else:
        print(f"  → bit=0: removendo página {proc[ponteiro]}")# Página com bit de referência 0 é removida
        proc.pop(ponteiro)
        bit_ref.pop(ponteiro)
        if proc:# Ajusta o ponteiro para a próxima posição após remoção
            ponteiro = ponteiro % len(proc)
print(f"Páginas restantes na memória: {proc}")
