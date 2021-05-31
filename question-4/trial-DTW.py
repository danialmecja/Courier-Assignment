from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from scipy.io import wavfile
import numpy as np

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# Read audio files in folder
fs1, data1 = wavfile.read("question-4/kami_ingin_memohon_maaf.wav")
fs2, data2 = wavfile.read("question-4/Hafizthingy.wav")
fs3, data3 = wavfile.read("question-4/Hafizthingydifferent.wav")
fs4, data4 = wavfile.read("question-4/IguessthatsokayHafiz.wav")

# Taking max values along axis
data1 = np.amax(data1, axis=1)
data2 = np.amax(data2, axis=1)
data3 = np.amax(data3, axis=1)
data4 = np.amax(data4, axis=1)

# Plot style
plt.style.use('seaborn-whitegrid')

print(fastdtw(data1, data2)[0])
print(fastdtw(data1, data3)[0])
print(fastdtw(data1, data4)[0])

# create subplots
ax = plt.subplot(1, 1, 1)
ax.plot(data1, color=("#67A0DA"), alpha=0.5)
ax.plot(data2, color="#DAA067", alpha=0.5)
ax.plot(data3, color='#DADA67', alpha=0.5)
ax.plot(data4, color='#3FBF7F', alpha=0.5)
fig = plt.show()
display(fig)
