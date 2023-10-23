<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 10</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Calculando a sua idade</h1>
    </header>
    <?php
        
        $nascimento = $_GET['nascimento'] ?? 0;
        $ano = $_GET['ano'] ?? date('Y');
    ?>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nascimento">Em que ano você nasceu?</label>
            <input type="number" name="nascimento" id="nascimento" max="<?=date('Y')?>" value="<?=$nascimento?>">
            <label for="ano">Quer saber sua idade em que ano? (atualmente estamos em <?=$ano?>)</label>
            <input type="number" name="ano" id="ano" min="<?=$nascimento?>" value="<?=$ano?>">
            <input type="submit" value="Qual Será Minha Idade?">            
        </form>
    </main>
    <section>
        <?php 
            $idade = $ano - $nascimento;
            echo "<h2>Resultado</h2>";
            echo "<p>Quem nasceu em $nascimento vai ter $idade anos em $ano</p>";
        ?>

    </section>
    <!-- 
        quuem nasceu em 1998 vai ter x anos em y!
     -->
    
</body>
</html>