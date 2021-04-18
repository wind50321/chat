import os

# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # utf-8-sig 去掉開頭紀錄編碼符號
        for line in f:
            lines.append(line.strip())
    return lines


# 對話統計
def count(lines, names):
    # [人名, 文字, 貼圖, 圖片]
    stats = []
    for name in names: # 對每個名字個別統計
        word_count = 0
        sticker_count = 0
        image_count = 0
        for line in lines: # 逐行訊息判斷
            s = line.split(' ') # 對訊息分割 [時間名字, 訊息...]
            if s[0][5:] == name: # 如果第一個項目從第六個字開始符合當前名字(字串可看作清單)
                if s[1] == '貼圖':
                    sticker_count += 1
                elif s[1] == '圖片':
                    image_count += 1
                else:
                    for msg in s[1:]: # 分割清單從s[1]到結尾
                        word_count += len(msg)
        stats.append([name, word_count, sticker_count, image_count])
    for p in stats:
        print(p[0], '字數', p[1], '貼圖', p[2], '圖片', p[3])


# 程式進入點
def main():
    input_file = '3.txt'
    names = ['Allen', 'Viki']
    if os.path.isfile(input_file): # 檢查檔案在不在
        print('找到檔案了！')
        lines = read_file(input_file)
        lines = count(lines, names)
    else:
        print('找不到檔案...')


if __name__ == '__main__': # 如果這個檔案是自己執行不是被import，才執行main()
    main()