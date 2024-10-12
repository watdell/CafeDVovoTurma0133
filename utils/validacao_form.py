
def verifica_campos(nome, email, telefone, nascimento, pais, cep, estado, cidade, bairro, logradouro, numero, complemento, **kwargs):
    def verif_campos_dinamicos():
        if kwargs['tipo'] == "Funcionário":
            if not kwargs['cpf'] or not kwargs['matricula'] or not kwargs['cargo'] or not kwargs['salario']:
                return False       
        if kwargs['tipo'] == "Estrangeiro":
            if not kwargs['doc_inter'] or not kwargs['descricao_es']:
                return False        
        if kwargs['select'] == 'Jurídica': 
            if not kwargs['cnpj'] or not kwargs['descricao']:
                return False            
        return True
        
    if not nome or not email or not telefone or not nascimento or not pais or not cep or not estado or not cidade or not bairro or not logradouro or not numero or not complemento or not verif_campos_dinamicos():
        return False, "Por favor, preencha todos os campos."
    return True, "Todos os campos foram preenchidos!"      
  