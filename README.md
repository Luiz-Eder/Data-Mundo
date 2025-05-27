
# 🧠 Data_Mundo - RPG Digital em Terminal

## 🎓 Informações dos Integrantes

- **Nome completo:** [Seu Nome Aqui]  
- **RA:** [Seu RA Aqui]  
- **Turma:** [Sua Turma Aqui]

---

## 📖 História

No ano de 1999, durante os instantes finais antes da virada do milênio, algo inesperado aconteceu. Três humanos foram escolhidos — ou talvez acidentalmente envolvidos — em um colapso digital causado por um bug desconhecido na infraestrutura global da internet. No momento em que os relógios marcaram a meia-noite, eles foram transportados para um mundo misterioso e cibernético, um universo chamado **Data_Mundo**.

**Data_Mundo** é um lugar onde os próprios blocos de informação tomam forma física. Dados fluem como rios luminosos, estruturas lembram chips e circuitos, e todo o ambiente pulsa com a energia de um superprocessador ancestral. É um mundo onde a lógica e o caos convivem, onde fragmentos de software abandonado criam criaturas hostis, e onde erros de sistema ganham vida como aberrações conhecidas como "Vírus".

---

## 🎯 Objetivo do Projeto

O projeto **Data_Mundo** é um RPG por terminal desenvolvido em Python para um trabalho acadêmico, com o objetivo de aplicar de forma prática estruturas de dados como **listas**, **tuplas**, **dicionários**, **pilhas** e **filas**. Os jogadores criam personagens digitais que enfrentam inimigos cibernéticos em batalhas baseadas em turnos e atributos.

---

## 🚀 Como Executar o Jogo

### Pré-requisitos

- Python 3.10 ou superior
- Terminal ou prompt de comando
- Editor de código (opcional)

### Instruções

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/data_mundo.git
   cd data_mundo
   ```

2. Execute o jogo:
   ```bash
   python data_mundo.py
   ```

3. Siga as instruções exibidas no terminal.

---

## 🕹️ Como o Sistema Funciona

O jogo simula uma aventura digital com batalhas entre heróis e inimigos virtuais. O jogador monta um grupo com **até 3 personagens**, escolhendo:

- **Nome**
- **Classe**
- **Distribuição de pontos de atributos**
- **Arma**

### Classes disponíveis

Cada classe oferece bônus iniciais únicos:

- **Espadachim Tecnológico**: Alta ofensiva de Dados  
- **Patrulheiro do Cyber Espaço**: Alta Manutenção  
- **Manipulador**: Focado em Vírus  
- **Restaurador**: Equilibrado

### Atributos

- **Dados**: poder ofensivo
- **Manutenção**: velocidade (define ordem de turno)
- **Vírus**: dano extra a cada 5 pontos

### Armas

Armas fornecem bônus adicionais nos atributos. Ex: Espada e Escudo (+3 em cada atributo).

---

## ⚔️ Sistema de Combate

O combate é por turnos e segue esta lógica:

1. Ordem definida pelo atributo **Manutenção**
2. O jogador escolhe um inimigo e o atributo de ataque
3. O inimigo possui um atributo de defesa (oculto para o jogador)

### Cálculo de Dano

- Dano = valor do atributo de ataque + (Vírus // 5)
- **Efetividade**:
  - Se o ataque for forte contra a defesa: **dano dobrado**
  - Se for fraco: **dano reduzido à metade**
  - Se igual: **dano normal**

Relação de efetividade (tipo pedra-papel-tesoura):

- **Dados > Manutenção > Vírus > Dados**

---

## 💾 Estruturas de Dados Utilizadas

### ✅ Listas

- Armazenam os personagens (`jogadores`) e ações (`acoes_realizadas`)

### ✅ Tuplas

- Retornam múltiplos valores ao calcular dano: `(atributo, defesa, dano, efetividade)`

### ✅ Dicionários

- Usados para armazenar:
  - Atributos das classes e armas
  - Fichas dos personagens
  - Atributos e status dos inimigos

### ✅ Pilha

- Histórico de ações é uma pilha (lista com `.pop()` para exibir do fim ao início)

### ✅ Fila (deque)

- Usada para gerenciar a **ordem de turnos** de jogadores e inimigos

---

## 📜 Exemplo de Fluxo

1. O usuário cria 3 personagens.
2. Escolhe suas armas e distribui pontos.
3. Um grupo de inimigos é gerado aleatoriamente.
4. O combate inicia com base nos atributos.
5. Ao final da luta, o histórico de ações é exibido.
6. O sistema pergunta se o jogador deseja jogar novamente.
