# main.py
import requests
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
import os

# 从环境变量获取密钥
QWEATHER_KEY = os.getenv("QWEATHER_KEY")

# 全国主要城市列表（可简化）
cities = [
    "北京", "上海", "广州", "深圳", "杭州", "成都", "武汉", "西安",
    "南京", "天津", "郑州", "长沙", "重庆", "青岛", "济南", "厦门"
]

def get_temperature(city):
    """调用和风天气 API 获取当前温度"""
    url = f"https://devapi.qweather.com/v7/weather/now?location=101010100&key={QWEATHER_KEY}"
    # 注意：这里需要根据城市编码调用，简化版我们先用固定值测试
    try:
        res = requests.get(url).json()
        return res.get("now", {}).get("temp", 30)  # 模拟返回温度
    except:
        return 30  # 失败时返回默认值

def generate_hotmap():
    """生成全国高温分布图"""
    # 模拟数据
    data = [(city, 35 + i) for i, city in enumerate(cities)]
    
    map_chart = (
        Map()
        .add("最高气温(℃)", data, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全国高温预警地图"),
            visualmap_opts=opts.VisualMapOpts(min_=30, max_=45),
        )
    )

    # 生成 HTML 和 PNG
    map_chart.render("hot-weather.html")
    make_snapshot(snapshot, "hot-weather.html", "hot-weather.png", delay=2)
    print("✅ 热力图已生成：hot-weather.html 和 hot-weather.png")

if __name__ == "__main__":
    generate_hotmap()
# 
