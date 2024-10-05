# C-WXbot
[视频号助手](https://channels.weixin.qq.com/login.html) 自动扫码登录脚本

# 原理

- 控制电脑浏览器打开视频号助手[登录页面](https://channels.weixin.qq.com/login.html)
- 截图登录二维码并传输到手机
- 通过[appium](http://appium.io) 控制手机微信扫码登录
- 登录成功后删除二维码缓存文件

# 环境配置

1. windows 电脑

- 安装 nvm，并安装 22.6.0 的 nodejs
- 用 nodejs 安装 appium: npm install -g appium
- 安装 appium 的 uiautomator2 驱动
- 安装安卓 sdk 里的 platform-tools 和 tools
- 系统变量里配置默认的 adb 端口为 5037（和 appium 相同）
- 使用 chrome 浏览器，首次需要先登录视频号助手网站，设置好视频号管理员

2. python

- 安装 python
- 依赖库： pip install DrissionPage appium-python-client

3. 安卓手机

- 最好安卓 10 以上版本,手机连接好电脑，确保可以传输文件
- 打开 adb 调试，并授权电脑
- 安装微信，并登录视频号管理员账户

# 使用

```python
python main.py
```

# 应用场景

自动发布视频：在 wx - CWX.py 文件中，已有发布视频的示例（被注释掉的代码），如需要可以自行调整
