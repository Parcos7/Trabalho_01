# =====================================================================
# NOTA DE NOMENCLATURA PESSOAL:
# 'db'  -> Simplificação de "banco_de_dados" 
# 'arq' -> Simplificação de "arquivos" ou "arquivo"
# =====================================================================

import json
from enum import Enum

class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    BANCO_DE_DADOS = 4

nome_db = 'inventario_db.json'

def ler_db():
    """
    Lê o arq JSON e retorna os dados como um dicionário (hash map).
    """
    try:
        # Abre o arq em modo de leitura ('r')
        with open(nome_db, 'r') as arq_leitura:
            dados = json.load(arq_leitura)
            return dados
            
    except FileNotFoundError:

        print("Aviso: arq do db não encontrado. Iniciando uma nova base vazia.")
        return {}
        
    except json.JSONDecodeError:
        print("Erro crítico: O arq do db está corrompido.")
        return {}

def salvar_db(db_atualizado):
    """
    Recebe o dicionário do sistema em memória e persiste no arq de texto JSON.
    """
    try:
        # Abre o arq em modo de escrita ('w')
        with open(nome_db, 'w') as arq_escrita:
            # Salva o dicionário no arq com indentação para ficar legível
            json.dump(db_atualizado, arq_escrita, indent=4)
            
    except Exception as erro:
        print(f"Erro ao tentar gravar no arq do db: {erro}")