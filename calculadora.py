
def fazer_conta(numero1, numero2, operacao):
    operacoes_possiveis = ["+", "-", "*", "/", "^"]

    # Verificar se os números são válidos e não booleanos
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)) or isinstance(numero1, bool) or isinstance(numero2, bool):
        return None

    if operacao not in operacoes_possiveis:
        return None

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            return None
        resultado = numero1 / numero2
    elif operacao == "^":
        resultado = numero1 ** numero2

    return resultado
