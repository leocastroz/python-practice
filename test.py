# Ler dois valores de ponto flutuante
A = float(input())
B = float(input())

# Pesos das notas
peso_A = 3.5
peso_B = 7.5

# Calcular a média ponderada
MEDIA = (A * peso_A + B * peso_B) / (peso_A + peso_B)

# Imprimir o resultado com a mensagem correspondente
print("MEDIA = {:.5f}".format(MEDIA))