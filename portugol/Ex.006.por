programa {
	funcao inicio() {
		// alguns erros que podem ocorrer ao usar operador aritm�tico e o tipo de dado inadequado
		
		inteiro soma
		real divisao
		
		// nesse caso como a vari�vel � inteira, ele vai ignorar a parte fracionada do n�mero
		soma = 2 + 1.5
		escreva(soma + "\n")
		
		
		// aqui a vari�vel era pra ser do tipo real, mas s� recebeu do tipo inteiro
		divisao = 10 / 3
		escreva(divisao + "\n")
		// para resolver basta atribuir um valor do tipo real em um dos dois n�meros
		divisao = 10.0 / 3
		escreva(divisao + "\n")
	}
}
