#!/usr/bin/env python
# -*- coding:utf-8 -*-
class btnDict:
	__dict = {}

	@classmethod
	def get(cls,name):
		return cls.__dict.get(name)

	@classmethod
	def add(cls,name,val):
		cls.__dict[name] = val


class btnConst(btnDict):
	def __init__(self,x,y,w,h,name):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.img ="{}.png".format(name)
		btnDict.add(name,self)

if __name__ == '__main__':
	print(1)

#资源秘境
btnConst(1,1,1,1,"test")
btnConst(630,580,70,70,"ziyuan_in")
btnConst(1570,140,126,76,"ziyuan_out")
btnConst(250,840,60,40,"ziyuan_qiangzhen_in")
btnConst(1010,680,50,30,"ziyuan_qiangzhen_times")
btnConst(890,730,120,40,"ziyuan_qiangzhen")
btnConst(1220,306,46,46,"ziyuan_qiangzhen_out")
btnConst(670,860,136,46,"ziyuan_kaicai_in")
btnConst(1130,720,80,40,"ziyuan_kaicai_sousuo")
btnConst(680,720,100,50,"ziyuan_kaicai_kaicai")
btnConst(1350,280,40,40,"ziyuan_kaicai_out")
btnConst(980,806,40,20,"ziyuan_lveduo_times")
btnConst(940,860,110,40,"ziyuan_lveduo_in")
btnConst(1540,840,50,50,"ziyuan_lveduo_lveduo")
btnConst(920,890,100,40,"ziyuan_lveduo_jieshu")
btnConst(910,690,80,30,"ziyuan_lveduo_ok")
#神将府
btnConst(810,550,90,60,"shenjiang_in")
btnConst(1400,590,50,20,"shenjiang_next")
btnConst(460,590,50,20,"shenjiang_pre")
btnConst(1340,850,70,30,"shenjiang_times")
btnConst(850,790,0,0,"shenjiang_1")
btnConst(850,790,0,0,"shenjiang_2")
btnConst(850,790,0,0,"shenjiang_3")
btnConst(1250,790,0,0,"shenjiang_4")
btnConst(880,700,70,70,"shenjiang_shitou")
btnConst(1250,690,90,90,"shenjiang_must")
btnConst(1040,800,140,46,"shenjiang_ok")
	# F 850,750,130,46 T 850,790,130,40
btnConst(910,790,0,0,"shenjiang_jueguo_ok")
btnConst(500,420,76,76,"shenjiang_winning")
btnConst(1420,200,50,40,"shenjiang_out")
#斩将塔
btnConst(990,500,70,130,"zhanjiang_in")
btnConst(1420,220,0,0,"zhanjiang_out")
btnConst(720,500,200,160,"zhanjiang_left_in")
btnConst(890,280,50,30,"zhanjiang_left_times")
btnConst(1060,840,120,36,"zhanjiang_left_chongzhi")
btnConst(770,660,90,40,"zhanjiang_left_chongzhi_ok")
btnConst(1280,840,120,36,"zhanjiang_left_saodang")
btnConst(770,650,90,40,"zhanjiang_left_saodang_ok")
btnConst(900,750,70,40,"zhanjiang_left_jieguo_ok")
btnConst(970,500,200,160,"zhanjiang_right_in")
btnConst(880,280,50,30,"zhanjiang_right_times")
btnConst(1030,850,140,36,"zhanjiang_right_chongzhi")
btnConst(770,660,90,40,"zhanjiang_right_chongzhi_ok")
btnConst(1260,850,140,36,"zhanjiang_right_saodang")
btnConst(780,676,90,40,"zhanjiang_right_saodang_ok")
btnConst(910,750,100,50,"zhanjiang_right_jieguo_ok")
#军团
btnConst(1180,600,80,70,"juntuan_in")
btnConst(490,800,66,36,"juntuan_hongbao")
btnConst(890,200,120,70,"juntuan_hongbao_title")
btnConst(890,790,100,46,"juntuan_hongbao_lingqu")
btnConst(890,790,100,46,"juntuan_hongbao_ok")
btnConst(1400,210,40,40,"juntuan_out")
#物资争霸
btnConst(1440,500,70,70,"wuzi_in")
btnConst(1300,770,90,36,"wuzi_yijian")
btnConst(1020,820,110,30,"wuzi_kaishi")
btnConst(1170,240,46,46,"wuzi_yijian_out")
btnConst(1380,200,36,36,"wuzi_out")
#每日签到
btnConst(1320,230,30,30,"qiandao_in")
btnConst(1410,200,46,46,"qiandao_out")
btnConst(1200,440,120,60,"qiandao_ok")
btnConst(1230,230,30,30,"fuli_in")
btnConst(1400,240,46,46,"fuli_out")
btnConst(500,390,120,60,"fuli_meiri")
btnConst(1250,620,110,40,"fuli_lingqu_1")
btnConst(1250,830,110,40,"fuli_lingqu_2")
btnConst(780,660,80,40,"fuli_meiri_ok")
btnConst(1180,370,40,40,"fuli_meiri_out")
btnConst(870,920,40,40,"junxie_in")
btnConst(1170,660,100,40,"junxie_lingqu")
btnConst(1380,210,40,40,"junxie_out")
btnConst(1220,300,46,36,"shenmo_in")
btnConst(790,460,70,30,"shenmo_yiguaji")
btnConst(800,400,50,40,"shenmo_guaji")
btnConst(900,730,90,26,"shenmo_kaishiguaji")
btnConst(790,680,66,26,"shenmo_guaji_ok")
btnConst(1440,210,40,40,"shenmo_out")
btnConst(1600,390,20,20,"xunbao_in")
btnConst(1210,450,50,50,"xunbao_jin")
btnConst(790,550,50,50,"xunbao_jin_one")
btnConst(1200,596,90,20,"xunbao_free")
btnConst(1070,786,50,30,"xunbao_ok")
btnConst(1386,240,36,36,"xunbao_out")
#国战
btnConst(1620,770,70,50,"guozhan_in")
btnConst(1650,710,30,30,"guozhan_xinxi_in")
btnConst(1400,200,40,40,"guozhan_xinxi_out")
btnConst(1080,260,86,30,"guozhan_juanzeng_in")
btnConst(910,470,86,26,"guozhan_juanzeng_times")
btnConst(1050,510,40,40,"guozhan_juanzeng_plus")
btnConst(780,660,80,30,"guozhan_juanzeng_ok")
btnConst(1190,380,40,40,"guozhan_juanzeng_out")
btnConst(1650,810,30,40,"guozhan_xuanba_in")
btnConst(530,690,70,36,"guozhan_xuanba_mobai_1")
btnConst(760,680,90,30,"guozhan_xuanba_putongmobai")
btnConst(1466,266,36,36,"guozhan_xuanba_out")
btnConst(1210,270,40,40,"guozhan_mobai_out")
btnConst(1620,896,30,10,"guozhan_out")
#攻城夺宝
btnConst(1140,310,30,30,"duobao_in")
btnConst(1500,210,30,30,"duobao_out")
btnConst(420,600,40,40,"duobao_city_1")
btnConst(800,580,40,40,"duobao_city_2")
btnConst(1080,570,40,40,"duobao_city_3")
btnConst(1370,580,40,40,"duobao_city_4")
btnConst(920,780,60,30,"duobao_tiaozhan")
btnConst(1060,780,30,30,"duobao_tiaoguo")
btnConst(930,680,60,30,"duobao_ok")
btnConst(900,830,80,30,"duobao_ok_2")
btnConst(910,670,40,40,"duobao_jiachen")
btnConst(810,810,40,30,"duobao_chongzhi")