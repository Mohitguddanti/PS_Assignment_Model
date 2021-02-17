# PS_Assignment_Model
Pyautogui automation of AnyDesk for file sharing automatically at regular intervals
Care must be taken that this code is meant for specific screen ratios. It is customizable to your given size and one can set them by specifying the x,y axis points on screen where the click must happen.
Steps:-
Before running the code enter the 
1) Open your command prompt and go to the directory where you have extracted the gui.py file.
2) Now run the script by typing "python gui.py" in command prompt.
The script will automatically open Anydesk software unless it's installed at some other custom directory which can be rectified by specifying the directory of Anydesk in the 44th Line of the code
Edit it using any editor.
3)Specify the number of hours after which the sending must take place.
4)Enter the client ID to which you want to connect to.
****IMPORTANT INSTRUCTIONS****

1)This script runs on image processing techniques hence it assumes that the picture of folder to be downloaded is present with you and is specified as File.png. One can take the relevant picture and 
paste it in the same folder as gui.py file.
2)Further ID_Box.png is the picture of the place where we enter the id of the client we wish to connect. This can be added if not present on you system by taking a snapshot of your screen in Anydesk software and cropping it to get relevant button in the picture.
3) Picture of file must be known to download as the script scans through the list of files by scrolling and then clicks on it and downloads.
4)Samples pictures  of all the relevant .png files needed have been added in the directory.
