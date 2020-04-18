import os
import pathlib
import re


class Rename:
    def __init__(self, directory):
        self.directory = directory

    def find_all_files_in_select_directory(self):
        return [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]

    def find_all_files_of_type_in_select_directory(self, file_type):
        files = []
        try:
            for f in os.listdir(self.directory):
                if pathlib.Path(f).suffix == filetype:
                    files.append(f)
        except Exception as e:
            print(e)
        return files

    def rename_files_as_sequence(self):
        files = self.find_all_files_in_select_directory(self.directory)
        i = 1
        for file in files:

            full_name = self.directory+'\\'+file
            splitted_file = os.path.splitext(file)

            os.rename(full_name, self.directory+'\\'+str(i)+splitted_file[1])
            i += 1
    def rename_files_of_specific_type__relative_to_base_file(self,file_type):
    	basename = os.path.basename(self.directory)
        total_files=self.find_all_files_of_type_in_select_directory(file_type)
        files, index = self.return_tuple_of_unformatted_files_and_largest_index(
            total_filesfiles,basename)
        i = index+1
        for file in files:
            full_name = self.directory+'\\'+file
            splitted_file = os.path.splitext(file)
            os.rename(full_name, self.directory+'\\' +
                      basename+'_'+str(i)+splitted_file[1])
            i += 1

    def rename_files_relative_to_base_file(self):
        # only works once initially, otherwise it will try to give multiple files the same name
        basename = os.path.basename(self.directory)
        total_files=self.find_all_files_in_select_directory()
        files, index = self.return_tuple_of_unformatted_files_and_largest_index(
            total_files,basename)
        i = index+1
        for file in files:
            full_name = self.directory+'\\'+file
            splitted_file = os.path.splitext(file)
            os.rename(full_name, self.directory+'\\' +
                      basename+'_'+str(i)+splitted_file[1])
            i += 1

    def return_tuple_of_unformatted_files_and_largest_index(self,files, base_file_name):
        new_files = []
        files_and_index = (None, 1)
        for file in files:
            if not self.check_file_name_for_correct_format(file, base_file_name):
                new_files.append(file)
        formatted_files = list(set(files)-set(new_files))

        greatest_number = self.get_largest_number(formatted_files)
        return (new_files, greatest_number)

    def get_largest_number(self, list_of_files):
        largest = 1
        for file in list_of_files:
            z = file.split('_')
            z = z[-1]
            z = z.split('.')
            z = z[0]
            z = int(z)

            if z > largest:
                largest = z
        return largest

    def check_file_name_for_correct_format(self, file, base_file_name):
        valid = False
        m = re.search('^('+base_file_name+')'+'(\d*)', file)
        if m != None:
            valid = True
        return valid
