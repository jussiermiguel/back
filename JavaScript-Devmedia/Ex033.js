const dias_semana = [
    "Domingo",
    "Segunda",
    "Terça",
    "Esse não é um dia",
    "Quarta",
    "Quinta",
    "Sexta",
];
const num_dia = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
]
let numeros = [
    255,
    123,
    5321,
    235,
    8654,
    68,
]

// adicionou o Sábado ao array dias_semana
dias_semana.push("Sábado");
console.log(dias_semana);

for (let i = 0; i < num_dia.length; i++){
    let numero = num_dia[i];
    console.log(numero);

}
// substituindo o for
dias_semana.map((dia) => console.log(dia));

// excluindo um item
dias_semana.splice(3,1); // remove a partir da posição 3 e apenas 1 valor será removido
console.log(dias_semana);

dias_semana.unshift("Primeiro")// adiciona um valor na primeira posição do array
dias_semana.push("ultimo")
console.log(dias_semana);
dias_semana.pop();// remove o ultimo
console.log(dias_semana);
dias_semana.shift();// remove o primeiro
console.log(dias_semana);

const produto = {
    nome: 'New Super Mario Bros.', qnt: 1, valor: 250
};

const carrinho = [
    {  nome: 'The Legend of Zelda', qnt: 1, valor: 250 },
    {  nome: 'Super Mario Kart 8', qnt: 1, valor: 300 },
];

// Insere o produto no carrinho
carrinho.push(produto);

// Remove o item "Super Mario Kart 8"
carrinho.splice(1,1);

// Remove todos os elementos do carrinho
const totalElementos = carrinho.length;
carrinho.splice(0,totalElementos);
console.log(carrinho);

const produtos = [
    { id: 1, nome: 'Açucar', estoque: 100, valor: 2.00 },
    { id: 2, nome: 'Álcool 70', estoque: 50, valor: 9.95 },
    { id: 3, nome: 'Luvas descartáveis', estoque: 1000, valor: 2.50 },
  ];
  
  function imprimirProduto (produto, index) {
    console.log(`Cod ${index} - Produto ${produto.nome}`);
    console.log(`Quantidade - ${produto.estoque}`);
    console.log(`Valor - R$${produto.valor.toFixed(2)}`);
}
  
  produtos.forEach(imprimirProduto)