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
         //"Confiance de reconnaissance : {$row['Confiance']} <br> ";
   }

   echo "Fetched data successfully\n";
   mysqli_close($conn);
?>
