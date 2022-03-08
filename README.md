# Dictionary_Attack

```python
# Answer: rdma

# condition
#   1. only lowcase Enlgish letter
#   2. 7 (_______)
#   3. 8.03GB = 26*26*26*26*26*26*26

import hashlib

outputfile = open("dictionary.txt",'w')
enc = hashlib.md5()


## 6
for i in range (0,26):
    target = chr(97+i)
    for j in range(0,26):
        target2 = target + chr(97+j)
        for k in range(0, 26):
            target3 = target2 + chr(97 + k)
            for l in range(0, 26):
                target4 = target3 + chr(97 + l)
                for n in range(0,26):
                        target5 = target4 + chr(97 + n)
                        for m in range(0,26):
                                target6 = target5 + chr(97+m)
                                hashval = enc.update(target6)
                                hashval = enc.hexdigest()
                                print(target6,str(hashval))
                                outputfile.write(target6 + ' ' + str(hashval)+'\n
```

![image](https://user-images.githubusercontent.com/67637935/156923377-7c414d68-e54d-4636-b401-3b24b98b5814.png)

![image](https://user-images.githubusercontent.com/67637935/157201403-4bee4fc0-fc98-4c9d-927b-684d5272c449.png)

![image](https://user-images.githubusercontent.com/67637935/156923524-7b229c21-2ef9-40ec-b4c4-d0ca49bae1c1.png)
