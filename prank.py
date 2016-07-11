import os

def renameFiles():
    #(1) Get file names from a folder
    files = os.listdir("/Users/jasonwuerch/Desktop/prank")
    os.chdir("/Users/jasonwuerch/Desktop/prank")
    print "Your current working directory is " + os.getcwd()

    #(2) for each file, rename filename
    for fileName in files:
        #Prints fileName before changes
        print "Old Name - " + fileName
        #Takes out numbers of fileName
        os.rename(fileName, fileName.translate(None, "0123456789"))
        print "New Name - " + fileName.translate(None, "0123456789")
    


renameFiles()
