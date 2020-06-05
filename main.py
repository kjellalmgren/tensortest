import tensorflow as tf
from tensorflow import keras
import datetime

print(tf.version.VERSION) 
print("Kjell Osse Almgren testar python 3 på Nvidia/xavier")

#fashion_mnist = keras.datasets.fashion_mnist

print("Tensorflow version: ".format(tf.version.VERSION))
tf.debugging.set_log_device_placement(True)
# tf.enable_eager_execution()
tf.executing_eagerly()
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
print("Num CPUs Available: ", len(tf.config.experimental.list_physical_devices('CPU')))
print("-------")

with tf.device("/device:cpu:0"):
   #
   start_cpu = datetime.datetime.now()
   print("Entering CPU")
   print(tf.reduce_sum(tf.random.normal([20000, 20000])))
   end_cpu = datetime.datetime.now()
   total_cpu_time = end_cpu - start_cpu
# 
with tf.device("/device:gpu:0"):
   #
   start_gpu = datetime.datetime.now()
   print("Entering GPU")
   print(tf.reduce_sum(tf.random.normal([20000, 20000])))
   end_gpu = datetime.datetime.now()
   total_gpu_time = end_gpu - start_gpu
#
print("------")
print("total CPU-time: ", total_cpu_time)
print("total GPU-time: ", total_gpu_time)

