Title: tcpdump
Tags: linux, tcpdump 
Date: 2015-01-21 14:00:00

### 常用选项

-i 指定interface

-n Don't convert addresses (i.e., host addresses, port numbers, etc.) to names.

-X 协议头和包内容都原原本本的显示出来（tcpdump会以16进制和ASCII的形式显示），这在进行协议分析时是绝对的利器。 

-x 跟-X区别是不显示ASCII 

-c 指定抓去的包数量

-l 输出变为行缓冲

-t 输出不打印时间戳

-v 更详细的信息

-w 把抓到的网络包能存储到磁盘上

-r 读取"-w"的输出

### 过滤表达式 

有三类限定词:

- type, 如: host, net, port
- dir(direction), 如: src, dst
- proto, 如: tcp, udp, icmp, ip, arp

也可以用: Negation (`!' or `not').  Concatenation (`&&' or `and').  Alternation (`||' or `or') 组合过滤条件"tcpdump -ltnvvvx  'port 80 and host 220.181.57.217'", 更多过滤规则参见 `man pcap-filter`.


refer:

- [http://roclinux.cn/?p=2851](http://roclinux.cn/?p=2851)
