<?php
$conn = new mysqli("localhost", "root", "", "test");

if ($conn->connect_error) {
    die("Erreur de connexion");
}

$id = $_GET['id'];
$sql = "SELECT * FROM users WHERE id = '$id'";

$result = $conn->query($sql);

if ($result) {
    while ($row = $result->fetch_assoc()) {
        echo "Utilisateur : " . $row["name"] . "<br>";
    }
}
?>
