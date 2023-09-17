programa {
  funcao inicio() {
    // estrutura de repetição
    inteiro num
    inteiro i = 0
    inteiro resultado
    escreva("Sistema de tabuada \n\n")

    escreva("Informe um número entre 1 e 10 para ver a tabuada de multiplicação: ")
    leia(num)

    enquanto(i <= 10){
      resultado = num * i
      escreva("\n", num , " x ", i , " = ", resultado)
      i++ // i = i + 1
    }
    
  }
}
