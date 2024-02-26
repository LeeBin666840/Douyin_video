import pandas
import requests

# 总列表
all_list = []

wz = {'referer':'https://www.douyin.com/user/MS4wLjABAAAAWZqNtIQKYP7gCM9hsRuKaS83bsWbm140y7C33ETx5nEqEPKGnX2f4MudhLL06mIG?', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'cookie': 'ttwid=1%7CZanD4Sp-L4UcZ_4vgXPJSeaBdBdnqAIQmY5_yWRnOc8%7C1691398365%7C54bbe726bb6d1e9701255173812e8d18fa35c7c0bdbeedc5c19c1783da118444; s_v_web_id=verify_ll0mx041_qvaG7tpS_LR9T_40XG_9SEa_xtgtI3KkE6Xb; xgplayer_user_id=732598413563; passport_csrf_token=1f8b47680e984d7547f436da4a9f5a4a; passport_csrf_token_default=1f8b47680e984d7547f436da4a9f5a4a; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; __live_version__=%221.1.1.2778%22; d_ticket=e77990919143333474d45c66aad05d8b1aca9; passport_assist_user=CjxzZtgvP9JLEZle10qOj9F8YKIC8I5_30c-zoHR6SV98EwsJqVtaFwiUYodhnAMpxQlBQD8kH3cMg2L1vMaSAo81LcUEv3iKCUSdUpJ5mgkSg_xAv-hnGVnRqjdd5a0RRWIpuLQW8HmoSf63us89-VFlpylOyhH3L91Keb-EMXnuQ0Yia_WVCIBA9l8be8%3D; n_mh=-vHs5ZUkL9X2DgWA6Rj8WI61Wi7mEl9l679KgRxPqWc; sso_auth_status=ae3e33f9670ed7f7dffd87a68f3589d8; sso_auth_status_ss=ae3e33f9670ed7f7dffd87a68f3589d8; sso_uid_tt=5535c20600c7212546f980077db3f0c5; sso_uid_tt_ss=5535c20600c7212546f980077db3f0c5; toutiao_sso_user=e4db29f4208776afe5147d62da340217; toutiao_sso_user_ss=e4db29f4208776afe5147d62da340217; sid_ucp_sso_v1=1.0.0-KDBhMmZiNTkwZDk2NDQyZmRiNGVkM2ZmZmJjMTQ5NTIwYWFhZmQ0ZmYKHQj1kKWC3QIQ-NaNpwYY7zEgDDDLw8HUBTgCQPEHGgJobCIgZTRkYjI5ZjQyMDg3NzZhZmU1MTQ3ZDYyZGEzNDAyMTc; ssid_ucp_sso_v1=1.0.0-KDBhMmZiNTkwZDk2NDQyZmRiNGVkM2ZmZmJjMTQ5NTIwYWFhZmQ0ZmYKHQj1kKWC3QIQ-NaNpwYY7zEgDDDLw8HUBTgCQPEHGgJobCIgZTRkYjI5ZjQyMDg3NzZhZmU1MTQ3ZDYyZGEzNDAyMTc; odin_tt=8386b5f3bf27a31c5630aad1752cf77e0e267b877126d0ea3be191f83f3c44ca86776924996d6d529a8e433bcb1bf755; passport_auth_status=7321f18f16a7c59957222c2c170f0e94%2Cc31a7932d379473b46a48a8c8e5a566c; passport_auth_status_ss=7321f18f16a7c59957222c2c170f0e94%2Cc31a7932d379473b46a48a8c8e5a566c; uid_tt=d0bb61de43588016cd576392ac27252f; uid_tt_ss=d0bb61de43588016cd576392ac27252f; sid_tt=7cbe90c3547154dafdb4124dcd6e9533; sessionid=7cbe90c3547154dafdb4124dcd6e9533; sessionid_ss=7cbe90c3547154dafdb4124dcd6e9533; publish_badge_show_info=%220%2C0%2C0%2C1692625793760%22; LOGIN_STATUS=1; store-region=cn-hn; store-region-src=uid; _bd_ticket_crypt_cookie=c1bc5a0a6f5b4d7e217e060c0ce9ed01; __security_server_data_status=1; sid_guard=7cbe90c3547154dafdb4124dcd6e9533%7C1692625795%7C5183992%7CFri%2C+20-Oct-2023+13%3A49%3A47+GMT; sid_ucp_v1=1.0.0-KDZmMzgzZDRkMDJiNWQ3OGZkYjdhNTc3NWQ1ZGYxYTZhZDkwMDBiNGEKGQj1kKWC3QIQg9eNpwYY7zEgDDgCQPEHSAQaAmhsIiA3Y2JlOTBjMzU0NzE1NGRhZmRiNDEyNGRjZDZlOTUzMw; ssid_ucp_v1=1.0.0-KDZmMzgzZDRkMDJiNWQ3OGZkYjdhNTc3NWQ1ZGYxYTZhZDkwMDBiNGEKGQj1kKWC3QIQg9eNpwYY7zEgDDgCQPEHSAQaAmhsIiA3Y2JlOTBjMzU0NzE1NGRhZmRiNDEyNGRjZDZlOTUzMw; EnhanceDownloadGuide=%221_1692629356_0_0_0_0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCR09yaXJWWlllOVlKTDl1bTlnU3k3L0hpM05mT1pDWmJtUEl3SXZGWERjeGh5djZHcHJDdWt6RmtIZVJrNXl2bklWZmE1SmhXYUxYTzZMdDZTZjMrZzA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; strategyABtestKey=%221693212138.042%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAASI2CwQgXnN8K1EAMWpExImmColM3l2oObDxHT3_s0kI%2F1693238400000%2F0%2F0%2F1693220120236%22; download_guide=%223%2F20230828%2F0%22; pwa2=%220%7C0%7C3%7C0%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAASI2CwQgXnN8K1EAMWpExImmColM3l2oObDxHT3_s0kI%2F1693238400000%2F1693219109255%2F1693219107168%2F0%22; douyin.com; device_web_cpu_core=6; device_web_memory_size=8; webcast_local_quality=null; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1693826185150%2C%22type%22%3A1%7D; csrf_session_id=6779e84befad4243d2daf9c6f88984e1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; __ac_nonce=064ec841300a3a57e9466; __ac_signature=_02B4Z6wo00f014XKvVQAAIDC5sB9P0rgnmuF6rnAAIWmwsG9ckAj3P.NEvxRpKjJpXPPVzGoArbCX.1WNQJbn2oCxacm-ka1-CBj0mHad0ubheDFb3x8LRFc5HW0PL3Mvgur7LokNbXe3woGdb; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A6%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; tt_scid=9IPEemY7W2NM5Ttz70nenjT3P6rdSI3fH7-w18buyJlPZN7c.UOLuCDKsUZRbHHTd14b; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; msToken=SV-JJ5FUtb4653u5jQbbHDdOc7XCFIJ0cmPcPnlJcoBMMvz9V6Q72eqBaDNeqSUYRsMvHJkvIDjozAWdctXvL0Uwp8Iq2Snv3MmSj1ApyBKJLDwIjITMQkvrSwUt; passport_fe_beating_status=true; msToken=1SThKWZRF2SoQJwgkFv8zjBYb5ulLQ6zDt4eNZIHzoZHn_7QJllw3eGboIFVCM67SMJurb8k-7rBkRx1irgSg5rQ3quBgWLbEnrw_80P9rusTXaDrFv_c5UJl-5a'}

