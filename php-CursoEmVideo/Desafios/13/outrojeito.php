<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 13</title>
    <link rel="stylesheet" href="style.css">
    <style>
        img.nota{
          width: 100px;
          margin: 5px;  
        }
    </style>
</head>
<body>
    <header>
        <h1>Caixa Eletrônico</h1>
    </header>
    <?php 
        $saque = $_REQUEST['saque'] ?? 0;
    ?>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="saque">Qual valor você deseja sacar? (R$ <?=number_format($saque, 2, ',', '.')?>)<sup>*</sup></label>
            <p style="font-size: 0,6em;"><sup>*</sup>Notas disponíveis: R$ 100, R$ 50, R$ 10 e R$ 5</p>
            <input type="number" name="saque" id="saque" required step="5" min="0" value="<?=$valor?>">        
            <input type="submit" value="Sacar">
        </form>
    </main>
    <section>
    <?php 
        $total = $saque;
        $valor = number_format($saque, 2, ',', '.');

        $n100 = floor($total / 100); // R$ 100
        $total %= 100;

        $n50 = floor($total / 50); // R$ 50
        $total %= 50;

        $n10 = floor($total / 10); // R$ 10
        $total %= 10;

        $n5 = floor($total / 5); // R$ 5
        $total %= 5;
        
        
        
        echo "<h2>Saque de <strong>R$ $valor</strong> realizado</h2>";
 
        echo "<img src=\"imagens/100-reais.jpg\" class=\"nota\"<p><strong>x$n100</strong></p>";
        echo "<img src=\"imagens/50-reais.jpg\" class=\"nota\"<p><strong>x$n50</strong></p>";
        echo "<img src=\"imagens/10-reais.jpg\" class=\"nota\"<p><strong>x$n10</strong></p>";
        echo "<img src=\"imagens/5-reais.jpg\" class=\"nota\"<p><strong>x$n5</strong></p>";

        if ($total > 0){
            $total = number_format($total, 2, ',', '.');
            echo "<p>Restou <strong>R$ $total</strong> de <strong>R$ $valor</strong>";            
            echo "<p>*Notas disponíveis: <strong>R$ 100, R$ 50, R$ 10 e R$ 5</strong></p>";
        }   
        
    ?>
    </section>
    
</body>
</html>