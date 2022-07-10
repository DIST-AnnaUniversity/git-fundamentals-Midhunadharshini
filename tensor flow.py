#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tensorflow


# In[2]:


import tensorflow as tf
tensor_a = tf.constant([[1,2]], dtype = tf.int32)
tensor_b = tf.constant([[3, 4]], dtype = tf.int32)
tensor_add = tf.add(tensor_a, tensor_b)
print(tensor_add)


# In[3]:


import tensorflow as tf
tensor_a = tf.constant([[1,2]], dtype = tf.int32)
tensor_b = tf.constant([[3, 4]], dtype = tf.int32)
tensor_subtract = tf.subtract(tensor_a, tensor_b)
print(tensor_subtract)


# In[4]:


import tensorflow as tf
tensor_a = tf.constant([[1,2]], dtype = tf.int32)
tensor_b = tf.constant([[3, 4]], dtype = tf.int32)
tensor_mul= tf.multiply(tensor_a, tensor_b)
print(tensor_mul)


# In[ ]:




