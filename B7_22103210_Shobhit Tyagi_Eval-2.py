#!/usr/bin/env python
# coding: utf-8

# In[1]:


{
   "provider_id": [],
   "accept_assignment": [],
   "participation_begin_date": [],
   "practice_name": [],
   "practice_address1": [],
   "practice_address2": [],
   "practice_city": [],
   "practice_zipcode":[],
   "telephone_number":[],
   "specialities_list":[],
   "provider_type_list":[],
   "supplies_list":[],
   }


# In[2]:


import pandas as pd
df = pd.read_csv('csvfile.csv')
print(df.head())


# In[3]:


df.loc[df['provider_id'] == 20506619, 'phone_number'] = '123123123'
print("\nUpdated phone number for provider ID 20506619:")
print(df[df['provider_id'] == 20506619])


# In[ ]:


ca_providers = df[df[].str.contains('CA', case=False)]
print("Providers in CA:")
print(ca_providers)

