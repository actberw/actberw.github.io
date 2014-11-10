### stdin 与 STDIN_FILENO
stdin类型为 FILE*(fileno可以获得文件描述符), STDIN_FILENO类型为 int; 使用stdin的函数主要有：fread、fwrite、fclose(stdio.h)等，基本上都以f开头, 使用STDIN_FILENO的函数有：read、write、close(unistd.h)等
