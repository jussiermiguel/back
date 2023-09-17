# solicitando o nome completo do usuário
nome = str(input('Digite o seu nome completo: ')).title().strip().split()# tirando os espaços indesejados e dividindo a string em partes, cada nome vira uma string
print("Seja bem-vindo, {}".format(nome))#imprimindo o nome completo
print("Seu primeiro nome é {}".format(nome[0]))#imprimindo o primeiro nome
print("Seu ultimo nome é {}".format(nome[-1]))#imprimindo o ultimo nome
