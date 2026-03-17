def valida_cpf(cpf):
    caracteres_validos = "1234567890"

    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    
    return "CPF válido."

print(valida_cpf("12a"))