import colecao_signos from './dados/dados1.js';
import retorna_signo from './funcoes/funcoes1.js';

let data_app = new Date();

const nome_signo = retorna_signo(colecao_signos, data_app);

console.log("O signo de hoje é: " + nome_signo);