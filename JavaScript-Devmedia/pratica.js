const times = [
    {nome: 'Vasco', estado: 'RJ'},
    {nome: 'Flamengo', estado: 'RJ'},
    {nome: 'Fluminense', estado: 'RJ'},
    {nome: 'Botafogo', estado: 'RJ'},
    {nome: 'Cruzeiro', estado: 'MG'},
    {nome: 'Atlético MG', estado: 'MG'},
    {nome: 'Inter', estado: 'RS'},
    {nome: 'Grêmio', estado: 'RS'},
    {nome: 'Athletico PR', estado: 'PR'},
    {nome: 'Coritiba', estado: 'PR'},
    {nome: 'São Paulo', estado: 'SP'},
    {nome: 'Palmeiras', estado: 'SP'},
    {nome: 'Santos', estado: 'SP'},
    {nome: 'Corinthians', estado: 'SP'},
    {nome: 'RB Bragantino', estado: 'SP'},
    {nome: 'Bahia', estado: 'BA'},
    {nome: 'Vitoria', estado: 'BA'},
    {nome: 'Fortaleza', estado: 'CE'},
    {nome: 'Ceara', estado: 'CE'},
    {nome: 'Cuiaba', estado: 'MS'},
];

console.log("Todos os times:");
times.forEach(time => {
    console.log(`${time.nome}`);
})

const timesRJ = times.filter(time => time.estado === 'RJ');
console.log("\nTimes do RJ:");
timesRJ.forEach(time => {
    console.log(`${time.nome}`);
})

const timesNE = times.filter(time => time.estado === 'CE' || time.estado === 'BA');
console.log("\nTimes do Nordeste:");
timesNE.forEach(time => {
    console.log(`${time.nome}`);
})

const timesSP = times.filter(time => time.estado === 'SP');
console.log("\nTimes de São Paulo:");
timesSP.forEach(time => {
    console.log(`${time.nome}`);
})

const timesSUL = times.filter(time => time.estado === 'PR' || time.estado === 'RS');
console.log("\nTimes do Sul:");
timesSUL.forEach(time => {
    console.log(`${time.nome}`);
})


const timesMGMS = times.filter(time => time.estado === 'MG' || time.estado === 'MS');
console.log("\nTimes de MG e Centro-Oeste:");
timesMGMS.forEach(time => {
    console.log(`${time.nome}`);

})
