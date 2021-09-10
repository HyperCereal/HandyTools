import pypinyin

def pinyinize(word):
    s1 = ''
    for i in pypinyin.pinyin(word,style=pypinyin.NORMAL):
        s1 = s1 + ' '.join(i)
    return  s1


def pinyinize_txt_batch(args):
    s2 = ''
    for i in args:
        s2 = s2 + ' '.join(i)
    s3 = pinyinize(s2)
    with open('./Transformed.txt','w',encoding='utf-8') as f:
        f.write(s3)
    print('Written')
    


selected_file = open('PinyinTransform.txt','r',encoding='utf-8')
file_content = selected_file.read()
pinyinize_txt_batch(file_content)