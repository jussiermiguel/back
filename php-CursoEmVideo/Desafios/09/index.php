<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 09</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Média Aritméticas</h1>
    </header>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nome">1° Valor</label>
            <label for="nome">1° Peso</label>
            <label for="nome">2° Valor</label>
            <label for="nome">2° Peso</label>
            
        </form>
        <!-- 
            analisando os valor x e x:
            * média aritmética simples
            * média aritmética ponderada
         -->
        <button onclick="javascript:window.location.href='numsorteado.php'">Sortear outro</button>

    </main>
    
</body>
</html>