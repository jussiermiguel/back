programa {
  funcao inicio() {
    inteiro cadeiras = 20
    inteiro ingressos = 0

    escreva("Ingressos de cinema\n")
    escreva("Cadeiras dispon�veis: ", cadeiras, "\n\n")

    enquanto(cadeiras > 0){
      escreva("Quantos ingressos voc� deseja comprar? ")
      leia(ingressos)

      se(ingressos > cadeiras){
        escreva("Voc� tentou comprar ", ingressos, " ingressos\n")
        escreva("Cadeiras dispon�veis: ", cadeiras, "\n\n")
      }
      senao{
        cadeiras = cadeiras - ingressos
        escreva("\nVoc� tentou comprar ", ingressos, " ingressos\n")

        se(cadeiras == 0){
          escreva("N�o h� mais cadeiras dispon�veis.\n\n")
          pare
        }
        senao{
          escreva("Cadeiras dispon�veis: ", cadeiras, "\n\n")
        }

      }
    }
  }
}
