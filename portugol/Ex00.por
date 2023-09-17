programa {
  funcao inicio() {
    inteiro senha
    cadeia login

    para(inteiro i = 0; i < 3; i++){
      escreva("Digite o login: ")
      leia(login)
      escreva("Digite a senha: ")
      leia(senha)
      se(senha == 10 e login == "Admin"){
        escreva("Seja bem-vindo!")
        pare
      }
      senao{
        escreva("Tente de novo: \n")
        
      }
      escreva("Login bloqueado!")
    }
    
  }
}
