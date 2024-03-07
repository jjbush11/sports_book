<!-- Connecting -->
<?php
$databaseName = 'JJBUSH_labs';
$dsn = 'mysql:host=webdb.uvm.edu;dbname=' . $databaseName;
$username = 'jjbush_writer';
$password = '5KTfOdryzPTS';
$pdo = new PDO($dsn, $username, $password);

?>
<!-- Connection complete  -->