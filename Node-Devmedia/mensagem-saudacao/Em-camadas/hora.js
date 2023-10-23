import { dataPC } from "./dadosPC.js"

function horaDataPC(){
    let data = dataPC();
    let hora = data.getHours();
    return hora;
}

export {horaDataPC}