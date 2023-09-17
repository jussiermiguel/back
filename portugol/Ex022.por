programa {
	funcao inicio() {
		inteiro opcao
		
		escreva("Sistema de ajuda escolar\n\n")
		escreva("O que você deseja calcular?\n\n")
		escreva("1 - Calcular a área do triângulo\n")
		escreva("2 - Calcular delta usando a fórmula de bhaskara\n >")
		leia(opcao)
		
		escolha(opcao){
		    caso 1:
		        real base
		        real altura
		        
    	        escreva("\nInforme a base do triângulo (cm): ")
		        leia(base)
		        escreva("Informe a altura do triângulo (cm): ")
		        leia(altura)
		        
		        se(base <= 0 ou altura <= 0){
		            escreva("A base e altura devem ser maiores que 0")
		        }
		        senao{
        	        escreva("A = (b * h) / 2\n")
        	        escreva("A = ", base , "*", altura , "/ 2\n")
        	        escreva("Área = ", base * altura / 2)
		        }
		    caso 2:
		        real a
		        real b
		        real c

		        escreva("\nInforme o valor de a: ")
		        leia(a)
		        escreva("Informe o valor de b: ")
		        leia(b)
		        escreva("Informe o valor de c: ")
		        leia(c)
		        
		        escreva("delta = (b * b) - (4*a*c)\n")
		        escreva("delta = (",b,"*", b ,") - (4*" , a, "*", c, ")\n")		        
		        escreva("delta = ", (b * b) - (4*a*c))

		}
	}
}
