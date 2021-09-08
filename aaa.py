readF = open("16_9_read.txt","r")
writeF = open("16_9_sum.txt","w")

list =readF.read().splitlines()

for i in list:
    total = 0
    str_list = i.split(",")
    for k in str_list[1:]:
        total += int(k)
    str_list.append(str(total))
    str_list.append(str(int(total/(len(str_list)-2)))+ "\n")
    writeF.write(",".join(str_list))

readF.close()
writeF.close()