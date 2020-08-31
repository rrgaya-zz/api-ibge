import json
import httpx


url = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes"


class Regioes:
    def __init__(self, json_ibge=None):
        response = httpx.get(url)
        self.json_ibge = json.loads(response.content.decode("utf-8"))

    def json(self):
        return self.json_ibge

    # def count(self):
    #     return len(self.json_ibge)

    # def getId(self):
    #     return [self.json_ibge[i]['id'] for i in range(self.count()
