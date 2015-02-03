shutdown, halt, reboot, poweroff

shutdown  does its job by signalling the init process, asking it to change the runlevel.

halt notes that the system is being brought down in the file /var/log/wtmp. If halt or reboot is called when the system is not in runlevel 0 or 6, in other words when  it's  running  normally, shutdown will be invoked instead


refer:

- [http://unix.stackexchange.com/questions/42572/is-halt-the-same-as-shutdown-h-and-poweroff-the-same-as-shutdown-p](http://unix.stackexchange.com/questions/42572/is-halt-the-same-as-shutdown-h-and-poweroff-the-same-as-shutdown-p)
