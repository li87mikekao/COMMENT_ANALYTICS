data = [] # 建立名為 data 的空清單
counter = 0
with open('reviews.txt', 'r') as f: # r = read , as f = 當作 f
	for line in f: # 將 f 每筆資料命名為變數 line
		data.append(line) #line (每筆資料) append 進 data 裡面
		# print(len(data)) # 每讀1筆印1次, 顯示進度
		counter = counter +1 # 等於 counter += 1
		if counter % 1000 == 0:
			print(len(data))
# print(len(data)) # 利用 len 列出總筆數
# print(data) # 會將所有100萬筆資料全部印出
# print(data[0]) # 將第1筆資料印出