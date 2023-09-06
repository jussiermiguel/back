# solicitando o nome completo do usuario
nome = str(input('Digite o seu nome completo: ')).strip().title() # tirando espaços indesejados e deixando primeiras letras das palavras em Caixa alta

print('Seu nome tem Oliveira?', 'Oliveira' in nome)# procurando a palavra oliveira dentro da string
print(nome)