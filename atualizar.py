from persistencia import ler_db, salvar_db

def atualizar_ativo():
    # Carrega o db do arquivo json para a memória
    db_inventario = ler_db()
    
    print("\n--- ATUALIZAR ATIVO DE TI ---")
    # Pede o ID. Como salvamos a chave do nosso dicionário como string, capturamos direto como texto
    id_busca = input("Digite o ID numérico do ativo que deseja atualizar: ").strip()
    
    # Verifica se a chave existe direto no dicionário (busca otimizada O(1))
    if id_busca in db_inventario:
        ativo = db_inventario[id_busca]
        print(f"\n[ ATIVO ENCONTRADO: {ativo['nome']} ]")
        
        # Atualizando o Responsável
        print(f"Responsável atual: {ativo['responsavel']}")
        novo_resp = input("Digite o novo responsável (ou aperte Enter para manter o atual): ").strip().title()
        
        # Se o usuário digitou algo (a string não ficou vazia), nós atualizamos o valor
        if novo_resp != "":
            ativo['responsavel'] = novo_resp
            
        # Atualizando a Localização
        print(f"Localização atual: {ativo['local']}")
        novo_local = input("Digite a nova localização (ou aperte Enter para manter a atual): ").strip().title()
        
        if novo_local != "":
            ativo['local'] = novo_local
            
        # Salva o dicionário inteiro de volta no arquivo de texto JSON usando o módulo de persistência
        salvar_db(db_inventario)
        print(f"\nSucesso: O ativo '{ativo['nome']}' foi atualizado e salvo no db!")
        
    else:
        print("\nErro: Nenhum ativo encontrado com esse ID no db.")