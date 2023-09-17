programa
{
 
funcao
 inicio()
 {
  inteiro numero
  
inteiro
 resultado = 0

  
escreva
("Digite um número: ")
  
leia(numero)


  
para
(inteiro 
contador
 = 0; contador <= 
numero
; 
contador
++)
  {
   
se
(
contador
 % 2 == 0)
   {
    resultado = 
resultado
 - contador
   }
   
senao

   {
    resultado = resultado + 
contador

   }
  }

  
escreva
("\nResultado: "+resultado)
 }
}