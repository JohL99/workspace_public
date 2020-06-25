import os
import shutil
from selenium import webdriver


#Function to copy specified file from specified path to other specified path
def CopyFile(npath, opath, fname):
    a = 1
    
    #if file exists remove file
    if os.path.isfile(npath+fname):
        os.remove(npath+fname)
    
    #if directory doesnt exist create directory
    if not os.path.exists(npath):
        os.makedirs(npath)
        print("Complete")
    else:
        print("Directory " + npath + " already exists.")
    
    #if file doesnt exist copy file
    if not os.path.isfile(npath+fname):
        fname = "\\" + fname
        shutil.copy2(opath+fname, npath)
        print("Complete")
    else:
        print("File " + fname + " already exists")
        
    #rename file
    if os.path.isfile(npath+fname):
        os.rename(npath+fname, npath+"\\Part"+str(a)+" - test.png")
    a += a


#function to open browser and dowload the file
def DownloadFile(link):
    driver = webdriver.Firefox()
    driver.get(link)
    #button = driver.find_element_by_id('btnI')
    #button.click()





def main():
    newpath = r'C:\\Users\\toxxi\\Desktop\\TestFolder'
    oldpath = r'C:\\Users\\toxxi\\Desktop\\School\\misc'
    file = 'test.png'
    #CopyFile('C:\\Users\\toxxi\\Desktop\\TestFolder', 'C:\\Users\\toxxi\\Desktop\\School\\misc', '\\Capture.png')
    DownloadFile("https://www.google.com")
    

main()