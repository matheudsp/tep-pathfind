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

    # print(pa['destinos'], pa['distancias'], pb['destinos'])


def distancia_entre(p1, p2):
    return sqrt((p2['latitude'] - p1['latitude']) ** 2 + (p2['longitude'] - p1['longitude']) ** 2)


def andarMapa(origem, destino):
    # Inicializa as listas de nós abertos e fechados
    abertos = [origem]
    fechados = []

    # Dicionário para armazenar os custos
    custos = {origem['id']: 0}

    # Dicionário para armazenar os pais de cada nó
    pais = {}

    while abertos:
        # Escolhe o nó com o menor custo até agora
        atual = min(
            abertos, key=lambda x: custos[x['id']] + distancia_entre(x, destino))

        # Se chegamos no destino, constrói o caminho e retorna
        if atual == destino:
            caminho = [destino['id']]

            while atual['id'] != origem['id']:
                caminho.append(pais[atual['id']]['id'])
                atual = pais[atual['id']]
            caminho.reverse()
            print("Caminho encontrado:", caminho)
            print("Distância total:", custos[destino['id']])
            return caminho

        # Remove o nó atual da lista de abertos e adiciona na lista de fechados
        abertos.remove(atual)
        fechados.append(atual)
        
        # Para cada vizinho do nó atual
        
        for vizinho_id in atual['destinos']:
            
            vizinho = next(item for item in mapa if item["id"] == vizinho_id)
            if vizinho in fechados:
                # Se o vizinho já está na lista de fechados, ignora
                continue
            
            # Calcula o custo até o vizinho
            if vizinho_id in atual['destinos']:
                novo_custo = custos[atual['id']] + atual['distancias'][atual['destinos'].index(vizinho_id)]
                if vizinho not in abertos:
                    abertos.append(vizinho)
                    # Se o novo custo é maior do que o custo já calculado até o vizinho, ignora
                elif novo_custo >= custos.get(vizinho['id'], float('inf')):
                    continue
            
            # Atualiza o custo e o pai do vizinho
                custos[vizinho['id']] = novo_custo
                pais[vizinho['id']] = atual
            else:
                
                print('vizinho_id não está presente na lista atual[destinos]')
                
            
         
    # Se não foi possível encontrar um caminho, retorna None
                
        
if '__main__' == '__main__':
    # ligaPontos(mapa[0], mapa[1], 140)
    ligaPontos(mapa[1], mapa[2], 38)
    ligaPontos(mapa[2], mapa[3], 200)
    ligaPontos(mapa[2], mapa[6], 71)
    # ligaPontos(mapa[4], mapa[3], 80)
    ligaPontos(mapa[5], mapa[4], 121)
    ligaPontos(mapa[5], mapa[7], 83)
    ligaPontos(mapa[7], mapa[0], 151)
    ligaPontos(mapa[6], mapa[4], 99)
    ligaPontos(mapa[6], mapa[7], 75)

    andarMapa(mapa[1], mapa[2])


