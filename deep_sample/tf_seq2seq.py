import tensorflow as tf
import random
import math
import numpy as np
from tensorflow_0_12 import seq2seq
from tensorflow_0_12 import rnn_cell
from tensorflow.models.tutorials.rnn.translate import seq2seq_model

model = seq2seq_model.Seq2SeqModel(10, 10, [(3, 3), (6, 6)], 16, 2,
                                   5.0, 5, 0.3, 0.99, num_samples=8)
sess = tf.Session()
sess.run(tf.initialize_all_variables())
data_set = ([([2, 3], [4])],[([6, 5, 4, 3], [ 3, 2 ])])
for i in xrange(100000):
   bucket_id = random.choice([0, 1])
   encoder_inputs, decoder_inputs, target_weights = model.get_batch(data_set, bucket_id)
   grad,loss,_ = model.step(sess, encoder_inputs, decoder_inputs, target_weights,bucket_id, False)
   if i%100==0:
       perplexity = math.exp(loss) if loss < 300 else float('inf')
       print ("step:{}  perplexity:{}".format(i,perplexity))
       _,loss,output = model.step(sess, encoder_inputs, decoder_inputs, target_weights, bucket_id, True)
       outs= [np.argmax(logit, axis=1) for logit in output]
       print ("encoder_inputs:",[ a[0] for a in encoder_inputs])
       print ("decoder_inputs:",[ a[0] for a in decoder_inputs])
       print ("output:",[ a[0] for a in outs])
