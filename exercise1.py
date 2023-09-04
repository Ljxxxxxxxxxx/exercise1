# 打开并读取文档read.txt
with open("D:/exercise1/file_to_read.txt", 'r') as file:
    text = file.read()

# 计算单词"terrible"出现的次数
count = text.count('terrible')

# 替换第偶数次出现的"terrible"为"pathetic"，第奇数次出现的"terrible"替换为"marvellous"
time = 1
new_text = ''
for word in text.split():
    if 'terrible'in word:
        if time % 2 == 0:
            new_text += 'pathetic '
            time += 1
        else:
            new_text += 'marvellous '
            time += 1
            if"!"in word:
                new_text +="!"
    else:
        new_text+= word + ' '

# 写入新的文档result.txt
with open("D:/exercise1/result.txt", 'w') as file:
    file.write(new_text)

# 输出单词"terrible"出现的次数
print("The total number of occurrences of the word terrible：", count)