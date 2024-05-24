# -*- coding: utf-8 -*-
# Author: Mr Lee
# Time: 2024/5/22 23:58
# File: 测试.py
# Project: PythonProject
# Software: PyCharm
# Motto: 人无横财不富 马无夜草不肥
import requests
import execjs
from urllib import parse
import urllib.parse
import random
from loguru import logger


def get_mstoken(randomlength=128):
    """
    根据传入长度产生随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
    length = len(base_str) - 1
    for _ in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


msToken = get_mstoken()
print('msToken:::', msToken)

sec_user_id = 'MS4wLjABAAAAAJgfLrYs0SeCX7z-eGAj5iB73gZhXcjPmUnDhX5vWNQ'
max_cursor = 0
headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7CNp1z1PBM1ZV45ylzKnybOXvRVwgPXBu0PT-WYHjdsM8%7C1716439972%7C05cf1af545eb5332c60cd365a62bc7e2e1a40820387a41e4c85a8df0e7ae43cb; dy_swidth=1707; dy_sheight=1067; s_v_web_id=verify_lwis1jln_yus8h7Vh_1Wzu_4wTF_B1yS_oH31PGeiJRB8; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; strategyABtestKey=%221716439973.516%22; passport_csrf_token=236de27cb718264dd1984a00dedbb73d; passport_csrf_token_default=236de27cb718264dd1984a00dedbb73d; bd_ticket_guard_client_web_domain=2; passport_assist_user=CjxN5yLLdFIbjHmW-EsNa6anLc_xvpqswT6_E_GSeGOub987kFbvsP9XAAcRxfED9HYuG7li-c2QnS0kTv0aSgo8LIbMhL__a5SVb-gZ9ttNTOQ_kt7MPP7TIG0gg6_I3vmDXPWO2oRXR-5iRgxgnxJ_Pyy8VXxc87FXyHfHEKuE0g0Yia_WVCABIgEDn5LUTA%3D%3D; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sso_uid_tt=f51dafeac5ea6413236fddd82fb15967; sso_uid_tt_ss=f51dafeac5ea6413236fddd82fb15967; toutiao_sso_user=96494d2ad89995d811a29dca723feb34; toutiao_sso_user_ss=96494d2ad89995d811a29dca723feb34; sid_ucp_sso_v1=1.0.0-KDllYzcwZWZmNjY3MWExM2ViZmRiYTZmYzAwMTg1YzQ4MzQ5YzVjODkKHQj24bLR4AEQvJe7sgYY7zEgDDCOst_IBTgGQPQHGgJsZiIgOTY0OTRkMmFkODk5OTVkODExYTI5ZGNhNzIzZmViMzQ; ssid_ucp_sso_v1=1.0.0-KDllYzcwZWZmNjY3MWExM2ViZmRiYTZmYzAwMTg1YzQ4MzQ5YzVjODkKHQj24bLR4AEQvJe7sgYY7zEgDDCOst_IBTgGQPQHGgJsZiIgOTY0OTRkMmFkODk5OTVkODExYTI5ZGNhNzIzZmViMzQ; passport_auth_status=8be835650533d276ab203057d132c847%2C; passport_auth_status_ss=8be835650533d276ab203057d132c847%2C; uid_tt=c272cb49f52163b362e35380e7d0b42c; uid_tt_ss=c272cb49f52163b362e35380e7d0b42c; sid_tt=4750e914e40190e5c3cc6fb4e7eb0517; sessionid=4750e914e40190e5c3cc6fb4e7eb0517; sessionid_ss=4750e914e40190e5c3cc6fb4e7eb0517; publish_badge_show_info=%220%2C0%2C0%2C1716440000974%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=687c9520b110bc9d218878fb1f3ecd13; __security_server_data_status=1; sid_guard=4750e914e40190e5c3cc6fb4e7eb0517%7C1716440002%7C5183997%7CMon%2C+22-Jul-2024+04%3A53%3A19+GMT; sid_ucp_v1=1.0.0-KDZhMDk3ZDM3ZjdjNWFlNjdlY2U1MmVhMDE2M2M2NzUzMmQyZGQxMDYKGQj24bLR4AEQwpe7sgYY7zEgDDgGQPQHSAQaAmhsIiA0NzUwZTkxNGU0MDE5MGU1YzNjYzZmYjRlN2ViMDUxNw; ssid_ucp_v1=1.0.0-KDZhMDk3ZDM3ZjdjNWFlNjdlY2U1MmVhMDE2M2M2NzUzMmQyZGQxMDYKGQj24bLR4AEQwpe7sgYY7zEgDDgGQPQHSAQaAmhsIiA0NzUwZTkxNGU0MDE5MGU1YzNjYzZmYjRlN2ViMDUxNw; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A32%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAxqeqaEl1H319U8Wauf7weMuUdLV0XYUzDObEmZlBkhY%2F1716480000000%2F0%2F1716441899822%2F0%22; __ac_nonce=0664f2b14007cbc85b3ae; __ac_signature=_02B4Z6wo00f01Rtk8DAAAIDAEUIrmzyyCQ0bRPSAACCYa4; douyin.com; device_web_cpu_core=32; device_web_memory_size=8; architecture=amd64; csrf_session_id=808e887ae70bfb12140688fb2a0698e3; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAxqeqaEl1H319U8Wauf7weMuUdLV0XYUzDObEmZlBkhY%2F1716480000000%2F0%2F1716464405712%2F0%22; passport_fe_beating_status=true; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; xg_device_score=7.835535958674097; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSlNLVkdFM2J1MjA1MnRhbFA5YjhDTlhTTFd5N3pabG12bDVTcmdGSjl0UFBzOWI3N2oreUt6UWFXai9RUTB1ZHFRMmsyVFc5M3ZSYnRZNVdvNHlYSXc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=ZYcqooDcTTmLvx6LVQwHnjIFNl2ieJw8oE7kWrIhJW-B6nFH8w25J9rQChtMkWsHi7vUAMmvbpUVPTj73TcanDgI0j2IlC_RjEuvR1YUxek1QQTyHak5MCjGSgxoLA==; odin_tt=63b4f5bb284e2daf364f1b5173aee13fe0367780b08671fec29fe4f83efa7e0d8c8c12b52c63879ad94c9ffa2c1552f5f9948d9bb91ff0f073e7bca688b73fa6; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22',
    'pragma': 'no-cache',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAA5nj2-CvYbzuStU4H6ZUghWi670PTS0XYj889X6t30Zw?vid=7371036615151537459',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

# url = (f"https://www.douyin.com/aweme/v1/web/aweme/post/?"
#        f"device_platform=webapp&aid=6383&channel=channel_pc_web&"
#        f"sec_user_id={sec_user_id}&max_cursor={max_cursor}&"
#        f"locate_item_id=7371789480795081984&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&"
#        f"count=18&"
#        f"publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=32&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7371328396721047040&"
#        f"msToken=K5iVolnEjOBxmGsAwZZXg9w61uir8sOT-dYAmEQhShp8xid6StBUgl9Tk_0HK_BFPenh7IB8QmTLC08THeyhXOgJHuZZhbGky-OahC1ZA2n65jqapVTfeuxjX8XTCg%3D%3D&"
#        f"a_bogus=OyRZMmwvdidNgDy65VALfY3q6W13YDt50trEMD2fEd3PE639HMO79exo0ZsvV3WjLG%2FlIebjy4hbTpOprQA701wf98ho%2F2AdsDSDSlVQ-9hj53iruyRMr0WF-vGACPBB-i3RrOX0oXpHFbLmlnAn5XqvPjoja3LkFk6FOomG&verifyFp=verify_lwfzjhjd_a88fa725_e8ff_bb1f_d60a_7639012b370d&fp=verify_lwfzjhjd_a88fa725_e8ff_bb1f_d60a_7639012b370d")
url = 'https://www.douyin.com/aweme/v1/web/aweme/post/'

params = {
    "device_platform": "webapp",
    "aid": "6383",
    "channel": "channel_pc_web",
    "sec_user_id": "MS4wLjABAAAA5nj2-CvYbzuStU4H6ZUghWi670PTS0XYj889X6t30Zw",
    "max_cursor": "0",
    "locate_item_id": "7371036615151537459",
    "locate_query": "false",
    "show_live_replay_strategy": "1",
    "need_time_list": "1",
    "time_list_query": "0",
    "whale_cut_token": "",
    "cut_version": "1",
    "count": "18",
    "publish_video_strategy_type": "2",
    "update_version_code": "170400",
    "pc_client_type": "1",
    "version_code": "290100",
    "version_name": "29.1.0",
    "cookie_enabled": "true",
    "screen_width": "1707",
    "screen_height": "1067",
    "browser_language": "zh-CN",
    "browser_platform": "Win32",
    "browser_name": "Chrome",
    "browser_version": "120.0.0.0",
    "browser_online": "true",
    "engine_name": "Blink",
    "engine_version": "120.0.0.0",
    "os_name": "Windows",
    "os_version": "10",
    "cpu_core_num": "32",
    "device_memory": "8",
    "platform": "PC",
    "downlink": "10",
    "effective_type": "4g",
    "round_trip_time": "50",
    "webid": "7372053453286295055",
    "msToken": "owO_Vd5q_R4jwIKsl_d55L_PKgk4mL5qe33k39xkavjkeyVoNGWNogSYnH1wIHavY2xaSlnPFPGSszT49djYJFKUhoCALtuMcodgNz1HC_e9mfOs-Nf0Jmds7b7n8d0=",
    "verifyFp": "verify_lwis1jln_yus8h7Vh_1Wzu_4wTF_B1yS_oH31PGeiJRB8",
    "fp": "verify_lwis1jln_yus8h7Vh_1Wzu_4wTF_B1yS_oH31PGeiJRB8"
}
params_str = urllib.parse.urlencode(params)
print(params_str)
response = requests.get(url, headers=headers, params=params)
abogus = execjs.compile(open('douyin.js', encoding='utf-8').read()).call('get_abogus', params_str)
print('abogus:::', abogus)
# print('abougs加密后长度:::',len(abogus))
logger.info(response.status_code)
print(response.text)


print(len('QX8MQfhgDi6PvfS65VQLfY3qV333YDte0SVkMDhe6n3PsL39HMPu9exow7zvMIueZsQlIbyjy4hGapPME/OjA36UHmJx/2aBm6fkSPPZ5om7s1feeLW/nGJC-XsdSPBm-XNUiKEmjfMKc00lBNSV'))