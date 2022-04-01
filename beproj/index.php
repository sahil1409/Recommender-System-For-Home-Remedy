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
     <div class="box" style="height: 650px; width:350px">
    <img src="https://tse4.mm.bing.net/th?id=OIP.ikBTrFhQWWad8pSdFlRx9gHaHa&pid=Api&P=0&w=300&h=300" class="avatar" >
         <h1>Register Here</h1>
         <form action="Entry.php" method="POST">
             <p>First Name<p>
             <input type="text" name="first_name" id="first_name" placeholder= "Enter First Name" pattern="[A-Za-z]{3,}" required>
             <p>Last Name</p>
             <input type="text" name="last_name" id="last_name" placeholder="Enter Last Name" pattern="[A-Za-z]{3,}" required>
             <p>Email</p>
             <input type="email" name="email" id="email" placeholder="Enter Email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{3,}$" required>
              <p>Password</p>
             <input type="password" name="password" id="password" placeholder="Enter Password" onkeyup="CheckPasswordStrength(this.value)" pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$" required oninvalid="this.setCustomValidity('Please use atleast 6 characters including Uppercase, Lowercase, Number, Special Character')"
      onchange="try{setCustomValidity('')}catch(e){}"
      oninput="setCustomValidity(' ')" /><br><br>
             <progress id="strength" value="0" max="100"></progress><br><br>
             <span>Strength of password : </span>
             <span id="strength_type"></span><br>

             <script type="text/javascript">
                function CheckPasswordStrength(password) {
                    //TextBox left blank.
                    if (password.length == 0) {
                        password_strength.innerHTML = "";
                        return;
                    }

                    //Regular Expressions.
                    var regex = new Array();
                    regex.push("[A-Z]"); //Uppercase Alphabet.
                    regex.push("[a-z]"); //Lowercase Alphabet.
                    regex.push("[0-9]"); //Digit.
                    regex.push("[$@$!%*#?&]"); //Special Character.

                    var passed = 0;

                    //Validate for each Regular Expression.
                    for (var i = 0; i < regex.length; i++) {
                        if (new RegExp(regex[i]).test(password)) {
                            passed++;
                        }
                    }

                    //Validate for length of Password.
                    if (passed > 2 && password.length > 5) {
                        passed++;
                    }
                    //Display status.
                    var strength = "";
                    switch (passed) {
                        case 0:
                        case 1:
                            strength = "25";
                            strength_type = "Weak (25%)";
                            break;
                        case 2:
                            strength = "50";
                            strength_type = "Average (50%)";
                            break;
                        case 3:
                        case 4:
                            strength = "75";
                            strength_type = "Good (75%)";
                            break;
                        case 5:
                            strength = "100";
                            strength_type = "Strong (100%)";
                            break;
                    }
                    document.getElementById("strength").value = strength;
                    document.getElementById("strength_type").innerHTML = strength_type;
                }
             </script><br>
             <input type="Submit" name="submit" value="Register">
         </form>
         <a href="Login.php">
             <input type="Button" name="" value="Login">
             </a>

    </div>

</body>
</html>