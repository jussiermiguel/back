programa {
  funcao inicio() {
    inteiro num
    inteiro resultado
    inteiro i
    escreva("Informe um número para ver a sua tabuada: ")
    leia(num)

    para(i = 0; i <= 10; i++){
      resultado = num * i
      escreva("\n", num, " x ", i, " = ", resultado)
    }
  }
}
