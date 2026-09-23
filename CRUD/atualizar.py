# =====================================================================
# NOTA DE NOMENCLATURA PESSOAL:
# 'db'  -> Simplificação de "banco_de_dados" 
# 'arq' -> Simplificação de "arquivos" ou "arquivo"
# 'resp' -> Simplificação de "Responsavel"
# 'at' -> Simplificalção de "Atualizar"
# =====================================================================

from persistencia import ler_db, salvar_db

def atualizar_ativo():
    db_inventario = ler_db()
    
    print("\n--- ATUALIZAR ATIVO DE TI ---")
    id_busca = input("Digite o ID numérico do ativo que deseja atualizar: ").strip()
     
    if id_busca in db_inventario:
        ativo = db_inventario[id_busca]
        print(f"\n[ ATIVO ENCONTRADO: {ativo['nome']} ]")
        while True:   
            print("Escolha a opção que deseja alterar:\n" \
            "1 - Nome do responsavel\n" \
            "2 - Localidade\n" \
            "0 - Cancelar")
            print("="*45)

            try:
                opcao_at = int(input("Digite o número da opção: "))
            except ValueError:
                print("Erro: Digite um número válido do menu.\n")
                continue             

            match opcao_at:
                case 1:
                    print(f"Responsável atual: {ativo['responsavel']}")
                    while True:
                        novo_resp = input("Digite o novo responsável (ou aperte Enter para manter o atual): ").strip().title()                                              
                        if novo_resp == "":
                            break 
                        elif novo_resp.replace(" ", "").isalpha():                            
                            ativo['responsavel'] = novo_resp
                            break 
                        else:
                            print("Erro: O nome não pode conter números ou símbolos. Tente novamente.\n")
                    break 
                    
                case 2:
                    print(f"Localização atual: {ativo['local']}")
                    while True:
                        novo_local = input("Digite a nova localização (ou aperte Enter para manter a atual): ").strip().title()
                        
                        if novo_local == "":
                            break
                        elif novo_local.replace(" ", "").isalpha():
                            ativo['local'] = novo_local 
                        else:
                            print("Erro: A localidade não pode conter números. Tente novamente.\n")
                    break 
                    
                case 0:
                    print("Atualização cancelada.")
                    break
                    
                case _:
                    print("Erro: Opção inválida. Escolha 1, 2 ou 0.\n")
                    
        if opcao_at != 0:
            salvar_db(db_inventario)
            print(f"\nSucesso: O ativo '{ativo['nome']}' foi atualizado e salvo no db!")
        
    else:
        print("\nErro: Nenhum ativo encontrado com esse ID no db.")