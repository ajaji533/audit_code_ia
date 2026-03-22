<?php
$page = $_GET['page'];

if ($page) {
    include($page . ".php");
} else {
    include("accueil.php");
}
?>
