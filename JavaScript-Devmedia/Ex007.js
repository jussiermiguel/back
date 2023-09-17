// tratando dados
import entradaDados from 'readline-sync';

console.log("Calculadora (errada) de soma entre x e y: \n")

let x = entradaDados.question("Informe o valor de x: ")
let y = entradaDados.question("Informe o valor de y: ")

// aqui tem um problema, pois o input recebe os dados na forma de strings
let soma_errada = x + y;

console.log(x+" + "+y+" = "+soma_errada);

console.log("Calculadora (certa) entre a e b: ")

let a = entradaDados.question("Informe o valor de a: ")
let b = entradaDados.question("Informe o valor de b: ")

// agora vamos resolver. Basta colocar "Number" antes do nome de cada variável entre parenteses
// Number(a)+Number(b)

let soma = Number(a)+ Number(b);
console.log(a+" + "+b+" = "+soma);