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
            <label for="valor">Qual valor você deseja sacar? (R$)</label>
            <p>*Notas disponíveis: R$ 100, R$ 50, R$ 10 e R$ 5</p>
            <input type="number" name="valor" id="valor" min="0" value="<?=$valor?>">        
            <input type="submit" value="Sacar">
        </form>
    </main>
    <section>
        <?php 
        $total = $valor;
        $valor = number_format($valor, 2, ',', '.');
        
        $nota = 100;
        $i = 0;
        
        echo "<h2>Ainda não terminei</h2>";
        while(true){
            if ($total >= $nota){
                $total -= $nota;
                $i += 1;
            }
            else{
                if ($i > 0){
                    echo "<p>O total de $i de notas de R$ $nota</p>";
                }

                if ($nota == 100){
                    $nota = 50;
                }
                else if ($nota == 50){
                    $nota = 10;
                }
                else if ($nota == 10){
                    $nota = 5;
                }

                $i = 0;
                if ($total == 0){
                    break;
                }
                else {
                    echo "<p>Troco: R$ $total.</p>";
                    break;
                }
            }
        }
        
           


    ?>
    </section>
    
</body>
</html>