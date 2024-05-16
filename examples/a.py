from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()  #新建相机实例
camera_config = picam2.create_preview_configuration() #生成相机预览配置文件
picam2.configure(camera_config) #使用该预览配置配置相机系统
picam2.start_preview(Preview.QTGL) #开启预览窗口
# while True:
#     picam2.start() #运行相机
picam2.start() #运行相机
time.sleep(2) #等待两秒钟
picam2.capture_file("./test.jpg") #将图像保存到test.jpg
