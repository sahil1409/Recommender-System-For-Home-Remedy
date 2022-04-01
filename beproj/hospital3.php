<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>BingeFlix</title>
    <link rel="stylesheet" href="CSS/MiniProjectStyle.css">
    <link rel="icon" href="https://img.icons8.com/wired/64/000000/tv-show.png"/>
    <script src="https://kit.fontawesome.com/409e648f2a.js"></script>
    <style type="text/css">
        
                .Title{
              overflow: hidden; /* Ensures the content is not revealed until the animation */
              border-right: .15em solid orange; /* The typwriter cursor */
              white-space: nowrap; /* Keeps the content on a single line */
              margin: 0 auto; /* Gives that scrolling effect as the typing happens */
              letter-spacing: .15em; /* Adjust as needed */
              animation: 
                typing 10s steps(40, end),
                blink-caret .75s step-end infinite;
        }
        /* The typing effect */
        @keyframes typing {
          from { width: 0 }
          to { width: 100% }
        }

        /* The typewriter cursor effect */
        @keyframes blink-caret {
          from, to { border-color: transparent }
          50% { border-color: transparent; }
        }
        
        .Container{
        position: relative;
        width: 100%;
        height: 375px;
      
        margin: 0 auto;
        background-size: 100%;
        background-position: center;
        transition: 0.5s;
    }
    </style>
</head>
<body style="background-color: #000000;
background-image: linear-gradient(147deg, #000000 0%, #04619f 74%);">
       
    <h1 class="Title" style="text-shadow: 2px 2px 30px black; text-align: center; color: #82CAFF; font-size: 3em;">Fortis Hospital</h1><br>
    
    <div class="Container">
        <i class="fas fa-map-marked-alt" style="font-size:100px;color:#82CAFF; padding-left: 45%"></i><br><br>

        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d120600.5018033867!2d72.87186985820315!3d19.161731500000005!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b85e410ad361%3A0x6ca97bfe9216e096!2sFortis%20Hospital%20Mulund%2C%20Mumbai!5e0!3m2!1sen!2sin!4v1646363696887!5m2!1sen!2sin" width="100%" height="470px" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
    </div>
    
</body>
</html> 