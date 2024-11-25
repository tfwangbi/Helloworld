# -- coding: utf-8 --
import time

import requests

url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
'''
Data:
case 1
from: zh
to: en
query: 下雨天
transtype: realtime
simple_means_flag: 3
sign: 114676.351429
token: a0df4994825e0404f784e91133afc2a8
domain: common
ts: 1710316845236

----------
case 2
from: zh
to: en
query: 去学校
transtype: realtime
simple_means_flag: 3
sign: 754877.1009548
token: a0df4994825e0404f784e91133afc2a8
domain: common
ts: 1710317511800


---- look for sign and ts

w = {
                                    from: _.fromLang,
                                    to: _.toLang,
                                    query: e,
                                    transtype: i,
                                    simple_means_flag: 3,
                                    sign: b(e),
                                    token: window.common.token,
                                    domain: k.getCurDomain(),
                                    ts: +new Date
                                }

sign = u(i), i is the key word which inputted to translate

'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Referer':'https://fanyi.baidu.com/?ext_channel=DuSearch',
    'Cookie':'BIDUPSID=56E7AD86AA3B7C0355E9993C555DE4E3; PSTM=1709039875; BAIDUID=56E7AD86AA3B7C032C167FEFF496BEEE:FG=1; BAIDUID_BFESS=56E7AD86AA3B7C032C167FEFF496BEEE:FG=1; ZFY=O0PLDpLNwXmDMBTHglu04UoHbGpcqGRg4Dc:B3Lt3FLo:C; BAIDU_WISE_UID=wapp_1709522676567_590; H_WISE_SIDS=40210_40206_40215_40222_40061_40295_40290_40288_40286_40318_40320_40079_40364_40351; RT="z=1&dm=baidu.com&si=c31848c6-a52a-4341-b0c5-d6955c194c96&ss=ltfj2nq4&sl=u&tt=vbd&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=bvg0q&ul=c0t1l&hd=c0t7p"; APPGUIDE_10_6_9=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=40210_40206_40215_40222_40295_40290_40288_40286_40320_40079_40364_40351_40369_40377_40317_40337_40415; BA_HECTOR=2l25ag8g2l2lak002021a00gkbrbve1iv2i3o1t; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=6; delPer=0; BCLID=10008607658910533993; BCLID_BFESS=10008607658910533993; BDSFRCVID=nE4OJeC62G4fePoqPJyduUFage8aPHbTH6aoUFRpO_kWePAp2KG5EG0PkM8g0KuhOSHfogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; BDSFRCVID_BFESS=nE4OJeC62G4fePoqPJyduUFage8aPHbTH6aoUFRpO_kWePAp2KG5EG0PkM8g0KuhOSHfogKKy2OTH9DF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; H_BDCLCKID_SF=JR48oIIKJK83eRjk2tu_2t40bMQyetJyaR3XKCbvWJ5TMCojj-jq0-4L0-68KnQP3D6M0CnqLpnDShPC-tnlQlDQXnnWL-QT064Hah0a3l02VbvEe-t2ynLJXnb7KtRMW238oq7mWITUsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJ9jj6jK4JKjG0HtTQP; H_BDCLCKID_SF_BFESS=JR48oIIKJK83eRjk2tu_2t40bMQyetJyaR3XKCbvWJ5TMCojj-jq0-4L0-68KnQP3D6M0CnqLpnDShPC-tnlQlDQXnnWL-QT064Hah0a3l02VbvEe-t2ynLJXnb7KtRMW238oq7mWITUsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJ9jj6jK4JKjG0HtTQP; APPGUIDE_10_7_0=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1709733382,1710316766; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1710316766; ab_sr=1.0.1_MWE3MTBjNDBhZjA1ODM4NGIzOWE3M2I3YmVkZGNiOWQ4MmI3ZGU2MGRiYWY3ZDQ4NDY0MDE1ZWQwNzcyOWEyNjVmNDU2OWU4MGNlYjFmNTVjMTVlZThiMTM0ZmY2MzkxMzJiOTE0MjI2MDg5ODg2MDdhYTVkMzdmZTBjNDE0MjBkZmJjYTUyMzExN2Q5MWM2MjIxNmJlZjZhYjg3YjVlNw=='
}

word = input("Please input a word:")
# word.encode('utf-8', 'replace').decode('utf-8')

# function u:
js_data = r'''
function b(t) {
        function e(t, e) {
            (null == e || e > t.length) && (e = t.length);
            for (var n = 0, r = new Array(e); n < e; n++)
                r[n] = t[n];
            return r
        }
        function n(t, e) {
            for (var n = 0; n < e.length - 2; n += 3) {
                var r = e.charAt(n + 2);
                r = "a" <= r ? r.charCodeAt(0) - 87 : Number(r),
                r = "+" === e.charAt(n + 1) ? t >>> r : t << r,
                t = "+" === e.charAt(n) ? t + r & 4294967295 : t ^ r
            }
            return t
        }
        var r = null;
        t.exports = function(t) {
            var o, i = t.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
            if (null === i) {
                var a = t.length;
                a > 30 && (t = "".concat(t.substr(0, 10)).concat(t.substr(Math.floor(a / 2) - 5, 10)).concat(t.substr(-10, 10)))
            } else {
                for (var s = t.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), c = 0, u = s.length, l = []; c < u; c++)
                    "" !== s[c] && l.push.apply(l, function(t) {
                        if (Array.isArray(t))
                            return e(t)
                    }(o = s[c].split("")) || function(t) {
                        if ("undefined" != typeof Symbol && null != t[Symbol.iterator] || null != t["@@iterator"])
                            return Array.from(t)
                    }(o) || function(t, n) {
                        if (t) {
                            if ("string" == typeof t)
                                return e(t, n);
                            var r = Object.prototype.toString.call(t).slice(8, -1);
                            return "Object" === r && t.constructor && (r = t.constructor.name),
                            "Map" === r || "Set" === r ? Array.from(t) : "Arguments" === r || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r) ? e(t, n) : void 0
                        }
                    }(o) || function() {
                        throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")
                    }()),
                    c !== u - 1 && l.push(i[c]);
                var p = l.length;
                p > 30 && (t = l.slice(0, 10).join("") + l.slice(Math.floor(p / 2) - 5, Math.floor(p / 2) + 5).join("") + l.slice(-10).join(""))
            }
            for (var d = "".concat(String.fromCharCode(103)).concat(String.fromCharCode(116)).concat(String.fromCharCode(107)), h = (null !== r ? r : (r = window[d] || "") || "").split("."), f = Number(h[0]) || 0, m = Number(h[1]) || 0, g = [], y = 0, v = 0; v < t.length; v++) {
                var _ = t.charCodeAt(v);
                _ < 128 ? g[y++] = _ : (_ < 2048 ? g[y++] = _ >> 6 | 192 : (55296 == (64512 & _) && v + 1 < t.length && 56320 == (64512 & t.charCodeAt(v + 1)) ? (_ = 65536 + ((1023 & _) << 10) + (1023 & t.charCodeAt(++v)),
                g[y++] = _ >> 18 | 240,
                g[y++] = _ >> 12 & 63 | 128) : g[y++] = _ >> 12 | 224,
                g[y++] = _ >> 6 & 63 | 128),
                g[y++] = 63 & _ | 128)
            }
            for (var b = f, w = "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(97)) + "".concat(String.fromCharCode(94)).concat(String.fromCharCode(43)).concat(String.fromCharCode(54)), k = "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(51)) + "".concat(String.fromCharCode(94)).concat(String.fromCharCode(43)).concat(String.fromCharCode(98)) + "".concat(String.fromCharCode(43)).concat(String.fromCharCode(45)).concat(String.fromCharCode(102)), x = 0; x < g.length; x++)
                b = n(b += g[x], w);
            return b = n(b, k),
            (b ^= m) < 0 && (b = 2147483648 + (2147483647 & b)),
            "".concat((b %= 1e6).toString(), ".").concat(b ^ f)
        }
    }
'''

import js2py

js = js2py.EvalJs()
js.execute(js_data)
sign = js.b(word)
print(sign)
ts = str(int(time.time()*1000))
print(ts)

data = {
    'from': 'zh',
    'to': 'en',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': sign,  # param 1
    'token': 'a0df4994825e0404f784e91133afc2a8',
    'domain': 'common',
    'ts': ts # param 2
}

response = requests.post(url, headers=headers, data=data)

print(response.text)



