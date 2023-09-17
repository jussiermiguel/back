import { question } from "readline-sync";

function calculadoraDivisao(){
var num1 = question("Digite um número: ");
var num2 = question("Digite outro número: ");
let i = 1
var a = 0
var b = 0

while(i<=2){
    a = question("Digite um num: ")
    i++
}
if(isNaN(a)||isNaN(b)){
    console.log("Valor inválido. Só aceitamos números.");
}
else{
    if(num2 === 0){
        console.log("Não é possível dividir por zero.");
    }
    else{
        var resultado = num1 / num2;
        console.log(resultado)
    }
}
}
calculadoraDivisao();