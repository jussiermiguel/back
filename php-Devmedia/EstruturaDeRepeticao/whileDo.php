<?php 
    $i = 0;
    while($i <= 10) {
        echo "$i<br>";
        ++$i;
    }
    $i = 1;
    while ($i <= 10):
        echo "while $i<br>";
        $i++;
    endwhile;

    $i = 1;
    do {
        echo "do while $i<br>";
        $i++;
    } while ($i < 11);

    echo "<br>";
    $i = 0;
    while (true) {
        if ($i == 5) {
            break;
        }
        echo $i;
        $i++;
    }

    echo "<br>";
    $i = 0;
    while($i < 10){
        $i++;
        if($i % 2 == 0){
            continue;
        }
        echo $i;
    }
?>