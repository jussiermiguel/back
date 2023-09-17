import { createInterface } from 'readline';

const rl = createInterface({
  input: process.stdin,
  output: process.stdout
});

function calcularDivisao() {
  rl.question('Digite o primeiro número: ', (num1) => {
    rl.question('Digite o segundo número: ', (num2) => {
      const numero1 = parseFloat(num1);
      const numero2 = parseFloat(num2);

      if (isNaN(numero1) || isNaN(numero2)) {
        console.log('Por favor, digite números válidos.');
      } else {
        if (numero2 === 0) {
          console.log('Não é possível dividir por zero.');
        } else {
          const resultado = numero1 / numero2;
          console.log(`O resultado da divisão é: ${resultado}`);
        }
      }

      rl.close();
    });
  });
}

calcularDivisao();