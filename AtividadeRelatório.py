# =========================================================
# Atividade Relatório
# Autor: Guilherme Augusto
# Versão: 3
# =========================================================

import time
import sys

linhas = "=" *20
linha2 = "=" *9
print(linhas)
print("ATIVIDADE RELATÓRIO")
print(linhas)

cliente = input("Digite seu nome: ")
valor = input("Digite o valor do produto: ")
produto = input("Digite o nome do produto: ")

relatorio = (   
    f"Cliente: {cliente}\n"
    f"Valor do produto: {valor}\n"
    f"Nome do produto: {produto}\n"
    f"Status: ✅"
)

relatorios = "RELATÓRIO:"

for letra in relatorios:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.2)

print(cliente)
time.sleep(1)
print(produto)
time.sleep(1)
print(valor)
time.sleep(1)

