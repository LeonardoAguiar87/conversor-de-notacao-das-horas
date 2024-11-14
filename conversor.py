# Solicita a entrada do usuário
x = input("Digite uma hora (HH:MM): ").split(":")

def mudar_hora(x):
    # Converte as partes da hora e dos minutos em inteiros
    hora = int(x[0])
    min = int(x[1])

    # Verifica se a hora está no formato correto
    if not (0 <= hora < 24) or not (0 <= min < 60):
        return "Por favor, insira uma hora válida no formato HH:MM."

    # Converte a hora de 24h para 12h
    if hora > 12:
        hora -= 12
        return f"{hora}:{min:02d} P.M."
    elif hora == 12:
        return f"{hora}:{min:02d} P.M."
    else:
        return f"{hora}:{min:02d} A.M."

# Chama a função e imprime o resultado
print(mudar_hora(x))