#!/usr/bin/env python
# coding: utf-8

# # First Python Project
# 
# This project is to analyze the mobile apps data to help our developers understand what type of apps are more likely to attract more users.
# Our goal is to categorize the different mobile applications on the basis of usage and understand which type of applications attract the maximum number of clients

# In[10]:


# Function to explore the data of the file 
def explore_data(data_list, start, end, val = False):
    data_slice = data_list[start:end]
    for row in data_slice:
        print(row)
        print('\n')
    
    if val:
        print('Number of rows in data slice: ',len(data_slice)) 
        print('Total Rows: ',len(data_list)-1)
        print('Number of columns: ',len(data_slice[0]), '\n')


# Function to open the file and extract the data into a list
def open_func(file_name):
    open_file = open(file_name, encoding="utf8")
    from csv import reader
    read_file = reader(open_file)
    app_list = list(read_file)
    return app_list

ios = 'C:\\Users\\stanwar\\Learning Folder\\AppleStore.csv'
android = 'C:\\Users\\stanwar\\Learning Folder\\googleplaystore.csv'

ios_list = open_func(ios)
android_list = open_func(android)

explore_data(android_list,0,1,True)
explore_data(ios_list,0,1,True)


# In[11]:


# Function to check whether any of the rows in the data has missing values. Return the updated list with all missing value rows removed
def check_missing_data(app_list):
    print('\n')
    print('Length of the list is: ', len(app_list)-1)
    header_length = len(app_list[0])
    flag = 0
    for row in app_list[1:]:
        if len(row) != header_length:
            print('Missing data error at location: ', app_list.index(row))
            print('\n Row data: ', row)
            del app_list[app_list.index(row)]
            flag = 1
    if flag == 0:
        print('No issues detected')
    print('Updated Length of list: ',len(app_list)-1)    
    return app_list


# In[12]:


android_list_updated = check_missing_data(android_list)
ios_list_updated = check_missing_data(ios_list)


# In[13]:


#function to check duplicate enteries in android list
def duplicate_entry_android(app_list):
    unique_apps = []
    duplicate_apps = []
    print('Total number of rows: ',len(app_list)-1)
    for row in app_list[1:]:
        name = row[0]
        if name in unique_apps:
            duplicate_apps.append(name)
        else:
            unique_apps.append(name)
    print('Number of duplicate apps: ',len(duplicate_apps))
    print('\n')
    print('Number of unique apps: ',len(unique_apps))
    
    unique = {}     #Dictionary to populate each app name along with the maximum number of reviews in each app
    for row in app_list[1:]:
        name = row[0]
        no_reviews = float(row[3])
        if name in unique and unique[name] < no_reviews:
            unique[name] = no_reviews
        elif name not in unique:
            unique[name] = no_reviews
    print('\n This is the length of dictionary with max reviews: ',len(unique))
    
    updated_android_list = []
    already_added = []
    for row in app_list[1:]:
        if (row[0] not in already_added) and (int(row[3]) == int(unique[row[0]])):
            updated_android_list.append(row)
            already_added.append(row[0])
    print('\n Length of updated list: ', len(updated_android_list))
    return updated_android_list
    
#function to check duplicate enteries in android list
def duplicate_entry_ios(app_list):
    unique_apps = []
    duplicate_apps = []    
    print('\n Total entries in ios_list:',len(app_list)-1)
    for row in app_list[1:]:
        name = row[1]
        if name in unique_apps:
            duplicate_apps.append(name)
        else:
            unique_apps.append(name)
    print('\n Number of duplicate apps: ',len(duplicate_apps))
    print('\n Number of unique apps: ',len(unique_apps))
    
    unique_app_max_review = {}    #Dictionary to populate each app name along with the maximum number of reviews in each app
    for row in app_list[1:]:
        name = row[1]
        no_reviews =  float(row[5])
        if name in unique_app_max_review and unique_app_max_review[name] < no_reviews:          
            unique_app_max_review[name] = no_reviews
        elif name not in unique_app_max_review:
            unique_app_max_review[name] = no_reviews            
    print('\n This is the length of dictionary with max reviews: ', len(unique_app_max_review))
    
    updated_ios_list = []
    for row in app_list[1:]:
        name = row[1]
        no_reviews = float(row[5])
        if (name in unique_app_max_review) and (no_reviews == float(unique_app_max_review[name])):
            updated_ios_list.append(row)
    print('\n Length of updated list', len(updated_ios_list))
    return updated_ios_list


# In[14]:


updated_andriod_list = duplicate_entry_android(android_list_updated)
print('\n')
updated_ios_list = duplicate_entry_ios(ios_list_updated)


# In[15]:


#function to check whether the name is english or not
def is_english(value):
    no_ascii = 0
    for x in value:
        if ord(x) > 127:
            no_ascii += 1
    if no_ascii > 3:
        return False
    else:
        return True

# Extracting only english apps from android list
count = 0
updated_list = []
for row in updated_andriod_list:
    name = row[0]   
    if is_english(name):
        count += 1
        updated_list.append(row)

print('Number of rows added are: ', count)
print('Updated android list has: ', len(updated_list), ' elements.' )
updated_andriod_list = updated_list


# In[16]:


# Extracting only english apps from ios list
count = 0
updated_list = []
for row in updated_ios_list:
    name = row[1]   
    if is_english(name):
        count += 1
        updated_list.append(row)

print('Number of rows added are: ', count)
print('Updated android list has: ', len(updated_list), ' elements.' )
updated_ios_list = updated_list


# In[17]:


# Extracting only free apps
new_andriod_list = []
for row in updated_andriod_list:
    if row[7] == '0':
        new_andriod_list.append(row)

print('\n Updated length of andriod list : ', len(new_andriod_list))
updated_andriod_list = new_andriod_list

new_ios_list = []
for row in updated_ios_list:
    if row[4] == '0.0':
        new_ios_list.append(row)

print('\n Updated length of ios list : ', len(new_ios_list), '\n')
updated_ios_list = new_ios_list


# In[18]:


# designing a sorted frequency table
def freq_table(app_list, index):
    list_genres = {}
    dummy_list = []
    for row in app_list:
        genres = row[index]
        if genres in list_genres:
            list_genres[genres] += 1
        else:
            list_genres[genres] = 1
    for row in list_genres:       
        list_genres[row] = (list_genres[row]/len(app_list)) * 100
        dummy_list.append([list_genres[row], row])
    
    list_genres = {}
    for row in sorted(dummy_list, reverse =1):
        list_genres[row[1]] = row[0]    
    
    dummy_list = []
    count = 0
    for row in list_genres:
        if ';' not in row:
            dummy_list.append([row, list_genres[row]])
        elif ';' in row:
            count += 1
            key = row.split(';')
            dummy_list.append([key[0],list_genres[row]])
            dummy_list.append([key[1],list_genres[row]])

    final_list = {}
    for row in dummy_list:
        if row[0] not in final_list:
            final_list[row[0]] = row[1]
        elif row[0] in final_list:
            val = final_list[row[0]]
            final_list[row[0]] = val + row[1]
    return final_list

        
freq_table_ios = freq_table(updated_ios_list, -5)
freq_table_android = freq_table(updated_andriod_list, 1)

freq_table_android


# In[ ]:




