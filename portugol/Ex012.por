programa {
	funcao inicio() {
		real dividendo
		real divisor
		real resultado
		// exemplo se fizer uma divis�o por
		real x1 = 100
		real x2 = 0
		escreva(x1 / x2) // a mensagem "Infinity" ser� impressa na tela
		
		escreva("\nInforme o dividendo: ")
		leia(dividendo)
		
		escreva("Informe o divisor: ")
		leia(divisor)
		
		se(divisor != 0){
		    resultado = dividendo / divisor
		    escreva(resultado)
		}
		
		senao{
		    escreva("N�o � poss�vel dividir por 0")
		}
	}
}
