<?php
session_start();

$conn = mysqli_connect(
  'db',
  'root',
  'password',
  'php_mysql_crud'
) or die(mysqli_error($mysqli));

?>
