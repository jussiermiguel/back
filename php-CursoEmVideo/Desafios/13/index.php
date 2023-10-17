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
    <main>
        <form action="<?=$_SERVER['PHP_SELF']?>" method="get">
            <label for="nome">Qual valor você deseja sacar? (R$)</label>
            <p>*Notas disponíveis: R$ 100, R$ 50, R$ 10 e R$ 5</p>
        
            
        </form>
        <!-- 
            O valor X segundos equivalem a um total de:
            * x semanas
            * x dias
            * x horas
            * x minutos
            * x segundos
         -->
        <button onclick="javascript:window.location.href='numsorteado.php'">Sortear outro</button>

    </main>
    
</body>
</html>