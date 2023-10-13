let data = new Date();

let hora = data.getHours();
let min = data.getMinutes();

let saudacao;
if (hora <= 11){
    saudacao = `${hora}h${min}min. Bom dia`
}
else if (hora <= 17){
    saudacao = `${hora}h${min}min. Boa tarde`
}
else{
    saudacao = `${hora}h${min}min. Boa noite`
}

console.log(`Olá! ${saudacao}`);
