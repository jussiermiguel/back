<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 07</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
    $salario_minimo = 1_380.60;
    $salario_form = $_GET['salario'] ?? $salario_minimo;
    ?>
    <main>
        <h1>Informe o seu salário</h1>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="salario">Salário (R$)</label>
            <input type="number" name="salario" id="salario" step="0.01" value="<?=$salario_form?>">
            <p>Considerando o salário mínimo de <strong>R$ <?=number_format($salario_minimo, 2, ',', '.')?></strong></p>
            <input type="submit" value="Calcular">
        </form>
    </main>
    <section>
        <h1>Resultado Final</h1>
        <?php 
            $salario = number_format($salario_form, 2, ',', '.');
            $quant_salario_minimos = intdiv($salario_form, $salario_minimo);
            $resto_salario_minimo = $salario_form % $salario_minimo;

            if ($resto_salario_minimo == 0){
                echo "Quem recebe um salário de R$ $salario ganha $quant_salario_minimos salários mínimos";
            }
            else{
                echo "Quem recebe um salário de R$ $salario ganha $quant_salario_minimos salários mínimos + R$ $resto_salario_minimo";
            }
        ?>
    </section>


    
</body>
</html>