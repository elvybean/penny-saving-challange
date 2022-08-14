from datetime import timedelta, date
#### ask start day

#### check how many days since that day

### calculate how much saved each day with func

### calculate how much you need to catch up on

## output

def penny_save(j: int):
    daily_list = []
    for i in range(1,j):
        daily_list.append(round(i/100, 2))
    return daily_list



def main():
    daysStarted = int(input("Please enter how many days ago you wish to start the penny saving challange  if it's today press 0: "))
    
    StartDate = date.today() - timedelta(days=daysStarted)
    EndDate = StartDate + timedelta(days=365)

    pennyValues = penny_save(366)

    elmSave = 0
    for k in range(0, daysStarted):
        elmSave += pennyValues[k]

    print(round(elmSave, 2))


if __name__ == "__main__":
    main()