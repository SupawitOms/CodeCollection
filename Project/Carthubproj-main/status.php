<?php

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CartHub | Cart Status</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&family=Playfair+Display:wght@600;700&family=Pacifico&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="status.css">
</head>
<body>
  <header class="navbar">
    <div class="left-nav">
      <div class="logo">
        <div class="logo-script">Cart<span>Hub</span></div>
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

  <main class="scene">
    <h1 class="title">Cart Status</h1>

    <div class="table-wrap">
      <table class="status-table">
        <thead>
          <tr>
            <th>Cart</th>
            <th>Building</th>
            <th>Status</th>
            <th>Card ID</th>
            <th>Name</th>
            <th>Room</th>
            <th>CheckoutTime</th>
            <th class="edit-col"></th>
          </tr>
        </thead>
      </table>

      <div class="header-divider"></div>

      <table class="status-table body">
        <tbody>
          <tr>
            <td>A1</td>
            <td>A</td>
            <td><span class="dot red"></span> <strong>In Use</strong></td>
            <td>6546464645</td>
            <td>Jones Doe</td>
            <td>104</td>
            <td>12 : 07</td>
            <td class="actions">
              <button class="edit-btn" aria-label="edit">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                  <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
                </svg>
              </button>
            </td>
          </tr>

          <tr>
            <td>A2</td>
            <td>A</td>
            <td><span class="dot green"></span> <strong>Available</strong></td>
            <td></td><td></td><td></td><td></td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>B1</td>
            <td>B</td>
            <td><span class="dot green"></span> <strong>Available</strong></td>
            <td></td><td></td><td></td><td></td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>B2</td>
            <td>B</td>
            <td><span class="dot red"></span> <strong>In Use</strong></td>
            <td>3564536435</td>
            <td>Indie Langley</td>
            <td>213</td>
            <td>09 : 43</td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>C1</td>
            <td>C</td>
            <td><span class="dot red"></span> <strong>In Use</strong></td>
            <td>2351534543</td>
            <td>Alma Winterbottom</td>
            <td>342</td>
            <td>14 : 31</td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>C2</td>
            <td>C</td>
            <td><span class="dot green"></span> <strong>Available</strong></td>
            <td></td><td></td><td></td><td></td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>D1</td>
            <td>D</td>
            <td><span class="dot red"></span> <strong>In Use</strong></td>
            <td>5245245242</td>
            <td>Johnathan Tracey</td>
            <td>487</td>
            <td>18 : 54</td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>D2</td>
            <td>D</td>
            <td><span class="dot green"></span> <strong>Available</strong></td>
            <td></td><td></td><td></td><td></td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>E1</td>
            <td>E</td>
            <td><span class="dot green"></span> <strong>Available</strong></td>
            <td></td><td></td><td></td><td></td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>

          <tr>
            <td>E2</td>
            <td>E</td>
            <td><span class="dot green"></span> <strong>Available</strong></td>
            <td></td><td></td><td></td><td></td>
            <td class="actions"><button class="edit-btn" aria-label="edit">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25Z"/>
                <path d="M14.06 4.19l3.75 3.75" fill="none" stroke="#666" stroke-width="1.2"/>
              </svg>
            </button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</body>
</html>
