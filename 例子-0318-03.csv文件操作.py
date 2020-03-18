#coding=utf-8
import csv
#读文件
with open('F:\\1.csv','r') as f:
    reader=csv.reader(f)
    for i in reader:
        print(i)

#写文件
with open('F:\\3.csv','w') as f:
    file=csv.writer(f,dialect='excel')
    file.writerow([1,2,3,4,5,6])
    file.writerow([1,2,3,4,5,6])
    
print('已经完成')
