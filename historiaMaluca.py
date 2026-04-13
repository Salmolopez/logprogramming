# --- Gerador de Histórias Malucas ---

# 1. Boas-vindas e explicação
print("🤪 Vamos criar uma história maluca juntos! 🤪")
print("Eu preciso que você me dê 6 palavras.")

# 2. Coletando as palavras do usuário
# A função input() mostra a mensagem e guarda o que o usuário digitar na variável.
lugar = input("1. Diga o nome de um lugar: ")
pessoa_famosa = input("2. Diga o nome de uma pessoa famosa: ")
objeto = input("3. Diga o nome de um objeto: ")
cor = input("4. Diga uma cor: ")
verbo = input("5. Diga um verbo (ex: dançar, correr, pular): ")
numero = input("6. Diga um número: ")

# 3. Montando e exibindo a história final
print("\n----------------------------------------")
print("📖 Sua história maluca está pronta! 📖")
print("----------------------------------------\n")

# Usando uma f-string (format string) para montar a história com as variáveis.
historia = f"Certo dia, no(a) {lugar}, eu vi ninguém menos que {pessoa_famosa} " \
           f"segurando um(a) {objeto} da cor {cor}. De repente, {pessoa_famosa} " \
           f"começou a {verbo} loucamente por toda parte. Isso durou por exatas {numero} horas! Foi incrível! 🤣"

print(historia)