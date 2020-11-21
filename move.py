import os
import shutil
path = "C:\\Users\\jorda\\Pictures"
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path,i)) and 'MSC_pic' in i:
        print(i)
        shutil.move("C:\\Users\\jorda\\Pictures\\" + i, "C:\\Users\\jorda\\Pictures\\msc photos\\" + i)
