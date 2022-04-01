<!DOCTYPE html>
<html>
<head>
    <title>HousedHealth</title>
    <link rel="stylesheet" type="text/css" href="CSS/RegisterStyle.css">
    <link rel="icon" href="https://img.icons8.com/external-kiranshastry-lineal-color-kiranshastry/64/000000/external-hospital-medical-kiranshastry-lineal-color-kiranshastry-2.png"/>
<style>
body {
 
            background: url(https://www.missouripartnership.com/wp-content/uploads/2018/01/iStock-695349930.jpg)
             no-repeat center center fixed; 
             -webkit-background-size: cover;
             -moz-background-size: cover;
             -o-background-size: cover;
             background-size: cover;">
}
</style>
</head>
<body>
     <div class="box">
    <img src="https://tse4.mm.bing.net/th?id=OIP.ikBTrFhQWWad8pSdFlRx9gHaHa&pid=Api&P=0&w=300&h=300" class="avatar">
         <h1>Login Here</h1>
         <form action="LoginCheck.php" method="POST">
             <p>Email</p>
             <input type="email" name="email" id="email" placeholder= "Enter Email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{3,}$" required>
             <p>Password</p>
             <input type="Password" name="password" id="password" placeholder="Enter Password" required>
             <input type="Submit" name="" value="Login">
         </form>
     
             <a href="index.php">
                 <input type="button" name="" value="Sign Up">
                 </a>
          </div>
</body>
</html>
