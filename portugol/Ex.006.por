programa {
	funcao inicio() {
		// alguns erros que podem ocorrer ao usar operador aritmético e o tipo de dado inadequado
		
		inteiro soma
		real divisao
		
		// nesse caso como a variável é inteira, ele vai ignorar a parte fracionada do número
		soma = 2 + 1.5
		escreva(soma + "\n")
		
		
		// aqui a variável era pra ser do tipo real, mas só recebeu do tipo inteiro
		divisao = 10 / 3
		escreva(divisao + "\n")
		// para resolver basta atribuir um valor do tipo real em um dos dois números
		divisao = 10.0 / 3
		escreva(divisao + "\n")
	}
}
