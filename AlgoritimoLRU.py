proc = [1, 2, 3, 4, 5, 6, 7]
RECENT = 1# Valor para indicar acesso recente
CAPACITY = 3# Capacidade da cache
bit_ref = [0] * len(proc)# Lista de bits de referência, inicialmente todos 0
# Simulando acessos a páginas
class Cache:
    def __init__(self, chave, valor):
        self._chave = chave
        self._valor = valor

    @property
    def chave(self):
        if self._chave != None:
            return self._chave
        else:
            return -1
#Assegura que a chave seja atualizada corretamente    
    @chave.setter
    def chave(self, valor):
        self._chave = valor
#Assegura que o valor seja atualizado corretamente
def access(value):
    idx = proc.index(value)
    bit_ref[idx] = RECENT
    print(f"Marcando acesso: {value} -> bit_ref[{idx}] = {RECENT}")
# Criando instâncias de Cache para cada página
pg = Cache(1,'A')
pg = Cache(2,'B')
pg = Cache(3,'C')
pg = Cache(4,'D')
pg = Cache(5,'E')
pg = Cache(6,'F')
pg = Cache(7,'G')
# Simulando acessos a páginas
access(1)
access(4)
access(7)

while len(proc) > CAPACITY:
    p = proc.pop(0)
    ref = bit_ref.pop(0)# Remove o bit de referência correspondente ao processo removido

    print(f"Processando: {p} ")
    # Se o processo foi acessado recentemente, re-enfileira e reseta o bit de referência
    if ref == RECENT:
        print(f"  → bit_ref == {RECENT}: movendo para o final e definindo bit_ref = 0")
        proc.append(p)
        bit_ref.append(0)
    else:
        # Se já estava com bit_ref == 0, remove-se da lista (evicção)
        print(f"  → bit_ref == 0: removendo")

    print(f"  Fila agora: {proc}\n")# Exibe a ordem de prioridade atual após cada iteração
print(f"Ordem de prioridade: {proc}\n")




    

    