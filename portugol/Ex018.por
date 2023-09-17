programa {
	funcao inicio() {
	    // declarando variáveis
	    inteiro opcao
	    real temperatura


        // entrada dos dados e escolha da conversão a ser feita
	  	escreva("Conversor de Temperatura \n\n")
	  	
	  	escreva("Escolha uma das opções abaixo:\n")
	  	escreva("1 - Celsius para Fahrenheit\n")
	  	escreva("2 - Fahrenheit para Celsius\n>")
	  	
	  	leia(opcao)
	  	// escolha, processamento e saída
	  	escolha(opcao){
	  	    caso 1:
	  	        escreva("Digite a temperatura em Celsius (°C): ")
	  	        leia(temperatura)
	  	        
	  	        escreva((temperatura * 1.8) + 32, " °F")
	  	        pare
	  	    
	  	    caso 2:
	  	        escreva("Digite a temperatura em Fahrenheit (°F): ")
	  	        leia(temperatura)
	  	        
	  	        escreva((temperatura - 32) / 1.8, " °C")
	  	        pare
	  	    
	  	    caso contrario:
	  	        escreva("Opção inválida!")
	  	        pare
	  	        
	  	}

 
	}
}