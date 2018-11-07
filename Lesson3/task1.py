ans2 = ans3 = ans4 = ans5 = ans6 = ans7 = ans8 = ans9 =0

SIZE = 100
for i in range(2, SIZE):
    if i % 2 == 0:
        ans2 += 1
    if i % 3 == 0:
        ans3 += 1
    if i % 4 == 0:
        ans4 += 1
    if i % 5 == 0:
        ans5 += 1
    if i % 6 == 0:
        ans6 += 1
    if i % 7 == 0:
        ans7 += 1
    if i % 8 == 0:
        ans8 += 1
    if i % 9 == 0:
        ans9 += 1

print (ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9)

