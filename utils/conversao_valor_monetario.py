def convert_monetary_to_float(salario):
    if salario:
        # Remove o 'R$', espaços em branco
        salario = salario.replace("R$", "").replace(" ", "")
        
        # Se houver um ponto, verificar sua posição
        if '.' in salario:
            partes = salario.split('.')
            if len(partes) > 1 and len(partes[-1]) <= 2:
                # Mantém o ponto se estiver antes de duas casas decimais
                return salario.replace(",", ".")
            else:
                # Se houver vírgula, substitui por ponto e remove outros pontos
                salario = salario.replace(".", "").replace(",", ".")
        else:
            # Se houver vírgula, substitui por ponto
            salario = salario.replace(",", ".")
        
        return salario
    return None


def convert_float_to_monetary(valor):
    if valor is None:
        return "R$ 0,00"  # Retorna um valor padrão caso o valor seja None

    # Converte para float, se já for uma string, e trata possíveis erros
    try:
        valor_float = float(valor)
    except ValueError:
        return "Valor inválido"

    # Formata o valor float para uma string com duas casas decimais
    valor_str = f"{valor_float:.2f}"

    # Separa a parte inteira e a parte decimal
    parte_inteira, parte_decimal = valor_str.split(".")

    # Formata a parte inteira com separadores de milhar
    parte_inteira_formatada = '{:,}'.format(int(parte_inteira)).replace(",", ".")

    # Combina a parte inteira formatada com a parte decimal
    valor_formatado = f"R$ {parte_inteira_formatada},{parte_decimal}"

    return valor_formatado