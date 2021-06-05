<?php

require_once '../vendor/autoload.php';

$parser = new TelegramParser();

$jsonInput = file_get_contents("php://input");
$input = json_decode($jsonInput);
var_dump($_POST);
