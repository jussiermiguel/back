<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 03</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Conversor de Moedas</h1>
    </header>
    <section>
        <?php 
            $valor_real = $_POST["valor"] ?? 0;
            $contação_euro = 5.1939;
            $valor_euro = $valor_real / $contação_euro;
            $contação_dolar = 5.13314;
            $valor_dolar = $valor_real / $contação_dolar;
            
            echo "<p>R$ " . number_format($valor_real, 2, ',', '.') . "</p>";
            echo "<p>E$ " . number_format($valor_euro, 2, ',', '.') . "</p>";
            echo "<p>U$ " . number_format($valor_dolar, 2, ',', '.'). "</p>";
        ?>

        <button onclick="javascript:window.location.href='convertermoeda.html'">&#x2B05;</button>
    </section>
    
</body>
</html>