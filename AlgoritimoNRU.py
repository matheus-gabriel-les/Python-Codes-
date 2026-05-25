mod = ['0', '1', '0', '1', '1', '0', '0', '1', '0', '1']# Lista de bits de modificação, inicialmente todos 0
ref = ['1', '1', '0', '0', '1', '1', '0', '1', '0', '0']# Lista de bits de referência, inicialmente todos 1
pg = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]# Lista de páginas
#Aqu simula o processo de classificação das páginas com base nos bits de referência e modificação
for p in pg[:]:
    i = p
    if ref[i] == '0' and mod[i] == '0':# Página não referenciada e não modificada tem a menor prioridade para remoção
        print(f"Página {p}: Não referenciado, não modificado")
        print("Removendo pagina")
        pg.remove(p)
    elif ref[i] == '0' and mod[i] == '1':# Página não referenciada mas modificada tem prioridade intermediária para remoção
        print(f"Página {p}: Não referenciado, modificado")
        pg.remove(p)
    elif ref[i] == '1' and mod[i] == '0':# Página referenciada mas não modificada tem prioridade mais alta para remoção
        print(f"Página {p}: referenciado, não modificado")
        pg.remove(p)
    else:
        print(f"Página {p}: referenciado, modificado")# Página referenciada e modificada tem a menor prioridade para remoção
        pg.remove(p)

