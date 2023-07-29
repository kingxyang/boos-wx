import os
SYS_CONFIG = {
    # 企业微信企业ID,必填 申请地址：https://work.weixin.qq.com/
    "wxid": "ww65a6b42ebb604d17",
    # 企业微信AgentId,必填
    "agentid": "1000002",
    # 企业微信应用Secret,必填
    "secret": "PSHye_Ls81koQvp9LMVMM0crxH8zkKVt8w1nkQBDejg",
    # 和风天气Key，非必填 申请地址： https://id.qweather.com/#/login
    "qweather": "862666dd590c4c88a3c4af7d5701d8d3",
    # 天气预报地址，非必填
    # 格式：市-市/县/区，多地址以&&分隔
    # 如：成都-双流&&成都-武侯
    "city": "周口-郸城",
    # 纪念日名称，非必填
    # 周期性日子，每年都有的日子，多个日期以&&分隔
    # 如：正式女朋友的生日&&小三的生日
    "targetname": "距离春节还有",
    # 纪念日日期，非必填
    # 公历格式20XX-XX-XX，农历年份前加n
    # 多日期以&&分隔，注意与targetname名称对应
    # 如：2022-08-10&&n2021-08-15
    "targetday": "n2023-12-30",
    # 单日项目名称，非必填
    # 只发生一次的日子，只有某一年有的日子，多日期以&&分隔
    # 如：跟小三在一起&&见面
    "beginname": "距离春节还有",
    # 单日日期，非必填
    # 公历格式20XX-XX-XX，农历年份前加n
    # 多日期以&&分隔，注意与beginname名称对应
    # 如：2022-08-15&&n2022-12-10
    "beginday": "n2023-12-30",
    # 图文类型，非必填
    # 1为单图文，2为多图文，默认单图文
    "msgtype": "1"
}


def get(key: str):
    value = os.getenv(key)
    if value is None:
        if key in SYS_CONFIG:
            value = SYS_CONFIG[key]
    return value