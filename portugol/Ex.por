programa {
	funcao inicio() {
	    inteiro divisor = 2
	    inteiro numero
	    inteiro contador = 0
	    
	    escreva("\nChecagem de n�meros primos \n")
        escreva("\nInforme um n�mero: ")
        leia(numero)
        
        enquanto(divisor<=numero/2){
            se(numero % divisor == 0){
            contador++
            pare
            }
        divisor = divisor + 1
        }
        se(contador == 0 e numero != 1){
            escreva("\n"+numero+" � um n�mero primo\n")
        }
        senao{
            escreva("\n"+numero+" n�o � um n�mero primo\n")        
        }
	}
}
