Title: 线程间同步
Tags: mutex, semaphore, futex

### mutex locks

从实现原理上来讲，Mutex属于sleep-waiting类型的锁。例如在一个双核的机器上有两个线程(线程A和线程B)，它们分别运行在Core0和Core1上。假设线程A想要通过pthread_mutex_lock操作去得到一个临界区的锁，而此时这个锁正被线程B所持有，那么线程A就会被阻塞(blocking)，Core0 会在此时进行上下文切换(Context Switch)将线程A置于等待队列中，此时Core0就可以运行其他的任务(例如另一个线程C)而不必进行忙等待。 mutex获取锁分为两阶段，第一阶段在用户态采用spinlock锁总线的方式获取一次锁，如果成功立即返回；否则进入第二阶段，调用系统的futex锁去sleep，当锁可用后被唤醒，继续竞争锁。

Mutex(基于futex)用pthread_mutex_t类型的变量表示，可以这样初始化和销毁：

    #include <pthread.h>

    struct pthread_mutexattr {
        int pshared;
        int kind; // LinuxThreads supports only one mutex attribute: the mutex kind
    };
    typedef struct pthread_mutexattr pthread_mutexattr_t;

    struct pthread_mutex {
        int lock;                 // Exclusive access to mutex state:
                                  //  0: unlocked/free
                                  //  1: locked - no other waiters
                                  // -1: locked - with possible other waiters

        int recursion;            // Number of unlocks a thread needs to perform
                                  // before the lock is released (recursive mutexes only)
        int kind;                 // Mutex type
        pthread_t owner;          // Thread owning the mutex
        handle_t event;           // Mutex release notification to waiting threads
    };
    typedef struct pthread_mutex pthread_mutex_t; 

    int pthread_mutex_init(pthread_mutex_t *restrict mutex,
                   const pthread_mutexattr_t *restrict attr);
    pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER; 
    int pthread_mutex_destroy(pthread_mutex_t *mutex);

pthread_mutex_init函数对Mutex做初始化，参数attr设定Mutex的属性，如果attr为NULL则表示缺省属性， 用pthread_mutex_init函数初始化的Mutex可以用pthread_mutex_destroy销毁。如果Mutex变量是静态分配的（全局变量或static变量），也可以用宏定义PTHREAD_MUTEX_INITIALIZER来初始化，相当于用pthread_mutex_init初始化并且attr参数为NULL。

    int pthread_mutex_lock(pthread_mutex_t *mutex);
    int pthread_mutex_trylock(pthread_mutex_t *mutex);
    int pthread_mutex_unlock(pthread_mutex_t *mutex);

每个Mutex有一个等待队列，一个线程要在Mutex上挂起等待，首先在把自己加入等待队列中，然后置线程状态为睡眠，然后调用调度器函数切换到别的线程。一个线程要唤醒等待队列中的其它线程，只需从等待队列中取出一项，把它的状态从睡眠改为就绪，加入就绪队列，那么下次调度器函数执行时就有可能切换到被唤醒的线程。


### semaphore

Mutex变量是非0即1的，可看作一种资源的可用数量，初始化时Mutex是1，表示有一个可用资源，加锁时获得该资源，将Mutex减到0，表示不再有可用资源，解锁时释放该资源，将Mutex重新加到1，表示又有了一个可用资源。

信号量（Semaphore）和Mutex类似，表示可用资源的数量，和Mutex不同的是这个数量可以大于1。

POSIX semaphore相关函数详见sem_overview(7)，这种信号量不仅可用于同一进程的线程间同步，也可用于不同进程间的同步。

    #include <semaphore.h>

    int sem_init(sem_t *sem, int pshared, unsigned int value);
    int sem_destroy(sem_t * sem);
    int sem_wait(sem_t *sem);
    int sem_trywait(sem_t *sem);
    int sem_post(sem_t * sem);

semaphore变量的类型为sem_t，sem_init()初始化一个semaphore变量，value参数表示可用资源的数量，pshared参数为0表示信号量用于同一进程的线程间同步，非0表示进程间同步. 在用完semaphore变量之后应该调用sem_destroy()释放与semaphore相关的资源。

调用sem_wait()可以获得资源，使semaphore的值减1，如果调用sem_wait()时semaphore的值已经是0，则挂起等待。如果不希望挂起等待，可以调用sem_trywait()。调用sem_post()可以释放资源，使semaphore的值加1，同时唤醒挂起等待的线程。


