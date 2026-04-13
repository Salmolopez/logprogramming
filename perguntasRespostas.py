def quiz_de_perguntas():
    """
    Um jogo de perguntas e respostas sobre Python com sistema de pontuação.
    """
    # Lista de listas no formato [pergunta, resposta_correta_em_minusculas]
    perguntas = [
        ["Qual a função para imprimir algo na tela em Python?", "print"],
        ["Qual estrutura de repetição percorre uma sequência de itens?", "for"],
        ["Como se chama uma coleção ordenada e mutável de itens em Python?", "lista"],
        ["Qual é a palavra-chave para definir uma nova função?", "def"],
        ["Qual o resultado da operação 2 ** 3?", "8"]
    ]

    # Variável para armazenar a pontuação, começando em zero
    pontuacao = 0

    print("--- Início do Quiz de Python! ---")
    print("Responda com palavras simples e em minúsculas.")

    # Laço 'for' para percorrer cada item na lista de perguntas
    for pergunta, resposta_correta in perguntas:
        
        # Mostra a pergunta ao usuário e armazena a resposta
        resposta_usuario = input(f"\n{pergunta}\nSua resposta: ").lower().strip()

        # Verifica se a resposta do usuário é igual à resposta correta
        if resposta_usuario == resposta_correta:
            print("Correto! Você ganhou +1 ponto.")
            pontuacao += 1  # Adiciona 1 à pontuação
        else:
            print(f"Incorreto. A resposta correta era: '{resposta_correta}'")

    # Ao final do laço, mostra a pontuação total
    print("\n------------------------------------")
    print(f"Quiz finalizado! Sua pontuação total foi: {pontuacao}/{len(perguntas)}")
    print("------------------------------------")

# Garante que o jogo só rode quando o script for executado diretamente
if __name__ == "__main__":
    quiz_de_perguntas()