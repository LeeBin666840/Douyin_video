import time
# 导入解码功能
from urllib import parse
# 导入模块
import requests
# 正则模块
import re
# json模块
import json
# 格式化输出  针对于字典数据解析
from pprint import pprint
# 导入selenium模块
from selenium import webdriver

# # 实例化浏览器对象
driver = webdriver.Chrome()
# # 进入官网
driver.get('https://www.douyin.com/user/MS4wLjABAAAA3Edl4dvMxf-9uaJf8Zi8pt6RDBKQPPUzczKMMtwgInzWsy9UP1MoLf9qFXUwTE13')
time.sleep(5)
yzm = input('请输入你的验证码:')
driver.find_element_by_css_selector('.input-container.hasinput input').send_keys(yzm)
driver.implicitly_wait(10)  # 隐式地等待
driver.find_element_by_css_selector('.button.done.normal').click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector('.trust-login-dialog-button-cancel').click()
# 滑动条
def xiala():
    """执行下拉操作"""
    for i in range(1, 50, 2):  # 1 3 5 7 9
        time.sleep(1)
        j = i / 9  # 1/9 3/9 5/9  7/9 9/9    可以下拉5次
        js_all = "document.documentElement.scrollTop=document.documentElement.scrollHeight * %f" % j  # %f百分号的占位符
        driver.execute_script(js_all)
