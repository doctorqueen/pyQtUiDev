from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar) 
import numpy as np
import random

class MatplotlibWidget(QMainWindow):    # MatplotLib Widget class 정의.  
    def __init__(self): 
        QMainWindow.__init__(self)  # self 인자 할당하기.  
        loadUi("mplWidgetUI.ui",self) #Ui 파일 로딩
        self.setWindowTitle("PyQt5 & MatplotLib Example GUI")
        self.btn_Generate.clicked.connect(self.update_graph)
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))
    
    def update_graph(self):  #그래프 함수 만들기. 
        fs = 500
        f = random.randint(1,100)
        ts = 1/fs
        length_of_signal = 100
        t = np.linspace(0,1, length_of_signal)

        
        cosine_signal = np.cos(2*np.pi*f*t)
        sin_signal = np.sin(2*np.pi*f*t)

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(t, cosine_signal)#cosine함수 그래프
        self.MplWidget.canvas.axes.plot(t, sin_signal)  #sin함수 그래프 
        self.MplWidget.canvas.axes.legend(('cosinus','sinus'), loc = 'upper right')
        self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')  # cos 함수 와 sin함수의 차이 그래프 그리기. 
        self.MplWidget.canvas.draw()


if __name__ == "__main__":
    app = QApplication([])
    window = MatplotlibWidget()
    window.show()
    app.exec_() # 그래프 그리고 실행해서 화면에 보여주기.  