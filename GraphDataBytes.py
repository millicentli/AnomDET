from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
import serial, csv, struct
from time import localtime, strftime

ser = serial.Serial('/dev/cu.LightBlue-Bean')
file = open('/Users/Millicent/Desktop/csvfile.csv', 'r+')
writer = csv.writer(file)
app = QtGui.QApplication([])
win = pg.GraphicsWindow()
win.showMaximized()
p1 = win.addPlot(title="X (Roll) vs No. of Samples")
p2 = win.addPlot(title="Y (Pitch) vs No. of Samples")
p3 = win.addPlot(title="Z (Yaw) vs No. of Samples")
pg.setConfigOptions(antialias=True)
p1.setLabel('left', text="X value")
p1.setLabel('bottom', text="No. of Samples")
p2.setLabel('left', text="Y value")
p2.setLabel('bottom', text="No. of Samples")
p3.setLabel('left', text="Z value")
p3.setLabel('bottom', text="No. of Samples")
curve1 = p1.plot()
curve2 = p2.plot()
curve3 = p3.plot()
data1 = []
data2 = []
data3 = []

def update():
	global curve, data, pos
	if ser.readline():
		#print strftime("%H:%M:%S", localtime())
	#line = ser.readline()
	#vals = line.split()
		x = struct.unpack_from('<L', ser.read(4))
		y = struct.unpack_from('<L', ser.read(4))
		z = struct.unpack_from('<L', ser.read(4))	
	#writer.writerow([vals[0], vals[1], vals[2], strftime("%H:%M:%S", localtime())])
		writer.writerow([x[0], y[0], z[0], strftime("%H:%M:%S", localtime())])
		a = float(x[0])
		b = float(y[0])
		c = float(z[0])
		data1.append(a)
		data2.append(b)
		data3.append(c)
		if len(data1 and data2 and data3) > 60:
			data1[:] = data1[1:]
			data2[:] = data2[1:]
			data3[:] = data3[1:]
		curve1.setData(np.array(data1))
		curve2.setData(np.array(data2))
		curve3.setData(np.array(data3))
		app.processEvents()
	
	
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()