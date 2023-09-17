let usuarios = [
    {id: 1, nome: "Jussiêr", idade: 25},
    {id: 2, nome: "Miguel", idade: 15},
    {id: 3, nome: "Oliveira", idade: 10}
];

for (let usuario in usuarios){
    console.log(usuarios[usuario].id);
    console.log(usuarios[usuario].nome);
    console.log(usuarios[usuario].idade);
}