'''

import nurbswb.needle_models
reload(nurbswb.needle_models)

#App.ActiveDocument.MyNeedle.Proxy.getExampleModel(nurbswb.needle_models.modelSpoon)
myNeedle=App.ActiveDocument.MyNeedle

#myNeedle.Proxy.getExampleModel(nurbswb.needle_models.modelEd4)

myNeedle.Proxy.getExampleModel(nurbswb.needle_models.modelSpoon)

'''

import numpy as np


class modelA():
	''' halbscharfe kante '''

	curve=[
			[0,0,0],
			[0,29,0],[0,30,0],[0,31,0],
			[100,30,25],
			[100,180,25],
			[-20,180,-5],
			[-20,-30,-5],
			[-100,-30,-25],[-99,-30,-25],
			[-100,-129,-25],[-100,-130,-25],[-99,-130,-25],
			[0,-40,-0]
		]

	bb= [[0,0,0],[0,0,50],[0,0,100],[0,0,200],[0,0,400],[0,0,499],[0,0,500],[0,0,600]]
	twister=[[0,0,0],[0,-25,0],[0,0,0],[00,0,0],[0,-25,0],[0,25,0],[0,25,0],[0,0,00]]
	sc=[[1,0],[1,0],[1,0],[1,0],[1,0],[1.3,0],[1.3,0],[1.,0]]


class modelB():
	''' schiefe abschlussebene '''

	curve=[
			[0,0,0],
			[0,29,0],[0,30,0],[0,31,0],
			[100,30,25],
			[100,180,25],
			[-20,180,-5],
			[-20,-30,-5],
			[-100,-30,-25],[-99,-30,-25],
			[-100,-129,-25],[-100,-130,-25],[-99,-130,-25],
			[0,-40,-0]
		]

	bb= [[0,0,0],[0,0,50],[0,0,100],[0,0,200],[0,0,400],[0,0,499],[0,0,500],[0,0,501],[0,0,800]]
	twister=[[0,0,0],[0,-25,0],[0,0,0],[00,0,0],[0,-25,0],[0,25,0],[0,25,0],[0,25,0],[20,30,40]]
	sc=[[1,0],[1,0],[1,0],[1,0],[1,0],[1.3,0],[1.3,0],[1.3,0],[1.5,0]]


class modelC():
	''' rotate along z-axis '''

	curve=[
			[0,0,0],
			[0,29,0],[0,30,0],[0,31,0],
			[100,30,25],
			[100,180,25],
			[-20,180,-5],
			[-20,-30,-5],
			[-100,-30,-25],[-99,-30,-25],
			[-100,-129,-25],[-100,-130,-25],[-99,-130,-25],
			[0,-40,-0]
		]

	bb= [[0,0,0],[0,0,50],[0,0,100],[0,0,200],[0,0,400],[0,0,499],[0,0,500],[0,0,501],[0,0,800]]
	twister=[[0,0,0],[0,0,40],[0,0,-20],[0,0,-20],[0,0,30],[0,0,0],[0,0,0],[0,0,0],[0,0,60]]
	sc=[[1,0],[1,0],[1,0],[1,0],[1,0],[1.3,0],[1.3,0],[1.3,0],[1.5,0]]


