from DrissionPage import ChromiumPage, ChromiumOptions
from datetime import datetime
from utils.utils import pushqrcode,rmqrcode,killadb,freshgallery
import os,time
from config.mediaconfig import ANDROID_QRCODE_PATH,PC_JIANYING_PATH
import subprocess
from wx.CWXdriver import WXdriver

def upload(content=None,vpath=None):
    co = ChromiumOptions(read_file=False)
    # 使用系统用户路径
    co.use_system_user_path()
    co.set_local_port(9222)
    # 创建ChromiumPage实例
    page = ChromiumPage(addr_or_opts=co)
    page.wait(2)

    tab = None
    tab_id = page.get_tab(url='channels.weixin.qq.com', as_id=True)
    if tab_id:
        tab = page.get_tab(tab_id)
        page.set.tab_to_front(tab)
        tab.get('https://channels.weixin.qq.com/login.html')
    else:
        tab = page.new_tab('https://channels.weixin.qq.com/login.html')
    tab.wait(5)
    #扫码登录：保存二维码-传输到手机-手机微信扫码登录-删除照片
    qrcode = tab.ele('@class=qrcode-area')
    location = qrcode.rect.location
    size = qrcode.rect.size
    qrfname = datetime.strftime(datetime.now(),'%Y%m%d_%H%M%S_qrcode')+'.jpg'
    tab.get_screenshot(path=os.path.join(PC_JIANYING_PATH,qrfname),left_top=(location[0],location[1]),right_bottom=(location[0]+size[0],location[1]+size[1]) )
    tab.wait(1)
    qrpath = pushqrcode(qrfname)
    time.sleep(1)
    freshgallery(qrpath) #刷新相册消息
    time.sleep(1)
    #微信扫码
    killadb()
    appium_process = subprocess.Popen('appium --relaxed-security', shell=True)
    time.sleep(4)
    WX = WXdriver()
    WX.scanqrcode()
    WX.quit()
    #删除手机里的二维码
    killadb()
    appium_process.kill()
    rmqrcode(qrpath)
    os.remove(os.path.join(PC_JIANYING_PATH,qrfname))
    print("登录成功success")
    
    #管理首页
    tab.get('https://channels.weixin.qq.com/platform')
    tab.wait(5) #需要多等会页面刷新

#--------------------------------------------------------------
    #自动发表视频示例

    # tab('发表视频').click()
    # tab.wait(4)
    # tab.set.upload_files(vpath)
    # tab('tag:input@type=file').input(vpath)
    # tab.wait.upload_paths_inputted()
    # tab.wait.eles_loaded('@class=video-content',timeout=360)
    # tab.wait(4)
    # #简介
    # tab('tag:div@class=input-editor').click()
    # if len(content) > 400:
    #     content = content[:400]
    # tab('tag:div@class=input-editor').input(content)
    # tab.wait(2)

    # #位置
    # tab('tag:div@class=tip').click()
    # tab.wait(1)
    # tab('不显示位置').click()
    # tab.wait(1)

    # tab.actions.move_to('@class=form-btns')

    # #短标题
    # n_title = metadata.get('title')
    # n_title = n_title.replace('{日期}',datetime.strftime(datetime.now(),'%Y%m%d'))
    # if len(n_title) > 30:
    #     n_title = n_title[:30]
    # tab('@class=post-short-title-wrap').ele('tag:input@type=text').clear()
    # tab('@class=post-short-title-wrap').ele('tag:input@type=text').input(n_title)
    # tab.wait(1)

    # #点击原创声明
    # tab('@class=declare-original-checkbox').ele('tag:input@type=checkbox').click()
    # tab('@class=original-proto-wrapper').ele('tag:input@type=checkbox').click()
    # tab('tag:button@text()=声明原创').click()

    # tab('@class=form-btns').ele('text=发表').click()
    # tab.wait(5)

    
