import pandas as pd
import glob
import os

#Thu thập danh sách tất cả bài tập
files = glob.glob("1_sbj_*.csv")
all_labels = set()

for f in files:
    df = pd.read_csv(f)
    if 'label' in df.columns:
        labels = df['label'].dropna().unique()
        all_labels.update(labels)

#Sắp xếp tên bài tập
sorted_labels = sorted(list(all_labels))

#Đếm 
participant_files = {
    'Participant 0': ['1_sbj_0.csv', '1_sbj_0_2.csv'],
    'Participant 1': ['1_sbj_1.csv'],
    'Participant 2': ['1_sbj_2.csv']
}

results = {}

for p, p_files in participant_files.items():
    p_counts = {}
    for f in p_files:
        if os.path.exists(f):
            df = pd.read_csv(f)
            if 'label' in df.columns:
                # Đếm trực tiếp theo tên nhãn
                counts = df['label'].value_counts()
                for label, count in counts.items():
                    if pd.notna(label):
                        p_counts[label] = p_counts.get(label, 0) + count
    results[p] = p_counts

#Tạo bảng
data_for_df = []
for label in sorted_labels:
    row = {'Activity': label}
    for p in participant_files.keys():
        row[p] = results[p].get(label, 0)
    data_for_df.append(row)

df_summary = pd.DataFrame(data_for_df)

print("\nBẢNG THỐNG KÊ SỐ LƯỢNG MẪU (SAMPLES)")
print(df_summary.to_string(index=False))