const nascimento = new Date("1998-03-11 11:00:59");
console.log(nascimento);

// Sem parâmetro: Data atual
const hoje= new Date();

// Com parâmetro: String com a data
const exemplo1 = new Date(  "2020-02-28"  );
const exemplo2 = new Date(  "2020-02-27 10:35:00"  );

//  Com parâmetro: Um número para ano, mês, dia, hora, minuto, segundo e milissegundo
const exemplo3 = new Date(  2020, 2, 28, 13, 20, 2, 15  );

console.log(hoje);
console.log(exemplo1);
console.log(exemplo2);
console.log(exemplo3);