import sys,string,threading,time
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyAPRS_ISpass_ui import *
import socket
class APMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(APMainWindow,self).__init__(parent)        
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)
    
    def calculate(self):
        callsignToCalc=self.lineEdit.text()
        self.lineEdit_2.setText("calculating...")
        #time.sleep(3)
        result=self.aprspass(callsignToCalc)
        self.lineEdit_2.setText(str(result))



    def aprspass(self,callsign):
        #deal with varient inputs
        callsign=callsign.strip()
        callsign=callsign.split("-")[0]
        callsign=callsign.upper()
        #initialize hash
        hash=0x73e2
        index=0
        length=len(callsign)
        while(index<length):
            hash=hash^(ord(callsign[index])<<8)
            index+=1
            if(index<length):                
                hash=hash^(ord(callsign[index]))
            else:
                hash=hash
            index+=1
        return hash&0x7fff
        



if __name__=='__main__':
    app=QApplication(sys.argv)
    myWin = APMainWindow()
    myWin.show()
    sys.exit(app.exec_())