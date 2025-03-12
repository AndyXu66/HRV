import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

FPS = 30  # Video frame rate

def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
    
    values = [float(line.strip()) for line in data if line.strip()]
    return values

def calculate_bpm(signal, fps):
    # Find peaks (set minimum distance to avoid detecting noise)
    peaks, _ = scipy.signal.find_peaks(signal, distance=fps//3)  

    # Ensure there are at least two peaks to calculate heartbeat intervals
    if len(peaks) > 1:
        peak_intervals = np.diff(peaks) / fps  # Calculate the time intervals between peaks (seconds)
        bpm_values = 60 / peak_intervals  # Compute BPM for each interval
        avg_bpm = np.mean(bpm_values)  # Compute the average BPM
    else:
        avg_bpm = 0  # Return 0 if there are not enough peaks

    return avg_bpm, peaks


def plot_rppg_with_peaks(signal1, peaks1, signal2, peaks2):
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))  
    
    
    axes[0].plot(signal1, color='blue', linestyle='-', linewidth=1, label="Predicted rPPG")
    axes[0].plot(peaks1, [signal1[i] for i in peaks1], "ro", label="Peaks")  
    axes[0].set_xlabel("Frame")
    axes[0].set_ylabel("Signal Amplitude")
    axes[0].set_title("rPPG Signal")
    axes[0].legend()
    axes[0].grid(True)
    axes[0].text(0.5, 0.99, f"Average Heart Rate: {avg_bpm1:.2f} BPM",
                 transform=axes[0].transAxes, fontsize=16, verticalalignment='top',
                 horizontalalignment='center', 
                 bbox=dict(facecolor='white', alpha=0.6))

    axes[1].plot(signal2, color='blue', linestyle='-', linewidth=1, label="PPG")
    axes[1].plot(peaks2, [signal2[i] for i in peaks2], "ro", label="Peaks")  
    axes[1].set_xlabel("Frame")
    axes[1].set_ylabel("Signal Amplitude")
    axes[1].set_title("PPG Signal Groundtruth")
    axes[1].legend()
    axes[1].grid(True)
    axes[1].text(0.5, 0.99, f"Average Heart Rate: {avg_bpm2:.2f} BPM",
                 transform=axes[1].transAxes, fontsize=16, verticalalignment='top',
                 horizontalalignment='center', 
                 bbox=dict(facecolor='white', alpha=0.6))

    plt.tight_layout()  
    plt.show()

if __name__ == '__main__':  
    file_path1 = "./UBFC_subject13_rPPG.txt"       # rPPG file
    file_path2 = "./subject13_rppg_signal_gt.txt"  # Ground truth PPG file

    rppg_signal1 = read_txt_file(file_path1)
    rppg_signal2 = read_txt_file(file_path2)

    avg_bpm1, peaks1 = calculate_bpm(rppg_signal1, FPS)
    avg_bpm2, peaks2 = calculate_bpm(rppg_signal2, FPS)

    print(f"rPPG - Average Heart Rate: {avg_bpm1:.2f} BPM")
    print(f"PPG Groundtruth - Average Heart Rate: {avg_bpm2:.2f} BPM")

    plot_rppg_with_peaks(rppg_signal1, peaks1, rppg_signal2, peaks2)
