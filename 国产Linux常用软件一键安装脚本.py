import os

print_info: str = """
======================================================
    国产Linux软件一键安装脚本
======================================================
    <作者: Linwin-Cloud ,  2023 , Apache2软件协议>
    (在终端内输入 exit 或者按 Ctrl + C 退出)

 [本列表内的所有软件都不会采用Wine软件，因为Wine软件相当的不可靠]

 > 最小化安装选项: (不可跳过)
        软件                类别                        备注
  1. Vim                命令行文本编辑器         (可能很多系统已经自带)
  2. WPS Office         办公软件                 (Linux上最好的办公软件之一)
  3. Microsoft Edge     浏览器                   (很多系统上面只有火狐,Chrome太多东西用不了，用Edge都是Chrome内核)
  4. 微信               聊天软件                 (啸而霉的聊天软件，中国人必备)
  5. QQ                 聊天软件                 (基本上肯定需要的)
  6. QQ音乐             音乐软件                 (在Linux上开发听个音乐放松不过分吧)
  7. 百度网盘           网盘软件                 (这个和Windows上的功能差不多)
  8. 钉钉               办公/聊天软件            (工作肯定要用到)
  9. Fcitx              输入法框架               (搜狗输入法依赖)
  10. 搜狗拼音           输入法软件               (这个输入法绝对好)

 > 开发 ()
        软件                类别                        备注
  1. VsCode             编程软件                 (国内镜像，比较快)
  2. Github Desktop     协作软件                 (国内镜像下载)
  
 > 游戏 ()
        软件                类别                        备注
  1. HMCL-MC Java版本   图像化游戏软件                 (Java版本我的世界)
  2. bastet             命令行游戏软件                 (俄罗斯方块)
  3. ninvaders          命令行游戏软件                 (太空侵略者)
  4. 2048               命令行游戏软件                 (2048游戏)

 > 工具 ()
        软件                类别                        备注
  1. zip                命令行版本压缩软件             (可能系统自带)
  2. 7zip               命令行版本压缩软件             (可能系统自带)
  3. 火绒安全软件       图像化安全软件                 (安全软件，企业版本)
  
"""

def install_0() -> None:
    os.system("sudo apt install vim")
    os.system("sudo apt install fcitx")
    os.system("sudo apt install github-desktop")
    os.system("sudo apt install bastet")
    os.system("sudo apt install ninvaders")
    os.system("sudo apt install 2048-qt")
    os.system("sudo apt install zip")
    os.system("sudo apt install 7zip")

    a = [
        "https://wps-linux-personal.wpscdn.cn/wps/download/ep/Linux2019/11704/wps-office_11.1.0.11704_amd64.deb",
        "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_118.0.2088.46-1_amd64.deb",
        "http://archive.ubuntukylin.com/software/pool/partner/weixin_2.1.1_amd64.deb",
        "https://dldir1.qq.com/qqfile/qq/QQNT/5b1d2011/linuxqq_3.2.1-17260_amd64.deb",
        "https://dldir1.qq.com/music/clntupate/linux/deb/qqmusic_1.1.5_amd64.deb",
        "http://archive.ubuntukylin.com/software/pool/partner/baidunetdisk_3.5.0_amd64.deb",
        "https://dtapp-pub.dingtalk.com/dingtalk-desktop/xc_dingtalk_update/linux_deb/Release/com.alibabainc.dingtalk_7.0.40.30829_amd64.deb",
        "http://archive.ubuntukylin.com/software/pool/partner/sogouimebs_2.1.0.2529_amd64.deb",
        "https://vscode.cdn.azure.cn/stable/f1b07bd25dfad64b0167beb15359ae573aecd2cc/code_1.83.1-1696982868_amd64.deb",
        "https://gitee.com/LinWin-Cloud/packages.LinWinCloud.gitee/raw/master/software/net.hmcl.huangyuhui_3.5.4.232_amd64.deb",
        "https://gitee.com/LinWin-Cloud/packages.LinWinCloud.gitee/raw/master/software/cn.huorong.esm_2.0.6.1_amd64.deb"
    ]
    for i in a:
        os.system("cd linwinsofttmp && wget --no-check-certificate "+str(i))
        pass

    for i in os.listdir("linwinsofttmp"):
        #print(i)
        os.system("cd linwinsofttmp && sudo apt install ./"+i)
    print("安装完毕！祝贺您的Linux之旅愉快")


if __name__ == "__main__":
    os.system("mkdir linwinsofttmp")

    os.system("clear")
    print(print_info)
    o = input("是否继续操作: [如果继续操作按下 Enter 键]")
    install_0()
