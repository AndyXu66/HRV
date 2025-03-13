# Heart rate validation
## Overview
This tool is designed to compare remote Photoplethysmography (rPPG) signal output with ground truth PPG signal from a text file. The tool reads the two signals, computes the heart rate in beats per minute (BPM), and visualizes the signals with detected peaks, making it easy to evaluate the model's performance.
## Purpose
+ Input:
  + An rPPG signal text file (model output)
  + A ground truth PPG signal text file
+ Output:
  + Two line plots displaying both signals with detected peaks
  + The average heart rate (BPM) for both signals
  + A clear comparison of model performance vs. ground truth
## Customization
+ Changing FPS
  If your video has a different frame rate, update the FPS variable accordingly.
+ Using Different Data Files
Modify file paths in the script to load different data.
