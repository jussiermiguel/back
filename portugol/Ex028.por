programa {
  funcao inicio() {
    inteiro num_pessoas
    real peso
    real peso_total = 0

    escreva("Informe quantas pessoas vão entrar no elevador: ")
    leia(num_pessoas)

    para(inteiro i = 1; i <= num_pessoas; i++){
      escreva("Informe o peso da ", i, "ª pessoa: ")
      leia(peso)

      peso_total = peso_total + peso

      se(peso_total > 100){
        escreva("Limite atingido!")
        pare
      }
    }
  }
}
