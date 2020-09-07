# break 的簡易範例
n=0
while n<5:
    if n==3:
        break
    print (n) # 印出迴圈的 n
    n+=1
print ("最後的 n :", n) # 印出迴圈結束後的 n

# continue 的簡易迴圈
n=0
for x in [0,1,2,3]:
    if x%2==0:
        continue
    print (x)
    n+=1
print ("最後的 n :", n)

# else 的簡易範例
sum=0
for x in range(11):
    sum+=x
else:
    print (sum) # 印出 1+2+...+10的結果

# 綜合範例: 找出整數平方根
# 輸入 9，得到 3
# 輸入 11，得到 沒有整數的平方根
n= input("輸入一個正整數: ")
n= int(n)
for i in range (n): # i 從 0 ~ n-1
    if i*i==n:
        print ("整數平方根", i)
        break # 用 break 強制結束迴圈時，不會執行else 區塊
else:
    print ("沒有整數平方根")
