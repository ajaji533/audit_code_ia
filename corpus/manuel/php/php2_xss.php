<?php
$nom = $_GET['name'];

function afficher_message($nom) {
    echo "<h1>Bonjour " . $nom . "</h1>";
}

afficher_message($nom);
?>
