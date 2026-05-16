import re
import os
import argparse

def analyze_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    max_acc = 0
    pre_loss = float('inf')
    min_loss = float('inf')
    best_epoch = 0
    reduce = True

    for line in lines:
        data = re.search(r'epoch=(\d+) loss=([\d.]+) acc=([\d.]+)', line)
        if data:
            epoch = int(data.group(1))
            loss = float(data.group(2))
            acc = float(data.group(3))
            if acc > max_acc:
                max_acc = acc
                best_epoch = epoch
            if loss < min_loss:
                min_loss = loss
            if loss > pre_loss:
                reduce = False
            pre_loss = loss

    return{
        'max_acc':max_acc,
        'min_loss':min_loss,
        'best_epoch':best_epoch,
        'reduce':reduce,
    }

def save_csv(file):
    with open(file, 'r', encoding='utf-8') as f, open('train.csv', 'w', encoding='utf-8') as c:
        c.write('epoch,loss,acc\n')
        for line in f:
            data = re.search(r'epoch=(\d+) loss=([\d.]+) acc=([\d.]+)', line)
            if data:
                epoch = int(data.group(1))
                loss = float(data.group(2))
                acc = float(data.group(3))
                c.write(f'{epoch},{loss},{acc}\n')
    print('已保存为csv')
    return

def main(file):
    data = analyze_file(file)
    print(f'最小loss为:{data["min_loss"]}')
    print(f'最高acc为:{data["max_acc"]}')
    print(f'最高acc轮次为:{data["best_epoch"]}')
    if data['reduce']:
        print('loss整体下降')
    else:
        print('loss非整体下降')
    save_csv(file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='处理log文件并保存为CSV'
    )
    parser.add_argument('-f', '--file', default='train.log', help='输入要处理的文件名')
    args = parser.parse_args()
    main(args.file)