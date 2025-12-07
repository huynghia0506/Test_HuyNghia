import pandas as pd
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import os

files = glob.glob("*.csv")
data_rows = []

for f in files:
    name = os.path.splitext(f)[0]
    parts = name.split('_')
    prefix = parts[0]
    side = 'Left' if prefix == '1' else 'Right'
    
    raw_id = "_".join(parts[2:])
    # Gộp participant 0 và 0_2
    if raw_id in ['0', '0_2']:
        participant_id = '0'
    else:
        participant_id = raw_id
    
    df = pd.read_csv(f)
    
    #Chia làm 2 parts
    mid = len(df) // 2   
    
    for segment, df_part in [('First Half', df.iloc[:mid]), ('Second Half', df.iloc[mid:])]:
        if 'arm_acc_x' in df_part.columns:
            for val in df_part['arm_acc_x']:
                data_rows.append({
                    'Participant': participant_id, 
                    'Side': side, 
                    'Limb': 'Arm', 
                    # Lưu thông tin segment để tô màu (hue) sau này
                    'Half': segment, 
                    'Value': val
                })
        if 'leg_acc_x' in df_part.columns:
            for val in df_part['leg_acc_x']:
                data_rows.append({'Participant': participant_id, 'Side': side, 'Limb': 'Leg', 'Half': segment, 'Value': val})

all_data = pd.DataFrame(data_rows)
rec_order = ['0', '1', '2']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

def plot_panel(ax, limb, side):
    subset = all_data[(all_data['Limb'] == limb) & (all_data['Side'] == side)]
    if not subset.empty:
        sns.boxplot(
            data=subset, x='Participant', y='Value', 
            hue='Half', # Tô màu dựa trên cột 'Half' (First/Second)
            order=rec_order, ax=ax, 
            palette={'First Half': '#a6cee3', 'Second Half': "#f1834d"}, # Xanh nhạt / Xanh đậm
            showfliers=False
        )
        ax.set_title(f"{side}-{limb} [acc-x]")
        

        if limb == 'Arm' and side == 'Left':
            ax.legend(loc='upper right')
        else:
            if ax.get_legend(): ax.get_legend().remove()

plot_panel(axes[0, 0], 'Arm', 'Left')
plot_panel(axes[0, 1], 'Arm', 'Right')
plot_panel(axes[1, 0], 'Leg', 'Left')
plot_panel(axes[1, 1], 'Leg', 'Right')

plt.tight_layout()
plt.show()
