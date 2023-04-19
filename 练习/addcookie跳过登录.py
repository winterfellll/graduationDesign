from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def apply_style(element):
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                          element, "border:5px solid red;")


def locator(ele):
    element = driver.find_element(By.XPATH, ele)
    apply_style(element)


driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.zhihu.com/')

cookie = [
    {
        "domain": ".zhihu.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "_xsrf",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "8d632417-80f3-4727-8262-08bcde26782b",
        "id": 1
    },
    {
        "domain": ".zhihu.com",
        "expirationDate": 1717939405.482684,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_zap",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "0da9cbe7-d971-4ce4-87b5-179cbe11bdcb",
        "id": 2
    },
    {
        "domain": ".zhihu.com",
        "expirationDate": 1682079833.753158,
        "hostOnly": False,
        "httpOnly": True,
        "name": "captcha_session_v2",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "2|1:0|10:1679487834|18:captcha_session_v2|88:bXRJallEekRxdnRic1RTNjh2ZDJrcVd2Y3l1ODRzR3NpSW1qTVpTTEMvajduRlo5NmZhc1o4bXlmK2FVMVVGSA==|165e30fe2d8394ae708e0ac02af0fe884068ef93dce2b448fb5d90a899a9cbba",
        "id": 3
    },
    {
        "domain": ".zhihu.com",
        "expirationDate": 1749475405.482735,
        "hostOnly": False,
        "httpOnly": False,
        "name": "d_c0",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "\"ADBfi9SFExWPTqgB1zb59qrocyaI7-hKIHk=|1654867404\"",
        "id": 4
    },
    {
        "domain": ".zhihu.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "expire_in",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "15552000",
        "id": 5
    },
    {
        "domain": ".zhihu.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "1679487889",
        "id": 6
    },
    {
        "domain": ".zhihu.com",
        "expirationDate": 1711023888,
        "hostOnly": False,
        "httpOnly": False,
        "name": "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "1678797790,1679400238,1679407519,1679487667",
        "id": 7
    },
    {
        "domain": ".zhihu.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "o_act",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "login",
        "id": 8
    },
    {
        "domain": ".zhihu.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "ref_source",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "other_https://www.zhihu.com/signin?next=/",
        "id": 9
    },
    {
        "domain": ".zhihu.com",
        "expirationDate": 1682079888,
        "hostOnly": False,
        "httpOnly": False,
        "name": "tst",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "r",
        "id": 10
    },
    {
        "domain": ".zhihu.com",
        "expirationDate": 1695039886.494157,
        "hostOnly": False,
        "httpOnly": True,
        "name": "z_c0",
        "path": "/",
        "sameSite": "None",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "2|1:0|10:1679487890|4:z_c0|92:Mi4xRzd1U0JnQUFBQUFBTUYtTDFJVVRGUmNBQUFCZ0FsVk5qMEVJWlFBSDRQQkJnRlFJZzVraXQwcktCTW0tbGRwZXRR|8151cf06df165a9ec47e9ccd450d5e233fb306852c00e58112f97ad20a726ea5",
        "id": 11
    },
    {
        "domain": "www.zhihu.com",
        "expirationDate": 1711023834,
        "hostOnly": True,
        "httpOnly": False,
        "name": "__snaker__id",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "ssL0rxqCqRMXGURH",
        "id": 12
    },
    {
        "domain": "www.zhihu.com",
        "expirationDate": 1813580432,
        "hostOnly": True,
        "httpOnly": False,
        "name": "_9755xjdesxxd_",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "32",
        "id": 13
    },
    {
        "domain": "www.zhihu.com",
        "expirationDate": 1682080734,
        "hostOnly": True,
        "httpOnly": False,
        "name": "gdxidpyhxdE",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "ZWl0JRRkevY%2Br3CEqd%5CgZnBST0nKnOwtPdGR6rXOmkijBGGq3XIGEYRtZCP%2BfybDDQ155QZbO%2F%2F36XglpTYvuUNhDYpwDELvLWXQyA%2F4%5Cm1ympBnujxMagPE6wuwZjUcuQ1Qgyn40DXAJqaVWTAjPj%2Fe48dqJZPx2ZE0t%2BvWSRODjTRy%3A1679488734475",
        "id": 14
    },
    {
        "domain": "www.zhihu.com",
        "hostOnly": True,
        "httpOnly": False,
        "name": "JOID",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "UFASBkvV_rfrpeYJUtKWoGF9ZBJCjJbEp9ShdGmelfScwqJVbmUBqoit4wRV2iJDIFIXMcDykVkyWo-ofx_K9zQ=",
        "id": 15
    },
    {
        "domain": "www.zhihu.com",
        "hostOnly": True,
        "httpOnly": False,
        "name": "KLBRSID",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "53650870f91603bc3193342a80cf198c|1679487894|1679487665",
        "id": 16
    },
    {
        "domain": "www.zhihu.com",
        "hostOnly": True,
        "httpOnly": False,
        "name": "osd",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "U1oUAUrW9LHspOUDVNWXo2t7YxNBhpDDptercm6flv6axaNWZGMGq4un5QNU2ShFJ1MUO8b1kFo4XIipfBXM8DU=",
        "id": 17
    },
    {
        "domain": "www.zhihu.com",
        "expirationDate": 1704630072.50802,
        "hostOnly": True,
        "httpOnly": False,
        "name": "q_c1",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "edb07f2d0c464d1a9786a2f40f6a8371|1670070071000|1670070071000",
        "id": 18
    },
    {
        "domain": "www.zhihu.com",
        "hostOnly": True,
        "httpOnly": False,
        "name": "SESSIONID",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "SgqIsMr9IaLubFV362XEAfKkwiIn04zgR7b8iA1m5sh",
        "id": 19
    },
    {
        "domain": "www.zhihu.com",
        "expirationDate": 1714047834.772955,
        "hostOnly": True,
        "httpOnly": False,
        "name": "YD00517437729195%3AWM_NI",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "LufeKqUU38sve6p9agDk1IpNKGZXRXITQZrvP4VI9YmGo8dxhGvLaWF%2BC4JIoE9ZrfsgQSnEHe7s91y6SlDw9eASMkiuRMBztxFaCuJLXbsXHjkvZUzCpssl4NXKhOt5UTk%3D",
        "id": 20
    },
    {
        "domain": "www.zhihu.com",
        "expirationDate": 1714047834.773582,
        "hostOnly": True,
        "httpOnly": False,
        "name": "YD00517437729195%3AWM_NIKE",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "9ca17ae2e6ffcda170e2e6ee96e762b686ad8cef5392868ba2d15f828f8f83d45cf3988885c77395adbdb2b62af0fea7c3b92a90abaa86ca7b978bfdd9f27ea7eac0dae46d88b5ffaaf346899996b9d1548b8c9fbbf17e94ec9aaabc53af99a1d9e774ac99baade45d86f58dd5c943ad9bf7bbf16eb1b99fb4ed4f8cbbf994bc3bbbea9d8dc77dfbbb8fb4d061abab9eaec172b8a88a82c27f8a949883f2548cb6a597d95fba9dc094f268f89298aceb45b8eb9bb5ea37e2a3",
        "id": 21
    },
    {
        "domain": "www.zhihu.com",
        "expirationDate": 1714047834.773804,
        "hostOnly": True,
        "httpOnly": False,
        "name": "YD00517437729195%3AWM_TID",
        "path": "/",
        "sameSite": "None",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "A%2F7SXi0MZ45EABQQBFfUAzW35YdkC5hG",
        "id": 22
    }
]

for i in cookie:
    driver.add_cookie(i)

sleep(2)
driver.get('https://www.zhihu.com/')

sleep(5)
