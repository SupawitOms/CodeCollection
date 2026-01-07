<?php
// signup.php — The sign-up page for users
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CartHub | Sign Up</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Pacifico&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="signup.css">
</head>
<body>
  <header class="navbar">
    <div class="left-nav">
      <div class="logo">
        <div class="logo-script">Cart<span>Hub</span></div>
        <div class="logo-tag">SCAN USE RETURN</div>
      </div>
    </div>
  </header>

  <main class="scene">
    <h1 class="title">Sign up</h1>
    <form class="signup-form" method="post">
      <input class="pill" type="text" name="username" placeholder="Username" required>
      <input class="pill" type="password" name="password" placeholder="Password" required>
      <input class="pill" type="password" name="confirm_password" placeholder="Confirm Password" required>
      <input class="pill" type="email" name="email" placeholder="Email" required>
      
      <div class="gender">
        <label>Gender : </label>

        <input type="radio" id="male" name="gender" value="Male">
        <label for="male">Male</label>
        
        <input type="radio" id="female" name="gender" value="Female">
        <label for="female">Female</label>
        
        <input type="radio" id="hidden" name="gender" value="Hidden">
        <label for="hidden">Hidden</label>
        </div>

      <input class="pill" type="text" name="phone" placeholder="Phone" required>
      <input class="pill" type="date" name="dob" placeholder="Date of birth" required>
      
      <button type="submit" class="signup-btn">Sign up</button>
    </form>
  </main>
</body>
</html>
