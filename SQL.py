import sqlite3
import asyncio


class CRUD:
    def __init__(self):
        # Conecta ao banco de dados SQLite
        self.conn = sqlite3.connect('cafevovo.db')
        self.cursor = self.conn.cursor()

    def insert(self, table, **kwargs):
        '''
        Insere um novo registro na tabela especificada.
        '''
        # Cria a consulta SQL e os valores com base na tabela especificada
        match table:
            case 'funcionario':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO pessoa (nome, email, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?);", (kwargs.get('nome'), kwargs.get('email'), kwargs.get('nascimento'), kwargs.get('data_cadastro')))
                    self.conn.commit()
                    
                    # Obtém o ID do último registro inserido
                    last_id = self.cursor.lastrowid
                    print("Último ID inserido:", last_id)
                    
                    self.cursor.execute("INSERT INTO telefone (id_pessoa, telefone) VALUES (?, ?);", (last_id, kwargs.get('tel')))
                    self.conn.commit()
                    
                    self.cursor.execute("INSERT INTO endereco (id_pessoa, pais, cep, estado, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (last_id, kwargs.get('pais'), kwargs.get('cep'), kwargs.get('estado'), kwargs.get('cidade'), kwargs.get('bairro'), kwargs.get('logradouro'), kwargs.get('numero'), kwargs.get('complemento')))
                    self.conn.commit()

                    self.cursor.execute("INSERT INTO funcionario (id_pessoa, cpf, matricula, cargo, salario) VALUES (?, ?, ?, ?, ?);", (last_id, kwargs.get('cpf'), kwargs.get('matricula'), kwargs.get('cargo'), kwargs.get('salario')))
                    self.conn.commit()
                    
                except Exception as e:
                    print(f"Ocorreu um erro ao cadastrar: {e}")
            
            case 'estrangeiro':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO pessoa (nome, email, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?);", (kwargs.get('nome'), kwargs.get('email'), kwargs.get('nascimento'), kwargs.get('data_cadastro')))
                    self.conn.commit()
                    
                    # Obtém o ID do último registro inserido
                    last_id = self.cursor.lastrowid
                    print("Último ID inserido:", last_id)
                    
                    self.cursor.execute("INSERT INTO telefone (id_pessoa, telefone) VALUES (?, ?);", (last_id, kwargs.get('tel')))
                    self.conn.commit()
                    
                    self.cursor.execute("INSERT INTO endereco (id_pessoa, pais, cep, estado, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (last_id, kwargs.get('pais'), kwargs.get('cep'), kwargs.get('estado'), kwargs.get('cidade'), kwargs.get('bairro'), kwargs.get('logradouro'), kwargs.get('numero'), kwargs.get('complemento')))
                    self.conn.commit()

                    self.cursor.execute("INSERT INTO estrangeiro (id_pessoa, passaporte, descricao) VALUES (?, ?, ?);", (last_id, kwargs.get('doc_inter'), kwargs.get('descricao_es')))
                    self.conn.commit()
                    
                except Exception as e:
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                    
            case 'p_juridica':
                try:
                    # Execute a query com os valores como um dicionário
                    self.cursor.execute("INSERT INTO pessoa (nome, email, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?);", (kwargs.get('nome'), kwargs.get('email'), kwargs.get('nascimento'), kwargs.get('data_cadastro')))
                    self.conn.commit()
                    
                    # Obtém o ID do último registro inserido
                    last_id = self.cursor.lastrowid
                    print("Último ID inserido:", last_id)
                    
                    self.cursor.execute("INSERT INTO telefone (id_pessoa, telefone) VALUES (?, ?);", (last_id, kwargs.get('tel')))
                    self.conn.commit()
                    
                    self.cursor.execute("INSERT INTO endereco (id_pessoa, pais, cep, estado, cidade, bairro, rua, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (last_id, kwargs.get('pais'), kwargs.get('cep'), kwargs.get('estado'), kwargs.get('cidade'), kwargs.get('bairro'), kwargs.get('logradouro'), kwargs.get('numero'), kwargs.get('complemento')))
                    self.conn.commit()

                    self.cursor.execute("INSERT INTO p_juridica (id_pessoa, cnpj, descricao) VALUES (?, ?, ?);", (last_id, kwargs.get('cnpj'), kwargs.get('descricao')))
                    self.conn.commit()
                    
                except Exception as e:
                    print(f"Ocorreu um erro ao cadastrar: {e}")
                    
            case _:
                print("Tabela não encontrada")
                return None

    def close(self):
        # Fecha a conexão com o banco de dados
        self.conn.close()

               
