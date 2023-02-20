def soma(numero_1, numero_2):
    return numero_1 + numero_2

def media(lista_de_numeros):
    return sum(lista_de_numeros) / len(lista_de_numeros)

def imprime_relatorio(nome, cpf, telefone):
    return f"""
    Relatorio parcial 

    {nome}, portador do CPF {cpf}

    usuario do telefone {telefone}
    
    esta oficialmente de ferias

    Ass. Direcao
    """
