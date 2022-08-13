if __name__ == "__main__":
    j = 0
    k = 0
    for i in range(1,366):
        j += i/100

        print("Today I have saved: £",round(float(i/100), 2),
          " in total that makes: £",round(j, 2))

        if i % 7 == 0:
            print("In week ",int(i/7),"This week you have saved: £", round(j - k, 2))
            k = j
            
    print("\nIn total that makes: £",round(j, 2))
