import math

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


ligaPontos(mapa[0], mapa[1], 140)
ligaPontos(mapa[0], mapa[1], 150)
ligaPontos(mapa[1], mapa[2], 38)
ligaPontos(mapa[2], mapa[3], 200)
ligaPontos(mapa[2], mapa[6], 71)
ligaPontos(mapa[4], mapa[3], 80)
ligaPontos(mapa[5], mapa[4], 121)
ligaPontos(mapa[5], mapa[7], 83)
ligaPontos(mapa[7], mapa[0], 151)
ligaPontos(mapa[6], mapa[4], 99)
ligaPontos(mapa[6], mapa[7], 75)


def andarMapa(origem, destino):
    distancia = {ponto['id']: math.inf for ponto in mapa}
    distancia[origem['id']] = 0
    anterior = {ponto['id']: None for ponto in mapa}

    naoVisitados = set(mapa)

    while naoVisitados:

        p = min(naoVisitados, key=lambda ponto: distancia[ponto['id']])
        naoVisitados.remove(p)
        for q_id in p['destinos']:
            q = next(ponto for ponto in mapa if ponto['id'] == q_id)
            novaDistancia = distancia[p['id']] + p['distancias'][p['destinos'].index(q_id)]
            if novaDistancia < distancia[q_id]:
                distancia[q_id] = novaDistancia
                anterior[q_id] = p['id']

    caminho = [destino['id']]
    distanciaTotal = distancia[destino]


       # desenvolver a estrela e encontrar o caminho
       # ler origem e destino
       # melhor rota e distancia
