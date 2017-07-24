import os
import shutil
from .sv_handler import SVHandler
from .xlsx_handler import XlsxHandler

def sv_dir_to_xlsx(dir_path,newpath,file_extenstion='.csv'):
	""" A function to convert a directory of sv files to a directory of xlsx files.
	:param dir_path: The path for where to directory is located
	:type dir_path: str
	:param newpath: The path for the new directory for where the xlsx files will be located
	:type newpath: str
	:param file_extenstion: The extension of the sv file that is being converted
	:type file_extenstion: str
	"""

	os.makedirs(newpath)
	for file_ in os.listdir(dir_path):
		if os.path.splitext(file_)[-1].lower() == file_extenstion:	
			handler = sv_handler.SVHandler(os.path.join(dir_path, file_))
			file_2 = xlsx_handler.XlsxHandler.dict_to_xlsx(handler.sv_to_dict(), os.path.join(newpath, os.path.splitext(file_)[0] + '.xlsx'))


def sv_dir_to_sv(dir_path,newpath,file_extenstion1='.csv',file_extenstion2='.psv', delimiter = '|'):
	""" A function to convert a directory of sv files to a directory of a different sv files.
	:param dir_path: The path for where to directory is located
	:type dir_path: str
	:param newpath: The path for the new directory for where the xlsx files will be located
	:type newpath: str
	:param file_extenstion: The extension of the sv file that is being converted
	:type file_extenstion: str
	:param file_extenstion2: The extension of the new sv files that will be created
	:type file_extenstion2: str
	:param delimiter: the delimiter that will be used for the new sv files
	"""
	os.makedirs(newpath)
	for file_ in os.listdir(dir_path):
		if os.path.splitext(file_)[-1].lower() == file_extenstion1:	
			handler = sv_handler.SVHandler(os.path.join(dir_path, file_))
			file_2 = sv_handler.SVHandler.dict_to_sv(handler.sv_to_dict(), os.path.join(newpath, os.path.splitext(file_)[0] + file_extenstion2), delimiter=delimiter)
		

def xlsx_dir_to_sv(dir_path,newpath,file_extenstion='.csv', delimiter=','):
	""" A function to convert a directory of xlsx files to a directory of a sv files.
	:param dir_path: The path for where to directory is located
	:type dir_path: str
	:param newpath: The path for the new directory for where the xlsx files will be located
	:type newpath: str
	:param file_extenstion: The extension of the new sv files that will be created
	:type file_extenstion: str
	:param delimiter: the delimiter that will be used for the new sv files
	"""
	os.makedirs(newpath)
	for file_ in os.listdir(dir_path):
		if os.path.splitext(file_)[-1].lower() == '.xlsx':
			handler = xlsx_handler.XlsxHandler(os.path.join(dir_path, file_))
			file_2 = sv_handler.SVHandler.dict_to_sv(handler.xlsx_to_dict(), os.path.join(newpath, os.path.splitext(file_)[0] + file_extenstion),delimiter=delimiter)


