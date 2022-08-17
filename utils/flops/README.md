# CNN model Flops 계산

### MobileNet V1, MobileNet V2, Inception V3 model (Tensorflow-FP32)
    python3 keras_flops.py


### Yolo V5 model (Tensorflow-FP32)
ref. https://pytorch.org/hub/ultralytics_yolov5/



### Yolo V5 model (EdgeTPU tflite-INT8, tflite-FP16, tflite-INT8)
    pip3 install git+https://github.com/lisosia/tflite-flops
    python3 -m tflite_flops [model name]


### Summary Table

|MobileNet V1 (TF-FP32)|MobileNet V2 (TF-FP32)|Inception V3 (TF-FP32)|Yolo V5 </br> (TF-FP32)|Yolo V5 </br> (EdgeTPU-tflite-INT8)|Yolo V5 </br> (tflite-FP16)|Yolo V5 </br> (tflite-INT8)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1.15(GFLOPS)|0.615(GFLOPS)|11.5(GFLOPS)|17.4(GFLOPS)|5.9(GFLOPS)|16.4(GFLOPS)|16.4(GFLOPS)|
