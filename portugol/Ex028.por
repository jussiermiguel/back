programa {
  funcao inicio() {
    inteiro num_pessoas
    real peso
    real peso_total = 0

    escreva("Informe quantas pessoas v�o entrar no elevador: ")
    leia(num_pessoas)

    para(inteiro i = 1; i <= num_pessoas; i++){
      escreva("Informe o peso da ", i, "� pessoa: ")
      leia(peso)

      peso_total = peso_total + peso

      se(peso_total > 100){
        escreva("Limite atingido!")
        pare
      }
    }
  }
}
