let numeros = [
    14,
    36,
    67,
    33,
    16,
    25,
    55,
    88,
    66,
    47,
    15,
    8,
]
let contador = 0
let quantidade_pares = 0
let quantidade_impares = 0
console.log(numeros)

while(contador < numeros.length){
    if(numeros[contador] % 2 == 0){
        quantidade_pares = quantidade_pares + 1        
    }
    else{
        quantidade_impares = quantidade_impares + 1        
    }
    contador++
}
console.log("A quantidade de pares é: "+ quantidade_pares)
console.log("A quantidade de ímpares é: "+ quantidade_impares)
