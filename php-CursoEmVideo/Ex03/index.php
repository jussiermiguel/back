<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Variáveis e Constantes</title>
</head>
<body>
    <h1>Variáveis e Constantes</h1>

    <?php 
        $nome = 'Jussiêr';
        $sobrenome = '';
        const _time = 'Vasco';
        $idade = 25;
        $peso = 95.5;
        $casado = false;
    
        $sobrenome = 'Miguel Oliveira';
        echo "Muito prazer, $nome $sobrenome. $idade anos. Torce pelo ". _time;
    ?>
</body>
</html>