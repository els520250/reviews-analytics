#讀取留言檔
data = []
count = 0
average_len = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count % 10000 == 0: #每存取1000次印1次
			print(len(data))
			#print是很耗時間的功能
			#若改成每讀1000筆資料印一次會快很多
		average_len = (average_len + len(line))
		#加總留言總長度

average_len = average_len / len(data)
#計算留言平均長度
print('檔案讀取完畢,共有', len(data), '筆資料')
print('平均評論長度: ', average_len)


new = []
for d in data: #每個d為一個單獨的評論
	if len(d) < 100: #把長度<100的評論存起來
		new.append(d)
print('一共有', len(new), '比留言長度小於100')


