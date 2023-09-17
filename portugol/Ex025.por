programa {
  funcao inicio() {
    inteiro i=1
    inteiro numero
    inteiro resultado = 1

    faca{
      escreva("\ninforme um número: ")
      leia(numero)

      resultado = resultado * numero
      escreva("\nResultado: ",resultado)

      i++

      se(resultado > 30){
        pare
      }
    }enquanto(i <= 5)

    escreva("\nResultado: ",resultado)

  }
}
