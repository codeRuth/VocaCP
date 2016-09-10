import win32com.client
import time

app = win32com.client.Dispatch("PowerPoint.Application")
presentation = app.Presentations.Open(FileName=u'C:\\path\\to\\mypresenation.pptx', ReadOnly=1)

presentation.SlideShowSettings.Run()

time.sleep(1)
presentation.SlideShowWindow.View.Next()
time.sleep(1)
presentation.SlideShowWindow.View.Next()
time.sleep(1)
presentation.SlideShowWindow.View.Previous()
time.sleep(1)

presentation.SlideShowWindow.View.Exit()

app.Quit()