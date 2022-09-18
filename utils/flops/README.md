# CNN model Flops 계산

### MobileNet V1, MobileNet V2, Inception V3 model (Tensorflow-FP32)
    python3 keras_flops.py


### Yolo V5 model (Tensorflow-FP32)
ref(1). https://github.com/ultralytics/yolov5


### Yolo V5 model (EdgeTPU tflite-INT8, tflite-FP16, tflite-INT8)
    pip3 install git+https://github.com/lisosia/tflite-flops
    python3 -m tflite_flops [model name]


# NLP model Flops 계산

### BERT(BASE), DistilBERT model (Tensorflow-FP32)
ref(1). Xiangyang Liu, Tianxiang Sun, Junliang He, Jiawen Wu, Lingling Wu, Xinyu Zhang, Hao Jiang, Zhao Cao, Xuanjing Huang, Xipeng Qiu, "Towards Efficient NLP: A Standard Evaluation and A Strong Baseline", Association for Computational Linguistics, July 2022, https://arxiv.org/pdf/2110.07038.pdf

ref(2). https://github.com/fastnlp/ElasticBERT/blob/main/FLOPs/flops_counter.py


# Summary Table

[CNN model]

|MobileNet V1 (TF-FP32)|MobileNet V2 (TF-FP32)|Inception V3 (TF-FP32)|Yolo V5 </br> (TF-FP32)|Yolo V5 </br> (EdgeTPU-tflite-INT8)|Yolo V5 </br> (tflite-FP16)|Yolo V5 </br> (tflite-INT8)|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1.15(GFLOPS)|0.615(GFLOPS)|11.5(GFLOPS)|16.5(GFLOPS)|5.9(GFLOPS)|16.4(GFLOPS)|16.4(GFLOPS)|

[NLP model]
|BERT (BASE-TF-FP32)|DistilBERT (TF-FP32)|
|:---:|:---:|
|13.39(GFLOPS)|6.7(GFLOPS)|
