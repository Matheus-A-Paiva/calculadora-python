import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from cal import Ui_MainWindow

class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        buttons =[self.push_0,self.push_1,self.push_2,self.push_3,self.push_4,
                  self.push_5,self.push_6,self.push_7,self.push_8,self.push_9,
                  self.push_ad,self.push_div,self.push_dot,self.push_mult,self.push_sub,]
        
        for button in buttons:
            button.clicked.connect(self.button_clicked)
        
        self.push_clear.clicked.connect(self.clear)
        self.push_del.clicked.connect(self.delete)
        self.push_equal.clicked.connect(self.equal)
        
        

    def button_clicked(self):
            sender = self.sender()
            if sender:
                if self.label.text() == "Wrong Input":
                    self.label.setText("")
                button_value = str(sender.text())
                current_text = self.label.text()
                self.label.setText(current_text + button_value)
                
            

    def clear(self):
        self.label.setText("")

    def delete(self):
        current_text = self.label.text()
        self.label.setText(current_text[:len(current_text)-1])

    def equal(self):
        current_text = self.label.text()
        try:
            ans=eval(current_text)
            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")
         
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec()



