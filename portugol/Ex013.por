programa {
	funcao inicio() {
	    // vari�veis
	    real num1
	    real num2
	    caracter opcao //escolher a opera��o a se realizar
	    real resultado
	    
		escreva("Mini calculadora +++++++++++++++++++++++++++++++++\n")
		escreva("=> a + b = c <=\n\n")
		
		// entrada dos dados
		escreva("Digite o primeiro n�mero: ")
		leia(num1)
		escreva("Digite o segundo n�mero: ")
		leia(num2)
		
		escreva("\n+ adi��o\n")
		escreva("- subtra��o\n")
		escreva("* multiplica��o\n")
		escreva("/ divis�o\n")
		escreva("Selecione a op��o: ")
		leia(opcao)
		
		
		
		// processamento e retorno dos dados
		
		se(opcao == '+'){
		    escreva("Voc� escolheu a op��o adi��o: \n")
		    resultado = num1 + num2
		    escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		}
		
		senao se(opcao == '-'){
		    escreva("Voc� escolheu a op��o subtra��o: \n")
		    resultado = num1 - num2
		    escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		}
		
		senao se(opcao == '*'){
		    escreva("Voc� escolheu a op��o multiplica��o: \n")
		    resultado = num1 * num2
		    escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		}
		
		senao se(opcao == '/'){
		    se(num2 != 0){
		        escreva("Voc� escolheu a op��o divis�o: \n")
		        resultado = num1 / num2
		        escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		    }
		    senao{
		        escreva("N�o � poss�vel dividir por 0")
		    }
		    
		}
		senao{
		    escreva("Opera��o inv�lida!")
		}
		
		
		
	}
}