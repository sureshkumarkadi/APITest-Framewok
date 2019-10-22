#-------------------------------------------------------------------------------
# Name:        Registration Form
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     21-07-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

import os
import sys
import pytest
import unittest

#Getting current working folder
dir_path = os.path.dirname(os.path.realpath(__file__))

#Getting parent of current working folder
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

#Navigating to the desired folder
sys.path.insert(0,folder_path+"\Syslibrary")

#Imoprting module from Syslibrary
from datadriver import readjson

#Creating class object and instance of that object
jsonread1 = readjson()
import requests
#env = jsonread1.jsonread(folder_path+'\Env\setup.json')
class launchapplication():
        def intializeresource(self):
            #from instance object calling function 'jsonread'
            env = jsonread1.jsonread(folder_path+'\Env\setup.json')
            if env['url'] == 'prestagurl':
                URL = env['prestagprotocol']
                #print(URL)
                return URL
            elif env['url'] == 'stagurl':
                 URL = env['stagprotocol']
                 #print(URL)
                 return URL

        def createresource(self,URL):

            #URI = "https://reqres.in/api/users"
            env = jsonread1.jsonread(folder_path+'\Env\setup.json')
            URI = URL + env['createapi']

            testdata = jsonread1.jsonread(folder_path+'\Data\Testdata.json')
            #testdata = jsonread1.jsonread(folder_path+'\Data\Testdata.json')

            data = {
                "name": testdata['name'],
                "job": testdata['job']
                   }

            headers  = {'Content-Type':'application/json'}

            response = requests.post(URI,json=data,headers=headers)
            return response
        def getresource(self,URL):

            env = jsonread1.jsonread(folder_path+'\Env\setup.json')

            URI = URL + env['getapi']
            print(URI)

            headers  = {'Content-Type':'application/json'}

            response = requests.get(URI,headers=headers)
            return response
##            print(response.status_code)
##            print(response.text)
##            print(response.headers)
##            print(len(response.content))
#if __name__ == '__main__':
 #   unittest.main()

