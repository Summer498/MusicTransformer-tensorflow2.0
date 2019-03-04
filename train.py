from model import MusicTransformer
import tensorflow as tf
import numpy as np
import params as par
import sequence
import utils
import time

if __name__ == '__main__':
    model = MusicTransformer()
    optimizer = tf.train.AdamOptimizer(par.l_r)
    model.compile(optimizer=optimizer, loss=par.loss_type)

    x= np.zeros(shape=[par.batch_size, par.max_seq])
    y = np.ones(shape=[par.batch_size], dtype=np.int)

    # print(model.summary())
    start_time = time.time()
    model.train_on_batch(x=x,y=model.processed_y(y))
    end_time = time.time()

    print(model.summary())
    print('update per time: {}'.format(end_time-start_time))