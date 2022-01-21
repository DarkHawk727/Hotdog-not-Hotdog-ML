import os
from PIL import Image         
from IPython.display import Image, display
import imghdr
import climage


def check_images( s_dir, ext_list):
    bad_images=[]
    bad_ext=[]
    s_list= os.listdir(s_dir)
    for klass in s_list:
        klass_path=os.path.join (s_dir, klass)
        print ('processing class directory ', klass)
        if os.path.isdir(klass_path):
            file_list=os.listdir(klass_path)
            for f in file_list:               
                f_path=os.path.join (klass_path,f)
                if os.path.isfile(f_path):
                    
                    class_name = klass_path.split('/')[-1] 
                    if class_name == "hot_dog":   
                        output = climage.convert(f_path, is_unicode=True)
                        print(output)
                        print("Is this a hotdog?")
                        r = input()
                        if (r == "y"):
                            print("cool")
                        else:
                            os.remove(f_path)
                    # else:
                    #     if (r == "y"):
                    #         print("moving...")
                    #     elif (r=="m"):
                    #         print("moving...")
                    #     else:
                    #         print("cool")
                else:
                    print('*** fatal error, you a sub directory ', f, ' in class directory ', klass)
        else:
            print ('*** WARNING*** you have files in ', s_dir, ' it should only contain sub directories')
    return bad_images, bad_ext

source_dir =r'dataset/test/'
good_exts=['jpg', 'png', 'jpeg', 'gif', 'bmp' ] # list of acceptable extensions
bad_file_list, bad_ext_list=check_images(source_dir, good_exts)
if len(bad_file_list) !=0:
    print('improper image files are listed below')
    for i in range (len(bad_file_list)):
        # os.remove(bad_file_list[i])
        print (bad_file_list[i])
else:
    print(' no improper image files were found')