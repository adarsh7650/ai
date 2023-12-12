import tensorflow.compat.v1 as tf
# If below two line give error then delete it or comment it 
print(f"TensorFlow Version: {tf.version}")
tf.compat.v1.disable_eager_execution()

print("\nAddition code:")
a = tf.constant(5)
b = tf.constant(3)
with tf.Session() as sess:
    sum = sess.run(a+b)
print(f"Result : {sum}")
