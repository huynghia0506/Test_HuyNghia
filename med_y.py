import pandas as pd
import os

#Group 0
file_1_0 = ['1_sbj_0.csv', '1_sbj_0_2.csv']
file_2_0 = ['2_sbj_0.csv', '2_sbj_0_2.csv']

#Group 1
file_1_1 = ['1_sbj_1.csv']
file_2_1 = ['2_sbj_1.csv']

#Group 2
file_1_2 = ['1_sbj_2.csv']
file_2_2 = ['2_sbj_2.csv']

def cal_med_y(file_list, column_name='arm_acc_y'):
    data_frames = []
    for file in file_list:
        df = pd.read_csv(file)
        data_frames.append(df[column_name])          
    if data_frames:
        combined_series = pd.concat(data_frames)
        return combined_series.median()
    else:
        return None


med_1_0 = cal_med_y(file_1_0)
med_2_0 = cal_med_y(file_2_0)


med_1_1 = cal_med_y(file_1_1)
med_2_1 = cal_med_y(file_2_1)


med_1_2 = cal_med_y(file_1_2)
med_2_2 = cal_med_y(file_2_2)



print("KẾT QUẢ TÍNH MEDIAN CỦA arm_acc_y")


print("Nhóm 0 (Gộp 0 & 0_2):")
print(f"  - 1_: {med_1_0}")
print(f"  - 2_: {med_2_0}")

print("\nNhóm 1:")
print(f"  - 1_: {med_1_1}")
print(f"  - 2_: {med_2_1}")

print("\nNhóm 2:")
print(f"  - 1_: {med_1_2}")
print(f"  - 2_: {med_2_2}")
