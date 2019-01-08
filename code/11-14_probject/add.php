<?php
if (isset($_POST["action"]) && $_POST["action"] == "add") {
  require_once("connMysql.php");
  // print "OK";
  // INSERT INTO `students`(`cName`,`cSex`,`cBirthday`,`cEmail`,`cPhone`,`cAddr`) VALUES ('aa','F','2018-12-11','aa','09999','aa');
  $sql = "INSERT INTO `students`(`cName`,`cSex`,`cBirthday`,`cEmail`,`cPhone`,`cAddr`) VALUES (";
  $sql .="'" . $_POST["cName"] . "',";
  $sql .="'" . $_POST["cSex"] . "',";
  $sql .="'" . $_POST["cBirthday"] . "',";
  $sql .="'" . $_POST["cEmail"] . "',";
  $sql .="'" . $_POST["cPhone"] . "',";
  $sql .="'" . $_POST["cAddr"] . "')";
  // print $sql;
  mysqli_query($conn,$sql);
  mysqli_close($conn);
  header("Location:data.php");
}

?>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>學生資料管理系統</title>
</head>
<body>
<h1 align="center">學生資料管理系統 - 新增資料</h1>
<p align="center"><a href="data.php">回主畫面</a></p>
<form action="" method="post" name="formAdd" id="formAdd">
  <table border="1" align="center" cellpadding="4">
    <tr>
      <th>欄位</th><th>資料</th>
    </tr>
    <tr>
      <td>姓名</td><td><input type="text" name="cName" id="cName"></td>
    </tr>
    <tr>
      <td>性別</td><td>
      <input type="radio" name="cSex" id="radio" value="M" checked>男
      <input type="radio" name="cSex" id="radio" value="F">女
      </td>
    </tr>
    <tr>
      <td>生日</td><td><input type="date" name="cBirthday" id="cBirthday"></td>
    </tr>
    <tr>
      <td>電子郵件</td><td><input type="text" name="cEmail" id="cEmail"></td>
    </tr>
    <tr>
      <td>電話</td><td><input type="text" name="cPhone" id="cPhone"></td>
    </tr>
    <tr>
      <td>住址</td><td><input name="cAddr" type="text" id="cAddr" size="40"></td>
    </tr>
    <tr>
      <td colspan="2" align="center">
      <input name="action" type="hidden" value="add">
      <input type="submit" name="button" id="button" value="新增資料">
      <input type="reset" name="button2" id="button2" value="重新填寫">
      </td>
    </tr>
  </table>
</form>
</body>
</html>