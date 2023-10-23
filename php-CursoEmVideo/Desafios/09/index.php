<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 09</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $valor1 = $_GET['valor1'] ?? ' ';
        $peso1 = $_GET['peso1'] ?? ' ';
        $valor2 = $_GET['valor2'] ?? ' ';
        $peso2 = $_GET['peso2'] ?? ' ';
    ?>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <h1>Média Aritméticas</h1>
            <label for="valor1">1° Valor</label>
            <input type="number" name="valor1" id="valor1" min="1" step="0.01" value="<?=$valor1?>">
            <label for="peso1">1° Peso</label>
            <input type="number" name="peso1" id="peso1" min="1" value="<?=$peso1?>">
            <label for="valor2">2° Valor</label>
            <input type="number" name="valor2" id="valor2" min="1" step="0.01" value="<?=$valor2?>">
            <label for="peso1">2° Peso</label>
            <input type="number" name="peso2" id="peso2" min="1" value="<?=$peso2?>">
            <input type="submit" value="Calcular Médias">
        </form>
    </main>
    <section>
        
        <?php
            $media_simples = ($valor1 + $valor2)/ 2;
            $media_ponderada = (($valor1 * $peso1) + ($valor2 * $peso2))/($peso1 + $peso2);

            echo "<h1>Cálculo das Médias</h1>";
            echo "<ul><li>A <strong>Média Aritmética Simples</strong> entre os valores <strong>$valor1</strong> e <strong>$valor2</strong> é igual a <strong>$media_simples</strong></li>";
            echo "<li>A <strong>Média Aritmética Ponderada</strong> entre os valores <strong>$valor1</strong> com peso <em>>$peso1</em> e <strong>$valor2</strong> com peso <em>>$peso2</em> é igual a <strong>$media_simples</strong></li>";
            
        ?>
        <!-- 
            analisando os valor x e x:
            * média aritmética simples
            * média aritmética ponderada
        -->
    </section>
    
</body>
</html>