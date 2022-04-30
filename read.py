#讀取留言檔
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count % 1000 == 0: #每存取1000次印1次
			print(len(data))
			#print是很耗時間的功能
			#若改成每讀1000筆資料印一次會快很多
			




