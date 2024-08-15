# _init_paths.py
from pathlib import Path

# 获取当前文件的绝对路径
_CURRENT_FILE_PATH = Path(__file__).resolve()

# 获取项目根目录
PROJECT_ROOT = _CURRENT_FILE_PATH.parent