import math

mapa = [
    {
        'id': 1,
        'nome': 'Jorge',
        'latitude': -6.768537311331842, 
        'longitude': -43.01755245674647,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 2,
        'nome': 'Farmácia',
        'latitude': -6.767967318790024,
        'longitude': -43.01831420404162,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 3,
        'nome': 'Auto Peças Falcão',
        'latitude': -6.76768498578645, 
        'longitude': -43.018555602832336,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 4,
        'nome': 'Subway',
        'latitude': -6.766960507889815,
        'longitude':  -43.0198806139725,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 5,
        'nome': 'Galeria dos Calçados',
        'latitude': -6.767637042429814, 
        'longitude': -43.01980551212649,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 6,
        'nome': 'Pastel do Chinês',
        'latitude': -6.768686468147581,
        'longitude': -43.01967676610478,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 7,
        'nome': 'Apartamento',
        'latitude': -6.767977972862394, 
        'longitude': -43.0190330359962,
        'destinos': [],
        'distancias': []
    },
    {
        'id': 8,
        'nome': 'Paraíba',
        'latitude': -6.768654505976653,
        'longitude':  -43.01894720531506,
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
    
    g_score = {}  # custo atual para chegar a cada ponto
    f_score = {}  # custo estimado total para chegar ao destino passando por cada ponto
    nao_explorados = set()  # pontos a serem explorados
    explorados = set()  # pontos já explorados
    visitados = {}  # mapa de caminhos percorridos

    # Inicializa os dicionários com valores infinitos utilizando o ID do ponto, exceto para o ponto de origem, 
    # afinal os valores associados a essas chaves ainda não foram determinados ou são desconhecidos.
    for ponto in mapa:  #percorre cada dicionário de ponto contido na lista mapa.
        g_score[ponto['id']] = math.inf 
        f_score[ponto['id']] = math.inf
    g_score[origem] = 0 # custo atual para chegar ao ponto de origem é 0.
    f_score[origem] = distancia_entre_pontos(mapa[origem-1]['latitude'], mapa[origem-1]['longitude'],mapa[destino-1]['latitude'], mapa[destino-1]['longitude'])
    # atribui o custo estimado total para chegar ao ponto de destino 
    nao_explorados.add(origem)

    while nao_explorados:
        
        # encontra o ponto atual a ser explorado com base no menor valor de f_score(menor custo estimado total)
        ponto_atual = min(nao_explorados, key=lambda x: f_score[x])

        if ponto_atual == destino:
            # Caminho encontrado
            caminho = [ponto_atual]
            gasto_total = g_score[ponto_atual]
            while ponto_atual in visitados:
                ponto_atual = visitados[ponto_atual]
                caminho.insert(0, ponto_atual)
            return caminho, gasto_total

        nao_explorados.remove(ponto_atual)
        explorados.add(ponto_atual)

        # Itera sobre os pontos adjacentes ao ponto atual
        for i, adjacente in enumerate(mapa[ponto_atual-1]['destinos']):
            # Verifica se o ponto adjacente já foi explorado, se sim, passa para o próximo
            if adjacente in explorados:
                continue
            # Calcula o custo atual para chegar ao ponto adjacente
            custo_atual = g_score[ponto_atual] + mapa[ponto_atual - 1]['distancias'][i]

             # Verifica se o ponto adjacente já foi descoberto ou se o custo atual é maior do que o custo anteriormente calculado
            # Se sim, passa para o próximo ponto adjacente
            if adjacente not in nao_explorados:
                nao_explorados.add(adjacente)
            elif custo_atual >= g_score[adjacente]:
                continue
            
            # Registra o ponto atual como o caminho percorrido para chegar ao ponto adjacente
            visitados[adjacente] = ponto_atual

            # Atualiza o custo atual e o custo estimado total para chegar ao ponto adjacente
            g_score[adjacente] = custo_atual
            f_score[adjacente] = custo_atual + distancia_entre_pontos(mapa[adjacente-1]['latitude'],mapa[adjacente-1]['longitude'],mapa[destino-1]['latitude'],mapa[destino-1]['longitude'])

    # Não foi possível encontrar um caminho
    return None, None

def exibir_pontos(mapa):
    print('\n-------------------------------------------------------------')
    print("Pontos disponíveis:")
    for ponto in mapa:
        print(f"{ponto['id']} - {ponto['nome']}")
    print('-------------------------------------------------------------\n')

def buscar_caminho(mapa):
    print('\n-------------------------------------------------------------\n')
    print("Caminho disponível:")
    for ponto in mapa:
        print(f"{ponto['id']} - {ponto['nome']}")
    
    origem = int(input("Digite o ponto de origem: "))
    destino = int(input("Digite o ponto de destino: "))

    caminho, gasto_total = a_estrela(mapa, origem, destino)

    if caminho:
        print('\n-------------------------------------------------------------\n')
        print("Caminho encontrado:")
        for ponto_id in caminho:
            ponto = mapa[ponto_id-1]
            print(f"{ponto['id']} - {ponto['nome']}")
        print('\n-------------------------------------------------------------\n')
        print(f"Gasto total: {gasto_total}m")
        print('\n-------------------------------------------------------------\n')
    else:
        print("Não foi possível encontrar um caminho entre os pontos de origem e destino.")

def exibir_menu():
    print("Menu:")
    print("1. Exibir pontos disponíveis")
    print("2. Buscar caminho")
    print("3. Sair")

def main():
    ligaPontos(mapa[0], mapa[1], 140)
    ligaPontos(mapa[1], mapa[2], 38)
    ligaPontos(mapa[2], mapa[3], 200)
    ligaPontos(mapa[2], mapa[6], 71)
    ligaPontos(mapa[4], mapa[3], 80)
    ligaPontos(mapa[5], mapa[4], 121)
    ligaPontos(mapa[5], mapa[7], 83)
    ligaPontos(mapa[7], mapa[0], 160)
    ligaPontos(mapa[6], mapa[4], 99)
    ligaPontos(mapa[6], mapa[7], 78)


    while True:
        exibir_menu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            exibir_pontos(mapa)
        elif opcao == 2:
            buscar_caminho(mapa)
        elif opcao == 3:
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if '__main__' == '__main__':
    main()    

    
    