#coding:utf-8
import time,sys,math,operator,os
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
		self.shenjiang_process(4,10,2)
		#斩将塔
		#self.zhanjiang_process()
		#物资争霸
		#self.wuzi_process()
		#self.wuzi_process()
		#每日签到
		#self.qiandao_process()
		return True

	def mouse_click(self,btn,img):
		if (self.testModel):
			print("btn : {}".format(btn.img.rsplit("/")[-1].split(".")[0]))
		result = 100
		_x = btn.x+(btn.w//2)
		_y = btn.y+(btn.h//2)
		time.sleep(0.5)
		self.mouse.move(_x, _y)
		time.sleep(0.5)
		self.mouse.click(_x, _y, 1)
		time.sleep(1)
		if not img is None:
			for i in range(30):
				if self.img_similarity(img):
					break
				else:
					time.sleep(2)

	def img_similarity(self,img,thr=20):
		src = ImageGrab.grab((img.x, img.y, img.x + img.w, img.y + img.h))
		#img1.save('temp.jpg')
		dst = Image.open(os.path.join("img", img.img))
		h1 = src.histogram()
		h2 = dst.histogram()
		diff = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
		if (self.testModel):
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
		self.mouse_click(btnConst.ziyuan_in,btnConst.ziyuan_qiangzhen_in)
		# 强征银币 x3
		self.mouse_click(btnConst.ziyuan_qiangzhen_in,btnConst.ziyuan_qiangzhen)
		for i in range(3):
			if not self.img_similarity(btnConst.ziyuan_qiangzhen_times,0.1) :
				self.mouse_click(btnConst.ziyuan_qiangzhen,None)
			else:
				break
		self.mouse_click(btnConst.ziyuan_qiangzhen_out,None)
		#开采资源
		self.mouse_click(btnConst.ziyuan_kaicai_in,None)
		if self.img_similarity(btnConst.ziyuan_kaicai_sousuo, 20):
			#self.mouse_click(btnConst.ziyuan_kaicai_sousuo, None)
			self.mouse_click(btnConst.ziyuan_kaicai_out, None)
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
		if not self.img_similarity(btnConst.shenjiang_times,1):
			self.mouse_click(switch[val], btnConst.shenjiang_ok)
			for i in range(times):
				if self.img_similarity(btnConst.shenjiang_winning,20):
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
		self.mouse_click(btnConst.zhanjiang_left_jieguo_ok,btnConst.zhanjiang_left_chongzhi)
		self.mouse_click(btnConst.zhanjiang_out,btnConst.zhanjiang_in)
		#右-神魔塔
		self.mouse_click(btnConst.zhanjiang_in,btnConst.zhanjiang_left_in)
		self.mouse_click(btnConst.zhanjiang_right_in,btnConst.zhanjiang_right_chongzhi)
		self.mouse_click(btnConst.zhanjiang_right_chongzhi,btnConst.zhanjiang_right_chongzhi_ok)
		self.mouse_click(btnConst.zhanjiang_right_chongzhi_ok,None)
		self.mouse_click(btnConst.zhanjiang_right_saodang,btnConst.zhanjiang_right_saodang_ok)
		self.mouse_click(btnConst.zhanjiang_right_saodang_ok,None)
		time.sleep(2)
		self.mouse_click(btnConst.zhanjiang_right_jieguo_ok,btnConst.zhanjiang_right_chongzhi)
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
		if self.img_similarity(btnConst.qiandao_ok,20):
			self.mouse_click(btnConst.qiandao_ok,None)
		self.mouse_click(btnConst.qiandao_out,btnConst.zhanjiang_in)

		self.mouse_click(btnConst.fuli_in, btnConst.fuli_out)
		self.mouse_click(btnConst.fuli_meiri, btnConst.fuli_out)
		if self.img_similarity(btnConst.fuli_lingqu_1,0.2) and self.img_similarity(btnConst.fuli_lingqu_2,20):
			self.mouse_click(btnConst.fuli_lingqu_1,None)
			self.mouse_click(btnConst.fuli_lingqu_2,btnConst.fuli_meiri_out)
			self.mouse_click(btnConst.fuli_meiri_ok, None)
		self.mouse_click(btnConst.fuli_out, btnConst.zhanjiang_in)

		self.mouse_click(btnConst.junjie_in, btnConst.junjie_out)
		if self.img_similarity(btnConst.junjie_lingqu,20):
			self.mouse_click(btnConst.junjie_lingqu,None)
		self.mouse_click(btnConst.junjie_out, btnConst.zhanjiang_in)
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


