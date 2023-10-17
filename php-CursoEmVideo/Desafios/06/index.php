<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 06</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Anatomia de uma divisão</h1>
    </header>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nome">Divisor</label>
            <label for="nome">Dividendo</label>
        </form>
        <!-- 
            25 |_4
            1   6
         -->
        <button onclick="javascript:window.location.href='numsorteado.php'">Sortear outro</button>

    </main>
    
</body>
</html>