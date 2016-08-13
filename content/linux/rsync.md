Title: rsync命令

rsync -avz --rsync-path="sudo rsync" /home/git/  howtou@182.92.103.217:/home/git/
-P same as --partial --progress

注意: 同步文件时注意目标末尾 "/" 表示目录，否则表示文件名. 同步目录时注意源目录末尾的 "/".
