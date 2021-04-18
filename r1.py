import os

# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # utf-8-sig 去掉開頭紀錄編碼符號
        for line in f:
            lines.append(line.strip())
    return lines


# 轉換對話紀錄
def convert(lines, people):
    new = []
    person = None
    for line in lines:
        if line in people: # 如果line為人名，記錄人名，跳過記錄對話
            person = line
            continue
        if person:
            new.append(person + ': ' + line)
    return new


# 寫入檔案
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


# 程式進入點
def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    people = ['Allen', 'Tom']
    if os.path.isfile(input_file): # 檢查檔案在不在
        print('找到檔案了！')
        lines = read_file(input_file)
        lines = convert(lines, people)
        write_file(output_file, lines)
    else:
        print('找不到檔案...')


if __name__ == '__main__': # 如果這個檔案是自己執行不是被import，才執行main()
    main()