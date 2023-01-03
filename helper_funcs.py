from timeit import default_timer as timer
import torch
from torch import nn

def print_train_time(start:float,
                     end:float,
                     device: torch.device = None):
  ''' print out the time inbetween'''
  total_time = end - start
  print(f'Train time on {device}: {total_time:.3f} seconds')
  return total_time


import requests
from pathlib import Path

# Download helper function
if Path("helper_functions.py").is_file():
  print("helper_function.py already exist")
else:
  request = requests.get("https://raw.githubusercontent.com/mrdbourke/pytorch-deep-learning/main/helper_functions.py")
  with open("helper_functions.py", "wb") as f:
    f.write(request.content)

from helper_functions import accuracy_fn