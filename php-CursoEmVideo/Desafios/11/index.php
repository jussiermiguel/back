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
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nome">Preço do Produto (R$)</label>
            <label for="nome">Qual será o percentual de reajuste? (X%)</label>
            <!-- aqui o percentual é pra ir alterando de acordo com o ajuste  -->
            
        </form>
        <!-- 
            o produto que custava R$ Z, com x% de aumento vai passar a custar R$ y a partir de agora.
         -->
        <button onclick="javascript:window.location.href='numsorteado.php'">Sortear outro</button>

    </main>
    
</body>
</html>