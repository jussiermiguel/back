programa {
	funcao inicio() {
	    // declarando vari�veis
	    real tc
	    real tf
	  	escreva("Conversor de temperatura \n\n")
		
		// converter celcius para fahrenheit
		escreva("Digite uma temperatura em �C: ")
		leia(tc)
		
		escreva("A temperatura convertida para Fahrenheit �: "+tc * 1.8 + 32+" �F\n\n")
		
		//Convertendo de Fahrenheit para Celsius
        escreva("Digite uma temperatura em �F: ")
        leia(tf)

        escreva("A temperatura convertida para Celsius �: "+(tf - 32) / 1.8+" �C\n\n")
 
	}
}
