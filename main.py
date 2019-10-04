import requests, hashlib
from juliocesar import *

token = {
    'token': '22c4c2f9247d694573ffce44049b807d87970dfe'
}
response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data", params=token)
api = json.loads(response.content)

cifrado = api['cifrado']
chave = api['numero_casas']
api['decifrado'] = decriptaJC(cifrado, chave)
api['resumo_criptografico'] = hashlib.sha1(api['decifrado'].encode('utf-8')).hexdigest()
json_arquivo(api)

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'
answer = {
    'answer':open('answer.json', 'rb')
}

r = requests.post(url, params=token, files=answer)
print(r.status_code)
print(json.loads(r.content))