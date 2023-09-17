let aM = " dsfd  Ju asdas";
let am = " assdas ju  dassd  ";
let name = "JUSSIER miguel";
if(am.toUpperCase() == aM.toUpperCase()){
    console.log("Iguais");
}
else{
    console.log("Diferentes");
}

console.log(name.split(" "));
console.log(am.indexOf("oi"));
console.log(aM.substring(3,4));
console.log(am.substring(0,1));
console.log(am.replace("j","Jussiêr").trim());
console.log(aM.replace("J","Miguel").trim());

console.log(am.padStart(20, '><'))
console.log(aM.padEnd(20,"><"))

var nome = "Jussiêr";

var tamanho_nome = nome.length;

let frase = nome + " é um estudante de programação.";

let resultado = frase.split("-");

console.log(nome);
console.log(resultado);
console.log(tamanho_nome);
console.log(frase);

let posicao_inicio = 0
let posicao_fim = 7
let palavra = ""

for(let i = 0; i<=frase.length; i++){
    if( i >= posicao_inicio && i <= posicao_fim){
        palavra = palavra + frase.charAt(i);
    }
}
console.log(palavra);

let word = frase.substring(posicao_inicio, posicao_fim);

console.log(word);
console.log(word[0]);

let tecnologia = `JavaScript`;
console.log(tecnologia);

var texto1 = "Para quebrar linhas"
texto1+= " temos que fazer assim"
texto1+= " \nTanto em aspas duplas ou simples"

var texto2 = `Já com o acento grave(também é uma string).
 Assim teremos uma template string.
 Basta digitar o texto como quiser e imprimir no console.log.
`
console.log(texto1);
console.log(texto2);

let a = "Olá"
let b = "Mundo"
let c = ` ${a} ${b}`
console.log(c)