programa
{
 funcao inicio()
 {
  inteiro marca
  inteiro modelo

  escreva("Escolha seu smartphone\n\n")

  escreva("Selecione a marca:\n\n")
  escreva("1) Samsung\n")
  escreva("2) Apple\n\n")

  leia(marca)

  
escolha(marca)

  {
   
caso 1
:
    escreva("\nSelecione o modelo:\n\n")
    escreva("1) Galaxy S21\n")
    escreva("2) Galaxy Note 20\n\n")
    leia(modelo)

    
escolha(modelo)

    {
     caso 1:
      escreva("\nVocê comprou um Galaxy S21 da Samsung")
      pare
     
caso 2
:
      escreva("\nVocê comprou um Galaxy Note 20 da Samsung")
      pare
     
caso contrario
:
      escreva("\nModelo inválido")
      pare
    }
    pare
   
caso 2
:
    escreva("\nSelecione o modelo:\n\n")
    escreva("1) iPhone 12\n")
    escreva("2) iPhone 12 Pro\n\n")
    leia(modelo)

    
escolha(modelo)

    {
     caso 1:
      escreva("\nVocê comprou um iPhone 12 da Apple")
      pare
     
caso 2
:
      escreva("\nVocê comprou um iPhone 12 Pro da Apple")
      pare
     
caso contrario
:
      escreva("\nModelo inválido")
      pare
    }
    pare
   
caso contrario
:
    escreva("\nMarca inválida")
    pare
  }
 }
}