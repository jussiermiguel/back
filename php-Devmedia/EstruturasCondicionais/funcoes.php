<?php 
    function somar($num1, $num2){
        $total = $num1 + $num2;
        return $total;
    }

    // somar(4,6);
    // echo $total;

    //Criada a referência em $num_1
function referencia(&$num_1){

    $num_1 *= 5;
  
    //retorno o valor de $num_1 * 5
    return $num_1;
  
  }
  
  $num_2 = 3;
  
  //Execução da função
  referencia($num_2);
  echo $num_2;
?>