
<!-- // membuat tabel dengan perulangan for php
// kamu isa mengganti {} dengan : diawal dan ednfor; diakhir disebut sintaks alternatif
// kamu juga bisa mengganti echo dengan = contohnya <?= $a ?> sama aja kayak echo $a ?> -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .warna-baris {
            background-color: tomato;
        }
        .warna-kolom {
            background-color: lightblue;
        }
    </style>
</head>
<body>
    <table border="1" cellpadding="20" cellspacing="0">
        <?php 
        for ($a=1; $a <= 5; $a++)
            if ($a % 2 == 1) {
                echo "<tr class='warna-baris'>";
            } else 
               for ($b=1; $b <= 5; $b++) {
                    echo "<td>$a-$b</td>";  
                }
            echo "</tr>";
        
        ?>
    </table>
</body>
</html>