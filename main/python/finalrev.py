def daily(i: int, j: int):
    print("Today I have saved: £",round(float(i/100), 2),
          " in total that makes: £",round(j, 2))

def weekly(i: int, j: int, k: int):
    if i % 7 == 0:
        print("In week ",int(i/7),"This week you have saved: £", round(j - k, 2))
        k = j
        

if __name__ == "__main__":
    j = 0
    k = 0
    for i in range(1,366):
        j += i/100
        #daily(i, j)
        weekly(i, j, k)
            
    print("\nIn total that makes: £",round(j, 2))
