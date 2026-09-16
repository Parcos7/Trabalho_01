ativo = {}

def cadastro(ativo):
    while True:
        try:
            ativo['id'] = int(input("digite o id numerico do ativo de TI: "))
            break 
        except ValueError:
            print("erro o id tem que ser um numero inteiro tenta de novo")
            
    ativo['nome'] = input("digite o nome ou hostname do equipamento: ").strip().lower()
    ativo['responsavel'] = input("digite o nome do responsavel pelo ativo: ").strip().title()
    ativo['local'] = input("digite a localidade do ativo: ").strip().title()