from module import daily, weekly


if __name__ == "__main__":
    j = 0
    k = 0
    for i in range(1,366):
        j += i/100
        #daily(i, j)
        weekly(i, j, k)
            
    print("\nIn total that makes: £",round(j, 2))
