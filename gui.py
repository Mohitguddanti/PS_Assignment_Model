import pyautogui as pg
import subprocess , os
import time

t = time.localtime()
current_time = time.strftime('%H:%M:%S',t)      #Gives current time

status = True #connection status

#User input for time interval of sending data
time_interval =int( input("Enter the time interval for downloading data(in hrs){0 - 24}:"))
cl_id = input("Enter the id of the user you want to connect to: ")
#Waiting till connection is established
def connection_check():
    while pg.locateOnScreen('Connecting.png', confidence = 0.7) is not None:
        print("Connecting")
        time.sleep(2)
    print("connected")
    time.sleep(2)

#Download the file (keeps scrolling till we dinf the required file)
def download_file():
    x,y = pg.locateCenterOnScreen('Download.png')
    pg.moveTo(x, y+200)
    while pg.locateOnScreen('File.png', confidence = 0.85) is None:
          print("searching")
          pg.scroll(-150)
          time.sleep(2)
          box = pg.locateOnScreen('File.png', confidence = 0.85)
    pg.moveTo(pg.center(box))
    print("File found")
    pg.click()
    pg.moveTo(pg.locateCenterOnScreen('Download.png',confidence = 0.7))
    pg.click()
    time.sleep(900) #Assuming download time of 15mins


def interval(time_interval):
    sleep_time = 3600*time_interval
    time.sleep(sleep_time)

while status:
    #Start the AnyDesk program
    subprocess.Popen(['C:\Program Files (x86)\AnyDesk\\AnyDesk.exe'])
    #wait for it to open
    time.sleep(6)
    #Locate the Id box, enter the ID and wait for connection to be established
    pg.moveTo(pg.locateCenterOnScreen('ID_box.png'))
    pg.click()
    pg.write(cl_id)
    pg.moveTo(839, 342)
    pg.click()
    time.sleep(1)
    pg.moveTo(pg.locateCenterOnScreen('Browse_files.png', confidence = 0.75))
    pg.click()
    time.sleep(10)
    #Checking for connection (Assuming the connection is always established and we have to wawit for the other end to accept)
    connection_check()

    #Download the file (image of the file/folder in the download method)
    download_file()

    os.system("taskkill /im AnyDesk.exe /f") #Kill/Close AnyDesk

    #sleep for the specified time interval
    interval(time_interval)
