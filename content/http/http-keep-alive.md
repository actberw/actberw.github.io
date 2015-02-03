Title: http keep-alive
Tags: http, keep-alive
Date: 2014-10-18 23:00:00

HTTP协议采用“请求-应答”模式，http 1.0每个请求/应答客户和服务器都要新建一个连接，完成 之后立即断开连接, http 1.1 新增了Keep-Alive模式，Keep-Alive功能使客户端到服务器端的连接持续有效，当出现对服务器的后继请求时，Keep-Alive功能避免了建立或者重新建立连接。

http 1.0中默认是关闭的，需要在http头加入"Connection: Keep-Alive"，才能启用Keep-Alive；http 1.1中默认启用Keep-Alive，如果加入"Connection: close "，才关闭。

nginx 中可以用keepalive_timeout 设置keep-alive的时间.

Keep-Alive模式，客户端如何判断请求所得到的响应数据已经接收完成（或者说如何知道服务器已经发生完了数据）？我们已经知道 了，Keep-Alive模式发送完数据HTTP服务器不会自动断开连接，所有不能再使用返回EOF（-1）来判断（当然你一定要这样使用也没有办法，可 以想象那效率是何等的低）！下面我介绍两种来判断方法: 

- 使用消息首部字段Conent-Length
- 消息首部字段Transfer-Encoding

当客户端向服务器请求一个静态页面或者一张图片时，服务器可以很清楚的知道内容大小，然后通过Content-length消息首部字段告诉客户端 需要接收多少数据。但是如果是动态页面等时，服务器是不可能预先知道内容大小，这时就可以使用Transfer-Encoding：chunk模式来传输 数据了。即如果要一边产生数据，一边发给客户端，服务器就需要使用"Transfer-Encoding: chunked"这样的方式来代替Content-Length。

chunk编码将数据分成一块一块的发生。Chunked编码将使用若干个Chunk串连而成，由一个标明长度为0 的chunk标示结束。每个Chunk分为头部和正文两部分，头部内容指定正文的字符总数（十六进制的数字 ）和数量单位（一般不写），正文部分就是指定长度的实际内容，两部分之间用回车换行(CRLF) 隔开。在最后一个长度为0的Chunk中的内容是称为footer的内容，是一些附加的Header信息（通常可以直接忽略）

refer:

- [http://www.httpwatch.com/httpgallery/chunked/](http://www.httpwatch.com/httpgallery/chunked/)
- [https://www.byvoid.com/blog/http-keep-alive-header](https://www.byvoid.com/blog/http-keep-alive-header)
