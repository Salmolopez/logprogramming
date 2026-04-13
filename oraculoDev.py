def oraculo_da_sabedoria():
    """
    Um assistente que responde perguntas sobre programação em Python.
    """
    # Pede ao usuário para digitar um assunto e converte para minúsculas e remove espaços extras
    assunto = input("Olá! Sou o Oráculo da Sabedoria Python. Sobre qual assunto você gostaria de aprender hoje? (variáveis, listas, funções, loops): ").lower().strip()

    # Utiliza a estrutura match case para verificar o assunto digitado
    match assunto:
        case "variáveis":
            print("\nEm Python, variáveis são como 'caixas' onde você guarda informações.")
            print("Você não precisa declarar o tipo (int, str, etc.).")
            print("Exemplo: nome = 'Maria' ou idade = 30")
        
        case "listas":
            print("\nListas são coleções ordenadas e mutáveis de itens. Pense nelas como um carrinho de compras.")
            print("Você pode adicionar, remover ou alterar itens.")
            print("Exemplo: minha_lista = ['maçã', 'banana', 'cereja']")

        case "funções":
            print("\nFunções são blocos de código reutilizáveis que realizam uma tarefa específica.")
            print("Elas ajudam a organizar o código e evitam repetição.")
            print("Exemplo: def saudacao(nome): print(f'Olá, {nome}!')")

        case "loops":
            print("\nLoops (ou laços de repetição) são usados para executar um bloco de código várias vezes.")
            print("Os mais comuns são o 'for' (para percorrer uma sequência) e o 'while' (enquanto uma condição for verdadeira).")
            print("Exemplo com for: for item in ['a', 'b', 'c']: print(item)")

        case _:
            # Caso o assunto não corresponda a nenhum dos casos acima
            print("\nHmm, sobre este assunto eu ainda estou aprendendo. Tente outro, como 'variáveis', 'listas', 'funções' ou 'loops'.")

# Bloco que garante que o código só será executado quando o script for o principal
if __name__ == "__main__":
    oraculo_da_sabedoria()