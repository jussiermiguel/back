programa
{
 funcao inicio()
 {
  inteiro opcao = 0
  inteiro ano_nascimento
  inteiro idade

  enquanto(opcao != 2)
  {
   escreva("Escolha uma op��o:\n\n")

   escreva("1) Verificar alistamento na marinha\n")
   escreva("2) Sair do sistema\n\n")

   leia(opcao)

   se(opcao == 1)
   {
    escreva("\nInforme o ano do seu nascimento: ")
    leia(ano_nascimento)

    idade = 2023 - ano_nascimento

    se(idade == 18)
    {
     escreva("\nVoc� deve se alistar este ano!\n\n")
    }
    senao
    {
     escreva("\nVoc� n�o precisa se alistar.\n\n")
    }
   }
   senao se(opcao == 2)
   {
    escreva("\nSistema encerrado\n")
   }
  }
 }
}