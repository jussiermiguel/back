<?php
    $i = 0;
    for ($i; $i <= 10; $i += 2){
        echo "$i<br>";
    }

    $vetor = array(1,2,3,4,5);
    for ($i = 0; $i < 5; $i++){
        $item = $vetor[$i];
        echo "For $item<br>";
    }

    foreach ($vetor as $x){
        echo "foreach $x<br>";
    }

    $pararLoop = 9;

    for($numero = 0; ; $numero++){
        if($numero == $pararLoop){
            break;
        }
        echo $numero."<br>";
    }

    for($i = 0; $i < 10; $i++){
        if($i % 2 == 0){
            continue;
        }
        echo $i."<br>";
    }

    $colecao = [1, 3, 6, 9, 13];
    $soma = 0;
    for($i = 0; $i < count($colecao); $i++){
        $soma += $colecao[$i];
    }
    echo $soma;
?>