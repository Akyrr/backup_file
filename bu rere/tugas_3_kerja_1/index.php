<?php 
include'koneksi.php';
$sql="SELECT * FROM mahasiswa";
$result=$conn->query($sql);
?>
<html>
<head>
    <title>Data Mahasiswa</title>
    <link rel="stylesheet" href="mystyle.css" media="all" />
</head>
<body>
    <h2>DATA MAHASISWA</h2>
    <table class="dttabel" width="100%" border="1">
        <tr>
            <th>No.</th>
            <th>No. Induk</th>
            <th>Nama Mahasiswa</th>
            <th>JK</th>
            <th>Tgl. Lahir</th>
            <th>Alamat</th>
            <th>Dosen Pembimbing</th>
            <th>No. Telepon</th>
        </tr>

        <tr>
            <td>1</td>
            <td>160202340010</td>
            <td>Agus</td>
            <td>L</td>
            <td>02-10-1990</td>
            <td>Malang</td>
            <td>Bambang</td>
            <td>081233456789</td>
        </tr>
        
        <tr>
            <td>2</td>
            <td>160202340013</td>
            <td>Budi</td>
            <td>L</td>
            <td>03-02-1989</td>
            <td>Surabaya</td>
            <td>Atin</td>
            <td>081145673456</td>
        </tr>

        <tr>
            <td>3</td>
            <td>160202340017</td>
            <td>Cahya</td>
            <td>P</td>
            <td>06-05-1991</td>
            <td>Blitar</td>
            <td>Atin</td>
            <td>081334556689</td>
        </tr>

        <tr>
            <td>4</td>
            <td>160202340018</td>
            <td>Doni</td>
            <td>L</td>
            <td>05-12-1990</td>
            <td>Malang</td>
            <td>Samsuddin</td>
            <td>-</td>
        </tr>
        <?php
        if ($result->num_rows>0) {
            $no=1;
            while ($row=$result->fetch_assoc()) { 
                echo "<tr>
                    <td>".$no."</td>
                    <td>".$row["no_induk"]."</td>
                    <td>".$row["nama"]."</td>
                    <td>".$row["jk"]."</td>
                    <td>".$row["tgl_lahir"]."</td>
                    <td>".$row["alamat"]."</td>
                    <td>".$row["dosen_pembimbing"]."</td>
                    <td>".$row["no_telepon"]."</td>
                </tr>";
                $no++;
            }
        } else {
            echo"<tr><td colspan='8'>Tidak ada data mahasiswa</td></tr>";
        }
        $conn->close();
        ?>
    </table>
    <br>
    <a href="add.html">Add Data</a>
</body>
</html>