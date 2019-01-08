<!DOCTYPE html><!-- 宣告文件類型 -->
<html lang="zh-tw"><!-- 指定網頁使用的語言 -->
<head><!-- 文件的標頭 -->
<meta charset="utf-8"><!-- 指定網頁編碼 -->
<title>網頁標題文字</title><!-- 文件標題 -->
</head>
<body><!-- 文件主體 -->
網頁內容

<?php
	print "hello world!";
	$servername = "localhost";
	$username = "root";
	$password = "1234";
	$database = "product";

	//create connection
	$conn = mysqli_connect($servername, $username, $password, $database);

	if (mysqli_connect_error()) 
	    print "Failed to connect to mysql:" . mysqli_connect_error();
	else 
	    print "連線成功" . "<br>";
	

	$sql = "SELECT * FROM `price`";

	if($result = mysqli_query($conn,$sql)){
		print "<table width='400' border='1'><tr align='center'>";
		print "<td>欄位名稱</td><td>長度</td></tr>";

		while ($meta = mysqli_fetch_field($result)) {
			print "<tr>";
			print "<td>" . $meta->name . "</td>";
			print "<td>" . $meta->max_length .  "</td>";
			print "</tr>";
		}

		print "</table>";
	}

	mysqli_close($conn);
?>

</body>
</html>
