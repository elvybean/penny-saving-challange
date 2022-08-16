j = 0
for i in range(1,366):
    j += i/100

    print("--------------------------------------------------------------")
    print("Today I have saved: £",round(float(i/100), 2))

    match bool(i == 1):
        case False:
            print("Adding that to yesterday which was £",round(float((i-1)/100), 2))

    print("including previous days that in total that makes: £",round(j, 2))
print("--------------------------------------------------------------")