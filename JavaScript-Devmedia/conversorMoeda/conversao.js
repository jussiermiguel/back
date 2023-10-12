function dolarReal(dolar){
    let real = dolar * 5.05;
    return `${real.toFixed(2)}`;
}
function dolarEuro(dolar){
    let taxa_conversao = 0.83;
    let euro = dolar * taxa_conversao;

    return `${euro.toFixed(2)}`;
}

function dolarDolar(dolar){
    let dolar_valor = dolar;
    return `${dolar_valor.toFixed(2)}`;
}
export {dolarEuro, dolarReal, dolarDolar};