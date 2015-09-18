Title: ssh 安全

密码破解和ip屏蔽

@sdjkx: 可以公网访问的服务器，ssh一定要好好配置一下，常见的方法：
1. 改端口
2. 强密码
3. root不允许登录
4. 使用密钥登录
5. fail2ban or denyhost自动屏蔽暴力破解IP 

不一定全部使用，两三种方式结合就可以有效防止

1. http://linuxtoy.org/archives/fail2ban.html
2. http://hi.baidu.com/p3rlish/item/774b9169121adc177ddecce0
3. http://www.linuxfly.org/post/611/
4. http://my.oschina.net/guyson/blog/124312

http://www.tecmint.com/5-best-practices-to-secure-and-protect-ssh-server/
http://serverfault.com/questions/128962/denyhosts-vs-fail2ban-vs-iptables-best-way-to-prevent-brute-force-logons

