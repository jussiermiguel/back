programa {
	funcao inicio() {
		real dividendo
		real divisor
		real resultado
		// exemplo se fizer uma divisão por
		real x1 = 100
		real x2 = 0
		escreva(x1 / x2) // a mensagem "Infinity" será impressa na tela
		
		escreva("\nInforme o dividendo: ")
		leia(dividendo)
		
		escreva("Informe o divisor: ")
		leia(divisor)
		
		se(divisor != 0){
		    resultado = dividendo / divisor
		    escreva(resultado)
		}
		
		senao{
		    escreva("Não é possível dividir por 0")
		}
	}
}
