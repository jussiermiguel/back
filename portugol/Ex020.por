programa {
	funcao inicio() {
		inteiro mes
		
		escreva("1 - Janeiro\n")
		escreva("2 - Fevereiro\n")
		escreva("3 - Março\n")
		escreva("4 - Abril\n")
		escreva("5 - Maio\n")
		escreva("6 - Junho\n")
		escreva("7 - Julho\n")
		escreva("8 - Agosto\n")
		escreva("9 - Setembro\n")
		escreva("10 - Outubro\n")
		escreva("11 - Novembro\n")
		escreva("12 - Dezembro\n")

		escreva("Digite o mês que para saber a quantidade de dias que ele tem: ")
		leia(mes)
		
        escolha(mes){
            caso 1:
                escreva("Janeiro\n")
    	        escreva("Tem 31 dias\n")
                pare	            
            caso 2:
                escreva("Fevereiro\n")
                escreva("Tem 28 ou 29 dias")
                pare
            caso 3:
                escreva("Março\n")
                escreva("Tem 31 dias\n")
                pare	                
            caso 4:
                escreva("Abril\n")
                escreva("Tem 30 dias")
                pare
            caso 5:
                escreva("Maio\n")
                escreva("Tem 31 dias\n")
                pare
            caso 6:
                escreva("Junho\n")
                escreva("Tem 30 dias")
                pare
            caso 7:
                escreva("Julho\n")
                escreva("Tem 31 dias\n")
                pare        
            caso 8:
                escreva("Agosto\n")
                escreva("Tem 31 dias\n")
                pare
            caso 9:
                escreva("Setembro\n")
                escreva("Tem 30 dias")
                pare
            caso 10:
                escreva("Outubro\n")
                escreva("Tem 31 dias\n")
                pare
            caso 11:
                escreva("Novembro\n")
                escreva("Tem 30 dias")
                pare
            caso 12:
                escreva("Dezembro\n")
                escreva("Tem 31 dias\n")
                pare
            caso contrario:{
                escreva("Mês inexistente.")
                pare
            }
        }
	}
}
