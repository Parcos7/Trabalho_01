# =====================================================================
# NOTA DE NOMENCLATURA PESSOAL:
# 'db'  -> Simplificação de "banco_de_dados" 
# 'arq' -> Simplificação de "arquivos" ou "arquivo" 
# =====================================================================

from persistencia import ler_db, salvar_db

def remover_ativo():
    # Carrega o db do disco para a memória
    db_inventario = ler_db()
    
    print("\n--- REMOVER ATIVO DE TI ---")
    id_busca = input("Digite o ID numérico do ativo que deseja remover: ").strip()
    
    # Verifica se o ID existe como chave no dicionário (hash map)
    if id_busca in db_inventario:
        # Guardamos o nome apenas para dar um feedback claro ao utilizador antes de o apagar
        nome_removido = db_inventario[id_busca]['nome']
        
        # O comando 'del' apaga a chave e todo o seu conteúdo (incluindo a lista de vulnerabilidades)
        del db_inventario[id_busca]
        
        # Persiste a alteração no ficheiro JSON
        salvar_db(db_inventario)
        
        print(f"\nSucesso: O ativo '{nome_removido}' e todas as suas vulnerabilidades foram removidos do db de forma permanente.")
    else:
        print("\nErro: Nenhum ativo encontrado com esse ID no db. Nenhuma ação foi realizada.")