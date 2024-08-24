import requests

def get_localidades():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
    response = requests.get(url)
    if response.status_code == 200:
        localidades = response.json()
        return [(localidade['nome'], localidade['nome']) for localidade in localidades]
    return []
