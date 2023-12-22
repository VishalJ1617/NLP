#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install the library

get_ipython().system('pip install langdetect')

from langdetect import detect, detect_langs

def language_detection(text, method = "single"):

  """
  @desc: 
    - detects the language of a text
  @params:
    - text: the text which language needs to be detected
    - method: detection method: 
      single: if the detection is based on the first option (detect)
  @return:
    - the langue/list of languages
  """

  if(method.lower() != "single"):
    result = detect_langs(text)

  else:
    result = detect(text)

  return result


# In[2]:


text = 'मेरा नाम सुहास  सदाशिव  कोलेकर है.'

language_detection(text)


# In[3]:


Text ='माझं नाव विशाल जगदाळे राहणार सातारा. '

language_detection(Text)


# In[7]:


sent ='hello there'

language_detection(sent)


# In[6]:


tst = 'и ам сухас садашев колекар.' 

language_detection(tst)


# In[8]:


tst = 'ই আমি ইন এই ক্লাস ' 

language_detection(tst)


# In[ ]:




