import json

def decriptaJC(texto, chave):
    #Decripta uma string criptografa com o Algoritmo de Júlio César
    CARACTERES = 'abcdefghijklmnopqrstuvwxyz'
    convertido = ''
    for caractere in texto:
        if caractere in CARACTERES:
            num = CARACTERES.find(caractere) - chave
            if num < 0:
                num = num + len(CARACTERES)
            convertido = convertido + CARACTERES[num]
        else:
            convertido += caractere
    return convertido

def json_arquivo(api):
        with open('answer.json', 'w') as f:
            json.dump(api, f)