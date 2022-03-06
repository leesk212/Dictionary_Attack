# Answer: gpurdma

# condition
#   1. only lowcase Enlgish letter
#   2. 7 (_______)
#   3. 8.03GB = 26*26*26*26*26*26*26

outputfile = open("dictionary.txt",'w')


## 7
# for i in range (0,26):
#     target = chr(97+i)
#     for j in range(0,26):
#         target2 = target + chr(97+j)
#         for k in range(0, 26):
#             target3 = target2 + chr(97 + k)
#             for l in range(0, 26):
#                 target4 = target3 + chr(97 + l)
#                 for n in range(0, 26):
#                     target5 = target4 + chr(97 + n)
#                     for m in range(0, 26):
#                         target6 = target5 + chr(97 + m)
#                         for o in range(0, 26):
#                             target7 = target6 + chr(97 + o)
#                             print(target7)
#                             outputfile.write(target7+'\n')

## 6
# for i in range (0,26):
#     target = chr(97+i)
#     for j in range(0,26):
#         target2 = target + chr(97+j)
#         for k in range(0, 26):
#             target3 = target2 + chr(97 + k)
#             for l in range(0, 26):
#                 target4 = target3 + chr(97 + l)
#                 for n in range(0, 26):
#                     target5 = target4 + chr(97 + n)
#                     for m in range(0, 26):
#                         target6 = target5 + chr(97 + m)
#                         print(target6)
#                         outputfile.write(target6+'\n')


## 4
for i in range (0,26):
    target = chr(97+i)
    for j in range(0,26):
        target2 = target + chr(97+j)
        for k in range(0, 26):
            target3 = target2 + chr(97 + k)
            for l in range(0, 26):
                target4 = target3 + chr(97 + l)
                print(target4)
                outputfile.write(target4 + '\n')




