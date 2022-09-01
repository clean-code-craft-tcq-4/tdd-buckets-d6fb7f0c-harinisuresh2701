def sample_to_amp_conversion(samples):
  current_samples_in_amps = []
  for i in samples:
    if (error_handling(i)=="All is well!"):
      current_samples_in_amps.append(round(10 * i / 4094))
  return current_samples_in_amps
      
def error_handling(sample):
  if (sample < 0 or type(sample)!= int):
    return "Current sample is not a positive integer!"
  elif sample not in range(0,4095):
    return "Current sample is out of valid range of [0 - 4094]!"
  else:
    return "All is well!"
