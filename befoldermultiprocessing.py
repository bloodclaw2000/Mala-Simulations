!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:41:29 2024

@author: Pablo
"""
import numpy as np
import mala
import subprocess
import ase
import ase.io.espresso
from ase import Atoms
from ase.visualize import view
import os
from os.path import join as pj
import matplotlib.pyplot as plt
import re
import random
import time
import os
import multiprocessing
import fnmatch


def myfunc(data):
    # Example function, you should replace this with your actual processing function
    return data * 2


def process_file(i):
    print(f"Be{i}.pw.out")
    parameters = mala.Parameters.load_from_file("mala_parameters_01.json")
    data_converter = mala.DataConverter(parameters)
    data_converter.add_snapshot(descriptor_input_type="espresso-out",
                                descriptor_input_path=f"Be{i}.pw.out",
                                target_input_type=".cube",
                                target_input_path=f"tmp.pp0*Be{i}_ldos.cube",
                                additional_info_input_type="espresso-out",
                                additional_info_input_path=f"Be{i}.pw.out",
                                )
    data_converter.convert_snapshots(
        "./snapshots/", naming_scheme="Be_snapshot*.npy", starts_at=i)
    print(f"done {i} ")
    return 1


def process_files(file_paths, numfiles, num_processes):
    with multiprocessing.Pool(processes=num_processes) as pool:
        # results = pool.starmap(process_file, [(i, func) for i in range(len(file_paths))])

        i = np.arange(1, numfiles + 1)
        print(i)
        results = pool.map(process_file, i)

    return results


if __name__ == "__main__":
    # Replace 'data*.out' with your file pattern
    time1 = time.time()
    file_pattern = 'Be*.pw.out'
    files = [filename for filename in os.listdir(
    ) if fnmatch.fnmatch(filename, file_pattern)]
    print(len(files))
    parameters = mala.Parameters.load_from_file("mala_parameters_01.json")
    num_processes = int(input("Enter the number of processes to use: "))
    results = process_files(files, len(files), num_processes)
    print(results)
    time2 = print(time.time - time1)
