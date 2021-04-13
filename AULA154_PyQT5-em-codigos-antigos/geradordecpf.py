from random import randint

def geraCPF():
    numero = str(randint(100000000, 999999999))

    novoCPF = numero
    total = 0
    contadorReverso = 10

    for i in range(19):
        if i > 8:
            i -= 9 # tirando 9, pois o cpf sem os digitos tem 9 caracteres

        total += int(novoCPF[i]) * contadorReverso # somando todos os resultados das multiplicações

        contadorReverso -= 1 # decrementando 1 do contador a cada loop
        if contadorReverso < 2:
            contadorReverso = 11  # quando o contador bater 2, recebe 11 para o calculo do outro digito
            d = 11 - (total % 11)

            if d > 9:
                d = 0

            total = 0
            novoCPF += str(d) # adicionando os 2 digitos calculados no final do cpf

    return novoCPF

