<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 02</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Sorteando números</h1>
    </header>
    <section>
        <!-- 
            > rand() = 1951 - Linear Congrential Gererator
            > mt_rand() = 1997 - Mersenne Twister > mais rápido
            > A partir do PHP 7.1, rand() é um simples apontamento para mt_rand() > mesmo código
            > random_int() gera números aleatórios criptograficamente seguros > senhas > mais lento
         -->
        <?php 
            $num = mt_rand(1, 100);
            echo "<p>Gerando um número aleatório de 1 a 100</p>";
            echo "<p>O valor gerado foi $num</p>";
        ?>
        <button onclick="javascript:window.location.href='numsorteado.php'">Sortear outro</button>
        <button onclick="javascript:window.location.href='numsorteado.html'">&#x2B05;</button>
    </section>
    
</body>
</html>