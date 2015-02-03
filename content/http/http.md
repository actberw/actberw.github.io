Title: http 协议
Tags: http
Date: 2014-10-18 21:00:00

HTTP协议是超文本传送协议(HyperText Transfer Protocol)的缩写，它是万维网(World Wide Web,www,也简称为Web)的基础, 位于TCP/IP协议栈的应用层。

### http 历史

第一个HTTP协议的版本是HTTP 0.9，它的组成极其简单，因为它只允许客户端发送GET这一种请求，它不包含协议头，每个请求只有一句话. 由于没有协议头，造成了HTTP 0.9协议只支持一种内容，即纯文本。不过网页仍然支持用HTML语言格式化，同时无法插入图片。所以HTTP 0.9能够支持的应用实在太有限了。一次HTTP 0.9的传输首先要建立一个由客户端到Web服务器的TCP连接，由客户端发起一个请求，然后由Web服务器返回页面内容，然后连接会关闭。如果请求的页面不存在，也不会返回任何错误码。

第二个版本是HTTP 1.0，直到HTTP 1.0成为最重要的面向事务的应用层协议。该协议对每一次请求/响应，同样是建立并关闭一次连接。其特点是简单、易于管理，所以它符合了大家的需要，得到了广泛的应用。

并且HTTP 1.0最显著的变化之一是开始支持客户端通过POST方法向Web服务器提交数据。从此客户端与Web服务器之间不再只能单向地获取数据，而可以实现交互，因此CGI（Common Gate Interface，通用网关接口）开始流行起来，Web上开始出现留言板、论坛等丰富的应用。
另一个巨大的改变是引入了HTTP头，使得HTTP不仅能返回错误代码，并且HTTP协议所传输的内容不仅限于纯文本，还可以是图片，动画等一系列格式。

第三个版本是HTTP 1.1, 它新增了很多引人注目的新特性，比如Host协议头, HTTP请求的头中包含 `Host: vimer.cn:80` 服务器根据Host这一行中的值来确定本次请求的是哪个具体的网站(虚拟主机). 长连接, 客户端默认与Web 服务器建立长连接，这种连接适合Web上数据量较大的丰富应用，使得资源消耗更少. 引入了Range头，使得客户端通过HTTP下载时只下载内容的一部分，这使得多线程下载也成为可能.

### Request message

The request message consists of the following:

- A request line for example "GET /images/logo.png HTTP/1.1", consist of three part(separate by space):
    - The HTTP method 
    - The relative URL of the resource 
    - The version of HTTP.
- Request header fields, such as "Accept-Language: en"
- An empty line(two consecutive CR-LF pairs).
- An optional message body.

![http request](/img/http/http_request.png)

    GET / HTTP/1.1
    Host: github.com
    Connection: keep-alive
    Cache-Control: max-age=0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
    Accept-Encoding: gzip, deflate, sdch
    Accept-Language: zh-CN,zh;q=0.8

### Response message

The response message consists of the following:

- A Status-Line for example "HTTP/1.1 200 OK"
    - The version of HTTP
    - The status code 
    - reason message
- Response header fields, such as "Content-Type: text/html"
- An empty line(two consecutive CR-LF pairs)
- An optional message body

![http response](/img/http/http_response.png)

    HTTP/1.1 200 OK
    Server: GitHub.com
    Date: Fri, 05 Dec 2014 03:13:18 GMT
    Content-Type: text/html; charset=utf-8
    Content-Encoding: gzip
    Transfer-Encoding: chunked
    Cache-Control: no-cache, private

### http request method

常用的request 方法有: GET, POST, PUT, DELETE, HEAD, TRACE, OPTION, CONNECT.

GET vs POST 区别

GET 可以完成类似form submit请求, 不过相对于POST有两个问题: 安全问题, GET请求所有的参数都在url中, 可以在浏览器历史记录中看到; 大小限制, 浏览器和http服务器实现对url的长度做限制, POST body也会有限制, 相对来说要比url长度大.

POST vs PUT 区别(idempotent method)

POST和PUT的区别容易被简单地误认为“POST表示创建资源，PUT表示更新资源”；而实际上，二者均可用于创建资源，更为本质的差别是在幂等性方面。

在HTTP/1.1规范中幂等性的定义是:
>Methods can also have the property of “idempotence” in that (aside from error or expiration issues) the side-effects of N > 0 identical requests is the same as for a single request.

从定义上看，HTTP方法的幂等性是指一次和多次请求某一个资源应该具有同样的副作用。

HTTP规范中对POST和PUT是这样定义的:
>The POST method is used to request that the origin server accept the entity enclosed in the request as a new subordinate of the resource identified by the Request-URI in the Request-Line. …… If a resource has been created on the origin server, the response SHOULD be 201 (Created) and contain an entity which describes the status of the request and refers to the new resource, and a Location header.

> The PUT method requests that the enclosed entity be stored under the supplied Request-URI. If the Request-URI refers to an already existing resource, the enclosed entity SHOULD be considered as a modified version of the one residing on the origin server. If the Request-URI does not point to an existing resource, and that URI is capable of being defined as a new resource by the requesting user agent, the origin server can create the resource with that URI.

POST所对应的URI并非创建的资源本身，而是资源的接收者。比如："POST http://www.forum.com/articles" 的语义是在 "http://www.forum.com/articles" 下创建一篇帖子，HTTP响应中应包含帖子的创建状态以及帖子的URI。两次相同的POST请求会在服务器端创建两份资源，它们具有不同的URI；所以，POST方法不具备幂等性。

而PUT所对应的URI是要创建或更新的资源本身。比如："PUT http://www.forum/articles/4231" 的语义是创建或更新ID为4231的帖子。对同一URI进行多次PUT的副作用和一次PUT是相同的；因此，PUT方法具有幂等性。

### http response status

http status 分类:

- Informational 1xx
- Successful 2xx
- Redirection 3xx
- Client Error 4xx
- Server Error 5xx

跳转 302 vs 303 vs 307

302 "Found" If the 302 status code is received in response to a request other than GET or HEAD, the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user, since this might change the conditions under which the request was issued.

303 "See Other" The response to the request can be found under a different URI and SHOULD be retrieved using a GET method on that resource.

307 "Temporary Redirect" If the 307 status code is received in response to a request other than GET or HEAD, the user agent MUST NOT automatically redirect the request unless it can be confirmed by the user, since this might change the conditions under which the request was issued. the request method is not allowed to be changed when reissuing the original request.

表面上看307 跟 302没什么区别, 现在大多数的浏览器对302的处理包括303的情况"See Other", 不管原来的请求方法而是发GET请求到新URL. 增加303和307就是为了区分这两种情况, 307跳转的时候是不允许修改请求方法的.

refer:

- [http://project67555.appspot.com/http.html](http://project67555.appspot.com/http.html)
- [http://www8.org/w8-papers/5c-protocols/key/key.html](http://www8.org/w8-papers/5c-protocols/key/key.html)
- [http://coolshell.cn/articles/4787.html](http://coolshell.cn/articles/4787.html)
