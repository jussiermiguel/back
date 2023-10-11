<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interação com Formulários</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Antecessor e Sucessor</h1>
    </header>
    <main>
        <?php 
            $num = $_GET["numero"] ?? 0;

            $antecessor = $num - 1;
            $sucessor = $num + 1;

            echo "<p>O número escolhido foi $num </p>";
            echo "<p>O seu antecessor é $antecessor </p>";
            echo "<p>O seu sucessor é $sucessor </p>";
        ?>
    
        <button onclick="javascript:window.location.href='antEsuc.html'">&#x2B05;<a href=""></a></button>
    </main>
    
</body>
</html>