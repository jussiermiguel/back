var mes = 12
var nota = 10

var s = nota > 7 ? "Aprovado" : "Reprovado";
var mensagem = (mes == 11 || mes == 12) ? "Promoção" : "Preço normal";
console.log(s)
console.log(mensagem)

//
var aprovado = true;

if (aprovado) {
    console.log("Parabéns");
}
var aprovado = true;

aprovado && console.log("Parabéns");

//
//Declaração da constante nome
const nome = '';

//Aqui é verificado se o nome possui ao menos um caractere
//Retorna true se possuir e false caso contrário
const nomeValido = nome.length > 0;

//Imprime o nome no console se for diferente de vazio
nomeValido && console.log(nome);

//
console.log("**");
var produto = "Smartphone";

switch(produto){
    case "Smartphone":
    case "Celular":
    case "Telefone":
        console.log("Produto: Smartphone");
        break;
    case "TV":
        console.log("Produto: TV");
        break;
    default:
        console.log("Produto inválido");
        break;
}

//
console.log("*")
var mes = "ff"

switch(mes){
    case "Janeiro":
    case "Fevereiro":
    case "Março":
        console.log("Verão");
        break;
    
    case "Abril":
    case "Maio":
    case "Junho":
        console.log("Outono");
        break;
    case "Julho":
    case "Agosto":
    case "Setembro":
        console.log("Inverno");
        break;
    case "Outubro":
    case "Novembro":
    case "Dezembro":
        console.log("Primavera");
        break;
    default:
        console.log("Mês inválido");
        break;
}