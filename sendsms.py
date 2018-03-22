import urllib.parse
import http.client

# apikey:成功注册后登录云片官网,进入后台可查看
# text:需要使用已审核通过的模板或者默认模板
# mobile:接收的手机号,仅支持单号码发送
# 短信接口
# https://sms.yunpian.com/v2/sms/single_send.json
# http://sms.yunpian.com/v2/sms/single_send.json
#http://sms.yunpian.com/v2/sms/single_send.json

def send_sms(apikey, text, mobile):
    #服务地址
    sms_host = "sms.yunpian.com"
    #端口号
    port = 80
    #版本号
    version = "v2"
    #智能匹配模板短信接口的URI
    sms_send_uri = "/" + version + "/sms/single_send.json"
    params = urllib.parse.urlencode({'apikey': apikey, 'text': text, 'mobile':mobile})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(sms_host, port=port, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

print(send_sms("d983be0b101b004b60ce80b7843e4aa9","【比特大陆】您好,本次登录验证码为:<VERIFYCODE>",18910025017))
