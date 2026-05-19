low, high = 1, 5000
print(f"Pense em um número entre {low} e {high}. Responda às perguntas com 'maior', 'menor' ou 'sim'.")
count = 0
while low <= high:
    mid = (low + high) // 2
    resposta = input(f"Seu número é {mid}? ").strip().lower()
    count += 1
    if resposta in ("sim", "s", "igual"):
        print(f"Encontrei: {mid} em {count} tentativas.")
        break
    if resposta in ("maior", ">"):
        low = mid + 1
        continue
    if resposta in ("menor", "<"):
        high = mid - 1
        continue
