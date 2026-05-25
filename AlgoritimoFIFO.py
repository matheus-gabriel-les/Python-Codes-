proc = [10, 5, 8, 3]
rod = 2  # Fatia de tempo por execução

print(f"Fila inicial: {proc}\n")

# Processa cada processo da fila em ordem FIFO
while proc:
    p = proc.pop(0)
    print(f"Processando: {p} (tempo restante)")
    p -= rod# Reduz o tempo do processo pela fatia de tempo

    if p <= 0:
        print(f"  → Processo completado, removendo")# Processo concluído, não re-enfileira
    else:
        proc.append(p)
        print(f"  → Tempo restante após redução: {p}, re-enfileirando")#Re-enfileira o processo com o tempo restante

    print(f"  Fila agora: {proc}\n")

print("Todos os processos foram concluídos.")
    
