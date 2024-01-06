<?php 
    // $a = 10;
    // $b = 5;

    // // echo $a/$b == 2 ? "O resultado é 2" : "O resultado não é 2";
    
    // switch($a){
    //     case !10:
    //         echo "O valor é 10";
    //         break;
    //     default:
    //         echo "Não é 10";
    // }

    // switch($b){
    //     case !5:
    //         echo "o valor é 5";
    //         break;
    //     default:
    //         echo "O valor não é 5";
    // }

    // $num = [1,2,3,4,5,6,7,8,9,10];

    // foreach ($num as $i => $n){
    //     if ($n == 8){
    //         $retorno = $n;
    //         break;
    //     }
    //     echo "<p>$n</p>";
    // }

    // echo $retorno;

    // $i = 0;
    // while ($i++ < 3) {
    //     echo "3\n";
    //     while (1) {
    //         echo "2\n";
    //         while (1) {
    //             echo "1\n";
    //             break 3;
    //         }
    //         echo "Essa linha nunca vai ser exibida\n";
    //     }
    //     echo "Nem essa linha\n";
    // }

    // $funcionarios = array(
    //     array('id' => 1, 'nome' => 'João', 'salario' => 5000),
    //     array('id' => 22, 'nome' => 'Mauro', 'salario' => 560),
    //     array('id' => 8, 'nome' => 'Alice', 'salario' => 4300),
    //     );
      
    //   foreach ($funcionarios as $i => $funcionario) {
    //     if ($funcionario['id'] == 22) {
    //           $busca = $funcionario;
    //           break;
    //     }
    //   }
      
    //   if (isset($busca)) {
    //     echo "Funcionário encontrado: {$busca['nome']} - {$busca['id']}";
    //   } else {
    //     echo "Funcionário não encontrado";
    //   }

    $funcionarios = array(
        array('id' => 1, 'nome' => 'João', 'salario' => 5000),
        array('id' => 22, 'nome' => 'Mauro', 'salario' => 560),
        array('id' => 8, 'nome' => 'Alice', 'salario' => 4300),
    );
      
    foreach ($funcionarios as $i => $funcionario) {
        if ($funcionario['salario'] >= 5000) {
              continue;
        }
      
        $funcionarios[$i]['salario'] = $funcionario['salario'] + ($funcionario['salario'] * 0.1);
    }
      
    foreach ($funcionarios as $funcionario) {
        echo $funcionario["nome"]." $".$funcionario["salario"]."\n";
    }
?>