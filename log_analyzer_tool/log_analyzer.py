import re
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def open_file(file):
    records = []
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            data = re.search(r'epoch=(\d+) loss=([\d.]+) acc=([\d.]+)', line)
            if data:
                records.append({
                    'epoch': int(data.group(1)),
                    'loss': float(data.group(2)),
                    'acc': float(data.group(3)),
                })
    return records

def analyze_file(records):
    best_row = records.loc[records['acc'].idxmax()]

    max_acc = best_row['acc']
    min_loss = records['loss'].min()
    best_epoch = best_row['epoch']
    reduce = records['loss'].is_monotonic_decreasing

    return{
        'max_acc':max_acc,
        'min_loss':min_loss,
        'best_epoch':best_epoch,
        'reduce':reduce,
    }

def save_csv(records):
    records.to_csv('train.csv', index=False)
    return

def pic_loss(records):
    plt.figure()
    plt.plot(records['epoch'], records['loss'])
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.title('Training Loss')
    plt.savefig('loss_curve.png')
    plt.close()

def pic_acc(records):
    plt.figure()
    plt.plot(records['epoch'], records['acc'])
    plt.xlabel('epoch')
    plt.ylabel('acc')
    plt.title('Training ACC')
    plt.savefig('acc_curve.png')
    plt.close()

def main(file):
    records = open_file(file)

    if not records:
        print('没有有效的数据')
        return

    df = pd.DataFrame(records)
    data = analyze_file(df)
    print(f'最小loss为:{data["min_loss"]}')
    print(f'最高acc为:{data["max_acc"]}')
    print(f'最高acc轮次为:{data["best_epoch"]}')
    if data['reduce']:
        print('loss整体下降')
    else:
        print('loss非整体下降')
    save_csv(df)
    pic_loss(df)
    pic_acc(df)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='处理log文件并保存为CSV'
    )
    parser.add_argument('-f', '--file', default='train.log', help='输入要处理的文件名')
    args = parser.parse_args()
    main(args.file)