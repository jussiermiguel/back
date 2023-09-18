const frutas = [
    "Manga", "Laranja", "Uva", "Maçã"
]
const num = [
    10, 2, 1, 54, 32, 22, 4, 3, 60
]

console.log("\nArray antes da ordenação:\n");
console.info(frutas);

frutas.sort();

console.log("\nArray depois da ordenação:\n");
console.info(frutas);
console.log("\n");

console.log("\nArray antes da ordenação:\n");
console.info(num);

num.sort();
console.log("\nArray depois da ordenação:\n");
console.info(num);
console.log("\n");

// customizando o sort()

function ordenarNumeros(a, b){
    console.log(`A: ${a}`);
    console.log(`B: ${b}`);
    console.log("");
    return a - b;
}
console.log(`\nParâmetros A e B`)
num.sort(ordenarNumeros);
console.log("\nArray depois da ordenação customizada:\n");
console.info(num);
console.log("\n");

let tabela = [
    {equipe: 'Time Azul', pontos: 25 },
    {equipe: 'Time Verde', pontos: 47 },
    {equipe: 'Time Amarelo', pontos: 39 },
    {equipe: 'Time Vermelho', pontos: 16 },
];

function ordenaMaisPontos(a, b){
    return b.pontos - a.pontos;
}

tabela.sort(ordenaMaisPontos);

for(let i = 0; i < tabela.length; i++)
{
    let posicao = i+1;
    console.log(posicao+" | "+tabela[i].equipe+" - "+tabela[i].pontos+" pts");
}