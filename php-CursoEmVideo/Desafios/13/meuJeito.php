<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 13</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Caixa Eletrônico</h1>
    </header>
    <?php 
        $valor = $_REQUEST['valor'] ?? 0;
    ?>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="valor">Qual valor você deseja sacar? (R$ <?=number_format($valor, 2, ',', '.')?>;)</label>
            <p>*Notas disponíveis: R$ 100, R$ 50, R$ 10 e R$ 5</p>
            <input type="number" name="valor" id="valor" required min="0" value="<?=$valor?>">        
            <input type="submit" value="Sacar">
        </form>
    </main>
    <section>
    <?php 
        $total = $valor;
        $valor = number_format($valor, 2, ',', '.');

        $n100 = (int) ($total / 100); // R$ 100
        $total = $total % 100;

        $n50 = (int) ($total / 50); // R$ 50
        $total = $total % 50;

        $n10 = (int) ($total / 10); // R$ 10
        $total = $total % 10;

        $n5 = (int) ($total / 5); // R$ 5
        $total = $total % 5;
        
        
        
        echo "<h2>Saque de <strong>R$ $valor</strong> realizado</h2>";
 
        echo "<p>Notas de <strong>R$ 100</strong>: $n100</p>";
        echo "<p>Notas de <strong>R$ 50</strong>: $n50</p>";
        echo "<p>Notas de <strong>R$ 10</strong>: $n10</p>";
        echo "<p>Notas de <strong>R$ 5</strong>: $n5</p>";

        if ($total > 0){
            $total = number_format($total, 2, ',', '.');
            echo "<p>Restou <strong>R$ $total</strong> de <strong>R$ $valor</strong>";            
            echo "<p>*Notas disponíveis: <strong>R$ 100, R$ 50, R$ 10 e R$ 5</strong></p>";
        }   
        
    ?>
    </section>
    
</body>
</html>