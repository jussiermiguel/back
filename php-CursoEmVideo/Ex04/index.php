<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipos primitivos em PHP</title>
</head>
<body>
    <h1>Teste de tipos primitivos</h1>
    <?php
    // 0x = hexadecimal 0b = binário 0 = octal 
        // $num = 0x1A;
        // echo "Ovalor da variável é $num";
        // $v = "true";
        // var_dump($v);

        // $num = (int)3e2; coerção
        // echo $num;
        // var_dump($num);

        // array
        // $vet = [6,"JU", 2, 4, true, 5, 1];
        // var_dump($vet);

        // object
        class Pessoa {
            private string $nome;
        }

        $p = new Pessoa;
        var_dump($p);
    ?>
</body>
</html>