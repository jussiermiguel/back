function fahrenheitParaCelsius (fahrenheit){
    let celsius = (fahrenheit - 32) / 1.8;
    return celsius; 
}

function celsiusParaFahrenheit(celsius)
{
    let fahrenheit;

    fahrenheit = (celsius * 1.8) + 32;

    return fahrenheit;
}

export {fahrenheitParaCelsius, celsiusParaFahrenheit};