"""
封装调用dwf_cli的命令
"""
import subprocess
import os
from _init_path import PROJECT_ROOT


target_dir = os.path.join(PROJECT_ROOT,"scripts")
command_path = command_path = os.path.join(target_dir,"dwf.bat") if os.name == 'nt' else os.path.join(target_dir,"dwf")


def dwf_connect(host: str, username: str, password: str):
    check_params(host,"host")
    check_params(username,"username")
    check_params(password,"password")
    args = ["connect", "-h", host, "-u", username, "-p", password]
    result = subprocess.run([command_path] + args, capture_output=True, text=True, cwd=target_dir)
    return result

# todo
def dwf_download():
    args = ["workspace", "--install"]
    result = subprocess.run([command_path] + args, capture_output=True, text=True, cwd=target_dir)
    return result


def check_params(param, name):
    if not param:
        raise ValueError(f'{name} cannot be None')

