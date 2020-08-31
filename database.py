import logging
from pymongo import MongoClient

status = True

while status:
    try:
        print("Estabelecendo conexão com DB...")
        logging.info("Estabelecendo conexão com DB...")
        client = MongoClient("localhost", 27017, username="root", password="rootpassword")
        db = client["unep_db"]
        # uf_collection = db["uf"]
        print(db.list_collection_names())
        status = False
    except:
        print("Erro ao tentar se conectar")
        logging.info("Erro ao tentar se conectar")
        status = False

