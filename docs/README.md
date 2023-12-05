# TataruBot2

基于NoneBot2的最终幻想14机器人塔塔露，为KOOK做了适配


## 当前功能

0. 塔塔露帮帮忙：显示所有功能
1. 暖暖：本周时尚品鉴作业
2. 选门：帮你选藏宝洞的门
3. 仙人彩：帮你选每周仙人仙彩数字
4. 物品 物品名：查询物品信息，例：`物品 铁矿`
5. 价格 大区 物品名：查询板子物价，大区不写默认豆豆柴，例：`价格 陆行鸟 铁矿`、`价格 叶小妖`
6. 看看微博：获取FF微博新闻
7. 房子 服务器名 主城名 房子大小：查询空房。主城名为：森都、海都、沙都、白银、雪都。房子大小为：S、M、L。例: `房子 银泪湖 森都 S`
8. 输出 boss名 职业名 (国服) (rdps) (day2): 查询logs上对应boss和职业的dps分段，括号内为可选的参数，默认国际服、adps、截止最后一天。
例: `输出 海德林 武士`，`输出 海德林 武士 国服 day10`
9. 攻略 (副本等级) 副本名关键字 (文本)：查简单副本攻略，括号内为可选参数，默认输出图片攻略
10. 日历：获取FF近期活动日历
11. 招募 大区名：获取指定大区招募板信息
12. 抽卡：随机抽取一张FF14塔罗牌

## 依赖

1. python >= 3.7.3
2. 如果有NoneBot v1则卸载 `pip uninstall nonebot`
3. 本代码测试使用的NoneBot版本是 nonebot2==2.0.0b4
4. 其他依赖安装`pip install -r requirements.txt`

## 使用

1. 安装脚手架nb-cli

   ```shell
   pip install nb-cli
   
   # 国内速度慢可以用阿里源加速，或者别的源，命令如下
   pip install nb-cli -i https://mirrors.aliyun.com/pypi/simple/
   ```

2. 安装适配器

   ```shell
   pip install nonebot-adapter-kaiheila
   ```

3. 安装驱动器

   ```shell
   nb driver install httpx
   ```

4. 下载本项目代码，并进入文件夹

   ```shell
   git clone https://github.com/aaron-lii/Tatarubot2-KOOK.git
   cd TataruBot2-KOOK
   ```

5. 根据需要修改配置文件`.env.prod`，（开发/调试环境则使用`.env.dev`，使用的配置在`.env`文件中指定）。
    更多信息见 [NoneBot2官方文档](https://v2.nonebot.dev/docs/appendices/config)

6. 将kook机器人的token填入`.env.prod`文件中的对应位置
   ```
   kaiheila_bots=[{"token": "此处填入token"}]
   ```

8. 启动一次机器人，自动生成配置文件`tatarubot2_conf.json`，如果旧版配置文件造成了错误，请删除旧版配置文件。根据需要把想开启的功能下面的"enable"改成true

   ```
   nb run
   ```

9. 再次启动机器人


## 备注

NoneBot2官方文档：https://v2.nonebot.dev/

NoneBot2 github：https://github.com/nonebot/nonebot2

