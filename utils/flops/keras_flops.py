import tensorflow as tf
from keras_flops import get_flops
from tensorflow.keras.applications import (
        mobilenet,
        mobilenet_v2,
        inception_v3
        )

mobilenet_v1 = mobilenet.MobileNet(weights='imagenet')
mobilenet_v2 = mobilenet_v2.MobileNetV2(weights='imagenet')
inception_v3 = inception_v3.InceptionV3(weights='imagenet')

# Calculae FLOPS
flops = get_flops(mobilenet_v1, batch_size=1)
print(f"FLOPS: {flops / 10 ** 9:.03} G")
