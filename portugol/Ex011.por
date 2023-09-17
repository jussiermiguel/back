programa {
	funcao inicio() {
		inteiro x
		
		escreva("Digite um número e descubra se ele é par ou ímpar: ")
		leia(x)
		
		se(x % 2 == 0){
		    escreva(x, " é par")
		}
		
		senao{
		    escreva(x, " é ímpar")
		}
	}
}
