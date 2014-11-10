Title: linux 信号
Tags: linux ,signal, c
Date: 2014-11-01 20:00:00

可以 `man 7 signal` 查看详细文档.  

### Signal Mask and Pending Signals  
A signal may be blocked, which means that it is queued by the kernel and delivered until it is later unblocked.Between the time when it is generated and when it is delivered a signal is said to be pending.

The SIG_SETMASK tells that the signals in set are to be blocked, and signals that are not present in the set are to be unblocked. 

### Reliable signals and Real-time signals  
Linux  supports the standard signals(Reliable signals) and so called real-time signals specified by The POSIX specification. 

real-time signals are to be used by the programmer and have no predefined meaning. Two macros are available: SIGRTMIN and SIGRTMAX that tells the range of these signals. You can use one using SIGRTMIN+n where n is some number. Never hard code their numbers, real time signals are used by threading library (both LinuxThreads and NTPL), so they adjust SIGRTMIN at run time.

Whats the difference between RT signals and standard signals? There are couple:

 - More than one RT signal can be queued for the process if it has the signal blocked while someone sends it. In standard signals only one of a given type is queued, the rest is ignored.
 - Order of delivery of RT signal is guaranteed to be the same as the sending order. PID and UID of sending process is written to si_pid and si_uid fields of siginfo_t.

### Signal Dispositions  
sigaction or signal

### Synchronously Accepting a Signal  
sigwaitinfo, sigtimedwait, and sigwait

### Signal handled in multi-thread  
UNIX allows individual threads to indicate which signals they are accepting and which they are ignoring. 

However the signal can only be delivered to one thread, which is generally the first thread that is accepting that particular signal. UNIX provides two separate system calls, kill( pid, signal ) and pthread_kill( tid, signal ), for delivering signals to processes or specific threads respectively. 

A process-directed signal may be delivered to any one of the threads that does not currently have the signal blocked. If more than one of the threads has the signal unblocked, then the kernel chooses an arbitrary thread to which to deliver the signal.

refer:

- [0][http://www.ibm.com/developerworks/cn/linux/l-cn-signalsec/](http://www.ibm.com/developerworks/cn/linux/l-cn-signalsec/)
