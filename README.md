# 💾 Data_Mundo

## 🌐 Um RPG de Terminal no Mundo Digital

**Data_Mundo** é um jogo de RPG baseado em texto, onde você cria personagens e enfrenta inimigos em um mundo digital corrompido. 

## 📜 História

No ano de 1999, durante os instantes finais antes da virada do milênio, algo inesperado aconteceu. Três humanos foram escolhidos — ou talvez acidentalmente envolvidos — em um 
colapso digital causado por um bug desconhecido na infraestrutura global da internet. No momento em que os relógios marcaram a meia-noite, eles foram transportados para um 
mundo misterioso e cibernético, um universo chamado Data_Mundo.

Data_Mundo é um lugar onde os próprios blocos de informação tomam forma física. Dados fluem como rios luminosos, estruturas lembram chips e circuitos, e todo o ambiente pulsa 
com a energia de um superprocessador ancestral. É um mundo onde a lógica e o caos convivem, onde fragmentos de software abandonado criam criaturas hostis, e onde erros de 
sistema ganham vida como aberrações conhecidas como "Vírus".

---

## ⚙️ Como Jogar

### ✅ Requisitos

- Python 3.8+ instalado

### ▶️ Rodando o Jogo

1. Abra o terminal na pasta do arquivo.
2. Execute o jogo com:

```
python Data_Mundo.py
```

> ❗ Execute no terminal, não no painel "Output".

---

## 🧍 Criação de Personagens

Você criará 3 personagens, um por vez.

- Escolha uma classe (com bônus únicos):
  - Espadachim Tecnológico 
  - Patrulheiro do Cyber Espaço 
  - Manipulador
  - Restaurador 

- Distribua 15 pontos entre os atributos:
  - Dados
  - Manutenção
  - Vírus

- Escolha uma arma (oferece bônus adicionais).

- A vida base é: `10 + (Atributo: Dados // 2)`

---

## 🧬 Atributos

| Atributo    | Função                                                    |
|-------------|-----------------------------------------------------------|
| `Dados`     | Ataque e vida                                             |
| `Manutenção`| Velocidade no combate                                     |
| `Vírus`     | Bônus de dano (+1 a cada 5 pontos)                        |

---

## ⚔️ Combate

- Os turnos são organizados por ordem de Manutenção.
- Jogadores e inimigos se alternam em combate.
- Você escolhe um inimigo e um atributo para atacar.
- O jogo calcula o dano com base em efetividade entre atributos:

### 🔄 Sistema de Fraqueza (tipo pedra-papel-tesoura)

- Dados > Manutenção
- Manutenção > Vírus
- Vírus > Dados

### 🎯 Cálculo de Dano

- Jogadores: `atributo_escolhido + (Vírus // 5)`
- Inimigos: dano fixo

> Efeitos:
> - Eficaz: dano dobrado
> - Ineficaz: dano reduzido à metade (mínimo 1)
> - Neutro: dano normal

---

## 👾 Inimigos

Você enfrentará inimigos como:

- Cyber Goblin
- Lobo Glitch
- Android
- Bug

Cada um com atributos de defesa e vida diferentes.

---

## 💾 Estruturas Usadas

- `deque`: Fila de inimigos e ordem de turnos
- `list`: Pilha de ações (histórico)
- `dict` e `tuple`: Atributos e retorno de funções
- `random`: Escolhas de inimigos e atributos

---

## 📜 Histórico

Ao final do jogo, você verá um resumo das ações em ordem reversa (última para a primeira).

---

## 🔁 Rejogar

Ao final da partida, o jogo pergunta se você deseja jogar novamente ou encerrar.

---

## 🎯 Exemplo de Combate

Turno de Poli (Restaurador)
Vida: 14/14
Atributos: {'Dados': 4, 'Manutenção': 4, 'Vírus': 2}

Inimigos disponíveis:
1. Android (Vida: 24)

Escolha o atributo para atacar:
1. Dados (4)
2. Manutenção (4)
3. Vírus (2)

-> Poli usou Manutenção contra Android (defesa: Vírus): 8 de dano (⚡ Eficaz!)

## 👨‍💻 Desenvolvido por

-Eder Luiz da Silva Ribeiro RA: 1971959 
-
-

---
