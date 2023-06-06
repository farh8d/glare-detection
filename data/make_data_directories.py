import glob
import random
import shutil
import os 



def train_val_test_seperator(name_list , val_percentage = 0.2 , test_percentage = 0.1): # return train , val , test
    if len(name_list) < 3:
        return None
    
    name_list = [s.split('\\')[-1] for s in name_list]
    
    random.shuffle(name_list)
    val_indx = int(len(name_list) * val_percentage)
    test_indx = int(len(name_list) * (val_percentage + test_percentage))

    tr = name_list[test_indx:]
    val = name_list[:val_indx]
    tst = name_list[val_indx:test_indx]


    return   tr , val , tst



def copy_files(file_list, source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)

    for file_name in file_list:
        source_path = source_dir + '/' + file_name
        dest_path = dest_dir + '/' + file_name
        shutil.copy(source_path, dest_path)




def make_directories(  val_percentage = 0.2 , test_percentage = 0.1 , glare = "GLARE" , no_glare ="NO_GLARE" ):
    glare_names = glob.glob("data/"+glare+"/*")
    noglare_names = glob.glob("data/"+no_glare+"/*")


    glare_train_names , glare_val_names, glare_test_names = train_val_test_seperator(glare_names , val_percentage , test_percentage)
    noglare_train_names , noglare_val_names, noglare_test_names = train_val_test_seperator(noglare_names , val_percentage , test_percentage)
    

    copy_files(glare_train_names, "data/"+ glare ,"data/train/glare" )
    copy_files(glare_val_names, "data/"+ glare ,"data/val/glare" )
    copy_files(glare_test_names, "data/"+ glare ,"data/test/glare" )

    copy_files(noglare_train_names, "data/"+no_glare ,"data/train/no_glare" )
    copy_files(noglare_val_names, "data/"+no_glare ,"data/val/no_glare" )
    copy_files(noglare_test_names, "data/"+no_glare ,"data/test/no_glare" )


