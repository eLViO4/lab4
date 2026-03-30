import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('west_nile.txt')
year = data[:, 0].astype(int)
cases_inv = data[:, 1]
cases_noninv = data[:, 2]

fig, ax = plt.subplots(figsize=(12, 7))

x = np.arange(len(year))
width = 0.35

bars1 = ax.bar(x - width/2, cases_inv, width, label='Нейроінвазивний', color='steelblue', edgecolor='black')
bars2 = ax.bar(x + width/2, cases_noninv, width, label='Ненейроінвазивний', color='coral', edgecolor='black')

ax.set_xlabel('Рік', fontsize=12)
ax.set_ylabel('Кількість випадків', fontsize=12)
ax.set_title('Захворюваність на лихоманку західного нілу у США (1999 -2008 )', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(year)
ax.legend(loc='upper left', fontsize=10)
ax.grid(axis='y', alpha=0.3, linestyle='--')

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('west_nile_virus.png', dpi=150)
plt.show()
