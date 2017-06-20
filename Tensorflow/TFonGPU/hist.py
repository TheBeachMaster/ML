import tensorflow as tf

k = tf.placeholder(tf.float32)

mean_moving_normal = tf.random_normal(shape=[1000], mean=(5*k), stddev=1)

tf.summary.histogram("Normal/Moving mean",mean_moving_normal)

sess = tf.Session()

sess = tf.Session()
writer = tf.summary.FileWriter("/tmp/histogram_example")
N = 400
for step in range(N):
    k_val = step/float(N)
    summ = sess.run(summaries,feed_dict={k: k_val})
    writer.add_summary(summ,global_step=step)