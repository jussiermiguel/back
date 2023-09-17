programa {
	funcao inicio() {
	    // declaração de variáveis
		real valor
		real taxa
		real resultado
		inteiro opcao
		
		escreva("Bem vindo a calculadora de Juros e Desconto")
		escreva("===========================================")
        escreva("\n")
        
        // entrada dos dados
        escreva("\nInforme o valor: R$")
        leia(valor)
        
        escreva("\nInforme a taxa %: ")
        leia(taxa)
        
        escreva("\nQual calculo você deseja realizar?")
        escreva("\n1 - Juros \n2 - Desconto \n:")
        leia(opcao)
        
        // processamento
        se (opcao == 1 ou opcao == 2){
            se (opcao == 1){
                resultado = valor + (valor * taxa)/100
                escreva(resultado)
            }
            senao{
                resultado = valor - (valor * taxa)/100
                escreva(resultado)
            }
        }senao{
            escreva("Opção inválida! Tente novamente")
        }
        
        
        

	}
}
