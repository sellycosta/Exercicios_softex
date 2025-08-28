#Mesclando dois dicionários
#Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.

def unir_dicionarios(dic1, dic2):
    novo_dic = {}
    
    for chave in dic1:
        novo_dic[chave] = dic1[chave]

    for chave in dic2:
        novo_dic[chave] = dic2[chave]
    
    return novo_dic
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}

resultado = unir_dicionarios(dicionario1, dicionario2)
print(resultado)