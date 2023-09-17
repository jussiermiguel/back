programa
{

 funcao inicio()
 {
  //Declaração de variáveis
  cadeia jogo
  cadeia plataforma
  inteiro unidades
  real preco
  logico pre_venda

  //Entrada de dados
  escreva("Sistema de cadastro de jogos da loja\n\n")

  escreva("Digite o nome do jogo: ")
  leia(jogo)

  escreva("Digite a plataforma do jogo: ")
  leia(plataforma)

  escreva("Digite o número de cópias disponíveis: ")
  leia(unidades)

  escreva("Digite o preço do jogo: R$")
  leia(preco)

  escreva("Produto em pré-venda?\nverdadeiro ou falso \n")
  leia(pre_venda)

  //Exibição dos dados cadastrados
  escreva("\n\nResumo do jogo cadastrado\n\n")

  escreva("Jogo: "+jogo+"\n")
  escreva("Plataforma: "+plataforma+"\n")
  escreva("Unidades disponíveis: "+unidades+"\n")
  escreva("Preco: R$ "+preco+"\n")
  escreva("Pré-venda: "+pre_venda+"\n")
 }
}