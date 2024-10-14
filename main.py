import os
import glob
import tkinter as tk
from tkinter import filedialog


def get_libname():
    folder_path = filedialog.askdirectory()
    lib_files = glob.glob(os.path.join(folder_path, '*.lib'))
    # 将文件名写入到txt文件中
    with open('lib_filenames.txt', 'w') as file:
        for lib_file in lib_files:
            file.write(os.path.basename(lib_file) + '\n')
    return lib_files


def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


if __name__ == '__main__':
    root = tk.Tk()
    root.title('getDLLnameDemo')
    tk.Button(root, text='选择文件夹', command=get_libname).pack(pady=20)
    center_window(root,100,100)
    root.mainloop()
