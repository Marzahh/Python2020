# 
# mitu = 10
# for i in range(1,mitu):
#     for j in range(1,mitu):
#         print("{:3d}".format(j*i),end=",")
#     print()



mitu = 10
for j in range(0,mitu):
    print("{:3d}".format (j),end=",")
print()
print("--------------------------------------")


for i in range(1,mitu):
    print("{:3d}".format (i),end="|")
 
    for j in range(1,mitu):
        print("{:3d}".format(j*i),end=",")
    print()