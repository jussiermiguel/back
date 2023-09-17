import entradaDados from 'readline-sync';

console.log("Conversor de Milhas para Quilômetros: \n");

let mi = entradaDados.question("Informe o valor em Milhas: ");

let km = Number(mi) / 0.62137;

console.log(mi+"mi equivale a "+km+"km");