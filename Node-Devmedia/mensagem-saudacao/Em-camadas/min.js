import { dataPC } from "./dadosPC.js";
// import { horaDataPC } from "./hora.js";

function minDataPC(){
    let hora = dataPC();
    let min = hora.getMinutes();

    return min;
}

export {minDataPC};