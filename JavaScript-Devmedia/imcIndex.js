import { cacularIMC, retornaStatusIMC, formatarIMC} from "./imcCalc.js";
import { validaAltura, validaPeso } from "./imcValidacao.js";

let peso = 90;
let altura = 1.72;
let verificaPesoValido = validaPeso(peso);
let verificaAlturaValida = validaAltura(altura);

if (verificaPesoValido && verificaAlturaValida){

    
    let resultado = cacularIMC(peso, altura);
    let imc = formatarIMC(resultado);
    let statusIMC = retornaStatusIMC(resultado);
    
    console.log(`Seu imc é ${imc} e você está ${statusIMC}`);
}
else{
    console.log(`Peso e altura devem ser maiores que zero`);
}
