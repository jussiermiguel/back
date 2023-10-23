<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 12</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Calculadora de tempo</h1>
    </header>
    <?php 
        $total = $_GET['total'] ?? 0;
    ?>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="total">Qual é o total de segundos?</label>
            <input type="number" name="total" id="total" min="0" step="1" required value="<?=$total?>">        
            <input type="submit" value="Calcular">
        </form>
    </main>    
    <?php
        // meu jeito
        $sobra = $total; 
        $semanas = intval($sobra / 604800); // 7D 168h 10080min 604800s
        $sobra = $sobra % 604800;

        $dias = intval($sobra / 86400); // 24h 1440min 86400s
        $sobra = $sobra % 86400;

        $horas = intval($sobra / 3600); // 60min 3600s
        $sobra = $sobra % 3600;

        $minutos = intval($sobra / 60); // 60s
        $sobra = $sobra % 60;
        
        $segundos = intval($sobra / 1); // 1s
    
        // Jeito de Guanabara
        // $sobra = $total;
        // $semanas = (int)($sobra / 604800); // 7D 168h 10080min 604800s
        // $sobra = $sobra % 604800;

        // $dias = (int)($sobra / 86400); // 24h 1440min 86400s
        // $sobra = $sobra / 86400;

        // $horas = (int)($sobra / 3600); // 60min 3600s
        // $sobra = $sobra % 3600;

        // $minutos = (int)($sobra / 60); // 60s
        // $sobra = $sobra % 60;

        // $segundos = $sobra;
    ?>
    <section>
        <h2>Totalizando tudo</h2>
        <p>Analisando que você digitou, <strong><?=number_format($total, 0, ',', '.')?> segundos</strong> equivalem a um total de: </p>
        <ul>
            <li><?=$semanas?> semanas</li>
            <li><?=$dias?> dias</li>
            <li><?=$horas?> horas</li>
            <li><?=$minutos?> minutos</li>
            <li><?=$segundos?> segundos</li>
        </ul>
    </section>    
</body>
</html>