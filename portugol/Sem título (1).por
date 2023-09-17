programa

{
  funcao 
inicio
()
  {
    cadeia nome
    cadeia email
    cadeia senha
    
inteiro
 opcao

    
faca

    {
      escreva("Escolha uma alternativa:\n\n")

      escreva("1) Fazer um novo cadastro\n")
      
escreva
("2) Sair do sistema\n\n")
      leia(opcao)

      
escolha
(opcao)
      {
        
caso
 1:
          escreva("\nNovo Cadastro\n")

          escreva("\nNome: ")
          leia(nome)

          escreva("\nEmail: ")
          leia(email)

          escreva("\nSenha: ")
          leia(senha)

          escreva("\nCadastro efetuado com sucesso\n\n")
          pare
        
caso
 2:
          escreva("\nSistema Encerrado\n")
          pare
        
caso contrario
:
          escreva("\nOpção Inválida\n")
          pare
      }
    }
    
enquanto(opcao != 2)

  }
}