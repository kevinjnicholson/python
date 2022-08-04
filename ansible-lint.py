#!/usr/bin/env python
#------------------------------------------------------ 
# Created By: KJN
# Created Date:  04/08/2022
# version: 0.1
# Title: Ansible Lint
# -----------------------------------------------------
import os
playbook = input('Enter your playbook name: ')
os.system("podman start 359ace75d4b3")
os.system("podman cp "+playbook+" 359ace75d4b3:/runner")
os.system("podman exec 359ace75d4b3 ansible-lint /runner/"+playbook+"")
os.system("podman exec 359ace75d4b3 rm /runner/"+playbook+"")
os.system("podman stop 359ace75d4b3")
