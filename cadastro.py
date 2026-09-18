# =====================================================================
# NOTA DE NOMENCLATURA PESSOAL:
# 'db'  -> Simplificação de "banco_de_dados" (representa a base em memória e o nome do arquivo).
# 'arq' -> Simplificação de "arquivos" ou "arquivo" (usado para variáveis que manipulam a abertura e leitura no disco).
# =====================================================================

# Importamos as funções modulares que criamos na Parte 1
from persistencia import ler_db, salvar_db, TipoAtivo

def cadastrar_ativo():
    """(Create) - Valida e cadastra um novo equipamento de TI na base."""
    # Carrega o db atual para a memória antes de fazer alterações
    db_inventario = ler_db()
    
    ativo = {}
    print("\n--- CADASTRO DE NOVO ATIVO ---")
    
    # 1. Validação rigorosa do ID numérico com try/except[cite: 1, 3]
    while True:
        try:
            id_num = int(input("Digite o ID numérico do ativo de TI: "))
            id_str = str(id_num) # Usamos string como chave do dicionário/JSON para otimizar buscas
            
            # Impede o cadastro de IDs duplicados
            if id_str in db_inventario:
                print("Erro: Este ID já existe no db. Tente outro.")
                continue
                
            ativo['id'] = id_num
            break
        except ValueError:
            print("Erro: O ID deve ser um número inteiro. Tente novamente.")