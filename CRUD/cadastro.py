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
            id_str = str(id_num)  
            
            # Impede o cadastro de IDs duplicados
            if id_str in db_inventario:
                print("Erro: Este ID já existe no db. Tente outro.")
                continue
                
            ativo['id'] = id_num
            break
        except ValueError:
            print("Erro: O ID deve ser um número inteiro. Tente novamente.")
            
    ativo['nome'] = ""
    while ativo['nome'] == "":
        print("Padrão da empresa:\n" \
        "Notebook = NOTP(Seguido do patrimônio)\n" \
        "Servidor = SERV(Seguido do patrimônio)\n" \
        "Desktop = MICP(Seguido do patrimônio)\n" \
        "Roteadores = ROTP(Seguido do patrimônio)\n")
        print("=\n"*45)
        
        pre_validos = ("notp", "serv", "micp", "rotp")
        ativo['nome'] = input("Digite o hostname do equipamento: ").strip().lower()
        if ativo['nome'] == "":
            print("Erro: O campo hostname não pode ficar vazio.")
        elif not ativo['nome'].startswith(pre_validos):
            print("Erro: Hostname fora do padrão. Inicie com NOTP, SERV, MICP ou ROTP") 
        else:
            break
               
    ativo['responsavel'] = ""
    while ativo['responsavel'] == "":
        # Nomes próprios formatados com a primeira letra maiúscula
        ativo['responsavel'] = input("Digite o nome do responsável: ").strip().title()
        if ativo['responsavel'] == "":
            print("Erro: O campo responsável não pode ficar vazio.")
            
    ativo['local'] = ""
    while ativo['local'] == "":
        ativo['local'] = input("Digite a localização do ativo: ").strip().title()
        if ativo['local'] == "":
            print("Erro: A localização não pode ficar vazia.")
            
    print("\nTipos de Ativos disponíveis:")
    for tipo in TipoAtivo:
        print(f"{tipo.value} - {tipo.name}")
        
    while True:
        try:
            escolha = int(input("Escolha o número correspondente ao tipo: "))
            ativo['tipo'] = TipoAtivo(escolha).name
            break
        except ValueError:
            print("Erro: Digite um dos números da lista.")
            
    ativo['vulnerabilidades'] = []
    
    db_inventario[id_str] = ativo
    salvar_db(db_inventario)
    
    print(f"\nSucesso: Ativo '{ativo['nome']}' cadastrado e salvo no db!")
