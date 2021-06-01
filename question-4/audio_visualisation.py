from matplotlib.pyplot import figure
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# Read stored audio files for comparison
fs1, data1 = wavfile.read("question-4/kami_ingin_memohon_maaf.wav")
fs2, data2 = wavfile.read("question-4/Hafiz_memohon_maaf_similar.wav")
fs3, data3 = wavfile.read("question-4/Hafiz_memohon_maaf_different.wav")
fs4, data4 = wavfile.read("question-4/Hafiz_apologising_english.wav")

# Take the max values (amplitude) along axis
data1 = np.amax(data1, axis=1)
data2 = np.amax(data2, axis=1)
data3 = np.amax(data3, axis=1)
data4 = np.amax(data4, axis=1)

figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')

# Configure matplotlib
plt.gcf().clear()
plt.style.use('seaborn-whitegrid')

# Plot 2x2 grid


# JNT: "Kami ingin memohon maaf"
ax = plt.subplot(2, 2, 1)
ax.plot(data1, color='#67A0DA')

# Change Title
ax.set_title('JNT: "Kami ingin memohon maaf"')
ax.title.set_fontsize(13)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


#
# Hafiz: "Kami ingin memohon maaf" - Similar speed & intonation
#
ax = plt.subplot(2, 2, 2)
ax.plot(data2, color='#DAA067')

# Change Title
ax.set_title('Hafiz: "Kami ingin memohon maaf" - Similar speed & intonation')
ax.title.set_fontsize(13)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


#
# Hafiz: "Kami ingin memohon maaf" - Different speed & intonation
#
ax = plt.subplot(2, 2, 3)
ax.plot(data3, color='#3FBF7F')

# Change Title
ax.set_title('Hafiz: "Kami ingin memohon maaf" - Different speed & intonation')
ax.title.set_fontsize(13)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


#
# Hafiz: "We want to apologise" - Similar speed & intonation
#
ax = plt.subplot(2, 2, 4)
ax.plot(data4, color='#DADA67')

# Change Title
ax.set_title('Hafiz: "We want to apologise" - Similar speed & intonation')
ax.title.set_fontsize(13)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


# Display created figure
fig=plt.show()
display(fig)