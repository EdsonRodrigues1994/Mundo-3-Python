nomes = ("caderno", "lapis")

for i in nomes:
    print(f"\n Na palavra {i} temos:", end=" ")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end=" ")