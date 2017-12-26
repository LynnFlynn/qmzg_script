#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time,sys,math,operator,os
import win32api,win32gui,win32con
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from win32gui import *
from win32api import *
from PIL import ImageGrab,Image
from functools import reduce
from const import btnDict
from config import cfgConst

class QMZGClass(object):

	def __init__(self):
		self.mouse = PyMouse()

	def test(self):
		print(cfgConst.testModel)
		width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
		height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
		print("{} X {}".format(width,height))

		#打开游戏窗口
		label = "全民主公 - 搜狗高速浏览器"
		try:
			hld = win32gui.FindWindow(None, label)
			win32gui.SetForegroundWindow(hld)
		except error:
			print("Error: 没有找到目标窗口")
			sys.exit()

		#资源秘境
		#self.ziyuan_process()
		#神将府
		#self.shenjiang_process(4,10,1)
		#斩将塔
		#self.zhanjiang_process()
		#军团
		#self.juntuan_process()
		#物资争霸
		#self.wuzi_process()
		#self.wuzi_process()
		#每日签到
		self.qiandao_process()
		return True

	def mouse_click(self,btn_name,img_name=""):
		btn = btnDict.get(btn_name)
		if (cfgConst.testModel):
			print("btn : {}".format(btn.img.rsplit("/")[-1].split(".")[0]))
		result = 100
		_x = btn.x+(btn.w//2)
		_y = btn.y+(btn.h//2)
		time.sleep(0.5)
		self.mouse.move(_x, _y)
		time.sleep(0.5)
		self.mouse.click(_x, _y, 1)
		time.sleep(1)
		print(img_name)
		if not (img_name == "" or img_name is None):
			for i in range(30):
				if self.img_similarity(img_name):
					break
				else:
					time.sleep(2)

	def img_similarity(self,img_name,thr=20):
		img = btnDict.get(img_name)
		src = ImageGrab.grab((img.x, img.y, img.x + img.w, img.y + img.h))
		#img1.save('temp.jpg')
		try:
			dst = Image.open(os.path.join("img", img.img))
		except IOError:
			print("Error: 图片读取失败")
		h1 = src.histogram()
		h2 = dst.histogram()
		diff = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
		if (cfgConst.testModel):
			print("similarity : {}".format(diff))
			if diff > 0:
				src.save("log/{}-{}".format(time.strftime("%Y%m%d%H%M%S"),img.img))
		if diff < thr :
			return True
		else :
			return False



	#资源秘境
	def ziyuan_process(self):
		print("资源秘境")
		time.sleep(1)
		self.mouse_click("ziyuan_in","ziyuan_qiangzhen_in")
		# 强征银币 x3
		self.mouse_click("ziyuan_qiangzhen_in","ziyuan_qiangzhen")
		for i in range(3):
			if not self.img_similarity("ziyuan_qiangzhen_times",0.1) :
				self.mouse_click("ziyuan_qiangzhen","")
			else:
				break
		self.mouse_click("ziyuan_qiangzhen_out","")
		#开采资源
		self.mouse_click("ziyuan_kaicai_in","")
		if self.img_similarity("ziyuan_kaicai_sousuo", 20):
			self.mouse_click("ziyuan_kaicai_sousuo", "ziyuan_kaicai_kaicai")
			self.mouse_click("ziyuan_kaicai_kaicai", "ziyuan_kaicai_in")
			#self.mouse_click("ziyuan_kaicai_out", None)
		#掠夺资源
		self.mouse_click("ziyuan_out","zhanjiang_in")
		return True

	#神将府
	def shenjiang_process(self,val,times,page):
		print("神将府")
		time.sleep(1)
		self.mouse_click("shenjiang_in","shenjiang_pre")
		if page >1:
			self.mouse_click("shenjiang_next","shenjiang_next")
		switch = {
			1: "shenjiang_1",
			2: "shenjiang_2",
			3: "shenjiang_3",
			4: "shenjiang_4"
		}
		if not self.img_similarity("shenjiang_times",1):
			self.mouse_click(switch[val], "shenjiang_ok")
			for i in range(times):
				if self.img_similarity("shenjiang_winning",20):
					self.mouse_click("shenjiang_must","shenjiang_must")
				else:
					self.mouse_click("shenjiang_shitou","shenjiang_shitou")
				self.mouse_click("shenjiang_ok","")
				time.sleep(2)
				self.mouse_click("shenjiang_jueguo_ok","shenjiang_ok")
			self.mouse_click("shenjiang_out","shenjiang_out")
		self.mouse_click("shenjiang_out","zhanjiang_in")
		return True

	# 斩将塔
	def zhanjiang_process(self):
		print("斩将塔")
		time.sleep(1)
		#左-斩将塔
		self.mouse_click("zhanjiang_in","zhanjiang_left_in")
		self.mouse_click("zhanjiang_left_in","zhanjiang_left_chongzhi")
		self.mouse_click("zhanjiang_left_chongzhi","zhanjiang_left_chongzhi_ok")
		self.mouse_click("zhanjiang_left_chongzhi_ok","")
		self.mouse_click("zhanjiang_left_saodang","zhanjiang_left_saodang_ok")
		self.mouse_click("zhanjiang_left_saodang_ok","")
		time.sleep(2)
		self.mouse_click("zhanjiang_left_jieguo_ok","zhanjiang_left_chongzhi")
		self.mouse_click("zhanjiang_out","zhanjiang_in")
		#右-神魔塔
		self.mouse_click("zhanjiang_in","zhanjiang_left_in")
		self.mouse_click("zhanjiang_right_in","zhanjiang_right_chongzhi")
		self.mouse_click("zhanjiang_right_chongzhi","zhanjiang_right_chongzhi_ok")
		self.mouse_click("zhanjiang_right_chongzhi_ok","")
		self.mouse_click("zhanjiang_right_saodang","zhanjiang_right_saodang_ok")
		self.mouse_click("zhanjiang_right_saodang_ok","")
		time.sleep(2)
		self.mouse_click("zhanjiang_right_jieguo_ok","zhanjiang_right_chongzhi")
		self.mouse_click("zhanjiang_out","zhanjiang_in")
		return True

	#军团
	def juntuan_process(self):
		print("军团")
		time.sleep(1)
		self.mouse_click("juntuan_in", "juntuan_out")
		self.mouse_click("juntuan_hongbao", "juntuan_hongbao_title")
		#
		if self.img_similarity("juntuan_hongbao_lingqu",20):
			self.mouse_click("juntuan_hongbao_lingqu", "")
			self.mouse_click("juntuan_hongbao_ok", "")
		else:
			self.mouse_click("juntuan_hongbao_ok", "")
		#
		self.mouse_click("juntuan_out", "zhanjiang_in")

	#物资争霸
	def wuzi_process(self):
		print("物资争霸")
		time.sleep(1)
		self.mouse_click("wuzi_in","wuzi_yijian")
		self.mouse_click("wuzi_yijian","wuzi_kaishi")
		self.mouse_click("wuzi_kaishi","wuzi_yijian_out")
		self.mouse_click("wuzi_yijian_out","wuzi_out")
		self.mouse_click("wuzi_out", "zhanjiang_in")
		return True

	#每日签到
	def qiandao_process(self):
		print("每日签到")
		time.sleep(1)
		#
		self.mouse_click("qiandao_in","qiandao_out")
		if self.img_similarity("qiandao_ok",20):
			self.mouse_click("qiandao_ok","")
		self.mouse_click("qiandao_out","zhanjiang_in")
		#
		self.mouse_click("fuli_in", "fuli_out")
		self.mouse_click("fuli_meiri", "fuli_out")
		if self.img_similarity("fuli_lingqu_1",0.2) and self.img_similarity("fuli_lingqu_2",20):
			self.mouse_click("fuli_lingqu_1","")
			self.mouse_click("fuli_lingqu_2","fuli_meiri_out")
			self.mouse_click("fuli_meiri_ok", "")
		self.mouse_click("fuli_out", "zhanjiang_in")
		#
		self.mouse_click("junxie_in", "junxie_out")
		if self.img_similarity("junxie_lingqu",20):
			self.mouse_click("junxie_lingqu","")
		self.mouse_click("junxie_out", "zhanjiang_in")
		#
		self.mouse_click("shenmo_in", "shenmo_out")
		if not self.img_similarity("shenmo_yiguaji",10):
			self.mouse_click("shenmo_guaji", "shenmo_kaishiguaji")
			self.mouse_click("shenmo_kaishiguaji", "shenmo_guaji_ok")
			self.mouse_click("shenmo_guaji_ok", "shenmo_yiguaji")
		self.mouse_click("shenmo_out", "zhanjiang_in")
		return True

	#群雄争霸
	def qunxiong_process(self):
		print("群雄争霸")
		time.sleep(1)

		return True

	#攻城夺宝
	def gongcheng_process(self):
		print("攻城夺宝")
		time.sleep(1)

		return True
# main
if __name__ == '__main__':
	#ctrl+F1 --> F5
	qmzg = QMZGClass()
	qmzg.test()


