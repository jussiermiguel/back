programa {
	funcao inicio() {
	    // declarando vari�veis
	    inteiro opcao
	    real temperatura


        // entrada dos dados e escolha da convers�o a ser feita
	  	escreva("Conversor de Temperatura \n\n")
	  	
	  	escreva("Escolha uma das op��es abaixo:\n")
	  	escreva("1 - Celsius para Fahrenheit\n")
	  	escreva("2 - Fahrenheit para Celsius\n>")
	  	
	  	leia(opcao)
	  	// escolha, processamento e sa�da
	  	escolha(opcao){
	  	    caso 1:
	  	        escreva("Digite a temperatura em Celsius (�C): ")
	  	        leia(temperatura)
	  	        
	  	        escreva((temperatura * 1.8) + 32, " �F")
	  	        pare
	  	    
	  	    caso 2:
	  	        escreva("Digite a temperatura em Fahrenheit (�F): ")
	  	        leia(temperatura)
	  	        
	  	        escreva((temperatura - 32) / 1.8, " �C")
	  	        pare
	  	    
	  	    caso contrario:
	  	        escreva("Op��o inv�lida!")
	  	        pare
	  	        
	  	}

 
	}
}