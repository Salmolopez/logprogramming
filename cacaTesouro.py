# --- Caça ao Tesouro Espacial ---

# Função para exibir o tabuleiro de forma organizada
def imprimir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro 3x3 no console."""
    print("\n   --- MAPA DO TESOURO ---")
    print("     Coluna 0   1   2")
    print("   ---------------------")
    for indice, linha in enumerate(tabuleiro):
        # O 'f' antes da string permite formatá-la, inserindo variáveis
        # O ' '.join(linha) transforma a lista [' ', 'X', ' '] em uma string "  X  "
        print(f"Linha {indice} | [ {'  |  '.join(linha)} ]")
    print("   ---------------------")

# 1. Configuração Inicial
# Cria uma lista de listas para representar o tabuleiro 3x3
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define a posição fixa do tesouro (linha 1, coluna 2)
tesouro_linha = 1
tesouro_coluna = 2

# Variável para saber se o tesouro foi encontrado
tesouro_encontrado = False

print("=============================================")
print("💎 BEM-VINDO À CAÇA AO TESOURO ESPACIAL! 💎")
print("=============================================")
print("Você tem 5 tentativas para encontrar o tesouro em um mapa 3x3.")

# 2. Loop Principal do Jogo
# O loop vai de 0 a 4 (total de 5 tentativas)
for tentativa in range(5):
    print(f"\n>>> Tentativa {tentativa + 1} de 5 <<<")
    
    imprimir_tabuleiro(tabuleiro)

    # 3. Entrada do Jogador
    try:
        chute_linha = int(input("Digite a linha para o seu palpite (0, 1 ou 2): "))
        chute_coluna = int(input("Digite a coluna para o seu palpite (0, 1 ou 2): "))
    except ValueError:
        print("\n❌ ERRO: Você deve digitar apenas números! Tente novamente. ❌")
        # O 'continue' pula para a próxima iteração do loop, sem gastar a tentativa
        # (na prática, o jogador apenas repete a jogada atual)
        continue

    # 4. Lógica e Validações
    # Verifica se o chute está fora do tabuleiro
    if chute_linha < 0 or chute_linha > 2 or chute_coluna < 0 or chute_coluna > 2:
        print("\n❌ POSIÇÃO INVÁLIDA! Escolha linhas e colunas entre 0 e 2. ❌")
        continue
    
    # Verifica se o jogador acertou o tesouro
    elif chute_linha == tesouro_linha and chute_coluna == tesouro_coluna:
        print("\n🎉 PARABÉNS! Você encontrou o tesouro! 🎉")
        tabuleiro[chute_linha][chute_coluna] = "💎"
        tesouro_encontrado = True
        # O 'break' encerra o loop 'for' imediatamente, pois o jogo acabou
        break
        
    # Verifica se o jogador já tentou esta posição antes
    elif tabuleiro[chute_linha][chute_coluna] == "X":
        print("\n⚠️ Você já tentou neste local! Tente outra coordenada. ⚠️")
        continue

    # Se não for nenhuma das opções acima, o jogador errou
    else:
        print("\n💥 Você errou! O tesouro não está aqui. 💥")
        # Marca a posição com 'X' para o jogador saber onde já tentou
        tabuleiro[chute_linha][chute_coluna] = "X"

# 5. Fim de Jogo
# Este bloco 'if' só é verificado após o loop 'for' terminar
if tesouro_encontrado:
    print("\nFIM DE JOGO - VOCÊ VENCEU!")
    imprimir_tabuleiro(tabuleiro)
else:
    print("\n--- FIM DE JOGO ---")
    print("Suas 5 tentativas acabaram e você não encontrou o tesouro.")
    # Revela onde o tesouro estava escondido
    tabuleiro[tesouro_linha][tesouro_coluna] = "💎"
    print("O tesouro estava aqui:")
    imprimir_tabuleiro(tabuleiro)
