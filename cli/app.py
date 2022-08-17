# ask start day
# check how many days since that day
# calculate how much saved each day with func
# calculate how much you need to catch up o
# output
from datetime import timedelta, date


def penny_save(j: int):
    daily_list = []
    for i in range(1, j):
        daily_list.append(i/100)
    return daily_list


def interateAdder(_list: list):
    k = 0
    for l in _list:
        k += l
    return k


def main():
    daysStarted = int(input(
        "Please enter how many days ago you wish to start the penny saving challange  if it's today press 0: "))

    match bool(daysStarted == 0):
        case False:
            print("You want to have started", daysStarted, "days ago")

    StartDate = date.today() - timedelta(days=daysStarted)
    EndDate = StartDate + timedelta(days=365)

    print("Your start date for saving : ", StartDate)
    print("Your end date for saving : ", EndDate)

    match bool(daysStarted == 0):
        case False:
            reduntacy = interateAdder(penny_save(daysStarted+1))
            print("In order to catch up our redundancy to catch up is £", reduntacy)

    pennyValues = interateAdder(penny_save(366))
    print("At the end of the 365 days you'll have £", pennyValues)


if __name__ == "__main__":
    main()
