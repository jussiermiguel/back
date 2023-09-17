programa {
  funcao inicio() {
    inteiro i = 1
    real nota
    real soma = 0
    real media

    faca{
      escreva("Informe a ", i, "ª nota: ")
      leia(nota)

      soma = soma + nota
      i = i + 1
    }enquanto(i <= 4)

    media = soma / 4
    escreva("Sua média é: ", media)
    
    se(media >= 6){
      escreva("\nVocê foi aprovado!")
    }
    senao se(media > 0){
      escreva("\nVocê foi reprovado!")
    }
    senao{
      escreva("Sem nota/média!")
    }
  }
}
