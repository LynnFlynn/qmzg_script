#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time, sys, math, operator, os
import win32api, win32gui, win32con
from pymouse import PyMouse
from pykeyboard import PyKeyboard
# from win32gui import *
# from win32api import *
from PIL import ImageGrab, Image
from functools import reduce
from const import btnDict
from config import cfgConst

BASE_DIR = os.path.dirname(__file__)
IMG_DIR = "img"
LOG_DIR = "log"


class QMZGClass(object):
    def __init__(self):
        self.mouse = PyMouse()

    def test(self):
        # clear log dir
        if False:
            os.rmdir(LOG_DIR)
            if not os.path.exists(LOG_DIR):
                os.mkdir(LOG_DIR)
        print(cfgConst.testModel)
        width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        print("{} X {}".format(width, height))

        # 打开游戏窗口
        label = "全民主公 - 搜狗高速浏览器"
        try:
            hld = win32gui.FindWindow(None, label)
            win32gui.SetForegroundWindow(hld)
        except win32gui.error:
            print("Error: 没有找到目标窗口")
            sys.exit()

        # 资源秘境
        self.ziyuan_process()
        # 神将府
        self.shenjiang_process(4, 10, 1)
        # 斩将塔
        self.zhanjiang_process()
        # 军团
        self.juntuan_process()
        # 每日签到
        self.qiandao_process()
        # 国战
        self.guozhan_process()
        # 物资争霸
        for i in range(2):
            self.wuzi_process()
        # 攻城夺宝
        self.gongcheng_process(1)
        return True

    ##鼠标点击
    def mouse_click(self, btn_name, img_name=""):
        btn = btnDict.get(btn_name)
        if (cfgConst.testModel):
            print("btn : {}".format(btn_name))
        _x = btn.x + (btn.w // 2)
        _y = btn.y + (btn.h // 2)
        time.sleep(0.5)
        self.mouse.move(_x, _y)
        time.sleep(0.5)
        self.mouse.click(_x, _y, 1)
        time.sleep(1)
        if not (img_name == "" or img_name is None):
            for i in range(30):
                if self.img_similarity(img_name):
                    break
                else:
                    time.sleep(1)

        return True

    ##图片比对
    def img_similarity(self, img_name, thr=20.0):
        time.sleep(1)
        img = btnDict.get(img_name)
        src = ImageGrab.grab((img.x, img.y, img.x + img.w, img.y + img.h))
        # img1.save('temp.jpg')
        h1 = src.histogram()
        h2 = src.histogram()
        try:
            dst = Image.open(os.path.join(IMG_DIR, img.img))
            h2 = dst.histogram()
        except IOError:
            print("Error: 图片读取失败")

        diff = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        if (cfgConst.testModel):
            print("sim : {}".format(diff))
            if diff > 0:
                src.save("log/{}-{}".format(time.strftime("%Y%m%d%H%M%S"), img.img))
        if diff < thr:
            return True
        else:
            return False

    # 资源秘境
    def ziyuan_process(self):
        print("资源秘境")
        time.sleep(1)
        self.mouse_click("ziyuan_in", "ziyuan_qiangzhen_in")
        # 强征银币 x3
        self.mouse_click("ziyuan_qiangzhen_in", "ziyuan_qiangzhen")
        for i in range(3):
            if not self.img_similarity("ziyuan_qiangzhen_times", 0.1):
                self.mouse_click("ziyuan_qiangzhen", "")
            else:
                break
        self.mouse_click("ziyuan_qiangzhen_out", "")
        # 开采资源
        self.mouse_click("ziyuan_kaicai_in", "")
        if self.img_similarity("ziyuan_kaicai_sousuo", 20):
            self.mouse_click("ziyuan_kaicai_sousuo", "ziyuan_kaicai_kaicai")
            self.mouse_click("ziyuan_kaicai_kaicai", "ziyuan_kaicai_in")
        # self.mouse_click("ziyuan_kaicai_out", None)
        # 掠夺资源
        for i in range(2):
            if not (self.img_similarity("ziyuan_lveduo_times", 0.1) or self.img_similarity("ziyuan_lveduo_times_2", 0.1)):
                self.mouse_click("ziyuan_lveduo_in", "ziyuan_lveduo_lveduo")
                self.mouse_click("ziyuan_lveduo_lveduo", "ziyuan_lveduo_jieshu")
                time.sleep(3)
                self.mouse_click("ziyuan_lveduo_jieshu", "ziyuan_lveduo_ok")
                self.mouse_click("ziyuan_lveduo_ok", "ziyuan_kaicai_in")
            else:
                break
        if self.img_similarity("ziyuan_yijian", 5):
            self.mouse_click("ziyuan_yijian", "ziyuan_yijian_ok")
            self.mouse_click("ziyuan_yijian_ok", "ziyuan_out")
        self.mouse_click("ziyuan_out", "zhanjiang_in")
        return True

    # 神将府
    def shenjiang_process(self, val, times, page):
        print("神将府")
        time.sleep(1)
        self.mouse_click("shenjiang_in", "shenjiang_pre")
        if page > 1:
            self.mouse_click("shenjiang_next", "shenjiang_next")
        switch = {
            1: "shenjiang_1",
            2: "shenjiang_2",
            3: "shenjiang_3",
            4: "shenjiang_4"
        }
        if not self.img_similarity("shenjiang_times", 1):
            self.mouse_click(switch[val], "shenjiang_ok")
            for i in range(times):
                if self.img_similarity("shenjiang_winning", 20):
                    self.mouse_click("shenjiang_must", "shenjiang_must")
                else:
                    self.mouse_click("shenjiang_shitou", "shenjiang_shitou")
                self.mouse_click("shenjiang_ok", "")
                time.sleep(2)
                self.mouse_click("shenjiang_jueguo_ok", "shenjiang_ok")
            self.mouse_click("shenjiang_out", "shenjiang_out")
        self.mouse_click("shenjiang_out", "zhanjiang_in")
        return True

    # 斩将塔
    def zhanjiang_process(self):
        print("斩将塔")
        time.sleep(1)
        # 左-斩将塔
        self.mouse_click("zhanjiang_in", "zhanjiang_left_in")
        self.mouse_click("zhanjiang_left_in", "zhanjiang_left_chongzhi")
        self.mouse_click("zhanjiang_left_chongzhi", "")
        if self.img_similarity("zhanjiang_left_chongzhi_ok", 5):
            self.mouse_click("zhanjiang_left_chongzhi_ok", "")
            self.mouse_click("zhanjiang_left_saodang", "zhanjiang_left_saodang_ok")
            self.mouse_click("zhanjiang_left_saodang_ok", "")
            time.sleep(2)
            self.mouse_click("zhanjiang_left_jieguo_ok", "zhanjiang_left_chongzhi")
        self.mouse_click("zhanjiang_out", "zhanjiang_in")
        # 右-神魔塔
        self.mouse_click("zhanjiang_in", "zhanjiang_left_in")
        self.mouse_click("zhanjiang_right_in", "zhanjiang_right_chongzhi")
        self.mouse_click("zhanjiang_right_chongzhi", "")
        if self.img_similarity("zhanjiang_right_chongzhi_ok", 5):
            self.mouse_click("zhanjiang_right_chongzhi_ok", "")
            self.mouse_click("zhanjiang_right_saodang", "zhanjiang_right_saodang_ok")
            self.mouse_click("zhanjiang_right_saodang_ok", "")
            time.sleep(2)
            self.mouse_click("zhanjiang_right_jieguo_ok", "zhanjiang_right_chongzhi")
        self.mouse_click("zhanjiang_out", "zhanjiang_in")
        return True

    # 军团
    def juntuan_process(self):
        print("军团")
        time.sleep(1)
        self.mouse_click("juntuan_in", "juntuan_out")
        #
        self.mouse_click("juntuan_hongbao", "juntuan_hongbao_title")
        if self.img_similarity("juntuan_hongbao_lingqu", 20):
            self.mouse_click("juntuan_hongbao_lingqu", "")
            self.mouse_click("juntuan_hongbao_ok", "")
        else:
            self.mouse_click("juntuan_hongbao_ok", "")
        #
        self.mouse_click("juntuan_jiejiang_in", "juntuan_jiejiang_out")
        if self.img_similarity("juntuan_jiejiang_time", 0.5):
            self.mouse_click("juntuan_jiejiang_huishou", "juntuan_jiejiang_huishou_ok")
            self.mouse_click("juntuan_jiejiang_huishou_ok", "juntuan_jiejiang_out")
        if self.img_similarity("juntuan_jiejiang_timeno", 5):
            self.mouse_click("juntuan_jiejiang_5", "juntuan_jiejiang_huishou_ok")
            self.mouse_click("juntuan_jiejiang_huishou_ok", "juntuan_jiejiang_out")
        self.mouse_click("juntuan_jiejiang_out", "juntuan_out")

        self.mouse_click("juntuan_out", "zhanjiang_in")

    # 物资争霸
    def wuzi_process(self):
        print("物资争霸")
        time.sleep(1)
        self.mouse_click("wuzi_in", "wuzi_yijian")
        self.mouse_click("wuzi_yijian", "wuzi_kaishi")
        self.mouse_click("wuzi_kaishi", "wuzi_yijian_out")
        self.mouse_click("wuzi_yijian_out", "wuzi_out")
        self.mouse_click("wuzi_out", "zhanjiang_in")
        return True

    # 每日签到
    def qiandao_process(self):
        print("每日签到")
        time.sleep(1)
        # 每日签到
        self.mouse_click("qiandao_in", "qiandao_out")
        time.sleep(1)
        if self.img_similarity("qiandao_ok", 20):
            self.mouse_click("qiandao_ok", "")
        self.mouse_click("qiandao_out", "zhanjiang_in")
        # VIP福利
        self.mouse_click("fuli_in", "fuli_out")
        self.mouse_click("fuli_meiri", "fuli_out")
        if self.img_similarity("fuli_lingqu_1", 0.2) and self.img_similarity("fuli_lingqu_2", 20):
            self.mouse_click("fuli_lingqu_1", "")
            self.mouse_click("fuli_lingqu_2", "fuli_meiri_out")
            self.mouse_click("fuli_meiri_ok", "")
        self.mouse_click("fuli_out", "zhanjiang_in")
        # 神魔主公
        self.mouse_click("shenmo_in", "shenmo_out")
        if not self.img_similarity("shenmo_yiguaji", 10):
            self.mouse_click("shenmo_guaji", "shenmo_kaishiguaji")
            self.mouse_click("shenmo_kaishiguaji", "shenmo_guaji_ok")
            self.mouse_click("shenmo_guaji_ok", "shenmo_yiguaji")
        self.mouse_click("shenmo_out", "zhanjiang_in")
        # 开箱寻宝
        self.mouse_click("xunbao_in", "xunbao_out")
        if self.img_similarity("xunbao_free", 1):
            self.mouse_click("xunbao_jin", "xunbao_ok")
            self.mouse_click("xunbao_ok", "xunbao_out")
        else:
            self.mouse_click("xunbao_jin", "xunbao_jin_one")
            self.mouse_click("xunbao_jin_one", "xunbao_ok")
            self.mouse_click("xunbao_ok", "xunbao_out")
        self.mouse_click("xunbao_out", "zhanjiang_in")
        # 军衔
        self.mouse_click("junxie_in", "junxie_out")
        if self.img_similarity("junxie_lingqu", 20):
            self.mouse_click("junxie_lingqu", "")
        self.mouse_click("junxie_out", "zhanjiang_in")

        return True

    # 国战
    def guozhan_process(self):
        print("国战")
        time.sleep(1)
        self.mouse_click("guozhan_in", "guozhan_out")
        #
        self.mouse_click("guozhan_xinxi_in", "guozhan_juanzeng_in")
        self.mouse_click("guozhan_juanzeng_in", "guozhan_juanzeng_out")
        if self.img_similarity("guozhan_juanzeng_times", 1):
            self.mouse_click("guozhan_juanzeng_plus", "")
            self.mouse_click("guozhan_juanzeng_ok", "guozhan_xinxi_out")
        else:
            self.mouse_click("guozhan_juanzeng_out", "guozhan_xinxi_out")
        self.mouse_click("guozhan_xinxi_out", "guozhan_out")
        #
        self.mouse_click("guozhan_xuanba_in", "guozhan_xuanba_out")
        self.mouse_click("guozhan_xuanba_mobai_1", "guozhan_mobai_out")
        if self.img_similarity("guozhan_xuanba_putongmobai", 1):
            self.mouse_click("guozhan_xuanba_putongmobai", "guozhan_xuanba_out")
        self.mouse_click("guozhan_mobai_out", "guozhan_xuanba_out")
        self.mouse_click("guozhan_xuanba_out", "guozhan_out")
        self.mouse_click("guozhan_out", "zhanjiang_in")
        return True

    # 群雄争霸
    def qunxiong_process(self):
        print("群雄争霸")
        time.sleep(1)

        return True

    # 攻城夺宝
    def gongcheng_process(self, times):
        print("攻城夺宝")
        time.sleep(1)
        self.mouse_click("duobao_in", "duobao_out")
        switch = {
            1: "duobao_city_1",
            2: "duobao_city_2",
            3: "duobao_city_3",
            4: "duobao_city_4"
        }
        for i in range(4):
            if self.img_similarity(switch[i + 1], 1):
                self.mouse_click(switch[i + 1], "duobao_tiaozhan")
                if not self.img_similarity("duobao_tiaoguo", 1):
                    self.mouse_click("duobao_tiaoguo", "")
                self.mouse_click("duobao_tiaozhan", "duobao_ok")
                self.mouse_click("duobao_ok", "")
                if self.img_similarity("duobao_chongzhi", 1):
                    self.mouse_click("duobao_chongzhi", "duobao_out")
                else:
                    self.mouse_click("duobao_jiachen", "duobao_ok_2")
                    self.mouse_click("duobao_ok_2", "duobao_out")
                    time.sleep(1)

        self.mouse_click("duobao_out", "zhanjiang_in")
        return True


# main
if __name__ == '__main__':
    # ctrl+F1 --> F5
    qmzg = QMZGClass()
    qmzg.test()
