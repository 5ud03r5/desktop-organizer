import os
import re


current_dir = os.environ['USERPROFILE']
onedrive_dir = os.environ['ONEDRIVECONSUMER']

def onedrivevalidator(onedrive_dir, current_dir):
    dir_to_desktop = ''
    if 'ONEDRIVECONSUMER' in os.environ:
        dir_to_desktop = onedrive_dir
    else:
        dir_to_desktop = current_dir

    for file in os.listdir(dir_to_desktop):
            if file == 'Pulpit':
                desktop = 'Pulpit'
            elif file == 'Desktop':
                desktop == 'Desktop'
    
    return dir_to_desktop, desktop


dir_to_desktop, desktop = onedrivevalidator(onedrive_dir, current_dir)
path = os.path.join(os.path.join(dir_to_desktop, desktop))
print(path)

lista = os.listdir(path)
reg = '\.[a-zA-Z]{1,3}'
for file in lista:
    
    name, extension = os.path.splitext(file)
    if file.endswith(extension) and extension != '.lnk' and extension:
        
        reg = re.search('[a-zA-Z]{1,3}', extension)
        reg = reg.group(0)
        
        path_pem = os.path.join(os.path.join(path, reg))
        path_file = os.path.join(os.path.join(path, file))
        
        if not os.path.exists(path_pem):
            os.makedirs(path_pem)
            
        path_pem = os.path.join(os.path.join(path_pem, file))
        os.replace(path_file, path_pem)

desktop_bin = os.path.join(path, 'Desktop_bin')
if not os.path.exists(desktop_bin):
            os.makedirs(desktop_bin)

for file in lista:
    path_file = os.path.join(path, file)
    desktop_bin_file = os.path.join(os.path.join(desktop_bin, file))
    if os.path.isdir(path_file) and desktop_bin != path_file:
        try:
            os.replace(path_file, desktop_bin_file)
        except PermissionError:
            pass

     
    