cursor = 0
aweme_id = input('请输入视频的id:')
while True:
    url = f'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web' \
          f'&aweme_id={aweme_id}&cursor={cursor}&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=116.0.0.0&browser_online=true&engine_name=Blink&engine_version=116.0.0.0&os_name=Windows&os_version=10&cpu_core_num=6&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7264500631289087545&msToken=SXewMRrQa5CTbZ8dW8iiUURauhdcUnV0n6SpstLCuZbOBXCZIiHJDPeJoJZiDsGdFunuPf_1n661vyNMgUeirCRp8CJ11zM0HamUDtI6j6hEKcg5jyg=&X-Bogus=DFSzswVY95bANnFQtxiD6VXAI'
    res = requests.get(url, headers=wz)

    JSON = res.json()   # 将响应转化为json数据
    comments = JSON['comments']  # comments-20条评论！
    if not comments:  # 如果评论是空的没有  找完了
        break
    cursor = JSON['cursor']      # 爬取到第一波评论的时候 给了我一个cursor的数据 20
    for com in comments:        # 遍历20条评论
        评论 = com['text']  # 具体的每一条！
        昵称 = com['user']['nickname']
        属地 = com['ip_label']
        lis = ['评论', 昵称, 属地, 评论]  # 构造一行数据
        all_list.append(lis)    # 把这一行数据加入总表
        print(f'来自{属地}的{昵称}说：{评论}')

        # 获取评论的id 构造这个评论的回复链接！
        comment_id = com['cid']
        reply = com['reply_comment_total']
        cursor_1 = 0
        if reply:  # 有回复！7272270551987588364
            while True:
                url_1 = 'https://www.douyin.com/aweme/v1/web/comment/list/reply/?'
                params ={
                    'device_platform': 'webapp',
                    'aid': '6383',
                    'channel': 'channel_pc_web',
                    'item_id': aweme_id,     # 视频的id
                    'comment_id': comment_id,  # 评论的id
                    'cursor': cursor_1,                        # 下一波回复的"钥匙"
                    'count': '10',
                    'item_type': '0',
                    'pc_client_type': '1',
                    'version_code': '170400',
                    'version_name': '17.4.0',
                    'cookie_enabled': 'true',
                    'screen_width': '1920',
                    'screen_height': '1080',
                    'browser_language': 'zh - CN',
                    'browser_platform': 'Win32',
                    'browser_name': 'Chrome',
                    'browser_version': '116.0.0.0',
                    'browser_online': 'true',
                    'engine_name': 'Blink',
                    'engine_version': '116.0.0.0',
                    'os_name': 'Windows',
                    'os_version': '10',
                    'cpu_core_num': '6',
                    'device_memory': '8',
                    'platform': 'PC',
                    'downlink': '10',
                    'effective_type': '4g',
                    'round_trip_time': '50',
                    'webid': '7264500631289087545',
                    'msToken': 'undaJrwXXTYJgJYjum51yR4APxSbUN8exlA3rLOFgHAUJju7TQMGFL5Y8RATDYYqOQHXRBt5J7JP_gTizcAcLISzKNINV93XID4ypOGybss2BHGwmx4wt6sHX0vY',
                    'X - Bogus': 'DFSzswVEwRkANnRgtxiITVXAIQ51'
                }
                # 得到回复的链接：  url 和 params
                res_1 = requests.get(url_1, headers=wz, params=params)
                JSON_1 = res_1.json()  # 将响应转化为json数据
                comments_1 = JSON_1['comments']  # comments-20条评论！
                if not comments_1:  # 如果评论是空的没有  找完了
                    break
                cursor_1 = JSON_1['cursor']  # 爬取到第一波评论的时候 给了我一个cursor的数据 20
                for com_1 in comments_1:  # 遍历20条评论
                    评论_1 = com_1['text']  # 具体的每一条！
                    昵称_1 = com_1['user']['nickname']
                    属地_1 = com_1['ip_label']
                    lis = ['回复', 昵称_1, 属地_1, 评论_1]
                    all_list.append(lis)
                    print(f'      来自{属地_1}的{昵称_1}回复：{评论_1}')

