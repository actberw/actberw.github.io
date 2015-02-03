VIRT(vsz), RES(RSS), SHR, SWAP
free
ps, top, pmap
cat /proc/{pid}/status
cat /proc/meminfo

The virtual memory size reported by Linux includes all the code, data and stack space reserved for use by a process, on both physical memory and swap space

Because this post is quite long, here is a short summary:

- top‘s man page cannot be trusted.
- top‘s RES gives you the actual physical RAM used by your process.
- top‘s VIRT gives you the actual virtual memory reserved by your process.
- top‘s DATA gives you the amount of virtual private anonymous memory reserved by your process. That memory may or may not be mapped to physical RAM. It corresponds to the amount of memory intended to store process specific data (not shared).
- top‘s SHR gives you the subset of resident memory that is file-backed (including shared anonymous memory). It represents the amount of resident memory that may be used by other processes.
- top‘s SWAP column can only be trusted with recent versions of top (3.3.0) and Linux (2.6.34) and is meaningless in all other cases.
- if you want details about the memory usage of your process, use pmap.

http://www.ehow.com/about_5497321_much-linux-memory-used-process.html
http://elinux.org/Runtime_Memory_Measurement
https://techtalk.intersec.com/2013/07/memory-part-2-understanding-process-memory/
