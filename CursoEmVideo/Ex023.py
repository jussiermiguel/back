#solicita ao usuário a cidade que ele nasceu
cidade = str(input('Digite a cidade que você nasceu: ')).strip() # strip para tirar espaços indesejados que o usuário possa digitar
# verifica se a cidade começa com santo
print(cidade[:5].title() == 'Santo')# [:5] imprime o valor do começo da string / .title() deixa a primeira letra em maiúscula
