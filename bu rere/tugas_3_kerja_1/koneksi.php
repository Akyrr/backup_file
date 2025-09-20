<?php 
$servername="localhost";
$username="root";
$password="";
$dbname="data_mahasiswa";

$conn=new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die ("koneksi gaagal: ." $conn->connect_error);
}
?>