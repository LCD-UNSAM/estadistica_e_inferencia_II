import matplotlib.pyplot as plt
import numpy as np
import arviz as az
import preliz as pz

az.style.use("arviz-doc")

_, ax = plt.subplots(figsize=(12, 4))
bw = 0.4
np.random.seed(202)
y = np.array([1.8, 2, 2.6, 3.6, 3.7, 3.9])
x = np.linspace(y.min() - bw * 3, y.max() + bw * 3, 200)
kernels = np.transpose([pz.Normal(i, bw).pdf(x) for i in y])
ax.plot(x, kernels, 'k--', alpha=0.5)
ax.plot(y, np.zeros(len(y)), 'C0o')
ax.plot(x, kernels.sum(1), color="C0", lw=3)

ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('w')
plt.savefig('KDE_example.png')
