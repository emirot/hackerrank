#!/bin/python3

import math
import os
import random
import re
import sys
from functools import lru_cache

# Complete the stepPerms function below.
@lru_cache(maxsize=128)
def stepPerms(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
