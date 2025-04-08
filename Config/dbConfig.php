<?php

    $dbHost = 'LocalHost';
    $dbUsername = 'root';
    $dbPassword ='';
    $dbName ='FlexSeat';

    $connect = new databricks($dbHost,$dbUsername,$dbPassword,$dbName)

    if($connect->connect_errno)
    {
        echo "Erro";

    }
    else
    {
        encho "Conexão conluída"
    }
?>