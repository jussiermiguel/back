<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 07</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Informe seu salário</h1>
    </header>
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nome">Salário (R$)</label>
            <p>Considerando o salário mínimo de <strong>R$ 1.380,00</strong></p>

        </form>
        <!-- 
            quem recebe salário de x ganha y salários mínimos + z ( se tiver sobra)
         -->
        <button onclick="javascript:window.location.href='numsorteado.php'">Sortear outro</button>

    </main>
    
</body>
</html>