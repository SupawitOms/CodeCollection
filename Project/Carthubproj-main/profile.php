<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CartHub | Profile</title>
  <link rel="stylesheet" href="profile.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Playfair+Display:wght@600;700&family=Pacifico&display=swap" rel="stylesheet">
</head>
  <body>
    <header class="navbar">
      <div class="left-nav">
        <div class="logo">
          <span class="logo-script">Cart<span>Hub</span></span>
          <div class="logo-tag">SCAN USE RETURN</div>
        </div>
        <nav>
          <a href="#">Home</a>
          <a href="#">Status</a>
          <a href="#">Payment</a>
        </nav>
      </div>

      <div class="profile-icon">
        <img src="https://cdn-icons-png.flaticon.com/512/4140/4140037.png" alt="Profile">
      </div>
    </header>


    <main class="container">
      <div class="profile-card">
        <div class="avatar">
          <div class="avatar-content">
            <img id="profilePic"
                src="https://cdn-icons-png.flaticon.com/512/4140/4140037.png"
                alt="User Avatar" />
            <label for="fileUpload" class="change-img">Change Image</label>
            <input type="file" id="fileUpload" accept="image/*"
                  style="display:none" onchange="previewImage(event)">
          </div>
        </div>



        <form class="profile-form" method="post" action="#">
          <label>Username</label>
          <input type="text" name="username" placeholder="Alexander Uhaha">

          <label>Password</label>
          <input type="password" name="password" placeholder="********">

          <label>Email</label>
          <input type="email" name="email" placeholder="alexander.official@gmail.com">

          <label>Phone</label>
          <input type="text" name="phone" placeholder="0635909868">

          <label>Gender</label>
          <div class="gender">
            <label><input type="radio" name="gender" checked> Male</label>
            <label><input type="radio" name="gender"> Female</label>
            <label><input type="radio" name="gender"> Hidden</label>
          </div>

          <label>Date of Birth</label>
          <input type="text" name="dob" placeholder="23 / 11 / 1987">

          <button type="submit" class="update-btn">UPDATE</button>
        </form>
      </div>
    </main>
      <script>
        function previewImage(event) {
          const reader = new FileReader();
          reader.onload = function(){
            const output = document.getElementById('profilePic');
            output.src = reader.result;
          };
          reader.readAsDataURL(event.target.files[0]);
        }
        </script>
  </body>
</html>
