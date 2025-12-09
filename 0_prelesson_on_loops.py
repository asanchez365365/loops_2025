# Loops video  https://www.youtube.com/watch?v=KWgYha0clzw&t=1s&pp=ygUOYnJvIGNvZGUgbG9vcHM%3D
# While loops  
#for loops = execute a block of code a fixed number of times

for x in range(1,11):
    print(x)
print("HAPPY NEW YEAR")

for x in range (1,11,2):
    print(x)

credit_card = "1234-4675-3333-3333"
for x in credit_card:
    print(x)

for x in range(1,21):
    if x == 13:
        continue #break
    else:
        print(x)
