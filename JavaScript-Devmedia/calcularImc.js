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

let peso = 0;
let altura = 1.72;

function validaPeso(peso){
    let pesoValido = false;
    
    if (peso > 0){
        pesoValido = true;
    }

    return pesoValido;
}

function validaAltura(altura){
    let alturaValida = false;

    if (altura > 0){
        alturaValida = true;
    }

    return alturaValida;
}


let verificaPesoValido = validaPeso(peso);
let verificaAlturaValida = validaAltura(altura);

if (verificaPesoValido && verificaAlturaValida){

    
    let resultado = cacularIMC(peso, altura);
    let statusIMC = retornaStatusIMC(resultado);
    
    console.log(`Seu imc é ${resultado} e você está ${statusIMC}`);
}
else{
    console.log(`Peso e altura devem ser maiores que zero`);
}


