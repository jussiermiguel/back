
import { retornaSerie } from "./funcao.js";
import { dataDeHoje } from "./diadasemana.js";

let dia_semana = dataDeHoje();
let serie_do_dia = retornaSerie(dia_semana)

console.log(`Série do dia: ${serie_do_dia}`);