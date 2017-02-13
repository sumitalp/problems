logged_in  = [23,5,6,0]
logged_out = [0,2,15,3]

def login_sequence(logged_in,logged_out):
  str_sequence = ''
  
  for idx, l in enumerate(logged_in):
    str_sequence += 'I' * l
    str_sequence += 'O' * logged_out[idx]
    
  return str_sequence
  
print login_sequence(logged_in, logged_out)

def calculate_peak(logged_in,logged_out):
  peak_val = 0
  
  for idx, l in enumerate(logged_in):
    if peak_val==0 or (peak_val + l) - logged_out[idx] > peak_val:
      peak_val += logged_in[idx] - logged_out[idx]
      
  return peak_val
  
print calculate_peak(logged_in, logged_out)


def calculate_average(logged_in,logged_out):
  peak_val = 0
  total = 0
  
  for idx, l in enumerate(logged_in):
    peak_val += logged_in[idx] - logged_out[idx]
    total += peak_val
      
  return total / len(logged_in)
  
print calculate_average(logged_in, logged_out)
