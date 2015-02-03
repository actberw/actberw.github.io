das, san, nas

- A block device is a handle to the raw disk.  Such as /dev/sda for a disk or /dev/sda1 for a partition on that disk. place a filesystem upon it before it can be used
- A filesystem is layered on top of the block device in order to store data. You can then mount this.  Such as mount /dev/sda1 /mnt/somepath. ready to mount and use

DAS is a block device from a disk which is physically [directly] attached to the host machine.
SAN is a block device which is delivered over the network.

NAS is a filesystem delivered over the network.


refer:

- [http://zh.wikipedia.org/wiki/%E5%AD%98%E5%82%A8%E5%8C%BA%E5%9F%9F%E7%BD%91%E7%BB%9C](http://zh.wikipedia.org/wiki/%E5%AD%98%E5%82%A8%E5%8C%BA%E5%9F%9F%E7%BD%91%E7%BB%9C)
