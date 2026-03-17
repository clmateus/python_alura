def saudacao_personalizada(horas):
    if horas < 12:
        return "Bom dia"
    elif horas < 18:
        return "Boa tarde"
    else:
        return "Boa noite"

try:    
    hora_atual = int(input("Digite a hora atual (0-23): "))
    print(f"{saudacao_personalizada(hora_atual)}")
except:
    print("Erro! Digite uma hora válida de 0 a 23")