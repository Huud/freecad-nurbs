
# auswertung heel -Linie



import FreeCAD,FreeCADGui
App=FreeCAD
Gui=FreeCADGui

from PySide import QtGui
import Part,Mesh,Draft,Points

import numpy as np
import random

import os, nurbswb

global __dir__
__dir__ = os.path.dirname(nurbswb.__file__)
print __dir__

import nurbswb.spreadsheet_lib
reload (nurbswb.spreadsheet_lib)
from nurbswb.spreadsheet_lib import ssa2npa, npa2ssa, cellname


def run():
	aktiv=App.ActiveDocument

	fn=FreeCAD.ParamGet('User parameter:Plugins/shoe').GetString("height profile")
	if fn=='':
		fn= __dir__+"/../testdata/heelsv3.fcstd"
		FreeCAD.ParamGet('User parameter:Plugins/shoe').SetString("height profile",fn)

	dok=FreeCAD.open(fn)

	sss=dok.findObjects("Sketcher::SketchObject")
	s=sss[0]

	c=s.Shape.Edge1.Curve

	pts=c.discretize(86)

	mpts=[]
	for i in [0,15,25,35,45,55,65,75,85]:
#		print pts[i]
		mpts.append(pts[i])


	App.closeDocument(dok.Name)

	dok2=aktiv
	App.setActiveDocument(dok2.Name)

	ss=dok2.Spreadsheet




	# daten ins spreadsheet schreiben
	for s in range(8):
		cn=cellname(s+3,9)
		ss.set(cn,str(mpts[-s-1].y))

	# ferse hochlegen
	for j in range(7):
		cn=cellname(j+2,26)
		ss.set(cn,str((mpts[-1].y)))


	dok2.recompute()
	import nurbswb.sole
	reload(nurbswb.sole)
	nurbswb.sole.run()
	dok2.recompute()
