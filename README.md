# Machine learning for computational materials science and chemistry with MALA. A Basic Fully Online Pipeline and Framework 
## Introduction
In this project we show how a Materials Learning Algorithms (MALA) [MALA](https://github.com/mala-project/mala) Framework and Pipeline works.
From the generation of the DFT data with Quantum Espresso, the conversion via descriptors to MALA,
the training and testing of a neural network and finally the hyperparameter optimisation of the neural network (TODO in v3).

We show a framework that can run locally on an Ubuntu machine, on a Windows machine using Google Colaboratory's free cloud
computing framework for [Quantum Espresso](https://www.quantum-espresso.org/)  and a locally installed MALA, and finally in a fully online pipeline using Google's resources
for both DFT simulations and neural network training.    
## DFT Files Generation
DFT simulations are created using Google Colab's tool, we focus on simulating both Be2 and Si2 systems's LDOS [Colab File](Quantum_Espresso_Input_Files_Colab.ipynb).
The files generated will be randomized by varying randomly Cell Parameters or Atomic Positions.
Files are then downloaded in Zip for following processing. Only needs the Pseudopotencial files included [Si pseudo](Si.pz-vbc.UPF)  [Be pseudo](Be.pbe-n-rrkjus_psl.1.0.0.UPF)

## MALA Simulation
MALA simulations are able to be run both through COLAB's environment  in [Colab File](mala_notebookv2_colab.ipynb) and locally with the [notebook](mala_notebookv2.ipynb). For running locally, only a MALA installation and 
[Pytorch](https://pytorch.org/get-started/locally/) are needed, and works both in Windows and Linux Environments. [LAMMPS](https://www.lammps.org/) is optional but not needed as it needs special compiling [instructions](https://github.com/mala-project/mala/blob/develop/docs/source/install/installing_lammps.rst). 
### Data Conversion
For Data conversion there is both a tool in the notebook and (as it is a slow process) optional .py files [befile](Sifoldermultiprocessing) [sifile](Sifoldermultiprocessing) to copy into materials folder to generate MALA conversion files using Multiprocessing.
It is needed to create the /snapshots folder inside the materials folder manually
### Results
We use a NN in Mala to predict the LDOS of the different snapshots as a proof of concept of the MALA environment and framework.
NN are very simple but are able to predict within <10meV/at the energy bands in Be2 systems and within <60meV in Si2 systems.
Showing a clear improvement over other ML-DFT algorithms
