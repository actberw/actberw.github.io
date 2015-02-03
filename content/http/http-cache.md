Title: http 缓存
Tags: http
Date: 2014-10-18 22:00:00

### HTTP cache headers

有两个主要的缓存控制头: "Expires" 和 "Cache-Control".

Expires

expires 头用来设定缓存过期的时间, 例如 "Expires:Fri, 05 Dec 2014 06:26:14 GMT" , 在这段时间内, 浏览器(代理)可以直接从缓存中响应请求, 这是一个绝对的时间.

Cache-Control

http 1.1新增cache-control头更好的控制缓存, 例如"cache-control: private, max-age=0, no-cache". 

- Public 指示响应可被任何缓存区缓存
- Private 指示对于单个用户的整个或部分响应消息，不能被共享缓存处理(proxy)。
- no-cache/no-store 不缓存
- max-age 缓存过期最长时间是一个相对时间,  单位是秒.
- s-maxage 比max-age多了一个s, 表示共享缓存. overrides both the max-age and expires header.

On most modern systems, the "cache-control" headers "max-age" and "s-maxage" will take precedence, but it's always good practice to set a matching value here for compatibility. Just make sure you format the date correctly.

### Conditional requests
While Cache-Control and Expires tells the browser when to next retrieve the resource from the network, a few additional headers specify how to retrieve the resource from the network. These types of requests are known as conditional requests.

Conditional requests are those where the browser can ask the server if it has an updated copy of the resource. The browser will send some information about the cached resource it holds and the server will determine whether updated content should be returned or the browser’s copy is the most recent. In the case of the latter an HTTP status of 304 (not modified) is returned

Last-Modified/If-Modified-Since(Time based)

"Last-Modified" 表示文件最后修改时间, 下次服务器再请求资源时会在 "If-Modified-Since" 头中加入 "Last-Modified" 的时间跟服务器确认, 如果没被修改则返回 304

ETag/If-None-Match(Content-based)

ETag 跟 "Last-Modified" 作用相同, 不过一般是文件的散列值, 用来跟服务器确认缓存的内容是否过期. 某些情况下虽然 "Last-Modified" 被修改了但是内容没变, ETag 能很好的处理这种情况.

### Vary & Content negotiation(内容协商)

要了解 Vary 的作用，先得了解 HTTP 的内容协商机制。有时候，同一个 URL 可以提供多份不同的文档，这就要求服务端和客户端之间有一个选择最合适版本的机制，这就是内容协商。

协商方式有两种，一种是服务端把文档可用版本列表发给客户端让用户选，这可以使用 300 Multiple Choices 状态码来实现。另外一种方案：服务端根据客户端发送的请求头中某些字段自动发送最合适的版本。可以用于这个机制的请求头字段又分两种：内容协商专用字段（Accept 字段）、其他字段。


请求头字段  | 说明 | 响应头字段
------------|------|-----------
Accept      | 告知服务器发何种媒体类型 | Content-Type
Accept-Language | 告知服务器发送何语言 | Content-Language
Accept-Charset | 告知服务器发送何种字符集 | Content-Type
Accept-Encoding | 告知服务器采用何种压缩方式 | Content-Encoding

例如客户端发送以下请求头：

    Accept:*/*
    Accept-Encoding:gzip,deflate,sdch
    Accept-Language:zh-CN,en-US;q=0.8,en;q=0.6

示它可以接受任何 MIME 类型的资源；支持采用 gzip、deflate 或 sdch 压缩过的资源；可以接受 zh-CN、en-US 和 en 三种语言，并且 zh-CN 的权重最高（q 取值 0 - 1，最高为 1，最低为 0，默认为 1），服务端应该优先返回语言等于 zh-CN 的版本。

浏览器的响应头可能是这样的：

    Content-Type: text/javascript
    Content-Encoding: gzip

表示这个文档确切的 MIME 类型是 text/javascript；文档内容进行了 gzip 压缩；响应头没有 Content-Language 字段，通常说明返回版本的语言正好是请求头 Accept-Language 中权重最高的那个。

客户端和服务端之间可能存在一个或多个中间实体（如缓存服务器），而缓存服务最基本的要求是给用户返回正确的文档, Vary 字段用于列出一个响应字段列表，告诉缓存服务器遇到同一个 URL 对应着不同版本文档的情况时，应如何缓存和筛选合适的版本。

### Pragma

Pragma 主要的用法就是 "pragma: no-cache", 指示不要缓存, 跟 "cache-control: no-cache" 和 "expires: 0" 作用一样.

refer:

- [https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers#visibility](https://devcenter.heroku.com/articles/increasing-application-performance-with-http-cache-headers#visibility) 
- [http://www.mobify.com/blog/beginners-guide-to-http-cache-headers/](http://www.mobify.com/blog/beginners-guide-to-http-cache-headers/)
- [https://www.imququ.com/post/four-ways-to-post-data-in-http.html](https://www.imququ.com/post/four-ways-to-post-data-in-http.html)
- [http://www8.org/w8-papers/5c-protocols/key/key.html](http://www8.org/w8-papers/5c-protocols/key/key.html)
- [http://blog.httpwatch.com/2007/12/10/two-simple-rules-for-http-caching/](http://blog.httpwatch.com/2007/12/10/two-simple-rules-for-http-caching/)
- [http://blog.allmyverse.com/http-vary-header-and-bp/](http://blog.allmyverse.com/http-vary-header-and-bp/)
