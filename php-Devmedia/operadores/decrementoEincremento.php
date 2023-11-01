<?php 
    $valor = 5;
    $resultado = -$valor; // $resultado agora é -5

    echo "<p>$valor</p>";
    echo "<p>$resultado</p>";

    $valor = 5;
    $resultado = ++$valor; // $valor é incrementado em 1 antes de ser usado em $resultado, então $resultado é 6, $valor é 6

    echo "<p>$valor</p>";
    echo "<p>$resultado</p>";

    $valor = 5;
    $resultado = --$valor; // $valor é decrementado em 1 antes de ser usado em $resultado, então $resultado é 4, $valor é 4
    echo "<p>$valor</p>";
    echo "<p>$resultado</p>";

    $num1 = 2;
    $num2 = 4;
    $num3 = 6;
    $num4 = 8;

    //Resultado igual a 3
    $resposta1 = ++$num2 - $num1;

    //Resultado igual a 8
    $resposta2 = $num3-- + $num1;

    //Resultado igual a 9
    $resposta3 = --$num1 + $num4;
    echo "<p>$resposta1</p>";
    echo "<p>$resposta2</p>";
    echo "<p>$resposta3</p>";
?>