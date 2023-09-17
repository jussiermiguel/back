function soma(num1, num2){
    return num1 + num2;
}

let num1 = 40;
let num2 = 4;

console.log(soma(Number(num1), Number(num2)));


function impar_ou_par() {
    var num = 6
    if (num % 2 === 0) {
        return `${num} é um número par`;
    } else {
        return `${num} é um número ímpar`;
    }
}

var resultado = impar_ou_par();
console.log(resultado)

function status_aluno(nota1, nota2){
    let media = (nota1 + nota2)/2
    let status;

    if (media >= 6){
        status = `Aprovado com média ${media}`;
    }
    else if (media >= 5 && media < 6){
        status = `Recuperação. Média parcial ${media}`;
    }
    else{
        status = `Reprovado com média ${media}`;
    }
    return status;
}
var nota1 = 5;
var nota2 = 7;
var aluno1 = status_aluno(nota1, nota2);

const retorna_media = (nota_1, nota_2) => {

    let media = (nota_1 + nota_2) / 2;
    return media;

}

let media_aluno = retorna_media(9, 8);
console.log("A média do aluno é: " + media_aluno);

const retorna_media2 = (nota_1, nota_2) => (nota_1 + nota_2) / 2;

let media_aluno2 = retorna_media2(5, 7);
console.log("A média do aluno é: " + media_aluno2);


