from math import sqrt

mapa = [
    {
        'id': 'P1',
        'nome': 'Jorge',
        'latitude': -6.768548275697400,
        'longitude': -4.301760423917900,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 'P2',
        'nome': 'Farmácia',
        'latitude': -6.767962277224870,
        'longitude': -43.018312302409400,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 'P3',
        'nome': 'Auto Peças Falcão',
        'latitude': -67.677172334928300,
        'longitude': -4.301856443005070,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 'P4',
        'nome': 'Subway',
        'latitude': -6.766944812219210,
        'longitude': -4.301986261918240,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 'P5',
        'nome': 'Galeria dos Calçados',
        'latitude': -6.767658636060210,
        'longitude': -4.301978751733180,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 'P6',
        'nome': 'Pastel do Chinês',
        'latitude': -67.687240428149800,
        'longitude': -43.019664135720100,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 'P7',
        'nome': 'Apartamento',
        'latitude': -6.767978258333520,
        'longitude': -43.019009676736300,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 'P8',
        'nome': 'Paraíba',
        'latitude': -6.768654791447370,
        'longitude': -43.018966761393100,
        'destinos': [],
        'distancias': []

    },

]


def ligaPontos(pa, pb, dist):
    pa['destinos'].append(pb['id'])
    pb['destinos'].append(pa['id'])
    pa['distancias'].append(dist)

    print(pa['destinos'], pa['distancias'], pb['destinos'])

def distancia(lat1, lon1, lat2, lon2):
    return sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

def encontrar_caminho(origem, destino, mapa):
    # Crie um dicionário para armazenar as distâncias percorridas
    distancias = {ponto['id']: float('inf') for ponto in mapa}
    distancias[origem] = 0

    # Crie um dicionário para armazenar o caminho percorrido
    caminho = {ponto['id']: [] for ponto in mapa}
    caminho[origem] = [origem]

    # Crie uma lista para armazenar os pontos visitados
    visitados = []

    # Comece pelo ponto de origem
    atual = origem

    while atual != destino:
        # Adicione o ponto atual à lista de visitados
        visitados.append(atual)

        # Encontre o destino mais próximo
        vizinhos = mapa[[ponto['id'] for ponto in mapa].index(atual)]['destinos']
        dist_vizinhos = mapa[[ponto['id'] for ponto in mapa].index(atual)]['distancias']
        for i, vizinho in enumerate(vizinhos):
            if vizinho not in visitados:
                nova_distancia = distancias[atual] + dist_vizinhos[i] + distancia(mapa[[ponto['id'] for ponto in mapa].index(vizinho)]['latitude'], mapa[[ponto['id'] for ponto in mapa].index(vizinho)]['longitude'], mapa[[ponto['id'] for ponto in mapa].index(destino)]['latitude'], mapa[[ponto['id'] for ponto in mapa].index(destino)]['longitude'])
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    caminho[vizinho] = caminho[atual] + [vizinho]

        # Se não houver mais vizinhos, pare o loop
        if not vizinhos:
            break

        # Selecione o próximo ponto a visitar
        nao_visitados = {ponto['id']: distancias[ponto['id']] for ponto in mapa if ponto['id'] not in visitados}
        atual = min(nao_visitados, key=nao_visitados.get)

    # Retorne o caminho e a distância percorrida
    return caminho[destino], distancias[destino]
        
if '__main__' == '__main__':
    # ligaPontos(mapa[0], mapa[1], 140)
    ligaPontos(mapa[1], mapa[2], 38)
    ligaPontos(mapa[2], mapa[3], 200)
    ligaPontos(mapa[2], mapa[6], 71)
    # ligaPontos(mapa[4], mapa[3], 80)
    # ligaPontos(mapa[5], mapa[4], 121)
    # ligaPontos(mapa[5], mapa[7], 83)
    # ligaPontos(mapa[6], mapa[4], 99)
    # ligaPontos(mapa[6], mapa[7], 75)

    origem = 'P2'
    destino = 'P3'
    caminho, distancia_percorrida = encontrar_caminho(origem, destino, mapa)

    # Imprima o resultado
    print('Caminho:', caminho)
    print('Distância: ', distancia_percorrida)


