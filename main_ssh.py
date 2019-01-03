#TODO pytail is required for this package
import sys
import subprocess
from pygtail import Pygtail
from ssh_data_addition import *
import time
import subprocess
import select
from  ssh_parse import *
from ssh_predict import *
auth_path = "/var/log/auth.log"

print("Initializing SSH session monitoring...")
up = Parse_SSH()
f = subprocess.Popen(['tail','-F',auth_path],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

p = select.poll()
p.register(f.stdout)
da = SSHDataAddition()
temp_dict = {}
ssh_p = SSHPerdiction()
while True:
    if p.poll(1):
        temp = f.stdout.readline()
        temp = str(temp.decode("utf-8"))
        #print(temp)
        if str(temp).find("ssh") != -1:
            dict = up.SSHProcessed(temp)
            if dict == {}:
                continue
            if dict != temp_dict:
                print("=========================================")
                #print(dict)
                perdiction = ssh_p.predictSSH(ssh_p.prepareDict(dict))
                print("is Attack : "+str(perdiction))
                temp_dict = dict
                if(perdiction > 0.95):
                    is_attack = 1
                else:
                    is_attack = 0
                dict.update({"class": is_attack})
                da.writeSSH(dict)
            else:
                continue


    time.sleep(0.01)
#Data
#[internal,failed,td,root,root_access,attempts]
