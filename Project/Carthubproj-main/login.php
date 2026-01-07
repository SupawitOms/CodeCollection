<?php
// login.php
// Simple static login page UI (no authentication logic).
// Replace action target with your handler if needed.
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CartHub — Login</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600&family=Pacifico&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="login.css" />
  <link rel="icon" href="data:,">
</head>
<body>

  <main class="wrap">
    <section class="card">
      <div class="logo">
        <!-- Logo crafted to match screenshot -->
        <div class="logo-script">Cart<span>Hub</span></div>
        <div class="logo-tag">SCAN&nbsp;&nbsp;USE&nbsp;&nbsp;RETURN</div>
      </div>

      <h2 class="title">Login</h2>

      <form class="form" method="post" action="#">
        <label class="label" for="email">Email</label>
        <input class="input" id="email" name="email" type="email" placeholder="Email" required />

        <label class="label" for="password">Password</label>
        <input class="input" id="password" name="password" type="password" placeholder="Password" required />

        <button class="btn" type="submit">Sign In</button>

        <p class="helper">
          <a href="#" class="link">Forgot password?</a>
        </p>
      </form>
    </section>
  </main>
</body>
</html>
