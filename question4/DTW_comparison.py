from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from scipy.io import wavfile
import numpy as np

from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

# Read audio files in folder
fs1, data1 = wavfile.read("question4/kami_ingin_memohon_maaf.wav")
fs2, data2 = wavfile.read("question4/Hafiz_memohon_maaf_similar.wav")
fs3, data3 = wavfile.read("question4/Hafiz_memohon_maaf_different.wav")
fs4, data4 = wavfile.read("question4/Hafiz_apologising_english.wav")

# Taking the max values (amplitude) along axis
data1 = np.amax(data1, axis=1)
data2 = np.amax(data2, axis=1)
data3 = np.amax(data3, axis=1)
data4 = np.amax(data4, axis=1)

# Plot style
plt.style.use('seaborn-whitegrid')

def compare_1_and_2():
    print("The distance between clip 1 and clip 2 is:", fastdtw(data1, data2)[0])

    plt.gcf().clear()
    plt.style.use('seaborn-whitegrid')
    plt.plot(data1, color='#67A0DA')
    plt.plot(data2, color='#DAA067', alpha=0.5)
    fig=plt.show()

def compare_1_and_3():
    print("The distance between clip 1 and clip 3 is:", fastdtw(data1, data3)[0])
    
    plt.gcf().clear()
    plt.style.use('seaborn-whitegrid')
    plt.plot(data1, color='#67A0DA', alpha=0.5)
    plt.plot(data3, color='#3FBF7F', alpha=0.5)
    fig=plt.show()

def compare_1_and_4():
    print("The distance between clip 1 and clip 4 is:", fastdtw(data1, data4)[0])
    
    plt.gcf().clear()
    plt.style.use('seaborn-whitegrid')
    plt.plot(data1, color='#67A0DA')
    plt.plot(data4, color='#DADA67', alpha=0.5)
    fig=plt.show()

def calculate_distance():
    distance1_2 = fastdtw(data1, data2)[0]
    distance1_3 = fastdtw(data1, data3)[0]
    distance1_4 = fastdtw(data1, data4)[0]


    print("The distance between clip 1 and clip 2 is:", distance1_2)
    print("The distance between clip 1 and clip 3 is:", distance1_3)
    print("The distance between clip 1 and clip 4 is:", distance1_4)

    compare_dict = {"Distance 1 to 2": distance1_2, "Distance 1 to 3": distance1_3, "Distance 1 to 4": distance1_4}
    
    print("\nSorted List using TimSort:")
    sorted_dict = dict(sorted(compare_dict.items(), key = lambda item: item[1]))
    
    print(sorted_dict)


# create subplots - comparing all
def visualise_all():
    ax = plt.subplot(1, 1, 1)
    ax.plot(data1, color=("#67A0DA"), alpha=0.5) # Blue - Sample file
    ax.plot(data2, color="#DAA067", alpha=0.5)   # Orange - Similar intonation + speed
    ax.plot(data3, color='#fcfc44', alpha=0.5)   # Yellow - Diff. intonation + speed
    ax.plot(data4, color='#21de80', alpha=0.5)   # Light green - Diff. Language - Similar intonation + speed
    fig = plt.show()


visualise_all()
calculate_distance()