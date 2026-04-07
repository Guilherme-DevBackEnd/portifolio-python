# =========================================================
# Sistema de Reserva - Colônia de Férias
# Autor: Guilherme Augusto
# Versão: 12
# =========================================================

# Biblioteca para cores no terminal

from colorama import Fore, Style, init

# Inicializa cores

init(autoreset=True)

# TABELA DE VALORES (simulando banco de dados)

diarias = {
    1: {1: 20.00, 2: 25.00},
    2: {1: 28.00, 2: 34.00},
    3: {1: 35.00, 2: 42.00},
    4: {1: 42.00, 2: 50.00},
    5: {1: 48.00, 2: 57.00},
    6: {1: 53.00, 2: 63.00}
}

# LOOP PRINCIPAL

import time
import sys

titulo = r"""
  _________.__          __                              .___       __________                                          
 /   _____/|__| _______/  |_  ____   _____ _____      __| _/____   \______   \ ____   ______ ______________  _______   
 \_____  \ |  |/  ___/\   __\/ __ \ /     \\__  \    / __ |/ __ \   |       _// __ \ /  ___// __ \_  __ \  \/ /\__  \  
 /        \|  |\___ \  |  | \  ___/|  Y Y  \/ __ \_ / /_/ \  ___/   |    |   \  ___/ \___ \\  ___/|  | \/\   /  / __ \_
/_______  /|__/____  > |__|  \___  >__|_|  (____  / \____ |\___  >  |____|_  /\___  >____  >\___  >__|    \_/  (____  /
        \/         \/            \/      \/     \/       \/    \/          \/     \/     \/     \/                  \/ """

for linha in titulo.split("\n"):
    print(linha)
    time.sleep(0.2)

while True: 

    # TÍTULO ASCII
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "               COLÔNIA DE FÉRIAS")
    print(Fore.CYAN + "=" * 50)

    # -------------------------------
    # ENTRADA DE DADOS
    # -------------------------------
    
    nome = input(Fore.YELLOW + "Digite o nome do cliente: ")

    print(Fore.MAGENTA + f"Olá {nome}, Segue nosso funcionamento:\n▪ O limite máximo do período de permanência é de sete dias;\n▪ Em cada apartamento podem ficar até seis pessoas;\n▪ Existem dois tipos de apartamentos (tipo 1 e 2);\n▪ Seguindo as informações, preencha abaixo:")

    # Validação de pessoas
    while True:
        pessoas = int(input("Quantidade de pessoas (1 a 6): "))
        if 1 <= pessoas <= 6:
            break
        else:
            print(Fore.RED + "Erro! Digite entre 1 e 6.")

    # Validação tipo apartamento
    while True:
        tipo = int(input("Tipo de apartamento (1 ou 2): "))
        if tipo in [1, 2]:
            break
        else:
            print(Fore.RED + "Erro! Digite 1 ou 2.")

    # Validação dias
    while True:
        dias = int(input("Quantidade de dias (máx 7): "))
        if 1 <= dias <= 7:
            break
        else:
            print(Fore.RED + "Erro! Máximo 7 dias.")

    # PROCESSAMENTO

    valor_diaria = diarias[pessoas][tipo]
    total = valor_diaria * pessoas * dias
    
    # RELATÓRIO

    print(Fore.GREEN + "\n======= RELATÓRIO DA RESERVA =======")
    print(f"Cliente: {nome}")
    print(f"Pessoas: {pessoas}")
    print(f"Tipo de apartamento: {tipo}")
    print(f"Dias: {dias}")
    print(f"Valor da diária por pessoa: R$ {valor_diaria:.2f}")
    print(Fore.BLUE + f"TOTAL A PAGAR: R$ {total:.2f}")
    print(Fore.GREEN + "====================================\n")
    
    # NOVA SIMULAÇÃO

    opcao = input("Deseja fazer nova reserva? (S/N): ").upper()
    if opcao != "S":
        print(Fore.CYAN + "Encerrando sistema...")
    else:
     final = "Sua reserva foi um sucesso!"  
     for letra in final:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.05) 
    
    
    
    break