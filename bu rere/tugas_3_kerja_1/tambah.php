<?php
include 'koneksi.php';

if ($_SERVER["REQUEST_METHOD"] == "GET") {
    $noinduk = $_GET['noinduk'];
    $nama = $_GET['nama'];
    $jk = $_GET['jk'];
    $tgllahir = $_GET['tgllahir'];
    $alamat = $_GET['alamat'];
    $dosen = $_GET['dosen'];
    $telp = $_GET['telp'];

    $sql = "INSERT INTO mahasiswa (no_induk, nama, jk, tgl_lahir, alamat, dosen_pembimbing, no_telepon)
    VALUES ('$noinduk', '$nama', '$jk', '$tgllahir', '$alamat', '$dosen', '$telp')";

    if ($conn->query($sql) === TRUE) {
        echo "Data berhasil ditambahkan. <a href='index.php'>Lihat Data</a>";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>