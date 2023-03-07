
import time
import numpy as np
from rtlsdr import RtlSdr

# Set the frequency and duration of the capture
frequency = 100e6
duration = 10

# Configure the RTL-SDR device
sdr = RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = frequency
sdr.gain = 'auto'

# Capture the RF signal and save it to a file
samples = sdr.read_samples(int(duration * sdr.sample_rate))
np.save('capture.npy', samples)

# Close the RTL-SDR device
sdr.close()