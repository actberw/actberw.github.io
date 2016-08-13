Title: 碎片问题(fregmentation)
Tag: fregmentation
Date: 2016-03-14

Types of fregmentation

- Internal fragmentation
- External fragmentation
- Data fragmentation

## linux fregmentation

Linux’s ext2, ext3, and ext4 file systems – ext4 being the file system used by Ubuntu and most other current Linux distributions – allocates files in a more intelligent way. Instead of placing multiple files near each other on the hard disk, Linux file systems scatter different files all over the disk, leaving a large amount of free space between them. When a file is edited and needs to grow, there’s usually plenty of free space for the file to grow into. If fragmentation does occur, the file system will attempt to move the files around to reduce fragmentation in normal use, without the need for a defragmentation utility.

You can measure the fragmentation of a Linux file system with the `fsck` command — look for "non-contiguous" in the output.

refer:

- https://en.wikipedia.org/wiki/Fragmentation_(computing)
- https://en.wikipedia.org/wiki/File_system_fragmentation
- http://superuser.com/questions/474536/in-linux-how-do-you-check-if-a-disk-is-fragmented
