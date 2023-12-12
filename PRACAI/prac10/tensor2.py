import   tensorflow as tf

mat = tf.fill((5,5) , 8)
zeros = tf.zeros((5,5))
ones = tf.ones((4,4))

op = [mat , zeros , ones]

for ops in op:
    print(op)