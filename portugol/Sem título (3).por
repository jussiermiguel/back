programa
{
 funcao inicio()
 {
  inteiro tentativas = 3
  inteiro resposta

  enquanto(tentativas > 0)
  {
   escreva("Responda à pergunta corretamente. Você tem "+tentativas+" tentativas\n\n")

   escreva("2 + 2 é igual a...?\n\n")
   escreva("1) 6\n")
   escreva("2) 4\n")
   escreva("3) 8\n")
   escreva("4) 9\n")
   leia(resposta)

   escolha(resposta)
   {
    caso 1:
     tentativas = tentativas - 1
     se(tentativas == 0)
     {
      escreva("\nVocê errou a questão e ficou sem tentativas")
     }
     pare
    caso 2:
     escreva("\nVocê acertou a questão")
     tentativas = 0
     pare
    caso 3:
     tentativas = tentativas - 1
     se(tentativas == 0)
     {
      escreva("\nVocê errou a questão e ficou sem tentativas")
     }
     pare
    caso 4:
     tentativas = tentativas - 1
     se(tentativas == 0)
     {
      escreva("\nVocê errou a questão e ficou sem tentativas")
     }
     pare
   }
  }
 }
}