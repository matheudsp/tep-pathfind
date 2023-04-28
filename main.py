import math

mapa = [
    {
        'id': 'P1',
        'nome': 'Jorge',
        'latitude': -6.768548275697400,
        'longitude': -4.301760423917900,
        'destinos': ['P2'],
        'distancias': []
    },
    {
        'id': 'P2',
        'nome': 'Farmácia',
        'latitude': -6.767962277224870,
        'longitude': -43.018312302409400,
        'destinos': ['P3'],
        'distancias': []
    },
    {
        'id': 'P3',
        'nome': 'Auto Peças Falcão',
        'latitude': -67.677172334928300,
        'longitude': -4.301856443005070,
        'destinos': ['P4, P7'],
        'distancias': []
    },
    {
        'id': 'P4',
        'nome': 'Subway',
        'latitude': -6.766944812219210,
        'longitude': -4.301986261918240,
        'destinos': [''],
        'distancias': []
    },
    {
        'id': 'P5',
        'nome': 'Galeria dos Calçados',
        'latitude': -6.767658636060210,
        'longitude': -4.301978751733180,
        'destinos': ['P4, P7'],
        'distancias': []
    },
    {
        'id': 'P6',
        'nome': 'Pastel do Chinês',
        'latitude': -67.687240428149800,
        'longitude': -43.019664135720100,
        'destinos': ['P8'],
        'distancias': []
    },
    {
        'id': 'P7',
        'nome': 'Apartamento',
        'latitude': -6.767978258333520,
        'longitude': -43.019009676736300,
        'destinos': ['P8'],
        'distancias': []
    },
     {
        'id': 'P8',
        'nome': 'Paraíba',
        'latitude': -6.768654791447370,
        'longitude': -43.018966761393100,
        'destinos': ['P1'],
        'distancias': []
    
    },
    
]

def ligaPontos(pa,pb,dist):
    pa['destinos'].append(pb['id'])
    pb['destinos'].append(pa['id'])
    pa['distancias'].append(dist)
    pb['distancias'].append(dist)

ligaPontos(mapa[0], mapa[1], 140)

print(mapa[0]['destinos'], mapa[0]['distancias'], mapa[1]['destinos'],mapa[1]['distancias'])