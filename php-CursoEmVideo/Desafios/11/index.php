<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 11</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Reajustador de Preços</h1>
    </header>
    <?php 
        $preco = $_GET['preco'] ?? '0';
        $reajuste = $_GET['reajuste'] ?? '0';
    ?>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="preco">Preço do Produto (R$)</label>
            <input type="number" name="preco" id="preco" min="0.10" step="0.01" value="<?=number_format($preco, 2, ",", ".")?>">

            <label for="reajuste">Qual será o percentual de reajuste? (<strong><span id="p">?</span>%</strong>)</label>
            <input type="range" name="reajuste" id="reajuste" min="0" max="100" step="1"  oninput="mudarValor()" value="<?=$reajuste?>">
            <!-- aqui o percentual é pra ir alterando de acordo com o ajuste  -->
            <input type="submit" value="Reajustar">            
        </form>
    </main>
    <section>
        <?php
            $aumento = ($preco * $reajuste) / 100;
            $novo_preco = $preco + $aumento;
        ?>
        <h2>Resultado do Reajuste</h2>
        <p>O produto que custava <strong>R$ <?=$preco?></strong>, com <strong><?=$reajuste?>% de aumento</strong> vai passar a custar <strong>R$ <?=number_format($novo_preco, 2, ",", ".")?></strong> a partir de agora</p>   
    </section>
     <script>
        mudarValor();
        function mudarValor(){
            document.getElementById('p').innerText = reajuste.value;
        }
     </script>
</body>
</html>