<html>
<head>
</head>
<body>
    <title>Data Mahasiswa</title>
    <link rel="stylesheet" href="mystyle.css" media="all" />
    <h2>DATA MAHASISWA</h2>
    <table class="frtabel" align="center">
        <form action="tambah.php">
            <caption>Tambah data Mahasiswa</caption>
            <tr>
                <td width="140px">No. Induk</td>
                <td><input type="text" name="noinduk" maxlength="12" /></td>
            </tr>
            <tr>
                <td>Nama Mahasiswa</td>
                <td><input type="text" name="nama" maxlength="50" /></td>
            </tr>
            <tr>
                <td>JK</td>
                <td>
                    <input type="radio" name="jk" value="L" checked /> Laki-laki
                    <input type="radio" name="jk" value="P" /> Perempuan
                </td>
            </tr>
            <tr>
                <td>Tgl. Lahir</td>
                <td><input type="date" name="tgllahir" /></td>
            </tr>
            <tr>
                <td>Alamat</td>
                <td><textarea name="alamat" cols="30"></textarea></td>
            </tr>
            <tr>
                <td>Dosen Pembimbing</td>
                <td><input type="text" name="dosen" maxlength="50" /></td>
            </tr>
            <tr>
                <td>No. Telepon</td>
                <td><input type="Tel" name="telp" /></td>
            </tr>
            <tr>
                <td><input type="submit" value="Simpan" /></td>
                <td><input type="reset" value="Batal" /></td>

        </form>
    </table>
</body>
</html>