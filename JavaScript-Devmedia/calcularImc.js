function cacularIMC(peso, altura){
    let imc = peso / (altura * altura);
    return imc;
}

function retornaStatusIMC(imc){
    let status;

    if (imc < 18.5){
        status = 'abaixo do peso';
    }

    else if (imc < 24.9){
        status = 'peso normal';
    }

    else if (imc < 30){
        status = 'acima do peso';
    }

    else{
        status = 'obeso';
    }

    return status;
}

let peso = 90;
let altura = 1.72;

let resultado = cacularIMC(peso, altura);
let statusIMC = retornaStatusIMC(resultado);

console.log(`Seu imc é ${resultado} e você está ${statusIMC}`);


