from persistencia import ler_db

def consultar_ativo():
    # Carrega o db atualizado do arquivo json para a memória (dicionário)
    db_inventario = ler_db()
    
    print("\n--- CONSULTA DE ATIVO DE TI ---")
    # Pede o termo de busca. O .strip().lower() ajuda a não dar erro se o usuário digitar com letras maiúsculas ou espaços
    termo_busca = input("Digite o ID numérico ou o Hostname do ativo que deseja buscar: ").strip().lower()
    
    encontrado = False
    
    # Varre o dicionário de ativos (hash map) para fazer a consulta
    for chave, ativo in db_inventario.items():
        # Verifica se o termo digitado bate com o ID (convertido pra string) ou com o hostname
        if str(ativo['id']) == termo_busca or ativo['nome'].lower() == termo_busca:
            print("\n[ ATIVO ENCONTRADO ]")
            print(f"ID: {ativo['id']}")
            print(f"Hostname: {ativo['nome']}")
            print(f"Responsável: {ativo['responsavel']}")
            print(f"Localização: {ativo['local']}")
            print(f"Tipo: {ativo['tipo']}")
            
            print("\n--- Vulnerabilidades Associadas ---")
            # Valida se a lista de vulnerabilidades está vazia e exibe a mensagem correspondente
            if len(ativo['vulnerabilidades']) == 0:
                print(" -> Este equipamento está limpo. Nenhuma vulnerabilidade registrada.")
            else:
                for vul in ativo['vulnerabilidades']:
                    print(f" -> [{vul['severidade'].upper()}] {vul['descricao']} | Status: {vul['status']}")
            
            encontrado = True
            break # Como já encontrou o ativo, para a busca para economizar processamento
            
    # Se terminar de varrer todo o dicionário e a variável continuar False, o ativo não existe
    if not encontrado:
        print("\nErro: Nenhum ativo encontrado com esse ID ou Hostname no db.")