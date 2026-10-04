import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    # i = 1
    # for file in files_with_ext:
    #     os.rename(file, f"photo-{i}{ext}")
    #     i+=1 
    if not(os.path.exists("images")):
        os.mkdir("images")  # used to create images folder 
        
    for i, file in enumerate(files_with_ext):
        os.rename(file, f"images/photo-{i+1}{ext}")

if __name__=="__main__":
    files = os.listdir()   # getting files form current folder 
    arrange_files(files, ".jpg")


# REVISION DONE BY ME FOR THSIC CODE 

'''
import os
def arrangingfiles_acctome=  :
file_with_ext=[file for file in files files_ends_with(jpg or ext)]
print(file_With_ext)

if not(os.path.exists){
 os.mkdir("images")
}

for i, file in enumerate(file_with_ext):
os.rename(file, f"photo{i+1}{ext}")



'''