data = pandas.DataFrame(all_list)
data.to_excel('抖音评论.xlsx', index=False, header=['类型', '昵称', 'ip属地', '评论'])

# https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7272270551987588364&cursor=0&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=116.0.0.0&browser_online=true&engine_name=Blink&engine_version=116.0.0.0&os_name=Windows&os_version=10&cpu_core_num=6&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7264500631289087545&msToken=SXewMRrQa5CTbZ8dW8iiUURauhdcUnV0n6SpstLCuZbOBXCZIiHJDPeJoJZiDsGdFunuPf_1n661vyNMgUeirCRp8CJ11zM0HamUDtI6j6hEKcg5jyg=&X-Bogus=DFSzswVY95bANnFQtxiD6VXAI
# https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7272270551987588364&cursor=20&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=116.0.0.0&browser_online=true&engine_name=Blink&engine_version=116.0.0.0&os_name=Windows&os_version=10&cpu_core_num=6&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7264500631289087545&msToken=LrvsL81nkvb5iSx8rHvQmON3w-6SnlOkve3M0G8B1A91MLM0w_fIxJ0lw4-Vlu_leg8nwj3lUl_tGIA-E-zaKQpgRH08QJEJbaSdqTpz2FN1Uxq_nPk=&X-Bogus=DFSzswVERokANnRgtxiQjKXAIQRq
# https://www.douyin.com/aweme/v1/web/comment/list/reply/?device_platform=webapp&aid=6383&channel=channel_pc_web&item_id=7272270551987588364&comment_id=7272292103483458338&cursor=0&count=3&item_type=0&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=116.0.0.0&browser_online=true&engine_name=Blink&engine_version=116.0.0.0&os_name=Windows&os_version=10&cpu_core_num=6&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7264500631289087545&msToken=undaJrwXXTYJgJYjum51yR4APxSbUN8exlA3rLOFgHAUJju7TQMGFL5Y8RATDYYqOQHXRBt5J7JP_gTizcAcLISzKNINV93XID4ypOGybss2BHGwmx4wt6sHX0vY&X-Bogus=DFSzswVEwRkANnRgtxiITVXAIQ51
# 1.回复的链接 多了一个reply
# 2.回复的链接 多了一个id  这个id是它回复的那一条评论的id
# 3.回复的链接 也有一个cursor  找到更多的回复


# 1.{..'xxx':'yyyy'...}    # json数据
# 2.<html> .......</html>  # html数据
# 3.<html> ...{.......}....</html>  # html里面嵌套json


# aweme_id   抖音里面每一个视频 唯一的编号！


# 拿到第1波评论的时候   抖音给了我一个数据cursor  这个数据是下一波评论的’钥匙‘
# 拿到第2波评论的时候   抖音给了我一个数据cursor  这个数据是下一波评论的’钥匙‘
# 拿到第3波评论的时候   抖音给了我一个数据cursor  这个数据是下一波评论的’钥匙‘
# ....所有的评论全部拿到！
