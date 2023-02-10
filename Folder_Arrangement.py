import os,shutil

dict_extension = {
    'audio_extension' : ('.mp3','.m4a','.wav','.flac'),
    'movie_extension' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'documnet_extension' : ('.pdf','.jpg','.png','.jpeg','.ppt','.webp','.pptx')
}

folderpath = input("Enter the path of folder :- ") # User have to enter the path of folder...

def file_finder(folder_path,file_extension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
                
    return files

# print(file_finder(folderpath, movie_extension)) # it gives the list of all files insides a particular category of extensions

for extension_type,extension_tuple in dict_extension.items():
    folder_name = extension_type.split('_')[0]+" Files"
    folder_path = os.path.join(folderpath , folder_name)
    os.mkdir(folder_path)
    for item in (file_finder(folderpath,extension_tuple)):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
        
        
    
    
    
    
    


