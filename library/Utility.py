"""
Author: Sujayyendhiren Ramarao Srinivasamurthi
Description: Reusable utilities across modules are placed here
"""

import os
import io
import json
import subprocess
from glob import glob
from socket import gethostname

import yaml
import requests


class Utility(object):
    """ Utility functions """

    @staticmethod
    def read_configuration(configfile="configuration.yml",\
            config=None):
        """ Read configuration """
        configfile = "configuration/{0}".format(configfile)
        with open(configfile, 'r') as read:
            if config:
                config = yaml.load(read.read())[config]
            else:
                config = yaml.load(read.read())
            return config

    @staticmethod
    def hostname():
        """ Get this device's hostname """
        return str(gethostname()).split(".")[0]

    @staticmethod
    def cache(filename="default", action="read", data=None):
        """ Cache network data and others that can be reused """

        hostname = Utility.hostname()
        filepath = "cache/{0}-{1}.cache".format(filename, hostname)

        if action == "read":
            if not os.path.exists(filepath):
                with open(filepath, 'w') as cache:
                    cache.write(json.dumps({}))
      
            with open(filepath, 'r') as cache:
                return json.loads(cache.read())

        elif action == "write":
            with open(filepath, 'w') as cache:
                cache.write(json.dumps(data, indent=4))
                return True
        return False


    @staticmethod
    def appletv_baseurl(action):
        """ Apple TV baseurl """
        appletvip = None
        devices = Utility.cache("devices", "read")

        for device in devices:
            if 'apple' in device.lower() and 'tv' in device.lower():
                appletvip = devices[device]['ip']

        config = Utility.read_configuration(config='APPLETV')

        return config['baseuri'].format(action=action,\
                                     appletvip=appletvip)

    @staticmethod
    def appletv_processing(action):
        """ Apple TV related info shall be added here """
        url = Utility.appletv_baseurl(action)

        print("URL: {0}".format(url))
        response = requests.put(url, data=json.dumps({}))

        print(response.status_code)
        print(response.text)

        return True

    @staticmethod
    def diagnostics(option):
        
        count = 0; data = ''; supportedopts = { "filetimestamp": "ls -lrt",
                          "viewcache": "ls cache/*",
                          "gitstatus": "git status",
                        }
        
        if option not in supportedopts: return None, None

        popen = subprocess.Popen(supportedopts[option], stdout=subprocess.PIPE, shell=True, bufsize=1)

        for idx, line in enumerate(io.TextIOWrapper(popen.stdout, encoding="utf-8")):
            if not line:
                count +=1 
                if count > 5: break
            else:
                count = 0
                data += line
        return supportedopts[option], data

    
        
            

