# Title: DS5100 HW03
# Name: Aubrey Winger
# UserID: alw8ef

lst = range(1,101)
for number in lst:
    if number%3==0 and number%5==0:
        print("Wahoowah!")
    elif number%3==0:
        print("Wahoo")
    elif number%5==0:
        print("wah!")
    else:
        print(number)