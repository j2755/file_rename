import os
import pathlib


class Rename:
	def __init__(self,directory):
		self.directory=directory

	def find_all_files_in_select_self.directory(self):
		return  [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]


	def find_all_files_of_type_in_select_self.directory( self, file_type):
	        files = []
	        try:
	            for f in os.listdir(self.directory):
	                if pathlib.Path(f).suffix == filetype:
	                    files.append(f)
	        except Exception as e:
	            print(e)
	        return files


	def rename_files_as_sequence(self):
		files=self.find_all_files_in_select_directory(self.directory)
		i=1
		for file in files:


			full_name=self.directory+'\\'+file
			splitted_file=os.path.splitext(file)

			os.rename(full_name,self.directory+'\\'+str(i)+splitted_file[1])
			i+=1


	def rename_files_relative_to_base_file(self):
		basename=os.path.basename(self.directory)
		files=self.find_all_files_in_select_self.directory(self.directory)
		i=1
		for file in files:
			full_name=self.directory+'\\'+file
			splitted_file=os.path.splitext(file)
			os.rename(full_name,self.directory+'\\'+basename+'_'+str(i)+splitted_file[1])
			i+=1

