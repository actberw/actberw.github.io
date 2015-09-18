Title: DNS
Tags: dns, dig, nslookup
Date: 2015-01-17

DNS(domian name server) 是把域名转为ip的服务, 其zone file的条目被称为资源记录(resource record, RR), 资源记录有不同类型用于不同的目的, 常用类型有: 
- A 记录(adress record) 把主机名映射成32位ipv4地址
- AAAA 记录(quad A) 把主机名映射成128位ipv6地址
- PTR 记录(pointer record, 指针记录) 把ip地址映射成主机名, 对于ipv4地址存储得是反转顺序后添加in-addr.arpa, 例如 "220.181.57.216" 实际对应得记录是 "216.57.181.220.in-addr.arpa"
- MX 记录即邮件交换记录, 可以使ip或者域名, 有相应得优先级, 优先级的数值越低，优先级别就越高.
- CNAME 记录(Canonical Name)别名记录也被称为规范名字。这种记录允许您将多个名字映射到同一台计算机。
- NS 记录指定解析该域名的dns服务器.
- SOA Start of Authority 记录, 表明 DNS 服务器是为该domian信息的primary来源.

### TTL值

TTL值全称是“生存时间（Time To Live)”，简单的说它表示DNS记录在DNS服务器上缓存时间.

### dig/nslookup

linux下可以用dig或者nslook进行dns解析.

nslookup比较简单可以直接`nslookup baidu.com` 即可

dig 有几个常用选项:
- "@" 指定dns server 
- "-t" 指定资源记录类型, `dig -t mx gmail.com`查询gmail的mx 记录, 'any' 可以查询所有类型记录.
- "-x" 进行反向解析即(ip -> 域名, 查询得就是PTR记录). 

dig的结果分成好几部分最主要的就是"ANSWER SECTION:", 具体分析见refer[2].

### 域名解析过程

具体解析过程如下:

- A network host is configured with an initial cache (so called hints) of the known addresses of the root name servers. Such a hint file is updated periodically by an administrator from a reliable source.
- A query to one of the root servers to find the server authoritative for the top-level domain.
- A query to the obtained TLD server for the address of a DNS server authoritative for the second-level domain.
- Repetition of the previous step to process each domain name label in sequence, until the final step which returns the IP address of the host sought.

![dns-resolve-process](/img/dns-resolve-process.jpg)

`dig -t ns .` 可以获得所有的根域名服务器, `dig @8.8.8.8 +trace +additional www.baidu.com` 可以跟踪整个解析过程.

### glue records

有的时候会在上面的解析过程的第三步, dns服务器是待查询的域名的子域名, 例如: `dig -t ns baidu.com`

    baidu.com.      57714   IN  NS  ns7.baidu.com.
    baidu.com.      57714   IN  NS  ns3.baidu.com.

要解析 "baidu.com" 要去 "ns7.baidu.com" 查询, 而要解析 "ns7.baidu.com" 就必须知道"baidu.com" 的ip, 这样就形成循环依赖了, 为了打破循环依赖dns服务器(本例是tld)还必须提供类似 "ns3.baidu.com" 的ip, 这样的"ns3.baidu.com" 到 IP的记录称为glue record.

refer:

- [0][http://en.wikipedia.org/wiki/List_of_DNS_record_types](http://en.wikipedia.org/wiki/List_of_DNS_record_types)
- [1][http://faq.domainmonster.com/dns/3rd_party/](http://faq.domainmonster.com/dns/3rd_party/)
- [2][http://kb.mediatemple.net/questions/909/Understanding+the+dig+command](http://kb.mediatemple.net/questions/909/Understanding+the+dig+command)
- [3][http://blog.catchpoint.com/2014/07/01/dns-lookup-domain-name-ip-address/](http://blog.catchpoint.com/2014/07/01/dns-lookup-domain-name-ip-address/)
- [4][http://en.wikipedia.org/wiki/Domain_Name_System#Circular_dependencies_and_glue_records](http://en.wikipedia.org/wiki/Domain_Name_System#Circular_dependencies_and_glue_records)
