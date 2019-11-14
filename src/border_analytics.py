import csv
import os
import math
# print (os.getcwd() )
os.chdir("..")


def round_value(value) :
    if value - math.floor(value) >= 0.5: 
        return math.ceil(value)
    else:
        return math.floor(value)

def sum_values(data):
    bmd_dict = {}
    for i,v in enumerate(data) :
        if i == 0 : continue
        tup = (v[3], v[5], v[4])
        value = int(v[6])
        if tup not in bmd_dict:
            bmd_dict[tup] = value
        else :
            bmd_dict[tup] += value
    sorted_bmd = sorted(bmd_dict.items(), key=lambda x:(x[0],x[1]))
    return sorted_bmd


def moving_avg(sorted_bmd) :
    output = []
    tup_prev = (" ", " ")
    sub_total = 0
    count = 0
    for i,v in enumerate(sorted_bmd) :
        value = v[1]
        tup_ = v[0]
        tup_cur = (tup_[0], tup_[1])
        date = tup_[2]

        if tup_cur != tup_prev:
            output.append([tup_cur[0],date,tup_cur[1],value,0])
            sub_total = value
            count = 1
        else:
            avg = sub_total/count
            avg = round_value(avg)
            output.append([tup_cur[0],date,tup_cur[1],value,avg])
            sub_total += value
            count += 1
        
        tup_prev = tup_cur

    return output



def final_output(output,column_names):
    final_output = sorted(output, key = lambda x:(x[1],x[3],x[2],x[0]), reverse = True)
    new_column_names = [column_names[3],column_names[4],column_names[5],column_names[6],"Average"]
    final_output.insert(0,new_column_names)
    return  final_output

## read csv
data = []
with open('./input/Border_Crossing_Entry_Data.csv') as csvfile:
    reader  = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(row)
csvfile.close()

## manipulation
column_names = data[0]
sorted_bmd = sum_values(data)
output = moving_avg(sorted_bmd)
foutput = final_output(output,column_names)

## write to csv
with open('./output/report.csv', 'w') as f:
    writer = csv.writer(f,)    
    for row in foutput:
        writer.writerow(row)
f.close()