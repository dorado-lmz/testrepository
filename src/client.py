import request

def send_request(url):
  r = request.get(url)
  return r.status_code

def visit_baidu():
  return send_request('http://www.baidu.com')
