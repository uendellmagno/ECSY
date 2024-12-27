import torch
import tensorflow as tf
import threading

from sandbox.ears import who_listens
from sandbox.mouth import who_speaks


def ml_models(a, b):
    x = torch.rand(a, b)
    y = tf.reduce_sum(x, axis=1)
    print(x, y)


def listen_and_respond():
    understood, language = who_listens()
    who_speaks(understood, language)

    print(f"You said: {understood}")
