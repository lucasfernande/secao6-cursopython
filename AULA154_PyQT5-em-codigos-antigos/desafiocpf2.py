import re


def validaCPF(cpf):
    cpf = str(cpf)

    cpf = re.sub(r'[^0-9]', '', cpf)  # tudo que for diferente de 0 a 9 será removido da string
    novo_CPF = cpf[:-2]  # tirando os últimos 2 dígitos do cpf

    if not cpf or len(cpf) < 11:
        return False

    total = 0
    contador_reverso = 10

    for i in range(19):
        if i > 8:
            i -= 9  # tirando 9, pois o cpf sem os digitos tem 9 caracteres

        total += int(novo_CPF[i]) * contador_reverso  # somando todos os resultados das multiplicações

        contador_reverso -= 1  # decrementando 1 do contador a cada loop
        if contador_reverso < 2:
            contador_reverso = 11  # quando o contador bater 2, recebe 11 para o calculo do outro digito
            d = 11 - (total % 11)

            if d > 9:
                d = 0

            total = 0
            novo_CPF += str(d)  # adicionando os 2 digitos calculados no final do cpf

    sequencia = novo_CPF == str(novo_CPF[0]) * len(cpf)  # evita sequencias. EX: 111.111.111-11

    if cpf == novo_CPF and not sequencia:
        return True
    else:
        return False
