'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
Depois mostre:
A) APENAS OS 5 PRIMEIROS COLOCADOS.
B) OS ULTIMOS 4 COLOCADOS DA TABELA
C) UMA LISTA COM OS TIMES EM ORDEM ALFABETICA
D) EM QUE POSICAO NA TABELA ESTÁ O TIME DA CHAPECOENSE'''

times = ("Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense", "Grêmio", "Palmeiras", "Santos",
         "Atlético-PR", "Bragantino", "Ceará", "Corinthians", "Atlético-GO", "Bahia", "Sport", "Fortaleza", "Vasco",
         "Goiás", "Coritiba", "Botafogo")

print(f" Os primeiros cinco colocados tabela do brasileirao são: {times[:5]}. \n "
      f"Os 4 últimos colocados são: {times[16:]}. \n"
      f" Os times em ordem alfabética: {sorted(times)}. \n"
      f" O Corinthians está na {times.index('Corinthians')}ª posição.")

