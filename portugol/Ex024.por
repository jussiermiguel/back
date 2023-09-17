programa {
  funcao inicio() {
    inteiro i = 1
    inteiro num
    inteiro soma = 0 

    enquanto(i <= 10){
      escreva("Informe o primeiro número: ")
      leia(num)

      soma = soma + num
      i++

      se(soma > 50){
        pare
      }
    }
    escreva("\nResultado: ", soma)
  }
}
