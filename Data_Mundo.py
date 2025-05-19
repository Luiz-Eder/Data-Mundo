
import os
import random
from collections import deque

# ==== CONSTANTES ====
CLASSES = [
    "Espadachim Tecnológico",
    "Patrulheiro do Cyber Espaço",
    "Manipulador Digital",
    "Restaurador Digital"
]

ARMAS = {
    "Espada e Escudo": {"Dados": 3, "Manutenção": 3, "Vírus": 3},
    "Arco": {"Dados": 2, "Manutenção": 4, "Vírus": 3},
    "Clava": {"Dados": 1, "Manutenção": 5, "Vírus": 0},
    "Espadão": {"Dados": 5, "Manutenção": 0, "Vírus": 2},
    "Cajado": {"Dados": 1, "Manutenção": 0, "Vírus": 5}
}

ATRIBUTOS = ["Dados", "Manutenção", "Vírus"]
TOTAL_PONTOS = 15
EFETIVIDADE = {
    "Dados": "Manutenção",
    "Manutenção": "Vírus",
    "Vírus": "Dados"
}

# ==== ESTRUTURAS DE DADOS ====
jogadores = []
fila_turnos = deque()
acoes_realizadas = []

# ==== FUNÇÕES ====
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def criar_ficha():
    limpar()
    print("🔷 Bem-vindo ao Fim do Cyber Espaço!")

    nome = input("Digite o nome do seu personagem: ").strip()
    while not nome:
        nome = input("Nome inválido. Digite novamente: ").strip()

    print("\nEscolha uma classe:")
    for i, classe in enumerate(CLASSES, 1):
        print(f"{i}. {classe}")

    while True:
        try:
            escolha = int(input("Número da classe: "))
            if 1 <= escolha <= len(CLASSES):
                classe = CLASSES[escolha - 1]
                break
            print(f"Digite um número entre 1 e {len(CLASSES)}")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    pontos_restantes = TOTAL_PONTOS
    atributos = {atributo: 0 for atributo in ATRIBUTOS}

    for atributo in ATRIBUTOS:
        while True:
            try:
                print(f"\nAtributos atuais: {atributos} | Pontos restantes: {pontos_restantes}")
                val = int(input(f"Pontos em {atributo}: "))
                if 0 <= val <= pontos_restantes:
                    atributos[atributo] = val
                    pontos_restantes -= val
                    break
                print(f"Digite um valor entre 0 e {pontos_restantes}")
            except ValueError:
                print("Digite um número válido.")

    print("\nEscolha uma arma:")
    for i, arma in enumerate(ARMAS, 1):
        print(f"{i}. {arma} - Bônus: {ARMAS[arma]}")

    while True:
        try:
            escolha = int(input("Número da arma: "))
            if 1 <= escolha <= len(ARMAS):
                arma_nome = list(ARMAS.keys())[escolha - 1]
                arma_bonus = ARMAS[arma_nome]
                break
            print(f"Digite um número entre 1 e {len(ARMAS)}")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    for atributo in ATRIBUTOS:
        atributos[atributo] += arma_bonus.get(atributo, 0)

    vida = 10 + (atributos["Dados"] // 2)

    ficha = {
        "nome": nome,
        "classe": classe,
        "atributos": atributos,
        "arma": arma_nome,
        "vida": vida,
        "vida_maxima": vida
    }
    jogadores.append(ficha)
    print(f"\n✅ Ficha de {nome} criada com sucesso!")
    input("Pressione ENTER para continuar...")

def gerar_inimigos():
    inimigos = deque([
        {"nome": "Cyber Goblin", "vida": 18, "atributo_defesa": "Dados", "dano": 6},
        {"nome": "Lobo Glitch", "vida": 20, "atributo_defesa": "Vírus", "dano": 5},
        {"nome": "Android", "vida": 24, "atributo_defesa": "Manutenção", "dano": 8},
        {"nome": "Bug", "cida": 10, "atributo_defesa": "vírus", "dano": 2 }
    ])
    print("\n🚨 Inimigos encontrados:")
    for i, inimigo in enumerate(inimigos, 1):
        print(f"{i}. {inimigo['nome']} (Vida: {inimigo['vida']})")
    return inimigos

def calcular_dano(atacante, alvo, atributo):
    #O cálculo de dano segue esta lógica:
    #Jogador: dano = atributo selecionado + (atributo Vírus // 5)
    #Inimigo: usa dano fixo
    # Efetividade:
    #Se for forte contra a defesa: dobra o dano
    #Se for fraco contra a defesa: reduz à metade (mínimo 1)
    #Se igual: dano normal
    if "atributos" in atacante:
        base = atacante["atributos"][atributo]
        extra = atacante["atributos"]["Vírus"] // 5
        dano = base + extra
    else:
        dano = atacante["dano"]

    if "atributo_defesa" in alvo:
        defesa = alvo["atributo_defesa"]
    else:
        defesa = random.choice(ATRIBUTOS)

    efetividade = ""
    if EFETIVIDADE[atributo] == defesa:
        dano *= 2
        efetividade = "⚡ Eficaz!"
    elif EFETIVIDADE[defesa] == atributo:
        dano = max(1, dano // 2)
        efetividade = "🛡️ Ineficaz!"
    else:
        efetividade = "🎯 Normal."

    return (atributo, defesa, dano, efetividade)

def combate(grupo, inimigos):
    fila_turnos.extend(sorted(grupo, key=lambda x: x["atributos"]["Manutenção"], reverse=True))

    while True:
        vivos_inimigos = [i for i in inimigos if i["vida"] > 0]
        vivos_jogadores = [j for j in grupo if j["vida"] > 0]

        if not vivos_inimigos:
            print("\n✅ Todos os inimigos foram derrotados!")
            break
        if not vivos_jogadores:
            print("\n💀 Todos os jogadores foram derrotados!")
            break

        for jogador in list(fila_turnos):
            if jogador["vida"] <= 0:
                continue

            limpar()
            print(f"\n⚔️ Turno de {jogador['nome']} ({jogador['classe']})")
            print(f"Vida: {jogador['vida']}/{jogador['vida_maxima']}")
            print(f"Atributos: {jogador['atributos']}")

            print("\nInimigos disponíveis:")
            for i, inimigo in enumerate(vivos_inimigos, 1):
                print(f"{i}. {inimigo['nome']} (Vida: {inimigo['vida']})")

            while True:
                try:
                    escolha = int(input("\nEscolha o inimigo (1-{}): ".format(len(vivos_inimigos)))) - 1
                    if 0 <= escolha < len(vivos_inimigos):
                        alvo = vivos_inimigos[escolha]
                        break
                    print(f"Digite um número entre 1 e {len(vivos_inimigos)}")
                except ValueError:
                    print("Entrada inválida. Digite apenas números.")

            print("\nEscolha o atributo para atacar:")
            for i, atributo in enumerate(ATRIBUTOS, 1):
                print(f"{i}. {atributo} ({jogador['atributos'][atributo]})")

            while True:
                try:
                    atq = int(input("Opção (1-3): "))
                    if 1 <= atq <= 3:
                        atributo_ataque = ATRIBUTOS[atq - 1]
                        break
                    print("Digite um número entre 1 e 3")
                except ValueError:
                    print("Entrada inválida. Digite apenas números.")

            atributo, defesa, dano, efetividade = calcular_dano(jogador, alvo, atributo_ataque)
            alvo["vida"] -= dano
            acao = f"{jogador['nome']} usou {atributo} contra {alvo['nome']} (defesa {defesa}): {dano} de dano ({efetividade})"
            acoes_realizadas.append(acao)

            print(f"\n{acao}")
            if alvo["vida"] <= 0:
                print(f"☠️ {alvo['nome']} foi derrotado!")
                vivos_inimigos.remove(alvo)

            input("\nPressione ENTER para continuar...")

        for inimigo in [i for i in inimigos if i["vida"] > 0]:
            if not vivos_jogadores:
                break

            alvo = random.choice(vivos_jogadores)
            atributo_ataque = random.choice(ATRIBUTOS)

            atributo, defesa, dano, efetividade = calcular_dano(inimigo, alvo, atributo_ataque)
            alvo["vida"] -= dano
            acao = f"{inimigo['nome']} atacou {alvo['nome']} com {atributo} (defesa {defesa}): {dano} de dano ({efetividade})"
            acoes_realizadas.append(acao)

            print(f"\n{acao}")
            if alvo["vida"] <= 0:
                print(f"💀 {alvo['nome']} foi derrotado!")
                vivos_jogadores.remove(alvo)

            input("\nPressione ENTER para continuar...")

def montar_grupo():
    while len(jogadores) < 3:
        criar_ficha()

    limpar()
    print("\n🎮 Grupo Montado com Sucesso!")
    for jogador in jogadores:
        print(f"\n👤 {jogador['nome']} ({jogador['classe']})")
        print(f"  Arma: {jogador['arma']}")
        print(f"  Vida: {jogador['vida']}/{jogador['vida_maxima']}")
        print(f"  Atributos: {jogador['atributos']}")

# ==== EXECUÇÃO PRINCIPAL ====
if __name__ == "__main__":
    while True:
        jogadores.clear()
        fila_turnos.clear()
        acoes_realizadas.clear()

        montar_grupo()
        input("\nPressione ENTER para encontrar inimigos...")
        inimigos = gerar_inimigos()
        input("\nPressione ENTER para iniciar o combate...")
        combate(jogadores, inimigos)

        print("\n📜 Histórico de Ações:")
        while acoes_realizadas:
            print(f"- {acoes_realizadas.pop()}")

        while True:
            opcao = input("\n🔁 Deseja jogar novamente? (S/N): ").strip().lower()
            if opcao == "s":
                break
            elif opcao == "n":
                print("\n👋 Obrigado por jogar! Até a próxima.")
                exit()
            else:
                print("Digite S para sim ou N para não.")
