import {dolarEuro, dolarReal, dolarDolar} from "./conversao.js";

let conversor = "";
let dolar = 1;

if (conversor == "real"){
    let valorReal = dolarReal(dolar);
    console.log(`U$ ${dolar}`);
    console.log(`R$ ${valorReal}`);
} 
else if(conversor == "euro"){
    let valorEuro = dolarEuro(dolar);
    console.log(`E$ ${dolar}`);
    console.log(`R$ ${valorEuro}`);
}
else{
    let valorDolar = dolarDolar(dolar);
    console.log(`U$ ${valorDolar}`);
}