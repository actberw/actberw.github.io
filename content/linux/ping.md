Title: ping 
Tags: linux, ping

ping 中的ttl是返回消息中的ttl, 需要根据初始值才能判断出具体经过的路由数, 初始值linux一般是64 `net.ipv4.ip_default_ttl = 64`, 有些系统可能是128或255.
