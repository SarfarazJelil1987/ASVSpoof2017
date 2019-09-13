## Get Started

### Grab a paperspace machine with ML-in-box configuration or create a virtual environment as follows:

pew new joint_anatomy_segmentation --python=python3 -r requirements.txt

pew workon joint_anatomy_segmentation

### Install Ipython kernel

python3 -m pip install ipykernel

python3 -m ipykernel install --user

## Pre-requisites
1) CUDA- 10.0 with tensorflow-gpu=1.13.1 and tensorboard==1.13.1

2) CUDA- 9.0 with tensorflow-gpu==1.12.0 and tensorboard==1.12.2

**Run the following notebooks in order to download data, build the segmentation model and do view classification**

1) For training the anatomy segmentation models with and without data balancing run the following notebook:
   
   [Joint_view_model_training.ipynb](Joint_view_model_training.ipynb)

2) To do view classification using the anatomy segmentation models run the following notebook:
   
   [view_classification.ipynb](view_classification.ipynb)

3) To download the new dataset and evaluate view classification use this notebook:
   
   [Test_on_new_data.ipynb](Test_on_new_data.ipynb)

4) To use the models for anatomy segmentation use this notebook:
   
   [Joint_anatomy_segmentation.ipynb](Joint_anatomy_segmentation.ipynb)   


