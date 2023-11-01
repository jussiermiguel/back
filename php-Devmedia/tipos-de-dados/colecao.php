<?php
 class CD
 {
    var $titulo;
    var $banda;
    var $ano_lancamento;
 }

 $disco = new CD();
    $disco ->titulo = "The Number of the Beast";
    $disco ->banda = "Iron Maiden";
    $disco ->ano_lancamento = 1982;

    echo "Título: " . $disco->titulo . "<br>";
    echo "Banda: " . $disco->banda . "<br>";
    echo "Ano de Lançamento: " . $disco->ano_lancamento . "<br>";
?>