# credit and copyright to https://blog.csdn.net/weixin_44281516/article/details/103200252
import hashlib

# 待加密信息
def md5(str):
	import hashlib
# 建立md5对象
	m = hashlib.md5()
	b = str.encode(encoding='utf-8')
	m.update(b)
	return m.hexdigest()
h=':'
pwfile = open('Input.csv')
pw = pwfile.read().splitlines()
print(pw)
md5file = open('Output.txt','a+')
for d in pw:
    print(md5(d))
    md5file.write((d)+(h)+md5(d))
    md5file.write('\n')
pwfile.close()
md5file.close()