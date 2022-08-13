j = 0
k = 0
for i in range(1,366):
    j += i/100
    
    if i % 7 == 0:
        print("In week ",int(i/7),"This week you have saved: £", round(j - k, 2))
        k = j
        
print("\nIn total that makes: £",round(j, 2))
