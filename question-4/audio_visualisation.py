from matplotlib.pyplot import figure
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# Read stored audio files for comparison
fs1, data1 = wavfile.read("question-4/kami_ingin_memohon_maaf.wav")
fs2, data2 = wavfile.read("question-4/Hafizthingy.wav")
fs3, data3 = wavfile.read("question-4/Hafizthingydifferent.wav")
fs4, data4 = wavfile.read("question-4/IguessthatsokayHafiz.wav")

# Take the max values along axis
data1 = np.amax(data1, axis=1)
data2 = np.amax(data2, axis=1)
data3 = np.amax(data3, axis=1)
data4 = np.amax(data4, axis=1)

figure(num=None, figsize=(12, 6), dpi=80, facecolor='w', edgecolor='k')

# Configure matplotlib
plt.gcf().clear()
plt.style.use('seaborn-whitegrid')

#
# Plot 2x2 grid
#

#
# Doors and corners, kid. That's where they get you.
#
ax = plt.subplot(2, 2, 1)
ax.plot(data1, color='#67A0DA')

# Change Title
ax.set_title("JNT memohon maaf")
ax.title.set_fontsize(10)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


#
# Doors and corners, kid. That's where they get you. (v2)
#
ax = plt.subplot(2, 2, 2)
ax.plot(data2, color='#DAA067')

# Change Title
ax.set_title("Hafiz memohon maaf")
ax.title.set_fontsize(10)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


#
# You walk into the room too fast, the room eats you.
#
ax = plt.subplot(2, 2, 3)
ax.plot(data3, color='#3FBF7F')

# Change Title
ax.set_title("Hafiz memohon maaf - diff intonation")
ax.title.set_fontsize(10)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


#
# Doors and corners, kid. That's where they get you. (v3)
#
ax = plt.subplot(2, 2, 4)
ax.plot(data4, color='#DADA67')

# Change Title
ax.set_title("Hafiz apologising in English")
ax.title.set_fontsize(10)

# change the style of the axis spines
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])


# Display created figure
fig=plt.show()
display(fig)