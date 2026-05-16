'''
# 1. 读取整个文件
# 2. 打印文件内容
# 3. 统计总行数
# 4. 统计非空行数
# 5. 统计 Python 出现了几次
# 6. 找出包含 "Python" 的所有行
'''

import argparse

def analyze_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    non_empty_lines = 0
    python_count = 0
    python_lines = []

    for line in lines:
        if line.split():
            non_empty_lines += 1
        
        if 'Python' in line:
            python_count += line.count('Python')
            python_lines.append(line)

    return{
        'lines':lines,
        'total_lines':total_lines,
        'non_empty_lines':non_empty_lines,
        'python_count':python_count,
        'python_lines':python_lines,
    }

def main(file):
    data = analyze_file(file)
    print(f'文件内容如下：')
    print(''.join(data['lines']))
    print('文件总行数为', data['total_lines'])
    print('非空行数量为', data['non_empty_lines'])
    print(f'Python 出现了 {data["python_count"]} 次')
    print('包含Python的行如下')
    print(data['python_lines'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='要处理的文件'
    )
    parser.add_argument('--file', default='practice1.txt', help='输入要处理的文件名')
    args = parser.parse_args()
    main(args.file)