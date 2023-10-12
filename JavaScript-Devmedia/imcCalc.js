function cacularIMC(peso, altura){
    let imc = peso / (altura * altura);
    return imc;
}

function formatarIMC(imc){
    return imc.toFixed(2);
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

export {cacularIMC, retornaStatusIMC, formatarIMC}