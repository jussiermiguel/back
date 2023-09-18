const carrinho = [
  {  nome: 'The Legend of Zelda', qnt: 1, valor: 250 },
  {  nome: 'Super Mario Kart 8', qnt: 1, valor: 300 },
  {  nome: 'New Super Mario Bros.', qnt: 1, valor: 250 }
];

function imprimirItem( produto, index ) {
  let texto = index + ' - ';
  texto += produto.qnt + ' UN - ';
  texto += produto.nome + ' - ';
  texto += 'R$ ' + produto.valor + ' - ';
  texto += 'R$ ' + produto.qnt * produto.valor;

  console.log( texto );
}

carrinho.forEach(imprimirItem);

function retornarProduto(produto){
  const produtoExibicao = {
    nome: produto.nome,
    valor: produto.valor
  }
  return produtoExibicao
}

const produtosExibicao = carrinho.map(retornarProduto);
console.log(produtosExibicao)