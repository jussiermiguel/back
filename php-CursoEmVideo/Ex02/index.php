<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
</head>
<body>
    <h1>Exemplo PHP</h1>
    <?php 
        // date_default_timezone_set("America/Sao_Paulo");
        echo "Hoje é dia" . date(' d/M/A / D');
        echo "E a hora atual" . date(' G:i:s T');
    ?>
    
</body>
</html>