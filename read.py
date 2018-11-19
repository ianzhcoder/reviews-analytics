#讀取檔案練習
data = []   #空的List
count = 0 
with open ("reviews.txt", 'r') as f:
    for line in f:
        count += 1  #每讀取一筆count +1
        data.append(line)
        #每讀取10000筆時列出進度
        if count % 10000 == 0:
            print (len(data))
    print ("總共有", len(data), "筆資料")
#印出前兩筆留言     
print(data[0])
print(data[1])
#計算平均長度
sum = 0
for d in data:
    sum += len(d)
    #print ("累積長度", sum)
print ("平均留言長度為", sum / len(data))

#篩選出留言字數小於100的留言筆數
new = []     #給一個空List，方便記錄筆數len(new)
for d in data:
    if len(d) < 100:
        new.append(d)
    #print ("目前有", len(new), "筆資料字數小於100")
print ("小於100字數的留言總共有", len(data), "筆")
#印出頭尾兩筆留言     
print(new[0])
print(new[len(new)-1])

#篩選出留言中有提到"good"的留言
good = []
for d in data:
    if "good" in d:
        good.append(d)
print ("總共有", len(good), "筆留言提到good")
#印出頭尾兩筆留言     
print(good[0])
print(good[len(good)-1])