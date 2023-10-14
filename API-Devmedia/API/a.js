const express = require('express');
const app = express();

app.get('/', (req, res) => {
    // res.send('Olá, mundo! Bom dia');
    let mensagem = {mensagem : 'Olá, mundo! Bom dia'};
    res.json(mensagem);
});

app.listen(8080, () => {
    let data = new Date();
    console.log(`Servidor node iniciado em: ${data}`);
    console.log("Servidor rodando na porta: 8080");
});