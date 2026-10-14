#!/usr/bin/env python
# coding: utf-8

# # Assignment 2 - custom exception

# In[ ]:


class OutOfSampleError(Exception):
    """
    Raised when a new input contains feature values
    outside the historical min/max range.
    """
    pass

