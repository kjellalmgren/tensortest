# nvidia

## http://support.system76.com/articles/cuda/

$ sudo apt install system76-cuda-10.2
$ sudo apt install system76-cudnn-10.2
$ sudo apt install system76-nccl-10.2
## toolkit
$ sudo apt install nvidia-cuda-toolkit
#
## You can switch between each CUDA version with the following command:
$ sudo update-alternatives --config cuda
## To verify installation, run this command to see the current version of the NVIDIA CUDA compiler:
$ nvcc -V
#
## You can also check the version of the installer and patches installed with this command:
$ cat /usr/lib/cuda/version.txt
## The following article will go over installing the System76 NVIDIA driver.
$ https://support.system76.com/articles/system76-driver/
##