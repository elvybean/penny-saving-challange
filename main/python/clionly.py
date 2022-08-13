if __name__ == "__main__":
    daily_list = []
    weekly_list = []
    j = 0
    k = 0
    for i in range(1,366):
        j += i/100

        daily_list.append(round(i/100, 2))

        if i % 7 == 0:
            weekly_list.append([int(i/7), round(j - k, 2)])
            k = j
            
    print(daily_list)
    print(weekly_list)
