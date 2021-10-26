from main import *

"""
Change these parameters.
dir_name is the directory of your docx
dir_out is the directory you want to extract your images at
rename is the name you want to rename your pics as. An incrementing number will be added at the end of the name.
"""

dir_name = None
dir_out = '/extracted/'
rename = 'New_image'

docx = DocXImageRename(dir_name, dir_out, rename)
docx.extract_files()
