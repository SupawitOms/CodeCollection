<?php
// UserList.php — Collects resident info
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CartHub | User List</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Playfair+Display:wght@600;700&family=Pacifico&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="UserList.css">
</head>
<body>
  <header class="navbar">
    <div class="left-nav">
      <div class="logo">
        <div class="logo-script">Cart<span>Hub</span></div>
        <div class="logo-tag">SCAN USE RETURN</div>
      </div>
      <nav class="main-nav">
        <a href="#">Home</a>
        <a href="#">Status</a>
        <a href="#">Payment</a>
        <a class="active" href="#">User List</a>
      </nav>
    </div>
    <div class="profile-icon">
      <img src="https://cdn-icons-png.flaticon.com/512/4140/4140037.png" alt="Profile">
    </div>
  </header>

  <main class="scene">
    <h1 class="title">User List</h1>

    <div class="table-wrap">
      <table class="user-table">
        <thead>
          <tr>
            <th>User ID</th>
            <th>Card ID</th>
            <th>Username</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Gender</th>
            <th>Room</th>
            <th>Building</th>
            <th>Actions</th>
          </tr>
        </thead>
        
        <tbody>
          <!-- Example rows with data -->
          <tr>
            <td>63754667587</td>
            <td>6546464645</td>
            <td>Jones1234</td>
            <td>Jone Does</td>
            <td>Jones.Doe@gmail.com</td>
            <td>0000000000</td>
            <td>Male</td>
            <td>453</td>
            <td>D</td>
            <td class="actions">
              <button class="update-btn">Update</button>
              <button class="delete-btn">Delete</button>
            </td>
          </tr>
          <tr>
            <td>7435838453</td>
            <td>3564536435</td>
            <td>Indiezaza</td>
            <td>Indie Langley</td>
            <td>Indie.Langley@gmail.com</td>
            <td>0000000000</td>
            <td>Female</td>
            <td>376</td>
            <td>C</td>
            <td class="actions">
              <button class="update-btn">Update</button>
              <button class="delete-btn">Delete</button>
            </td>
          </tr>
          <!-- Repeat similar rows for all users -->
        </tbody>
      </table>
    </div>

    <!-- Pagination -->
    <div class="pager">
      <a href="#">‹</a>
      <a href="#">1</a>
      <a href="#">2</a>
      <a href="#">3</a>
      <a href="#">10</a>
      <a href="#">›</a>
    </div>
  </main>
</body>
</html>
