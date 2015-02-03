Title: traceroute
Tags: linux, traceroute, ping
Date: 2015-01-21 13:00:00

### 实现原理

- 从SRC发出一个探测包到DST，并将TTL设置为1；
- 每一跳TTL将会减一；
- 当TTL变为0时，包被丢弃，路由器向SRC发回一个 "ICMP TTL Exceed response" 包
- 当SRC收到该ICMP包时，显示这一跳信息；
- 重复1～5，并每次TTL加1；
- 直至DST收到探测数据包，并返回ICMP Dest Unreachable包；
- 当SRC收到ICMP Dest Unreachable包时停止traceroute


traceroute可以用UDP, TCP, ICMP发送probes请求默认使UDP(返回的一定是icmp协议), 可以使用下面两个选项, 指定协议.

    -I     Use ICMP ECHO for probes
    -T     Use TCP SYN for probes

显示的时间是rtt(round trip time)

refer:

- [http://www.slashroot.in/how-does-traceroute-work-and-examples-using-traceroute-command](http://www.slashroot.in/how-does-traceroute-work-and-examples-using-traceroute-command)
- [http://blog.yunn.io/archives/499/](http://blog.yunn.io/archives/499/)
- [http://blog.yunn.io/archives/508/](http://blog.yunn.io/archives/508/)

