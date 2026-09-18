# =====================================================================
# NOTA DE NOMENCLATURA PESSOAL:
# 'db'  -> Simplificação de "banco_de_dados" 
# 'arq' -> Simplificação de "arquivos" ou "arquivo" 
# =====================================================================


from persistencia import ler_db, salvar_db, TipoAtivo

def cadastrar_ativo():
    """(Create) - Valida e cadastra um novo equipamento de TI na base."""
    # Carrega o db atual para a memória antes de fazer alterações
    db_inventario = ler_db()
    
    ativo = {}
    print("\n--- CADASTRO DE NOVO ATIVO ---")
    
    while True:
        try:
            id_num = int(input("Digite o ID numérico do ativo de TI: "))
            id_str = str(id_num) # Utilizei string como chave do dicionário/JSON para otimizar buscas
            
            # Impede o cadastro de IDs duplicados
            if id_str in db_inventario:
                print("Erro: Este ID já existe no db. Tente outro.")
                continue
                
            ativo['id'] = id_num
            break
        except ValueError:
            print("Erro: O ID deve ser um número inteiro. Tente novamente.")