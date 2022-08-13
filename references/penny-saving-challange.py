j = 0
for i in range(1,366):
    j += i/100
    print("Today I have saved: £",round(float(i/100), 2),
          " in total that makes: £",round(j, 2))
