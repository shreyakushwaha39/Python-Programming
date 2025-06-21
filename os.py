#import os module and i.create a directory ii.list the files in the directory iii.remove the directory
import os
from stringutils import *
os.mkdir('mydir')
print('Directory created')
print('Files in the directory:',os.listdir('mydir'))
os.rmdir('mydir')
print('Directory removed')

