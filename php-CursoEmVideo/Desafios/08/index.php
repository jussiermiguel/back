<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 08</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <?php 
        $numero = $_GET['numero'] ?? 0;
    ?>
 
    <main>
        <h1>Informe um número</h1>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="numero">Numero</label>
            <input type="number" name="numero" id="numero" value="<?=$numero?>">
            <input type="submit" value="Calcular">
        </form>
    </main>
    <section>
        <h2>Resultado</h2>
        <?php 
            $raiz_quadrada = $numero**(1/2);
            $raiz_cubica = $numero**(1/3);
            
            echo "<p>Analisando o número $numero, temos:</p>";
    
            echo "<ul><li>Raíz Quadrada: $raiz_quadrada</li>";
            echo "<li>Raíz Cúbica: $raiz_cubica</li></ul>";

        ?>
        <!-- 
            analisando o número x, temos:
            
            * a sua raiz quadrada é y
            * a sua raiz cúbica é z
        -->
    </section>
    
</body>
</html>