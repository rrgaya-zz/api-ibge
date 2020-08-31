import json
import httpx


class Municipios(object):

    def __init__(self, json_ibge=None):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
        request = httpx.get(url)
        self.json_ibge = json.loads(request.content.decode('utf-8'))

    def json(self):
        return self.json_ibge

    def __repr__(self):
        return repr(self.json())

    def count(self):
        return len(self.json_ibge)
        
    def getId(self):
        return [self.json_ibge[i]['id'] for i in range(self.count())]

    def getNome(self):
        return [self.json_ibge[i]['nome'] for i in range(self.count())]

    def getDescricaoUF(self):
        return [self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['nome'] for i in range(self.count())]

    def getSiglaUF(self):
        return [self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['sigla'] for i in range(self.count())]

    def getDados(self):
        dados = []
        for i in range(self.count()):
            data = dict()
            data['ibge'] = self.json_ibge[i]['id']
            data['nome'] = self.json_ibge[i]['nome']
            data['uf'] = self.json_ibge[i]['microrregiao']['mesorregiao']['UF']['sigla']
            dados.append(data)
        return dados