import subprocess
import os
from _init_path import PROJECT_ROOT

# 命令和参数
target_dir = os.path.join(PROJECT_ROOT,"scripts")
args = ["connect", "-h", "172.21.11.55", "-u", "admin", "-p", "123456"]

command_path = os.path.join(target_dir,"dwf.bat")


result = subprocess.run([command_path] + args, capture_output=True, text=True, cwd=target_dir)

# 打印命令的输出
print("Output:", result.stdout)

# 如果命令执行失败，打印错误信息
if result.returncode != 0:
    print("Error:", result.stderr)