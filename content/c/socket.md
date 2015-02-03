Title: linux socket编程
Tags: c, socket
Date: 2015-01-16

### 字节序转换

有关字节序问题参见 [大端和小端](/posts/c/endian.html)

"arpa/inet.h" 中定义了, 四个相关的字节序转换函数.

       uint32_t htonl(uint32_t hostlong);

       uint16_t htons(uint16_t hostshort);

       uint32_t ntohl(uint32_t netlong);

       uint16_t ntohs(uint16_t netshort);

其中: n 代表network, h 代表host, s代表short, l代表long.

另外还有两个ip 相关的转换函数.

    int inet_pton(int af, const char *src, void *dst);
    const char *inet_ntop(int af, const void *src,
                                 char *dst, socklen_t size);

用于ip地址在点分十进制和二进制之间转换, p 代表presentation, n 代表 numeric, inet_pton 转换后的结果是网络字节序.


### DNS 解析

getaddrinfo/getnameinfo 进行DNS解析.

    char buf[INET_ADDRSTRLEN];
    struct addrinfo *ai;
    struct sockaddr_in *ac_addr;
    getaddrinfo("baidu.com", NULL, NULL, &ai);
    ac_addr = (struct sockaddr_in*)(ai->ai_addr);
    memset(buf, 0, INET_ADDRSTRLEN);
    inet_ntop(ac_addr->sin_family, &(ac_addr->sin_addr), buf, INET_ADDRSTRLEN); // ipv6: INET6_ADDRSTRLEN
    printf("%s\n", buf);
    return 0;

### 相关结构体

struct sockaddr_in struct sockaddr_in6 struct sockaddr_storage struct sockaddr

### 相关api

![socket program](/img/socket-program.png)

socket bind listen accept connect

INADDR_ANY netinet/in.h arpa/inet.h

read/write readv/writev send/recv  sendto/recvfrom sendmsg/recvmsg

close/shutdown

close使描述符引用数减1并立即返回(可以通过下面介绍的SO_LINER选项控制), shutdown 可以控制关闭方式: SHUT_RD, SHUT_WR, SHUT_RDWR

getsockname/getpeername

The backlog argument defines the maximum length to which the queue of pending connections for sockfd may  grow.

The behavior of the backlog argument on TCP sockets changed with Linux 2.2.  Now it specifies the queue  length for completely established sockets waiting to be accepted, instead of the number of incomplete connection requests. The maximum length of the queue for incomplete sockets can be set using /proc/sys/net/ipv4/tcp_max_syn_backlog(sysctl net.ipv4.tcp_max_syn_backlog). If the backlog argument is greater than the value in "/proc/sys/net/core/somaxconn", then it is  silently trun‐cated to that value; the default value in this file is 128.


### 套接字选项

getsockopt/setsockopt 

可以设置或获取如下级别(level)的选项:

- SOL_SOCKET socket 级别, 常用的有SO_REUSEADDR, SO_LINER, SO_KEEPALIVE 
- IPPROTO_TCP tcp 级别, 只有两个选项: TCP_MAXSEG 控制mss(max segment size)大小, TCP_NODELAY 控制negle算法.
- IPPROTO_IP/IPPROTO_IP6 ipv4/ipv6 级别

fcntl

O_NONBLOCK, FD_CLOEXEC

refer:

http://stackoverflow.com/questions/21099041/why-do-we-cast-sockaddr-in-to-sockaddr-when-calling-bind
http://veithen.github.io/2014/01/01/how-tcp-backlog-works-in-linux.html
http://long.ccaba.upc.es/long/045Guidelines/eva/ipv6.html
http://www.beej.us/guide/bgnet/output/html/multipage/sockaddr_inman.html
http://www.yeolar.com/note/2012/05/18/linux-socket/
