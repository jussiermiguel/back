<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 05</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Analisando números</h1>
    </header>
    <section>
        <?php 
            $numero = $_GET["num"] ?? 0;
            $numero_inteiro = (int)$numero;
            // $numero_inteiro = intval($numero);
            $numero_float = $numero - $numero_inteiro;

            echo "<p>O número digitado foi: " . number_format($numero, 3, ",", ".") . "</p>";
            echo "<p>Sua parte inteira: " . number_format($numero_inteiro, 0, ",", ".") . "</p>";
            echo "<p>Sua parte real: " . number_format($numero_float, 3, ",", ".") . "</p>";
            
        ?>
        <button onclick="javascript:window.location.href='analisadorDenumero.html'">&#x2B05;</button>
    </section>
    
</body>
</html>