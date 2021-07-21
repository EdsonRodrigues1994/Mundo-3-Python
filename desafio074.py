import random


aleatorios = (random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100))
print(f" Os números sorteados foram: {aleatorios} \n "
      f"O menor número é {min(aleatorios)} e o maior número é {max(aleatorios)}.")
