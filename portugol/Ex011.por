programa {
	funcao inicio() {
		inteiro x
		
		escreva("Digite um n�mero e descubra se ele � par ou �mpar: ")
		leia(x)
		
		se(x % 2 == 0){
		    escreva(x, " � par")
		}
		
		senao{
		    escreva(x, " � �mpar")
		}
	}
}
