#coding:utf-8
import time,sys,math,operator
import win32api,win32gui,win32con
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from win32gui import *
from win32api import *
from PIL import ImageGrab,Image
from functools import reduce
from const import btnConst


class QMZGClass(object):

	def __init__(self):
		self.mouse = PyMouse()
		self.testModel = True

	def test(self):

		width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
		height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
		print("{} X {}".format(width,height))

		#打开游戏窗口
		label = "全民主公 - 搜狗高速浏览器"
		hld = win32gui.FindWindow(None, label)
		win32gui.SetForegroundWindow(hld)

		#资源秘境
		#self.ziyuan_process()
		#神将府
		#self.shenjiang_process(4,10,1)
		#斩将塔
		#self.zhanjiang_process()
		#物资争霸
		#self.wuzi_process()
		#self.wuzi_process()
		#每日签到
		self.qiandao_process()
		return True

	def mouse_click(self,btn,res,copy=False):
		if (self.testModel):
			print("btn : {}".format(btn["img"]))
		result = 100
		_x = btn["x"]+int(btn["w"]/2)
		_y = btn["y"]+int(btn["h"]/2)
		self.mouse.move(_x, _y)
		time.sleep(0.5)
		self.mouse.click(_x, _y, 1)
		time.sleep(0.5)
		for i in range(3):
			if res is None:
				time.sleep(1)
				break
			if result <20 :
				break
			if not res is None:
				time.sleep(2)
				result = self.img_similarity(res)
			else:
				result = 0



	def img_similarity(self,res):
		img1 = ImageGrab.grab((res["x"], res["y"], res["x"] + res["w"], res["y"] + res["h"]))
		#img1.save('temp.jpg')
		img2 = Image.open(res["img"])
		h1 = img1.histogram()
		h2 = img2.histogram()
		result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
		if (self.testModel):
			print("similarity : {}".format(result))
		return result

	#资源秘境
	def ziyuan_process(self):
		print("资源秘境")
		time.sleep(1)
		self.mouse_click(btnConst.ziyuan_in,btnConst.ziyuan_qiangzhen_in)
		# 强征银币 x3
		self.mouse_click(btnConst.ziyuan_qiangzhen_in,btnConst.ziyuan_qiangzhen)
		if not self.img_similarity(btnConst.ziyuan_qiangzhen_times) <  0.1:
			for i in range(3):
				self.mouse_click(btnConst.ziyuan_qiangzhen,None)
		self.mouse_click(btnConst.ziyuan_qiangzhen_out,None)
		#开采资源
		#掠夺资源
		self.mouse_click(btnConst.ziyuan_out,btnConst.zhanjiang_in)
		return True

	#神将府
	def shenjiang_process(self,val,times,page):
		print("神将府")
		time.sleep(1)
		self.mouse_click(btnConst.shenjiang_in,btnConst.shenjiang_pre)
		if page >1:
			self.mouse_click(btnConst.shenjiang_next,btnConst.shenjiang_next)
		switch = {
			1: btnConst.shenjiang_1,
			2: btnConst.shenjiang_2,
			3: btnConst.shenjiang_3,
			4: btnConst.shenjiang_4
		}
		self.mouse_click(switch[val], btnConst.shenjiang_ok)
		for i in range(times):
			if self.img_similarity(btnConst.shenjiang_winning)<20:
				self.mouse_click(btnConst.shenjiang_must,btnConst.shenjiang_must)
			else:
				self.mouse_click(btnConst.shenjiang_shitou,btnConst.shenjiang_shitou)
			self.mouse_click(btnConst.shenjiang_ok,None)
			time.sleep(2)
			self.mouse_click(btnConst.shenjiang_jueguo_ok,btnConst.shenjiang_ok)
		self.mouse_click(btnConst.shenjiang_out,btnConst.shenjiang_out)
		self.mouse_click(btnConst.shenjiang_out,btnConst.zhanjiang_in)
		return True

	# 斩将塔
	def zhanjiang_process(self):
		print("斩将塔")
		time.sleep(1)
		#左-斩将塔
		self.mouse_click(btnConst.zhanjiang_in,btnConst.zhanjiang_left_in)
		self.mouse_click(btnConst.zhanjiang_left_in,btnConst.zhanjiang_left_chongzhi)
		self.mouse_click(btnConst.zhanjiang_left_chongzhi,btnConst.zhanjiang_left_chongzhi_ok)
		self.mouse_click(btnConst.zhanjiang_left_chongzhi_ok,None)
		self.mouse_click(btnConst.zhanjiang_left_saodang,btnConst.zhanjiang_left_saodang_ok)
		self.mouse_click(btnConst.zhanjiang_left_saodang_ok,None)
		time.sleep(2)
		self.mouse_click(btnConst.zhanjiang_jieguo_ok,btnConst.zhanjiang_chongzhi)
		self.mouse_click(btnConst.zhanjiang_out,btnConst.zhanjiang_in)
		#右-神魔塔
		self.mouse_click(btnConst.zhanjiang_in,btnConst.zhanjiang_left_in)
		self.mouse_click(btnConst.zhanjiang_right_in,btnConst.zhanjiang_right_chongzhi)
		self.mouse_click(btnConst.zhanjiang_right_chongzhi,btnConst.zhanjiang_right_chongzhi_ok)
		self.mouse_click(btnConst.zhanjiang_right_chongzhi_ok,None)
		self.mouse_click(btnConst.zhanjiang_right_saodang,btnConst.zhanjiang_right_saodang_ok)
		self.mouse_click(btnConst.zhanjiang_right_saodang_ok,None)
		time.sleep(2)
		self.mouse_click(btnConst.zhanjiang_jieguo_ok,btnConst.zhanjiang_chongzhi)
		self.mouse_click(btnConst.zhanjiang_out,btnConst.zhanjiang_in)
		return True

	#物资争霸
	def wuzi_process(self):
		print("物资争霸")
		time.sleep(1)
		self.mouse_click(btnConst.wuzi_in,btnConst.wuzi_yijian)
		self.mouse_click(btnConst.wuzi_yijian,btnConst.wuzi_kaishi)
		self.mouse_click(btnConst.wuzi_kaishi,btnConst.wuzi_yijian_out)
		self.mouse_click(btnConst.wuzi_yijian_out,btnConst.wuzi_out)
		self.mouse_click(btnConst.wuzi_out, btnConst.zhanjiang_in)
		return True

	#每日签到
	def qiandao_process(self):
		print("每日签到")
		time.sleep(1)
		self.mouse_click(btnConst.qiandao_in,btnConst.qiandao_out)
		if self.img_similarity(btnConst.qiandao_ok) < 20:
			self.mouse_click(btnConst.qiandao_ok,None)
		self.mouse_click(btnConst.qiandao_out,btnConst.zhanjiang_in)

		self.mouse_click(btnConst.fuli_in, btnConst.fuli_out)
		self.mouse_click(btnConst.fuli_meiri, btnConst.fuli_out)
		if self.img_similarity(btnConst.fuli_lingqu_1) < 20:
			self.mouse_click(btnConst.fuli_lingqu_1,None)
		if self.img_similarity(btnConst.fuli_lingqu_2) < 20:
			self.mouse_click(btnConst.fuli_lingqu_2,btnConst.fuli_meiri_out)
			self.mouse_click(btnConst.fuli_meiri_ok, None)
		self.mouse_click(btnConst.fuli_out, btnConst.zhanjiang_in)
		return True
# main
if __name__ == '__main__':
	#ctrl+F1 --> F5
	qmzg = QMZGClass()
	qmzg.test()

