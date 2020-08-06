from wsgiref.simple_server import make_server
from urls import url_dict

def run(env,response):
    path = env.get('PATH_INFO')
    for url_dic in url_dict:
        if path == url_dic[0]:
            func = url_dic[1]
            break
    if func:
        res = func()
    else:
        res = func()
    response('200 OK', [('token', 'xxx')])
    return [str.encode(res,'utf-8')]



if __name__ == '__main__':
    server = make_server('127.0.0.1', 8000, run)
    server.serve_forever()
