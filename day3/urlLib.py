from urllib import request, parse

# 抓取HTTP响应头和JSON数据
# with request.urlopen('https://www.v2ex.com/api/topics/hot.json') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# 模拟浏览器发送GET请求
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent',
#                 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' % (k, v))
#     print('Data:',data.decode('utf-8'))

# Post请求
# print('Login to weibo.cn...')
# username = input('username:')
# password = input('password:')
# login_data = parse.urlencode([
#     ('username', username),
#     ('password', password),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'),
# ])
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent',
#                'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer',
#                'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s' % (k, v))
#     print('Data:',f.read().decode('utf-8'))

# #通过代理访问网站
# proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm','host','username','password')
# opener = request.build_opener(proxy_handler,proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass