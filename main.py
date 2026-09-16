import Db

Db.cadastro(Db.ativo)

print("\n--- dados do equipamento cadastrado ---")
print(f"id cadastrado: {Db.ativo['id']}")
print(f"nome do ativo: {Db.ativo['nome']}")
print(f"responsavel: {Db.ativo['responsavel']}")
print(f"localizado: {Db.ativo['local']}")