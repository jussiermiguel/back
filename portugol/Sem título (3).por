programa
{
 funcao inicio()
 {
  inteiro tentativas = 3
  inteiro resposta

  enquanto(tentativas > 0)
  {
   escreva("Responda � pergunta corretamente. Voc� tem "+tentativas+" tentativas\n\n")

   escreva("2 + 2 � igual a...?\n\n")
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
      escreva("\nVoc� errou a quest�o e ficou sem tentativas")
     }
     pare
    caso 2:
     escreva("\nVoc� acertou a quest�o")
     tentativas = 0
     pare
    caso 3:
     tentativas = tentativas - 1
     se(tentativas == 0)
     {
      escreva("\nVoc� errou a quest�o e ficou sem tentativas")
     }
     pare
    caso 4:
     tentativas = tentativas - 1
     se(tentativas == 0)
     {
      escreva("\nVoc� errou a quest�o e ficou sem tentativas")
     }
     pare
   }
  }
 }
}