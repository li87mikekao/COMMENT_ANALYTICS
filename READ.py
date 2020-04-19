data = [] # 建立名為 data 的空清單
counter = 0 # 新增計數用變數
with open('reviews.txt', 'r') as f: # r = read , as f = 當作 f
	for line in f: # 將 f 每筆資料命名為變數 line
		data.append(line) #line (每筆資料) append 進 data 裡面, 從後看到前
		# print(len(data)) # 每讀1筆印1次, 顯示進度
		counter = counter +1 # 等於 counter += 1
		if counter % 1000 == 0:
			print(len(data))
# print(len(data)) # 利用 len 列出總筆數
# print(data) # 會將所有100萬筆資料全部印出
# print(data[0]) # 將第1筆資料印出
print('總共有', len(data), '筆資料') # 需注意逗點

sum_len = 0 # 新增每筆留言長度變數
for comment in data: # 將 data 每筆資料命名為變數 comment
	sum_len = sum_len +len(comment)
	# print(sum_len) # 顯示加總過程
print('所有留言平均長度為', sum_len/len(data))

lessthan100 = [] # 新增長度"小於100"的留言筆數清單
for shortcomment in data: # 從 data 清單撈資料命名為變數 lcomment
	if len(shortcomment) < 100: # 如果留言長度小於100
		lessthan100.append(shortcomment) # 將如果留言長度小於100的留言加到 lessthan100 清單
print('長度小於100的留言有', len(lessthan100), '筆')
print('長度小於100第一筆資料為', lessthan100[0])