xiala()
lis = driver.find_elements_by_css_selector('.niBfRBgX.Q_uOVQ1u.SBWUpJd_')
for li in lis:
    href = li.find_element_by_css_selector('a').get_attribute('href')
    vid = href.split('/')[-1]
    # print(vid)
    # 1.定义网址
    url = f'https://www.douyin.com/user/MS4wLjABAAAA3Edl4dvMxf-9uaJf8Zi8pt6RDBKQPPUzczKMMtwgInzWsy9UP1MoLf9qFXUwTE13?modal_id={vid}'
    # 2.模拟浏览器  headers伪装
    headers = {
        'cookie': '__ac_referer=__ac_blank; douyin.com; ttwid=1%7CwcqrshikVplQmQ0mCAEm2XWYKRUCdkNjL1bDhrkTTjg%7C1704893594%7Ce3cf4574f4041b74a7c78278a96c12c62c6eb9728cc0b90af616b871ab2833c9; douyin.com; device_web_cpu_core=32; device_web_memory_size=8; architecture=amd64; home_can_add_dy_2_desktop=%220%22; dy_swidth=1707; dy_sheight=1067; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; csrf_session_id=d6b4b518577fab669ff8c5019f10faaa; strategyABtestKey=%221704893596.158%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; s_v_web_id=verify_lr7tmm5i_V1dpTXLQ_cWA7_4bq1_BZaR_F7Jdvht0EZQ2; xgplayer_user_id=84463848990; passport_csrf_token=405859b2fb8d776e5788ff7847d5c49d; passport_csrf_token_default=405859b2fb8d776e5788ff7847d5c49d; bd_ticket_guard_client_web_domain=2; ttcid=1e34d8f9e2824bfbb3f895d9336b4f8c21; passport_assist_user=CkHltVXFgXiDHU_pmBnmWbQteP3RVEEzyCMK3yXs0rygj3y6RKue-GZMwLs-JNIlcLOabuD3O4ze1z8TUXa-3XimkRpKCjwxZV8o9WOz_k2pMQQfvbmbffXQ5rJdB1XUn_NpzbNTrnoJ2FzeXKPMUxPiuKdjHsenDrniXrVrbziTEEUQhKXGDRiJr9ZUIAEiAQMYaHC9; n_mh=8NZxYz6uIaKVYln5xfsBmJhrTB_KYL4arvIgi89nPiE; sso_uid_tt=3b2e106e28a45cc4d683bfb11a9a07d9; sso_uid_tt_ss=3b2e106e28a45cc4d683bfb11a9a07d9; toutiao_sso_user=5b516c6d561c9f39e610b882e8229954; toutiao_sso_user_ss=5b516c6d561c9f39e610b882e8229954; sid_ucp_sso_v1=1.0.0-KGVjNjJiYWUzNzA1NzQ1YTRmZTBkYTZmZGJmNzk5NTk2Y2Y0ZWYwN2YKHwidm4CO9Y2FBhC3ufqsBhjvMSAMMJ651JcGOAZA9AcaAmxmIiA1YjUxNmM2ZDU2MWM5ZjM5ZTYxMGI4ODJlODIyOTk1NA; ssid_ucp_sso_v1=1.0.0-KGVjNjJiYWUzNzA1NzQ1YTRmZTBkYTZmZGJmNzk5NTk2Y2Y0ZWYwN2YKHwidm4CO9Y2FBhC3ufqsBhjvMSAMMJ651JcGOAZA9AcaAmxmIiA1YjUxNmM2ZDU2MWM5ZjM5ZTYxMGI4ODJlODIyOTk1NA; passport_auth_status=2b002dda9283fbd742c348765eb070c8%2C; passport_auth_status_ss=2b002dda9283fbd742c348765eb070c8%2C; uid_tt=4874f39fc9ec25e02c95f655c3836d67; uid_tt_ss=4874f39fc9ec25e02c95f655c3836d67; sid_tt=8bed006696d7145f6dd6218aa992552f; sessionid=8bed006696d7145f6dd6218aa992552f; sessionid_ss=8bed006696d7145f6dd6218aa992552f; __ac_nonce=0659e9cb900130ebfc110; publish_badge_show_info=%220%2C0%2C0%2C1704893631916%22; LOGIN_STATUS=1; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA5vY86eOGOs7vRGj424E8OO45IJgtIq0XvfDm-Mhi1tiGWvW-vIy8MyZqR8LWFxSJ%2F1704902400000%2F0%2F1704893632307%2F0%22; store-region=cn-hn; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=3313f072b3cb0b3208776c287627d02e; __security_server_data_status=1; sid_guard=8bed006696d7145f6dd6218aa992552f%7C1704893633%7C5183993%7CSun%2C+10-Mar-2024+13%3A33%3A46+GMT; sid_ucp_v1=1.0.0-KGU4MGI3YTRlMDc5ZjBkOTIxMGVhNWY0M2Q0ZDFjMjM1MDk3ZTg0YjkKGwidm4CO9Y2FBhDBufqsBhjvMSAMOAZA9AdIBBoCbHEiIDhiZWQwMDY2OTZkNzE0NWY2ZGQ2MjE4YWE5OTI1NTJm; ssid_ucp_v1=1.0.0-KGU4MGI3YTRlMDc5ZjBkOTIxMGVhNWY0M2Q0ZDFjMjM1MDk3ZTg0YjkKGwidm4CO9Y2FBhDBufqsBhjvMSAMOAZA9AdIBBoCbHEiIDhiZWQwMDY2OTZkNzE0NWY2ZGQ2MjE4YWE5OTI1NTJm; tt_scid=vcBAS3BH9gc-Dgp0ZbRw-hO5qNYEzO8eLBwyZWWAIk2uB5HAz-iTmUn1yvRnneDPf4c7; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; xg_device_score=7.892358684285341; SEARCH_RESULT_LIST_TYPE=%22single%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A32%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTHhjaDdBZFdsVlIyeDdNMmVaay9xT2NwQ2pCNUc1TU93bjB0cFY5R3c4TUFKc2kwYzdzd0RtNFlUUXRPaFRYdktoMFB6RmxwdmNQVGlJdkNZejNucUk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=9S1J_s5TG67YvHoK0glFbB5lF3Bi5IuL65COdnKRw9DNrsAOxWOwN8oIywuN1H_APy-iQn3TR6sTKnoNbpN8PV9bRWixUxW4VKhFgAhu9DY4FZR9PTxsOQF9DL0=; msToken=Z-l0oTJygOGWkGaLDSDDFZ9D7U_WFizby-9OJgqeH0kQdapxdkvUxWm5M5SVzLmKVYx-mqlwQpI-tkF3Bg1I3jyjNBd-QMR8UxL36WbRZePkvHDGo-eRoZr4aNg=; odin_tt=993bf433c850443e5fd021e045d7809048c4ad867baa96186dca227d36a6b814e4f302baafbf07a3c78e146d376ed72275dd1515e998359c327fb7467025b164; IsDouyinActive=false; passport_fe_beating_status=false',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    # 3.发送请求
    response = requests.get(url=url, headers=headers)
    # 4.获取数据
    # print(response)
    # print(response.text)
    # 5.解析数据
    video_info = re.findall(
        '<script id="RENDER_DATA" type="application/json">(.*?)</script>',
        response.text)[0]
    # print(video_info)
    video_data = parse.unquote(video_info)
    vide_json = json.loads(video_data)
    # 标题
    title = vide_json['app']['videoDetail']['desc']
    title = re.sub(r'[\/:*?|\n<>"]', '', title)
    try:
        video_url = 'https:' + vide_json['app']['videoDetail']['video']['bitRateList'][0]['playAddr'][0]['src']
        print(title)
        print(video_url)
        # 6.保存数据
        content = requests.get(video_url).content
        with open(f'video/{title}.mp4', 'wb') as f:
            f.write(content)
    except Exception as e:
        video_url = 'https:' + re.findall('{"src":"(.*?)"}', video_data)[0]
        music_content = requests.get(video_url).content
        with open(f'video/{title}.mp3', 'wb') as f:
            f.write(music_content)
        print(e, '该链接为音频链接！')
