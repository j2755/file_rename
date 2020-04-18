import os
import pathlib




def find_all_files_in_select_directory(directory):
	return  [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def find_all_files_of_type_in_select_directory( directory, file_type):
        files = []
        try:
            for f in os.listdir(directory):
                if pathlib.Path(f).suffix == filetype:
                    files.append(f)
        except Exception as e:
            print(e)
        return files


def rename_files_as_sequence(directory):
	files=find_all_files_in_select_directory(directory)
	i=1
	for file in files:


		full_name=directory+'\\'+file
		splitted_file=os.path.splitext(file)

		os.rename(full_name,directory+'\\'+str(i)+splitted_file[1])
		i+=1


def rename_files_relative_to_base_file(directory):
	basename=os.path.basename(directory)
	files=find_all_files_in_select_directory(directory)
	i=1
	for file in files:
		full_name=directory+'\\'+file
		splitted_file=os.path.splitext(file)
		os.rename(full_name,directory+'\\'+basename+'_'+str(i)+splitted_file[1])
		i+=1

