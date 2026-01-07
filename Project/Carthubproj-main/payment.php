<?php /* Static UI only — no filter logic */ ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>CartHub | Invoice List</title>

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=Playfair+Display:wght@600;700&family=Pacifico&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="payment.css"/>
</head>
<body>
  <!-- Top bar -->
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
    <h1 class="title">Invoice List</h1>

    <!-- Grey “filter” pills (purely visual; not functional) -->
    <form class="filters" method="get">
      <input class="pill" type="text" name="bill_no"   placeholder="Bill No." value="<?= htmlspecialchars($filters['bill_no']) ?>">
      <input class="pill" type="text" name="card_id"   placeholder="Card ID"  value="<?= htmlspecialchars($filters['card_id']) ?>">
      <input class="pill" type="text" name="name"      placeholder="Name"     value="<?= htmlspecialchars($filters['name']) ?>">
      <input class="pill" type="text" name="bill_date" placeholder="Bill Date" value="<?= htmlspecialchars($filters['bill_date']) ?>">
      <input class="pill" type="text" name="amount"    placeholder="Amount"   value="<?= htmlspecialchars($filters['amount']) ?>">
      <input class="pill" type="text" name="status"    placeholder="Status"   value="<?= htmlspecialchars($filters['status']) ?>">
    </form>

    <div class="table-wrap">
      <!-- thin divider like screenshot -->
      <div class="divider"></div>

      <table class="invoice-table">
        <tbody>
          <tr>
            <td class="bill">0000000013</td>
            <td>6546464645</td>
            <td>Jones Doe</td>
            <td>10/10/2025</td>
            <td>50.00</td>
            <td class="status-cell"><span class="pending">Pending</span></td>
          </tr>
          <tr>
            <td class="bill">0000000014</td>
            <td>3564536435</td>
            <td>Indie Langley</td>
            <td>12/10/2025</td>
            <td>100.00</td>
            <td class="status-cell"><span class="pending">Pending</span></td>
          </tr>
          <tr>
            <td class="bill">0000000015</td>
            <td>2351534543</td>
            <td>Alma Winterbottom</td>
            <td>12/10/2025</td>
            <td>100.00</td>
            <td class="status-cell"><span class="paid">Paid</span></td>
          </tr>
          <tr>
            <td class="bill">0000000016</td>
            <td>8678576554</td>
            <td>Lila Alfson</td>
            <td>14/10/2025</td>
            <td>50.00</td>
            <td class="status-cell"><span class="paid">Paid</span></td>
          </tr>
          <tr>
            <td class="bill">0000000017</td>
            <td>6457474743</td>
            <td>Colette Beech</td>
            <td>16/10/2025</td>
            <td>150.00</td>
            <td class="status-cell"><span class="pending">Pending</span></td>
          </tr>
          <tr>
            <td class="bill">0000000018</td>
            <td>3643643664</td>
            <td>Carlton Cory</td>
            <td>17/10/2025</td>
            <td>150.00</td>
            <td class="status-cell"><span class="paid">Paid</span></td>
          </tr>
          <tr>
            <td class="bill">0000000019</td>
            <td>3634543523</td>
            <td>Jessy Case</td>
            <td>21/10/2025</td>
            <td>50.00</td>
            <td class="status-cell"><span class="paid">Paid</span></td>
          </tr>
          <tr>
            <td class="bill">0000000020</td>
            <td>5245245242</td>
            <td>Johnathan Tracey</td>
            <td>02/11/2025</td>
            <td>100.00</td>
            <td class="status-cell"><span class="pending">Pending</span></td>
          </tr>
          <tr>
            <td class="bill">0000000021</td>
            <td>5473689789</td>
            <td>Lynnette Austin</td>
            <td>05/11/2025</td>
            <td>50.00</td>
            <td class="status-cell"><span class="pending">Pending</span></td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- <div class="pager">‹ 1 2 3 … 10 ›</div> -->
    <div class="pager">
      <a href="?page=1">‹</a>
      <a href="?page=1">1</a>
      <a href="?page=2">2</a>
      <a href="?page=3">3</a>
      . . .
      <a href="?page=10">10</a>
      <a href="?page=10">›</a>
    </div>

  </main>
</body>
</html>
