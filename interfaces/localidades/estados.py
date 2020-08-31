import json
import httpx


url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"


class Estados:
    def __init__(self):
        response = httpx.get(url)
        self.json_ibge = json.loads(response.content.decode("utf-8"))

    def json(self):
        return self.json_ibge

    def count(self):
        return len(self.json_ibge)

    def get_id(self):
        return [self.json_ibge[i]["id"] for i in range(self.count())]

    def get_name(self):
        return [self.json_ibge[i]["nome"] for i in range(self.count())]
