programa {
  funcao inicio() {
    inteiro i = 1
    real nota
    real soma = 0
    real media

    faca{
      escreva("Informe a ", i, "� nota: ")
      leia(nota)

      soma = soma + nota
      i = i + 1
    }enquanto(i <= 4)

    media = soma / 4
    escreva("Sua m�dia �: ", media)
    
    se(media >= 6){
      escreva("\nVoc� foi aprovado!")
    }
    senao se(media > 0){
      escreva("\nVoc� foi reprovado!")
    }
    senao{
      escreva("Sem nota/m�dia!")
    }
  }
}
