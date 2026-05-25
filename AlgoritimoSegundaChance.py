proc = [10, 5, 8, 3, 5, 6, 7, 9]
RECENT = 1# Valor para indicar acesso recente
bit_ref = [0] * len(proc)

# A função index() encontra a primeira posição do valor na lista
def access(value):
    idx = proc.index(value)
    bit_ref[idx] = RECENT
    print(f"Marcando acesso: {value} -> bit_ref[{idx}] = {RECENT}")
#Simulando acesso de alguns processos
access(10)
access(8)
access(6)
print(f"Fila inicial: {proc}\n")

while proc:
    p = proc.pop(0)
    ref = bit_ref.pop(0)
    print(f"Processando: {p} (bit_ref={ref})")

    if ref == RECENT:
        print(f"  → bit_ref == {RECENT}: movendo para o final e definindo bit_ref = 0")# Se o processo foi acessado recentemente, re-enfileira e reseta o bit de referência
        proc.append(p)
        bit_ref.append(0)
    else:
        # Se já estava com bit_ref == 0, remove-se da lista (evicção)
        print(f"  → bit_ref == 0: removendo")

    print(f"  Fila agora: {proc}\n")

print("Todos os processos foram concluídos.")

