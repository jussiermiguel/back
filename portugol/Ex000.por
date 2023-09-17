programa {
  funcao inicio() {
    inteiro cadeiras = 20
    inteiro ingressos = 0

    escreva("Ingressos de cinema\n")
    escreva("Cadeiras disponíveis: ", cadeiras, "\n\n")

    enquanto(cadeiras > 0){
      escreva("Quantos ingressos você deseja comprar? ")
      leia(ingressos)

      se(ingressos > cadeiras){
        escreva("Você tentou comprar ", ingressos, " ingressos\n")
        escreva("Cadeiras disponíveis: ", cadeiras, "\n\n")
      }
      senao{
        cadeiras = cadeiras - ingressos
        escreva("\nVocê tentou comprar ", ingressos, " ingressos\n")

        se(cadeiras == 0){
          escreva("Não há mais cadeiras disponíveis.\n\n")
          pare
        }
        senao{
          escreva("Cadeiras disponíveis: ", cadeiras, "\n\n")
        }

      }
    }
  }
}
