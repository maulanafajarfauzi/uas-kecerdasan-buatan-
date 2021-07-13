import CameraClient
import StreaServer
import threading
import time
receiving = StreamingServer('192.168.0.17',9999)
sending = StreamingServer('192.168.0.172',9999)
a= threading.Thread(target = receiving.start_server)
r1.start()
time.sleep(10)
a2 = threading.Thread(target=sending.start_stream)
r2.start()
while input("")!="Stop":
    continue
receiving.stop_server()
senidng.stop_stream() 
