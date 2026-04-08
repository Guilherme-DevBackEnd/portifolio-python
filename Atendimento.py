# =========================================================
# Atividade Atendimento
# Autor: Guilherme Augusto
# Versão: 4
# =========================================================

vez = input("Você está bem? (sim/não): ").strip().lower()

if vez == "sim":
    print("Que bom! Tenha um ótimo dia 😁")
else:
    agendamento = input("Deseja agendar um horário? (sim/não): ").strip().lower()
    
    if agendamento == "sim":
        try:
            horarios = int(input("Temos horários disponíveis das 08 às 19. Escolha seu horário: "))
            
            if 9 <= horarios <=19:
                print("Ótimo dia! Horário marcado.")
            elif horarios < 18:
                print("Ótima tarde! Horário marcado.")
            else:   
                print("Ótima noite! Horário marcado.")
                      
        except ValueError:
            print("Por favor, digite um número válido.")
