import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('planck_data.txt', dtype=float)
h = data[0]
c = data[1]
kB = data[2]
T = data[3]
lambda_start = data[4]
lambda_end = data[5]
num_points = int(data[6])

lambda_m = np.linspace(lambda_start * 1e-9, lambda_end * 1e-9, num_points)

B = (2 * h * c**2) / (lambda_m**5) * 1 / (np.exp((h * c) / (lambda_m * kB * T)) - 1)

plt.figure(figsize=(10, 6))
plt.plot(lambda_m * 1e9, B, 'b-', linewidth=1.5, label='Спектр Планка')
plt.fill_between(lambda_m * 1e9, B, where=(lambda_m >= 400e-9) & (lambda_m <= 750e-9), 
                  color='yellow', alpha=0.3, label='Видимий діапазон')

lambda_max = 2.898e-3 / T
plt.axvline(x=lambda_max * 1e9, color='r', linestyle='--', 
            label=f'Максимум (λ_max = {lambda_max*1e9:.1f})')

plt.xlabel('Довжина хвилі λ', fontsize=12)
plt.ylabel('B(λ)', fontsize=12)
plt.title(f'Випромінювання абсолютно чорного тіла', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.xlim(lambda_start, 3000)
plt.tight_layout()
plt.savefig('planck_spectrum.png', dpi=150)
plt.show()

print(f"Довжина хвилі максимуму: {lambda_max*1e9:.1f} нм")
