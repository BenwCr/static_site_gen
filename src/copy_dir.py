import os
import shutil

publicPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'public')) #set path to root/public
staticPath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static')) #set path to root/static



def Copy_srcTopublic(public_currentPath=None, static_currentPath=None):
    if public_currentPath == None and static_currentPath == None: #If first time
        shutil.rmtree(publicPath,ignore_errors=True) #delete public and everything underneath.
        os.mkdir(publicPath) #make public file
        static_currentPath = staticPath
        public_currentPath = publicPath
    listDir = os.listdir(static_currentPath)
    print (listDir)
    for i in listDir:
        currentItem = os.path.join(static_currentPath, i)
        if os.path.isfile(currentItem) == True:
            shutil.copy(currentItem, public_currentPath)
            print(f"Copy: {currentItem}")
            continue
        futurePath = os.path.join(public_currentPath, i)
        os.mkdir(futurePath)
        Copy_srcTopublic(os.path.join(public_currentPath, i),currentItem)
        
            
