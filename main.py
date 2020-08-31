from database import client
from interfaces.localidades.regioes import Regioes
from interfaces.localidades.estados import Estados
from interfaces.localidades.municipios import Municipios
from interfaces.cnae.cnae import Cnae


regioes = Regioes()
regioes_data = regioes.json_ibge
print(regioes_data)

db = client["db"]
regiao_collection = db["regiao_collection"]

for regiao in regioes_data:
    regiao_collection.insert_one(regiao)


estados = Estados()
estado_data = estados.json_ibge
print(estado_data)

estado_collection = db["estado_collection"]

for estado in estado_data:
    estado_collection.insert_one(estado)


my_collections = db.list_collection_names()
print("\n")
print(f"Tolas collections do DB: {my_collections}")


# Municípios por Estado

cidades_collection = db["cidades"]

# estado_id = [estados.get_id()]
cidades = Municipios()
cidades_data = cidades.json_ibge

for cidade in cidades_data:
    print(f"Cidade: {cidade}")
    cidades_collection.insert_one(cidade)


# CNAE

cnae_collection = db["cnae"]

cnae = Cnae()
cnae_data = cnae.json_ibge



for cnae in cnae_data:
    cnae_collection.insert_one(cnae)
    print(f"CNAE: {cnae}")
