<?php
require_once("connMysql.php");
$sql = "SELECT * FROM `students`";
?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>學生資料管理系統</title>
</head>
<body>

<?php 
if ($result = mysqli_query($conn,$sql)) {
	$total_records = mysqli_num_rows($result);
?>

    
<h1 align="center">學生資料管理系統</h1>
<p align="center">目前資料筆數:<?php print $total_records;?>,<a href="add.php">新增學生資料</a></p>

<?php
print "<table border='1' align='center'><tr align='center'>";
print "<th>" . "座號" . "</th>";
print "<th>" . "姓名" . "</th>";
print "<th>" . "性別" . "</th>";
print "<th>" . "生日" . "</th>";
print "<th>" . "電子郵件" . "</th>";
print "<th>" . "電話" . "</th>";
print "<th>" . "住址" . "</th>";
print "<th>" . "功能" . "</th>";
print "</tr>";

while($row = mysqli_fetch_array($result,MYSQLI_ASSOC)){
	// print_r($row);
	// print "<hr>";
	print "<tr>";

	print "<td>" . $row["cID"] . "</td>";
	print "<td>" . $row["cName"] . "</td>";
	print "<td>" . $row["cSex"] . "</td>";
	print "<td>" . $row["cBirthday"] . "</td>";
	print "<td>" . $row["cEmail"] . "</td>";
	print "<td>" . $row["cPhone"] . "</td>";
	print "<td>" . $row["cAddr"] . "</td>";
	print "<td><a href='update.php?id=" . $row["cID"] . "'>修改</a>";
	print "<a href='delete.php?id=" . $row["cID"] . "'>刪除</a></td>";

	print "</tr>";
	}
print "</table>";
}
mysqli_close($conn);
?>

</body>
</html>