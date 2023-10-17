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
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nome">Em que ano você nasceu?</label>
            <label for="nome">Quer saber sua idade em que ano? (atualmente estamos em 2023)</label>
            
            
        </form>
        <!-- 
            quuem nasceu em 1998 vai ter x anos em y!
         -->
        <button onclick="javascript:window.location.href='numsorteado.php'">Sortear outro</button>

    </main>
    
</body>
</html>