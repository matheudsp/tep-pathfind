import math

mapa = [
    {
        'id': 1,
        'nome': 'Jorge',
        'latitude': -6.768548275697400,
        'longitude': -4.301760423917900,
        'destinos': [2],
        'distancias': [140]
    },
    {
        'id': 2,
        'nome': 'Farmácia',
        'latitude': -6.767962277224870,
        'longitude': -43.018312302409400,
        'destinos': [1,3],
        'distancias': [140,38]
    },
    {
        'id': 3,
        'nome': 'Auto Peças Falcão',
        'latitude': -67.677172334928300,
        'longitude': -4.301856443005070,
        'destinos': [2],
        'distancias': [38]
    },
    {
        'id': 4,
        'nome': 'Subway',
        'latitude': -6.766944812219210,
        'longitude': -4.301986261918240,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 5,
        'nome': 'Galeria dos Calçados',
        'latitude': -6.767658636060210,
        'longitude': -4.301978751733180,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 6,
        'nome': 'Pastel do Chinês',
        'latitude': -67.687240428149800,
        'longitude': -43.019664135720100,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 7,
        'nome': 'Apartamento',
        'latitude': -6.767978258333520,
        'longitude': -43.019009676736300,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 8,
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
    pb['distancias'].append(dist)

    # print(pa['destinos'], pa['distancias'], pb['destinos'], pb['distancias'])

def distancia_entre_pontos(lat1, lon1, lat2, lon2):
    # Utiliza a fórmula de haversine para calcular a distância entre dois pontos
    R = 6371  # Raio da Terra em quilômetros
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distancia = R * c
    return distancia

def a_estrela(mapa, origem, destino):
    # Encontra a melhor rota utilizando o algoritmo A*
    g_score = {}  # custo atual para chegar a cada ponto
    f_score = {}  # custo estimado total para chegar ao destino passando por cada ponto
    open_set = set()  # pontos a serem explorados
    closed_set = set()  # pontos já explorados
    came_from = {}  # mapa de caminhos percorridos

    # Inicializa os dicionários com valores infinitos, exceto para o ponto de origem
    for ponto in mapa:
        g_score[ponto['id']] = math.inf
        f_score[ponto['id']] = math.inf
    g_score[origem] = 0
    f_score[origem] = distancia_entre_pontos(mapa[origem-1]['latitude'], mapa[origem-1]['longitude'],mapa[destino-1]['latitude'], mapa[destino-1]['longitude'])

    open_set.add(origem)

    while open_set:
        # Encontra o ponto com o menor custo estimado total
        ponto_atual = min(open_set, key=lambda x: f_score[x])

        if ponto_atual == destino:
            # Caminho encontrado
            caminho = [ponto_atual]
            gasto_total = g_score[ponto_atual]
            while ponto_atual in came_from:
                ponto_atual = came_from[ponto_atual]
                caminho.insert(0, ponto_atual)
            return caminho, gasto_total

        open_set.remove(ponto_atual)
        closed_set.add(ponto_atual)

        for i, adjacente in enumerate(mapa[ponto_atual-1]['destinos']):
            if adjacente in closed_set:
                continue

            custo_atual = g_score[ponto_atual] + mapa[ponto_atual-1]['distancias'][i]

            if adjacente not in open_set:
                open_set.add(adjacente)
            elif custo_atual >= g_score[adjacente]:
                continue

            came_from[adjacente] = ponto_atual
            g_score[adjacente] = custo_atual
            f_score[adjacente] = custo_atual + distancia_entre_pontos(mapa[adjacente-1]['latitude'],mapa[adjacente-1]['longitude'],mapa[destino-1]['latitude'],mapa[destino-1]['longitude'])

    # Não foi possível encontrar um caminho
    return None, None



if '__main__' == '__main__':
    ligaPontos(mapa[0], mapa[1], 140)
    ligaPontos(mapa[1], mapa[2], 38)
    ligaPontos(mapa[2], mapa[3], 200)
    ligaPontos(mapa[2], mapa[6], 71)
    ligaPontos(mapa[4], mapa[3], 80)
    ligaPontos(mapa[5], mapa[4], 121)
    ligaPontos(mapa[5], mapa[7], 83)
    ligaPontos(mapa[6], mapa[4], 99)
    ligaPontos(mapa[6], mapa[7], 75)
    
    origem = 3
    destino = 4

    caminho, gasto_total = a_estrela(mapa, origem, destino)

    if caminho:
        print("Caminho encontrado:")
        for ponto_id in caminho:
            ponto = mapa[ponto_id-1]
            print(f"{ponto['id']} - {ponto['nome']} - Latitude: {ponto['latitude']}, Longitude: {ponto['longitude']}")
        print(f"Gasto total: {gasto_total}m")
    else:
        print("Não foi possível encontrar um caminho entre os pontos de origem e destino.")
    