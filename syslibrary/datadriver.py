#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     21-07-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json
import unittest
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))
print(folder_path)

class readjson(unittest.TestCase):
    def jsonread(self,filename):         # run time will provide the filepath
        with open(filename) as jsonfile: # opens the json object
            value = json.load(jsonfile)  # converts json object into python object
            return value                 # returns value

    def multiplejsonread(self):
        path_to_json = folder_path+'\Data'
        json_files = [json_file for json_file in os.listdir(path_to_json) if json_file.endswith('.json')]
        return json_files

    def multiplejsonbrowser(self):
        path_to_json = folder_path+'\Env'
        browser_json_files = [browser_json_files for browser_json_files in os.listdir(path_to_json) if browser_json_files.endswith('.json')]
        return browser_json_files

if __name__ == '__main__':
    unittest.main()



