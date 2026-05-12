'''
# 1. 读取整个文件
# 2. 打印文件内容
# 3. 统计总行数
# 4. 统计非空行数
# 5. 统计 Python 出现了几次
# 6. 找出包含 "Python" 的所有行
'''

import sys

def read_print(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    return content

def num_line(file):
    num = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            num = num + 1

    return num

def num_fkong(file):
    num = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.split():
                num = num + 1
    
    return num

def num_python(file):
    num = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            num = num + line.count('Python')
    
    return num

def line_python(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Python' in line:
                print(line)

def main(file='practice.txt'):
    content = read_print(file)
    nol = num_line(file)
    nof = num_fkong(file)
    nop = num_python(file)
    print(f'文件内容如下：')
    print(content)
    print(f'文件总行数为 {nol}')
    print(f'非空行数量为 {nof}')
    print(f'Python 出现了 {nop} 次')
    line_python(file)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        file = sys.argv[1]
        main(file)
    else:
        main()