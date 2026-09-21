from cadastro import cadastrar_ativo
from consulta import consultar_ativo
from atualizar import atualizar_ativo
from remover import remover_ativo
from vulnerabilidades import registrar_vulnerabilidade

def menu_principal():
    # O laço while True mantém o menu a repetir-se até o comando 'break' ser acionado
    while True:
        print("\n" + "="*45)
        print("   INVENTÁRIO DE CIBERSEGURANÇA - GESTÃO   ")
        print("="*45)
        print("1 - Cadastrar novo ativo de TI (Create)")
        print("2 - Consultar ativo existente (Read)")
        print("3 - Atualizar dados do ativo (Update)")
        print("4 - Remover ativo do sistema (Delete)")
        print("5 - Registrar nova vulnerabilidade")
        print("0 - Sair do sistema")
        print("="*45)
        
        opcao = int(input("Escolha uma opção do menu: "))
        try:
            match opcao: 
                case 1:
                    cadastrar_ativo()
                case 2:
                    consultar_ativo()
                case 3:
                    atualizar_ativo()
                case 4:
                    remover_ativo()
                case 5:
                    registrar_vulnerabilidade()
                case 0:
                    print("\nEncerrando o sistema de inventário. Até logo!")
                    break                
                case _:
                    print("\nErro: Opção inválida. Digita um número entre 0 e 5.")

        except ValueError:
            print("\nErro: Entrada inválida. Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    menu_principal()