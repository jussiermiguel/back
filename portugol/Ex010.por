programa {
	funcao inicio() {
	    // variáveis
	    inteiro num1
	    inteiro num2
	    caracter opcao //escolher a operação a se realizar
	    real resultado
	    
		escreva("Mini calculadora +++++++++++++++++++++++++++++++++\n")
		escreva("=> a + b = c <=\n\n")
		
		// entrada dos dados
		escreva("Digite o primeiro número: ")
		leia(num1)
		escreva("Digite o segundo número: ")
		leia(num2)
		
		escreva("\n+ adição\n")
		escreva("- subtração\n")
		escreva("* multiplicação\n")
		escreva("/ divisão\n")
		escreva("Selecione a opção: ")
		leia(opcao)
		
		
		
		// processamento e retorno dos dados
		
		se(opcao == '+'){
		    escreva("Você escolheu a opção adição: \n")
		    resultado = num1 + num2
		    escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		}
		
		se(opcao == '-'){
		    escreva("Você escolheu a opção subtração: \n")
		    resultado = num1 - num2
		    escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		}
		
		se(opcao == '*'){
		    escreva("Você escolheu a opção multiplicação: \n")
		    resultado = num1 * num2
		    escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		}
		
		se(opcao == '/'){
		    escreva("Você escolheu a opção divisão: \n")
		    resultado = num1 / num2
		    escreva(num1 , " ", opcao ," ", num2, " = " , resultado)
		}
		senao{
		    escreva("Operação inválida!")
		}
		
		
		
	}
}
