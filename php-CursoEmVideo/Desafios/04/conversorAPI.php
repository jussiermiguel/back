<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 03</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Conversor de Moedas</h1>
    </header>
    <section>
        <?php
            // cotação vinda da API do Banco 
            $inicio = date("m-d-Y", strtotime("-7 days"));
            $fim = date("m-d-Y");
            $url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=\''. $inicio .'\'&@dataFinalCotacao=\''. $fim .'\'&$top=1&$orderby=dataHoraCotacao%20desc&$format=json&$select=cotacaoCompra,dataHoraCotacao';
        
            $dados = json_decode(file_get_contents($url), true);
        
            $cotacao = $dados["value"][0]["cotacaoCompra"];
           
            $valor_real = $_REQUEST["valor"] ?? 0;
            
            $valor_dolar = $valor_real / $cotacao;
            
            echo "<p>R$ " . number_format($valor_real, 2, ',', '.') . "</p>";
           
            echo "<p>U$ " . number_format($valor_dolar, 2, ',', '.'). "</p>";
        ?>

        <button onclick="javascript:window.location.href='conversorAPI.html'">&#x2B05;</button>
    </section>
    
</body>
</html>