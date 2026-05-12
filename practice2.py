import sys
import re
import os

def save_csv(file):
    with open(file, 'r', encoding='utf-8') as f, \
        open('train.csv', 'w', encoding='utf-8') as c:
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

def main(file='train.log'):
    print('当前工作目录:', os.getcwd())
    max_acc = 0
    pre_loss = float('inf')
    min_loss = float('inf')
    best_epoch = 0
    reduce = True
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
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
    print(f'最小loss为：{min_loss}')
    print(f'最高acc为:{max_acc}')
    print(f'最高acc轮次为:{best_epoch}')
    if reduce:
        print('loss整体下降')
    else:
        print('loss非整体下降')
    save_csv(file)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        main()