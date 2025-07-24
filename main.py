from random import randint

lista_npcs = []

jogador = {
    'nome': 'Samuel',
    'level': 1,
    'exp': 0,
    'exp_max': 30,
    'hp': 100,
    'hp_max': 100,
    'dano': 25,
}

def criar_npcs(level):
    novo_npc = {
        'nome': f'Monstro #{level}',
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'exp': 7 * level,
    }

    return novo_npc

def gerar_npcs(n_npcs):
    for x in range(n_npcs):
       npc = criar_npcs(x + 1)
       lista_npcs.append(npc)

def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_npc(npc):
    print(
        f'Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}'
        )

def exibir_jogador():
    print(
        f'Nome: {jogador['nome']} // Level: {jogador['level']} // Dano: {jogador['dano']} // HP: {jogador['hp']}/{jogador['hp_max']} // EXP: {jogador['exp']}/{jogador['exp_max']}'
        )

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def reset_jogador():
    jogador['hp'] = jogador['hp_max']

def level_up():
    if jogador['exp'] >= jogador['exp_max']:
        jogador['level'] += 1
        jogador['exp'] = 0
        jogador['exp_max'] *= 2
        jogador['hp_max'] += 20

def iniciar_batalha(npc):
    while jogador['hp'] > 0 and npc['hp'] > 0:
        atacar_npc(npc)
        atacar_jogador(npc)
        exibir_info_batalha(npc)

    if jogador['hp'] > 0:
        print(f'{jogador['nome']} venceu a batalha. Voce ganhou {npc['exp']} de EXP')
        jogador['exp'] += npc['exp']
        exibir_jogador()
    else:
        print('voce morreu')
        exibir_npc(npc)
    
    level_up()
    reset_jogador()
    reset_npc(npc)

def atacar_npc(npc):
    npc['hp'] -= jogador['dano']

def atacar_jogador(npc):
    jogador['hp'] -= npc['dano']

def exibir_info_batalha(npc):
    print(f'Jogador: {jogador['hp']}/{jogador['hp_max']}')
    print(f'{npc['nome']}:  {npc['hp']}/{npc['hp_max']}')
    print('---------------------\n')

gerar_npcs(5)

npc_selecionado = lista_npcs[0] 

iniciar_batalha(npc_selecionado)

exibir_jogador()