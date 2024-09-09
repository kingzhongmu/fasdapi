## 备用知识
### cookie和session的区别：  
zhihu.com/question/19786827
### 解释一下 http.response.start 和http.response.body

在ASGI（Asynchronous Server Gateway Interface）协议中，`http.response.start` 和 `http.response.body` 是两种类型的事件消息，它们用于在异步Web服务器和应用程序之间传递HTTP响应的信息。这些消息是由应用程序发送给服务器，以便服务器能够将这些信息转发给客户端（如Web浏览器）。下面是对这两种事件消息的详细解释：

#### `http.response.start`

`http.response.start` 消息标志着HTTP响应的开始。当应用程序准备好发送响应给客户端时，它会首先发送一个`http.response.start`消息。这个消息包含了响应的一些基本信息，如状态码、响应头和可选的响应开始时的部分响应体（虽然这很少见）。但是，通常情况下，`http.response.start`消息只包含状态码和响应头，而响应体则通过后续的`http.response.body`消息发送。

`http.response.start`消息的主要目的是让服务器知道应用程序已经开始发送响应，并允许服务器设置HTTP响应的初始状态码和响应头。一旦服务器接收到这个消息，它就可以开始向客户端发送响应的头部信息。

#### `http.response.body`

`http.response.body`消息用于发送HTTP响应的体部分。在发送了`http.response.start`消息之后，应用程序可以通过发送一个或多个`http.response.body`消息来传递响应体的内容。每个`http.response.body`消息都包含响应体的一部分数据，直到整个响应体都被发送完毕。

如果响应体很大，或者出于性能考虑，应用程序可能会选择将响应体分成多个较小的块来发送。在这种情况下，它会发送多个`http.response.body`消息，每个消息都包含响应体的一部分。当所有`http.response.body`消息都被发送完毕后，整个HTTP响应就完成了。

#### 总结

- `http.response.start`消息标志着HTTP响应的开始，并包含状态码和响应头信息。
- `http.response.body`消息用于发送HTTP响应的体部分，可以发送一个或多个这样的消息来传递完整的响应体。
- 这两个消息共同构成了ASGI应用程序发送给服务器的完整HTTP响应。服务器随后将这些信息转发给客户端。  

## 对于中间件的理解
假设中间件的添加顺序： 自定义Middleware，SessionMiddleware， CORSMiddleware  
请求发过来时的处理顺序是CORSMiddleware -> SessionMiddleware -> Middleware  
对请求的响应处理顺序是Middleware -> SessionMiddleware -> CORSMiddleware【回调send_wrap】  

## SessionMiddleware的理解
0 在app中add_middleware时，会初始化seesion和cookie 都为空的字典  
- 浏览器首次请求时  
    1 请求到来时，可以通过req.session.setdefault("session", "session_strxxxx")为seesion设置值【代码中是在自定义的Middleware中设置】  
    2 响应时，SessionMiddleware的send_wrap被回调，对这个session值进行加密【由加密盐+base64+时间+其他】，保存在cookie中的 "session_id"【可配置】中,cookie被挂载到headers（headers.append("Set-Cookie", header_value)）；发送响应到客户端  
    3 浏览器收到请求，把cookie保存在应用中
- 浏览器再次请求时  
    1 请求携带cookie到后端  
    2 浏览器的SessionMiddleware 会先解析出cookie，通过session_id字段，解析出session加密值，再解密出session的原始值，保存在scope中  
    3 这样浏览器就可以通过seesion去判断是哪个用户的请求



## 安装依赖
pip install -r requirement.txt

## 程序运行
uvicorn app:app --reload or  
uvicorn app:app --reload --host 0.0.0.0 --port 8000

## Redis 启动
Redis 安装：https://blog.csdn.net/weixin_44893902/article/details/123087435
windows: 进入到Redis安装目录  
执行 redis-server.exe redis.windows.conf  



