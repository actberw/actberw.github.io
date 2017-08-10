Title: 独立的debuginfo文件
Date: 2017-08-10

GDB supports two ways of specifying the separate debug info file:

- The executable contains a debug link that specifies the name of the separate debug info file. The separate debug file’s name is usually executable.debug, where executable is the name of the corresponding executable file without leading directories (e.g., ls.debug for /usr/bin/ls). In addition, the debug link specifies a 32-bit Cyclic Redundancy Check (CRC) checksum for the debug file, which GDB uses to validate that the executable and the debug file came from the same build.
- The executable contains a build ID, a unique bit string that is also present in the corresponding debug info file. (This is supported only on some operating systems, when using the ELF or PE file formats for binary files and the GNU Binutils.) For more details about this feature, see the description of the --build-id command-line option in Command Line Options in The GNU Linker. The debug info file’s name is not specified explicitly by the build ID, but can be computed from the build ID, see below.

objcopy --only-keep-debug main main.debug
objcopy --strip-debug main // strip --strip-debug --strip-unneeded main
objcopy --add-gnu-debuglink main.debug main // .gnu_debuglink
objdump -s -j .gnu_debuglink libtest.so

gdb -s main.debug -e main

-Wl,--build-id .note.gnu.build-id
file <prog> 获得buildid

refer:

- https://sourceware.org/gdb/onlinedocs/gdb/Separate-Debug-Files.html
- https://www.technovelty.org/code/separate-debug-info.html
- http://www.lenky.info/archives/2013/04/2261
