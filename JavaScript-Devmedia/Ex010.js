import entradaDados from 'readline-sync';

console.log("Área do triângulo: \n");

let base = entradaDados.question("Informe a base: ");
let altura = entradaDados.question("Informe a altura: ");

let area = (Number(base) * Number(altura)) / 2;

console.log("A área do triângulo é: "+area);