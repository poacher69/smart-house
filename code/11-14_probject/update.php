<?php
require_once("connMysql.php");

if(isset($_POST["action"]) && $_POST["action"] == "update"){
  // print "ok";
  $sql = "UPDATE `students` SET";
  $sql .="`cName`='" . $_POST["cName"] . "',";
  $sql .="`cSex`='" . $_POST["cSex"] . "',";
  $sql .="`cBirthday`='" . $_POST["cBirthday"] . "',";
  $sql .="`cEmail`='" . $_POST["cEmail"] . "',";
  $sql .="`cPhone`='" . $_POST["cPhone"] . "',";
  $sql .="`cAddr`='" . $_POST["cAddr"] . "' ";
  $sql .="WHERE `cID`=" . $_POST["cID"];
  // print $sql;
  mysqli_query($conn,$sql);
  mysqli_close($conn);
  header("Location:data.php");
}

$sql = "SELECT * FROM `students` WHERE `cID`=" . $_GET["id"];
// print $sql;

$result = mysqli_query($conn,$sql);
$row = mysqli_fetch_array($result,MYSQLI_ASSOC);
// print_r($row);
mysqli_close($conn);
?>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>學生資料管理系統</title>
</head>
<body>
<h1 align="center">學生資料管理系統 - 修改資料</h1>
<p align="center"><a href="data.php">回主畫面</a></p>
<form action="" method="post" name="formFix" id="formFix">
  <table border="1" align="center" cellpadding="4">
    <tr>
      <th>欄位</th><th>資料</th>
    </tr>
    <tr>
      <td>姓名</td><td><input type="text" name="cName" id="cName" value="<?php print $row["cName"];?>"></td>
    </tr>
    <tr>
      <td>性別</td><td>
      <input type="radio" name="cSex" id="radio" value="M" <?php if($row["cSex"]=="M") print "checked"; ?>>男
      <input type="radio" name="cSex" id="radio" value="F" <?php if($row["cSex"]=="F") print "checked"; ?>>女
      </td>
    </tr>
    <tr>
      <td>生日</td><td><input type="date" name="cBirthday" id="cBirthday" value="<?php print $row["cBirthday"];?>"></td>
    </tr>
    <tr>
      <td>電子郵件</td><td><input type="text" name="cEmail" id="cEmail" value="<?php print $row["cEmail"];?>"></td>
    </tr>
    <tr>
      <td>電話</td><td><input type="text" name="cPhone" id="cPhone" value="<?php print $row["cPhone"];?>"></td>
    </tr>
    <tr>
      <td>住址</td><td><input name="cAddr" type="text" id="cAddr" size="40" value="<?php print $row["cAddr"];?>"></td>
    </tr>
    <tr>
      <td colspan="2" align="center">
      <input name="cID" type="hidden" value="<?php print $row["cID"]; ?>">
      <input name="action" type="hidden" value="update">
      <input type="submit" name="button" id="button" value="更新資料">
      <input type="reset" name="button2" id="button2" value="重新填寫">
      </td>
    </tr>
  </table>
</form>
</body>
</html>