'''This app is going to be a folder cleaner and cleans your by
moving all the files to classified folders'''
import os
import tkinter
from tkinter import filedialog
'''Importing os for doing Operating System operations like cut
and all. Importing Tkinter for making GUI'''

listbox = False
clean_folder = False
scan_btn = False

videos = ['WEBM', 'MPG', 'MP2', 'MPEG', 'MPE', 'MPV', 'OGG', 'MP4',
          'M4P', 'M4V', 'AVI', 'WMV', 'MOV', 'QT', 'FLV', 'SWF', 'AVCHD', '3GP']
images = ['tif', 'tiff', 'bmp', 'jpg', 'jpeg', 'gif',
          'png', 'eps', 'raw', 'cr2', 'nef', 'orf', 'sr2']
audios = ['aif', 'cda', 'mid', 'midi',
          'mp3', 'mpa', 'ogg', 'wav', 'wma', 'wpl']
documents = ['doc', 'docx', 'pdf', 'odt',
             'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt']
# defines all the types of extension


def clean(files_array, dirp):
    """
    Cleans the folder
    """
    folders = [dirp+'/Documents', dirp+'/Images',
               dirp+'/Music', dirp+'/Videos', dirp+'/Others']
    # list of all directories to create
    for folder in folders:
        if not os.path.isdir(folder):
            os.mkdir(folder)
    # makes all the needed folderes
    for item in files_array:
        file_type = item.split('.')[-1]
        if file_type.upper() in videos:
            os.rename(dirp+'/'+item, dirp+'/Videos/'+item)
        elif file_type.lower() in images:
            os.rename(dirp+'/'+item, dirp+'/Images/'+item)
        elif file_type.lower() in audios:
            os.rename(dirp+'/'+item, dirp+'/Music/'+item)
        elif file_type.lower() in documents:
            os.rename(dirp+'/'+item, dirp+'/Documents/'+item)
        else:
            os.rename(dirp+'/'+item, dirp+'/Others/'+item)
        listbox.delete(0, 'end')

    # The for loop above will move all files to it's directory


def scan_for_virus(list_folder, folder_path):
    """
    This scans all potential viruses in the folder
    """
    global listbox
    sus = []
    # a list of all suspecious files
    for lists in list_folder:
        try:
            sus_one = lists.split('.')[-1].lower()
            sus_two = lists.split('.')[-2]
            if sus_one == 'exe' or sus_one == 'dll':
                if sus_two.upper() in videos or sus_two.lower() in images or sus_two.lower() in documents or sus_two.lower() in audios:
                    sus.append(lists)
        except:
            pass

    if listbox:
        listbox.destroy()
    listbox = tkinter.Listbox(window, width=50, height=5)
    if sus == []:
        listbox.insert(0, 'No Potential Viruses found')
    else:
        x = 0
        for s in sus:
            x+=1
            listbox.insert(x, s)
    
    listbox.pack()
            


def ask():
    """
    Gets a directory
    """
    global listbox
    global scan_btn
    global clean_folder

    directory = filedialog.askdirectory()
    if listbox:
        listbox.destroy()
    if scan_btn:
        scan_btn.destroy()
    if clean_folder:
        clean_folder.destroy()
    # destroys listbox
    i = 0
    # this i will increment
    listbox = tkinter.Listbox(window, width=50, height=5)
    # creates a listbox
    things = []
    for files in os.listdir(directory):
        if os.path.isfile(directory+'/'+files):
            i = i+1
            things.append(files)
            listbox.insert(i, files)
    # appends all needed files to list
    listbox.pack()
    clean_folder = tkinter.Button(
        window, text='Clean Directory', command=lambda: clean(things, directory))
    clean_folder.pack()
    # a button that will clean folder
    scan_btn = tkinter.Button(window, text='Scan Viruses', command=lambda: scan_for_virus(things, directory))
    scan_btn.pack()
    # creates and pack all the buttons and stuff


window = tkinter.Tk()
window.title('Karma')
# you can change the title by changing karma 
window.geometry('450x250')
# you can change the dimension of the window by changing value above
window.iconbitmap(r'icon.ico')
'''
defines the icon
you can change the icon by:
1: design your logo
2: conver your logo to .ico file
3: rename your logo to 'icon'
4: copy the file to this folder and replace the old logo
'''
# creates the window
ask_files = tkinter.Button(window, text='Choose Files', command=ask)
ask_files.pack()
# creates a button that asks for a folder

window.mainloop()