### condition variables
Condition Variable用pthread_cond_t类型的变量表示，可以这样初始化和销毁:

    #include <pthread.h>

    struct pthread_condattr {
        int pshared;
    };
    typedef struct pthread_condattr pthread_condattr_t;

    struct pthread_cond {
        int waiting;
        handle_t semaphore;
    };
    typedef struct pthread_cond pthread_cond_t;

    int pthread_cond_destroy(pthread_cond_t *cond);
    int pthread_cond_init(pthread_cond_t *restrict cond,
                   const pthread_condattr_t *restrict attr);
    pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

和Mutex的初始化和销毁类似，pthread_cond_init函数初始化一个Condition Variable，attr参数为NULL则表示缺省属性，pthread_cond_destroy函数销毁一个Condition Variable。如果Condition Variable是静态分配的，也可以用宏定义PTHEAD_COND_INITIALIZER初始化，相当于用pthread_cond_init函数初始化并且attr参数为NULL。Condition Variable的操作可以用下列函数：

    int pthread_cond_timedwait(pthread_cond_t *restrict cond,
                   pthread_mutex_t *restrict mutex,
                   const struct timespec *restrict abstime);
    int pthread_cond_wait(pthread_cond_t *restrict cond,
                   pthread_mutex_t *restrict mutex);
    int pthread_cond_broadcast(pthread_cond_t *cond);
    int pthread_cond_signal(pthread_cond_t *cond);


Condition Variable总是和一个Mutex搭配使用的。一个线程可以调用pthread_cond_wait在一个Condition Variable上阻塞等待，这个函数做以下三步操作：

- 释放Mutex
- 阻塞等待
- 当被唤醒时，重新获得Mutex并返回

一个线程可以调用pthread_cond_signal唤醒在某个Condition Variable上等待的另一个线程，也可以调用pthread_cond_broadcast唤醒在这个Condition Variable上等待的所有线程。

### read-write locks

### spinlocks

Spin lock属于busy-waiting类型的锁，如果线程A是使用pthread_spin_lock操作去请求锁，那么线程A就会一直在 Core0上进行忙等待并不停的进行锁请求，直到得到这个锁为止。

Spin Lock锁操作相关的API主要有：

    int   pthread_spin_destroy(pthread_spinlock_t *);
    int   pthread_spin_init(pthread_spinlock_t *, int);
    pthread_spin_lock (pthread_spinlock_t *lock);
    pthread_spin_trylock (pthread_spinlock_t *lock);
    pthread_spin_unlock (pthread_spinlock_t *lock);


spinlock在多处理器多线程环境的场景中有很广泛的使用，一般要求使用spinlock的临界区尽量简短，这样获取的锁可以尽快释放，以满足其他忙等的线程。Spinlock和mutex不同，spinlock不会导致线程的状态切换(用户态->内核态)，但是spinlock使用不当(如临界区执行时间过长)会导致cpu busy飙高。

对比mutex:

- Spinlock优点：没有昂贵的系统调用，一直处于用户态，执行速度快 , 缺点：一直占用cpu，而且在执行过程中还会锁bus总线，锁总线时其他处理器不能使用总线

- Mutex优点：不会忙等，得不到锁会sleep, Mutex缺点：sleep时会陷入到内核态，需要昂贵的系统调用

refer:

- [http://akaedu.github.io/book/ch35s03.html](http://akaedu.github.io/book/ch35s03.html)
- [http://www.parallellabs.com/2010/01/31/pthreads-programming-spin-lock-vs-mutex-performance-analysis/](http://www.parallellabs.com/2010/01/31/pthreads-programming-spin-lock-vs-mutex-performance-analysis/)
- [http://www.searchtb.com/2011/01/pthreads-mutex-vs-pthread-spinlock.html](http://www.searchtb.com/2011/01/pthreads-mutex-vs-pthread-spinlock.html)
- [http://www.searchtb.com/2011/06/spinlock%E5%89%96%E6%9E%90%E4%B8%8E%E6%94%B9%E8%BF%9B.html](http://www.searchtb.com/2011/06/spinlock%E5%89%96%E6%9E%90%E4%B8%8E%E6%94%B9%E8%BF%9B.html)
