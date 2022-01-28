# Currency converter
with open('CurrData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amt = int(input("Enter the amount: \n"))
print("Available exchange options --> \n")
[print(item) for item in currencyDict.keys()]
currency = input("In which currency do you want to convert ? \n")
print(f"{amt} INR is equal to {amt * float(currencyDict[currency])}{currency}")