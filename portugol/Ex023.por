programa {
  funcao inicio() {
    // estrutura de repeti��o
    inteiro num
    inteiro i = 0
    inteiro resultado
    escreva("Sistema de tabuada \n\n")

    escreva("Informe um n�mero entre 1 e 10 para ver a tabuada de multiplica��o: ")
    leia(num)

    enquanto(i <= 10){
      resultado = num * i
      escreva("\n", num , " x ", i , " = ", resultado)
      i++ // i = i + 1
    }
    
  }
}
