<?php
//database connection
$con=mysqli_connect('localhost','root','','proj_register');

if(!$con){
	echo "No DB connection";
}
//varibales to take input from form 
$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$email = $_POST['email'];
$password = $_POST['password'];
//selection of database where the input data will be stored
mysqli_select_db($con,'proj_register');


// Attempt insert query execution
if(isset($_POST['submit'])){

$reg= "insert into info(first_name, last_name, email, password) values ('$first_name', '$last_name', '$email', '$password')";
$result=mysqli_query($con,$reg);
include 'AfterRegister.php';
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($con);
}
 
// Close connection
mysqli_close($con);
?>