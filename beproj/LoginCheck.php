<?php

//database connection
$con=mysqli_connect('localhost','root','','proj_register');
$db=mysqli_select_db($con,"proj_register");

session_start();

//varibales to take input from form 
$mail = $_POST['email'];
$pass = $_POST['password'];

//to prevent from mysqli injection
$mail=stripcslashes($mail);
$pass=stripcslashes($pass);
$mail=mysqli_real_escape_string($con,$mail);
$pass=mysqli_real_escape_string($con,$pass);

$sql="select *from info where email='$mail' and password='$pass'";
$result=mysqli_query($con,$sql);
$row=mysqli_fetch_array($result, MYSQLI_ASSOC);
$count=mysqli_num_rows($result);

if($count==1){
    $_SESSION['email_var']=$mail;
    include 'Homepage.php';
}
else{
    echo "<h1><center> Login failed. Invalid username or password.</center></h1>";
}
?>
