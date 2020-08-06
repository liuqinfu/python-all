from wsgiref.simple_server import make_server

def run(env,response):
    response('200 OK',[('token','xxx')])
    print(env.get('PATH_INFO'))
    with open("html.html",'r',encoding='utf-8') as f:
        data = f.read()
    return [str.encode(data)]

if __name__ == '__main__':
    server = make_server('127.0.0.1', 8000, run)
    server.serve_forever()
