// import { prompt } from "readline-sync";
import { celsiusParaFahrenheit, fahrenheitParaCelsius } from "./conversor.js";
let opcao = 6;
let temperatura = 100;
switch (opcao){
    
    case 1:
        // fah => cel
        let fah_cel = fahrenheitParaCelsius(temperatura);

        console.log(`${temperatura}°F equivalem a ${fah_cel}°C`)
        break;

    case 2:
        // cel => fah
        let cel_fah = celsiusParaFahrenheit(temperatura);
        console.log(`${temperatura}°C equivalem a ${cel_fah}°F`);
        break;

    default:
        console.log("Inválido")
}