class modelD():
	''' rotate along y-axis '''

	curve=[
			[0,0,0],
			[0,29,0],[0,30,0],[0,31,0],
			[100,30,25],
			[100,180,25],
			[-20,180,-5],
			[-20,-30,-5],
			[-100,-30,-25],[-99,-30,-25],
			[-100,-129,-25],[-100,-130,-25],[-99,-130,-25],
			[0,-40,-0]
		]

	bb= [[0,0,0],[0,0,50],[0,0,100],[0,0,200],[0,0,400],[0,0,499],[0,0,500],[0,0,501],[0,0,800]]
	twister=[[0,0,0],[0,45,0],[0,0,0],[00,0,0],[0,-45,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	sc=[[1,0],[1,0],[1,0],[1,0],[1,0],[1.3,0],[1.3,0],[1.3,0],[1.5,0]]




class modelE():
	''' rotate along x-axis '''

	curve=[
			[0,0,0],
			[0,29,0],[0,30,0],[0,31,0],
			[100,30,25],
			[100,180,25],
			[-20,180,-5],
			[-20,-30,-5],
			[-100,-30,-25],[-99,-30,-25],
			[-100,-129,-25],[-100,-130,-25],[-99,-130,-25],
			[0,-40,-0]
		]

	bb= [[0,0,0],[0,0,50],[0,0,100],[0,0,200],[0,0,400],[0,0,499],[0,0,500],[0,0,501],[0,0,800]]
	twister=[[0,0,0],[35,0,0],[35,0,0],[00,0,0],[-45,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
	sc=[[1,0],[1,0],[1,0],[1,0],[1,0],[1.3,0],[1.3,0],[1.3,0],[1.5,0]]


class modelEd0():
	''' edge tests base '''

	curve=[
			[0,0,0],
			[0,40,0],[80,40,0],[80,80,0],
			[-80,80,0],
			[-80,-80,0],
			[80,-80,0],
			[80,-40,0],
			[0,-40,0]
		]

	bb=[[0,0,0],[0,0,100],[0,0,200],[0,0,300],[0,0,400]]
	twister=[[0,0,0]]*len(bb)
	sc=[[1,0]]*len(bb)



class modelEd1():
	''' edge tests base '''

	curve=[
			[0,0,0],[0,0,0],
			[0,40,0],[80,40,0],[80,80,0],
			[-80,80,0],
			[-80,-80,0],
			[80,-80,0],
			[80,-40,0],
			[0,-40,0]
		]

	bb=[[0,0,0],[0,0,100],[0,0,200],[0,0,300],[0,0,400]]
	twister=[[0,0,0]]*5
	sc=[[1,0]]*5





class modelEd2():
	''' edge tests roundings '''

	curve=[
			[0,0,0],[0,0,0],
			[0,39,0],[0,40,0],[0,40,1],
			[79,40,0],[80,40,0],[80,41,0],
			[80,60,0],[80,80,0],[60,80,0],
			[-60,80,0],[-80,80,0],[-80,60,0],
			[-80,-79,0],[-80,-80,0],[-79,-80,0],
			[79,-80,0],[80,-80,0],[80,-79,0],
			[80,-60,0],[80,-40,0],[60,-40,0],
			[20,-40,0],[0,-40,0],[0,-20,0],
		]

	bb=[[0,0,0],[0,0,100],[0,0,200],[0,0,300],[0,0,400]]
	twister=[[0,0,0]]*5
	# sc=[[1,0]]*5
	sc=[[1,0],[1,0],[3,0],[0.3,0],[1,0]]



class modelEd3():
	''' edge tests backbone roundings base'''

	curve=[
			[0,0,0],[0,0,0],
			[0,39,0],[0,40,0],[0,40,1],
			[79,40,0],[80,40,0],[80,41,0],
			[80,60,0],[80,80,0],[60,80,0],
			[-60,80,0],[-80,80,0],[-80,60,0],
			[-80,-79,0],[-80,-80,0],[-79,-80,0],
			[79,-80,0],[80,-80,0],[80,-79,0],
			[80,-60,0],[80,-40,0],[60,-40,0],
			[20,-40,0],[0,-40,0],[0,-20,0],
		]

	bb=[[0,0,0],[0,0,100],[100,0,100],[100,0,300],[0,0,300],[0,0,400],[-100,0,400],[-100,0,500],[0,0,500],[0,0,600]]
	twister=[[0,0,0]]*len(bb)
	sc=[[1,0]]*len(bb)


class modelEd4():
	''' edge tests backbone roundings '''

	curve=[
			[0,0,0],[0,0,0],
			[0,39,0],[0,40,0],[0,40,1],
			[79,40,0],[80,40,0],[80,41,0],
			[80,60,0],[80,80,0],[60,80,0],
			[-60,80,0],[-80,80,0],[-80,60,0],
			[-80,-79,0],[-80,-80,0],[-79,-80,0],
			[79,-80,0],[80,-80,0],[80,-79,0],
			[80,-60,0],[80,-40,0],[60,-40,0],
			[20,-40,0],[0,-40,0],[0,-20,0],
		]

	bb=[[0,0,0],
		[0,0,80],[0,0,100],[20,0,100],
		[80,0,100],[100,0,100],[100,0,120],
		
		[100,0,299],[100,0,300],[99,0,300],
		[1,0,300],[0,0,300],[0,0,301],
		
		[0,0,399],[0,0,400],[-1,0,400],
		[-70,0,400],[-100,0,400],[-100,0,430],
		
		[-100,0,499],[-100,0,500],[-99,0,500],
		[-40,0,500],[0,0,500],[0,0,540],
		
		[0,0,600]]
	twister=[[0,0,0]]*len(bb)
	sc=[[1,0]]*len(bb)



class modelSpoon():

	curve=[
			[0,0,0], 
			[0,50,10],
			[0,99,40],[0,100,40],[0,100,35],
			[0,50,10],
			[0,0,-10],
			[0,-50,10],
			[0,-100,35],[0,-100,40],[0,-99,40],
			[0,-50,10],
		]

	bb=[[0,0,0],[150,0,-20],[250,0,-10],[297,0,20],[300,0,20]]
	twister=[[0,0,0],[0,45,0],[0,70,0],[0,90,0],[0,90,0]]
	sc=[[1,1],[2.0,1.7],[1.3,1.],[0.8,0.02],[0.01,0.001]]



if 0:

	App.ActiveDocument.MyNeedle.Proxy.getExampleModel(nurbswb.needle_models.modelSpoon)
	App.ActiveDocument.MyNeedle.Proxy.getExampleModel(nurbswb.needle_models.modelEd4)

'''
	modelA(ss)
	modelB(ss)
	modelC(ss)
	modelD(ss)

	modelE(ss)


	modelEd0(ss)
	modelEd1(ss)
	modelEd2(ss)
	modelEd3(ss)
	modelEd4(ss)


	modelSpoon(ss)
'''




class modelXY():

	curve=[
			[0,0,0], 
			[0,399,0],[0,400,0],
			[0,400,100],[0,400,101],
			[0,0,400],
			[0,-100,101],[0,-100,100],
			[0,-100,0],[0,-99,0],
		]

	bb=[[0,0,0],[200,0,0],[400,0,0],[600,0,0],[1000,0,00],[2001,0,00]]
	twister=[[0,-90,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,90,0]]
	sc=[[1,1]]*6
	sc=[[2,1],[3,5],[4,5],[4,5],[3,5],[2,1]]


class modelX():

	curve=[
			[0,0,0], 
			[0,299,-30],[0,300,-30],
			[0,349,-300],[0,350,-300],
			[0,399,-500],[0,400,-500],
			[0,400,100],[0,400,101],
			[0,0,150],
			[0,-100,101],[0,-100,100],
			[0,-100,-100],[0,-99,-100],
		]

	bb=[[0,0,0],[200,0,0],[300,0,0],[410,0,0],[1000,0,00],[2001,0,00]]
	twister=[[0,-90,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,90,0]]
	sc=[[1,1]]*6
	sc=[[0.2,0.1],[3,1],[2.1,0.1],[.1,0.1],[.1,0.4],[.2,.4]]



class model():

	def __init__(self,bbl=5):
		self.curve=[
				[0,0,0], 
				[0,299,-30],[0,300,-30],
				[0,349,-300],[0,350,-300],
				[0,399,-500],[0,400,-500],
				[0,400,100],[0,400,101],
				[0,0,150],
				[0,-100,101],[0,-100,100],
				[0,-100,-100],[0,-99,-100],
			]

		self.sc=[[1,1]]*bbl
		self.twister=[[0,0,0]]*bbl
		self.bb=[[0,0,100*i] for i in range(bbl)]



class modelS():

	def __init__(self,bbl=12):
		self.curve=[
				[200,0,0],
				[200,600,0],
				[-200,400,0],[-200,0,0],
			]

		self.sc=[[1,1]]*bbl

		self.twister=[[0,0,0]]*bbl
		self.twister[3]=[0,0,50]
		self.twister[4]=[0,60,0]
		self.twister[5]=[70,0,0]

		self.bb=[[0,0,300*i] for i in range(bbl)]
		self.bb[10][1]=300
		self.bb[8][0]=300




class modelBanana(model):
	def __init__(self):
		model.__init__(self)

		# 3 edges model
		# self.curve=[[0,0,0], [100,100,0],[-100,100,0],[-30,0,0]]

		# 4 edges model
		self.curve=np.array([
					[0,0,0], 
					[60,0,0],[65,0,0],
					[80,120,0],[77,125,0],
					[-70,150,0],[-80,150,0],[-80,140,0], # very strong edge
					[-100,0,0], # very soft edge
					[-30,0,0]
				])

		self.sc=np.array([
					[0.8,0.8],[1,1],[1,1], # blossom
					[4,4],[5,5],[4,3], # belly
					[1,1],[1,1.4],[1.3,1.3] # stalk
			])

		self.bb=np.array([
					[0,-40,100],[0,-30,110],[0,0,120], # blossom
					[0,0,140],[0,100,600],[0,0,1200], # belly
					[0,0,1250],[0,0,1290],[0,-200,1450]  # stalk
			])

		self.twister=np.array([
				[-30,-15,-10,-10,15,30,40,50,80], # Crooked banana y
				[0,0,0,0,-30,0,0,20,20], # some torsion of blossom and stalk: y,z
				[15,10,0,0,0,10,0,0,30]
			]).swapaxes(0,1)

'''
class modelMiniBanana(modelBanana):
	def __init__(self):
		modelBanana.__init__(self)
		self.curve *= 0.1
		self.bb *= 0.1

App.ActiveDocument.MyNeedle.Proxy.getExampleModel(modelMiniBanana)
App.ActiveDocument.MyNeedle.Shape.BoundBox.DiagonalLength

class modelMiniBanana(modelBanana):
	def __init__(self):
		modelBanana.__init__(self)
		self.curve *= 0.02
		self.bb *= 0.02

App.ActiveDocument.MyNeedle.Proxy.getExampleModel(modelMiniBanana)
App.ActiveDocument.MyNeedle.Shape.BoundBox.DiagonalLength
'''


if __name__=='__main__':
	# testcase

	class modelY(modelBanana):
		pass

	App.ActiveDocument.MyNeedle.Proxy.lock=False
	App.ActiveDocument.MyNeedle.Proxy.getExampleModel(modelY)
