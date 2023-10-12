import { serie } from "./series.js";
function retornaSerie(i){
    if (i >= 0 && i < serie.length) {
        return serie[i];
    } else {
        return "Índice fora do alcance da série";
    }
}

export {retornaSerie};