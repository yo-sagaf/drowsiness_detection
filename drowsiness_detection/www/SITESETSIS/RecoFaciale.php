<!DOCTYPE html>
<html lang="en">
<title>Home</title>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
.w3-bar,h1,button {font-family: "Montserrat", sans-serif}
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-red w3-card w3-left-align w3-large">
    <a href="#" class="w3-bar-item w3-button w3-padding-large w3-white">Bienvenue</a>
  </div>
</div>

<!-- Header -->
<header class="w3-container w3-red w3-center" style="padding:50px 16px">
  <p> <img src = "uca.jpg" alt="logo uca" style ="width:700px; height:150px"/></p>
  <h6 class="w3-margin w3-jumbo">Attendance par reconnaissance faciale</h6>
  <p class="w3-xlarge">Presenté par Sagaf et Moussab</p>
</header>

<div class="w3-row-padding w3-light-grey w3-padding-64 w3-container">
  <div class="w3-content">
    <div class="w3-twothird">
      <h1>Raspberry Pi</h1>
      <h5 class="w3-padding-32">Open CV, MySQL, Python, PHP, Computer Vision, Digital Image Processing</h5>
       <?php
          $dbhost = 'localhost';
          $dbuser = 'setsisuser';
          $dbpass = 'setsis0809';
          $dbname = 'SETSISBASE';
          $conn = mysqli_connect($dbhost, $dbuser, $dbpass,$dbname);
          
          // Check connection
          if (mysqli_connect_errno())
          {
             echo "Failed to connect to MySQL: " . mysqli_connect_error();
          }

          $sql = 'SELECT Name, Date FROM EVENTS';
          $retval = mysqli_query( $conn,$sql);
          
          if(! $retval ) {
             die('Could not get data: ' . mysqli_error());
          }

          while($row = mysqli_fetch_array($retval, MYSQLI_ASSOC)) {
             echo "Name de l'employee : {$row['Name']} <br> ".
                "Date d'arrivee : {$row['Date']} <br> ";
          }
                 
          #echo "Fetched data successfully\n";
          
          #echo '<br><button type ="button", name="delete", value="delete"> Supprimer les données </button><br>';
          
          if (isset($_GET['delete'])){
              $requete = "DELETE FROM EVENTS"; 
              mysqli_query($conn, $requete);
          }
          
          
          mysqli_close($conn);
       ?>
       <br><br>
       <form><input type ="submit", class = "button" name="delete", value="Supprimer les données"></button></form>
       
    </div>   
  </div>
</div>

<div class="w3-container w3-black w3-center w3-opacity w3-padding-64">
    <h1 class="w3-margin w3-xlarge">Projet pour le module développement terminal mobile connecté</h1>
</div>

<script>
// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}
</script>

</body>
</html>
