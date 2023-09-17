programa
{
 funcao inicio()
 {
  inteiro contador = 1
  inteiro soma = 0

  enquanto(contador <= 100)
  {
    escreva(contador+"\n")
   soma = soma + contador

   se(contador % 2 == 0)
   {
    contador = contador + 1
   }
   senao
   {
    contador = contador + 2
   }
  }

  escreva("Soma: "+soma)
 }
}