def jogo_numero_secreto():
    """
    Jogo de adivinhar um número secreto, contando as tentativas.
    """
    numero_secreto = 73  # Número fixo que o jogador deve adivinhar
    tentativas = 0
    chute = None  # Variável para guardar o chute do jogador

    print("--- Bem-vindo ao Jogo do Número Secreto! ---")
    print("Eu escolhi um número. Tente adivinhar qual é.")

    # O laço 'while' continua executando enquanto o chute for diferente do número secreto
    while chute != numero_secreto:
        
        # Pede ao jogador para digitar um número e o armazena como string
        chute_str = input("\nQual o seu chute? ")

        # Incrementa o contador de tentativas a cada vez que o jogador tenta
        tentativas += 1

        # Tenta converter a entrada do usuário para um número inteiro
        try:
            chute = int(chute_str)
        except ValueError:
            # Se a conversão falhar (ex: usuário digitou texto), avisa e recomeça o laço
            print("Entrada inválida. Por favor, digite apenas um número.")
            continue # Pula para a próxima iteração do laço

        # Verifica se o chute está errado para dar o feedback
        if chute != numero_secreto:
            print("Você errou. Tente mais uma vez!")
    
    # Esta parte do código só é alcançada quando o laço 'while' termina,
    # o que só acontece quando 'chute' for igual a 'numero_secreto'.
    print(f"\n*** Parabéns! Você acertou o número secreto '{numero_secreto}'! ***")
    print(f"Você precisou de {tentativas} tentativa(s) para adivinhar.")

# Garante que o jogo rode quando o script for executado
if __name__ == "__main__":
    jogo_numero_secreto()