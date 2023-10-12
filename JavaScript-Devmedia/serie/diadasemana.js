function dataDeHoje(){
    
    let data = new Date();
    let dia = data.getDay();

    return dia;
}

export {dataDeHoje};