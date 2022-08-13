def daily(i: int, j: int):
    print("Today I have saved: £",round(float(i/100), 2),
          " in total that makes: £",round(j, 2))

def weekly(i: int, j: int, k: int):
    if i % 7 == 0:
        print("In week ",int(i/7),"This week you have saved: £", round(j - k, 2))
        k = j