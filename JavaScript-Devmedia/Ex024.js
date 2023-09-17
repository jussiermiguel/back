let usuarios = [
    {id: 1, nome: "Jussiêr", idade: 25},
    {id: 2, nome: "Miguel", idade: 15},
    {id: 3, nome: "Oliveira", idade: 10}
];

for(let usuario of usuarios){
    let id = usuario.id;
    let nome = usuario.nome;
    let idade = usuario.idade;
    console.log(id);
    console.log(nome);
    console.log(idade);
}