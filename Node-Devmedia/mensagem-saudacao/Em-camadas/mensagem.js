import { horaDataPC } from "./hora.js";
import { minDataPC } from "./min.js";

let hora = horaDataPC();
let min = minDataPC();

function mensagemHora(){
        
    if (hora <= 12){
            if (hora != 12){
                return `Bom dia. ${hora} e ${min} minutos`;
            }
            else{
        }
    }
    else if (hora <= 18){
        if (hora != 18){
            return `Boa tarde. ${hora} e ${min} minutos`;
        }
        else{
        }
    }
    else{
        return `Boa noite. ${hora} e ${min} minutos`;
    }
}

export {mensagemHora};