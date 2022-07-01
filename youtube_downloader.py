from importlib.resources import path
from pytube import YouTube
from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QTextEdit, QVBoxLayout, QComboBox
from PyQt6.QtGui import QIcon, QFontDatabase
import sys
## Ryan Shanz
# GUI #

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(QIcon('ytimage.ico'))

        layout=QVBoxLayout()
        self.setLayout(layout)
        id = QFontDatabase.addApplicationFont("Quicksand-VariableFont_wght.ttf")
        

        self.inputField = QLineEdit()
        self.choice_box= QComboBox()
        self.choice_box.addItem("Video")
        self.choice_box.addItem("Audio Only")
        button=QPushButton(QIcon('ytimage.ico'), "Show Information", clicked=self.Information)
        button2=QPushButton(QIcon('downloadicon.ico'), "Download", clicked=self.Downloader)
        self.output= QTextEdit("Enter link")
        

        layout.addWidget(self.inputField)
        layout.addWidget(self.output)
        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(self.choice_box)

      
    def Information(self):   

# prints information on video using pytube #
        link= self.inputField.text()
        video= YouTube(link)
        self.output.setText(format(f"Title:   {video.title} \nChannel: {video.author} \nLength:  {round(video.length/60, 2)} minutes"))

# Youtube downloader using pytube #
    def Downloader(self): 
        choice=self.inputField.text()
        def on_complete(stream, filepath):
            self.output.setText(format(f"Download Complete. \n\nFile path: {filepath}"))
        def on_progress(stream, chunk, bytes_remaining):
            progress=100-(bytes_remaining / stream.filesize *100)
            self.output.setText(format(f"Progress: {round(progress)}%"))
        video= YouTube(choice, on_progress_callback=on_progress,on_complete_callback=on_complete)
 
 # .currentText method checks text selected in drop down menu:
        choice_box_text= self.choice_box.currentText()
        if(choice_box_text=="Audio Only"):
            video.streams.get_audio_only().download()
        else:
            video.streams.get_highest_resolution().download()


      
app = QApplication(sys.argv)
# insert CSS stylesheet
app.setStyleSheet(open('c:/Users/ryans/Documents/Code examples/web for coding/youtube_downloader/youtube_downloader_stylesheet.css').read())
window= MyApp()
window.show()

app.exec()