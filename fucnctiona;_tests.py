# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import os
from selenium import webdriver


# driver = webdriver.Firefox("驱动路径")


driver = webdriver.Edge()      # Edge浏览器


# 打开网页
driver.get('http://localhost:8000')
# python.exe 和 lib 位于同一目录
print(os.path.dirname(os.path.__file__))

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi("name")