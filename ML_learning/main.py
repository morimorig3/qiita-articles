import numpy as np
import matplotlib.pyplot as plt

# 関数定義
def f(x):
    return x**2

# グラフ描画
plt.figure(figsize=(10, 8))

# ズーム範囲を狭く
x = np.linspace(1.3, 1.7, 200)
y = f(x)

x0 = 1.5
x1 = 1.51
h = x1 - x0

plt.plot(x, y, 'b-', linewidth=3, label='f(x) = x^2')

# 2点をプロット
plt.scatter([x0, x1], [f(x0), f(x1)], color='red', s=200, zorder=5)

# 2点を結んだ線を延長
slope = (f(x1) - f(x0)) / h
x_line = np.linspace(1.3, 1.7, 100)
y_line = f(x0) + slope * (x_line - x0)
plt.plot(x_line, y_line, 'r--', linewidth=2, alpha=0.8, 
         label=f'Line through x={x0} and x={x1}')

# ラベル
plt.text(x0-0.03, f(x0)-0.05, f'A ({x0})', fontsize=12, 
         bbox=dict(boxstyle='round,pad=0.4', facecolor='yellow', alpha=0.8))
plt.text(x1+0.02, f(x1)+0.02, f'B ({x1})', fontsize=12,
         bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgreen', alpha=0.8))

plt.xlim(1.3, 1.7)
plt.ylim(1.6, 3.0)
plt.grid(True, alpha=0.4)
plt.xlabel('x', fontsize=13)
plt.ylabel('f(x)', fontsize=13)
plt.title('Zoomed: Two close points -> tangent line', fontsize=15, fontweight='bold')
plt.legend(fontsize=11)

plt.tight_layout()
plt.show()

print(f"Point A: x = {x0}, f(x) = {f(x0)}")
print(f"Point B: x = {x1}, f(x) = {f(x1)}")
print(f"Distance: h = {h}")
print(f"Slope: {slope:.3f}")