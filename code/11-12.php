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

	mysqli_query($conn,"SET NAMES utf8");
	// $sql = "SELECT * FROM `price`";
	$sql = "SELECT * FROM `price` WHERE `category`='主機板'";

	if($result = mysqli_query($conn,$sql)){
		print "<table border='1' align='center'><tr align='center'>";
		while ($meta = mysqli_fetch_field($result)) {
			print "<td>" . $meta->name . "</td>";
		}
		print "</tr>";

		while($row = mysqli_fetch_row($result)){
			// print_r($row);
			// print "<hr>";
			print "<tr>";
			while ($row = mysqli_fetch_array($result,MYSQLI_ASSOC)) {
				// print_r($row);
				// print "<hr>";
				print "<tr>";
				print "<td>" . $row["no"] . "</td>";
				print "<td>" . $row["category"] . "</td>";
				print "<td>" . $row["no"] . "</td>";
				print "<td>" . $row["no"] . "</td>";
				print "<td>" . $row["no"] . "</td>";
				print "<td>" . $row["no"] . "</td>";
				print "<td>" . $row["no"] . "</td>";
			}
			print "</tr>";
		}

		print "</table>";
	}

	mysqli_close($conn);
?>

</body>
</html>
