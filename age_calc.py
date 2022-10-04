def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today - dob).days / 365.25)
    print(age)
#I was having an error running this and I realized I didnt call the function, always remember to call your function guys
ageCalculator(2000, 12, 9)    