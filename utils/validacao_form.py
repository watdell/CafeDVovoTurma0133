import re
from datetime import datetime
from utils.datetime_converter import convert_to_datetime_format

def verifica_campos(nome, email, telefone, nascimento, pais, cep, estado, cidade, bairro, logradouro, numero, complemento, **kwargs):
    formatted_salary = 0
    def verif_campos_dinamicos():
        nonlocal formatted_salary
        if kwargs['tipo'] == "Funcionário":
            if not kwargs.get('cpf') or not kwargs.get('matricula') or not kwargs.get('cargo'):
                return False, "Todos os campos de funcionário devem ser preenchidos."
            salario_formatado = formata_salario(kwargs.get('salario'))
            formatted_salary = salario_formatado
            if not salario_formatado or not valida_salario(salario_formatado):
                return False, "O salário deve ser um número positivo."
        if kwargs['tipo'] == "Estrangeiro":
            if not kwargs.get('doc_inter') or not kwargs.get('descricao_es'):
                return False, "Todos os campos de estrangeiro devem ser preenchidos."
        if kwargs['select'] == 'Jurídica': 
            if not kwargs.get('cnpj') or not kwargs.get('descricao'):
                return False, "Todos os campos de jurídica devem ser preenchidos."
        return True, ""

    # Verificações básicas
    if not nome:
        return False, "", "O campo 'Nome' é obrigatório."
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False, "", "Por favor, insira um email válido."
    if not telefone:
        return False, "", "O campo 'Telefone' é obrigatório."
    if not nascimento or not convert_to_datetime_format(nascimento):
        return False, "", "Por favor, insira uma data de nascimento válida no formato DD-MM-YYYY."
    if not pais:
        return False, "O campo 'País' é obrigatório."
    if not cep:
        return False, "", "O campo 'CEP' é obrigatório."
    if not estado:
        return False, "", "O campo 'Estado' é obrigatório."
    if not cidade:
        return False, "", "O campo 'Cidade' é obrigatório."
    if not bairro:
        return False, "", "O campo 'Bairro' é obrigatório."
    if not logradouro:
        return False, "", "O campo 'Logradouro' é obrigatório."
    if not numero:
        return False, "", "O campo 'Número' é obrigatório."
    if not complemento:
        return False, "", "O campo 'Complemento' é obrigatório."

    # Verificações dinâmicas
    campos_ok, mensagem_dinamica = verif_campos_dinamicos()
    if not campos_ok:
        return False, formatted_salary, mensagem_dinamica

    return True, formatted_salary, "Todos os campos foram preenchidos corretamente!"


def formata_salario(salario):
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

def valida_salario(salario):
    try:
        salario_float = float(salario)
        return salario_float > 0  # Verifica se o salário é um número positivo
    except ValueError:
        return False  # Retorna falso se a conversão falhar
