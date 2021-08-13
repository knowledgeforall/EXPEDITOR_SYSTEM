#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import random for vf capacity simulation
import random
#import mysql.connector to interface with mysql
import mysql.connector
#import os to loop through files
import os
#import pandas to create dataframes and read in csv files
import pandas as pd
#import numpy to manipulate and test arrays in the LSTM model
import numpy as np
#import libraries for LSTM (Long Short-Term Memory network)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dropout
#import matplotlib.pyplot to visualize predictions
import matplotlib.pyplot as plt
#import math to help retrieve various outputs from predictions
import math
#import datetime to create a deliver date
import datetime
#import xlrd to read and write to distance matrix
import xlrd
#import smtplib, ssl to send confirmation email
import smtplib, ssl


# In[2]:


# path of excel file to be read
loc = "E:\ExpeditorDistanceMatrix.xlsm"

# open RestMatrix workbook
ExpeditorDistanceMatrix = xlrd.open_workbook(loc)
RestMatrix = ExpeditorDistanceMatrix.sheet_by_index(1)

#create random number for vertical farm capacities to simulate real world fluctuations
vf1capacity = random.randint(1,775)
vf2capacity = random.randint(1,775)
vf3capacity = random.randint(1,775)
vf4capacity = random.randint(1,775)
vf5capacity = random.randint(1,775)
vf6capacity = random.randint(1,775)
vf7capacity = random.randint(1,775)
vf8capacity = random.randint(1,775)
vf9capacity = random.randint(1,775)
vf10capacity = random.randint(1,775)


# In[3]:


#write random number into available capacity for vertical_farm_1
mydb = mysql.connector.connect(
  host="localhost",
  user="Paul",
  password="********",
  database="expeditor"
)
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_1 WHERE idVf1 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_1 (idVf1, Available_capacity) VALUES (%s, %s)"
val = (1, (vf1capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_2
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_2 WHERE idVf2 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_2 (idVf2, Available_capacity) VALUES (%s, %s)"
val = (1, (vf2capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_3
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_3 WHERE idVf3 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_3 (idVf3, Available_capacity) VALUES (%s, %s)"
val = (1, (vf3capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_4
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_4 WHERE idVf4 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_4 (idVf4, Available_capacity) VALUES (%s, %s)"
val = (1, (vf4capacity))
mycursor.execute(sql, val)

mydb.commit()

mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_5 WHERE idVf5 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_5 (idVf5, Available_capacity) VALUES (%s, %s)"
val = (1, (vf5capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_6
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_6 WHERE idVf6 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_6 (idVf6, Available_capacity) VALUES (%s, %s)"
val = (1, (vf6capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_7
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_7 WHERE idVf7 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_7 (idVf7, Available_capacity) VALUES (%s, %s)"
val = (1, (vf7capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_8
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_8 WHERE idVf8 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_8 (idVf8, Available_capacity) VALUES (%s, %s)"
val = (1, (vf8capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_9
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_9 WHERE idVf9 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_9 (idVf9, Available_capacity) VALUES (%s, %s)"
val = (1, (vf9capacity))
mycursor.execute(sql, val)

mydb.commit()

#write random number into available capacity for vertical_farm_10
mycursor = mydb.cursor()

sql = "DELETE FROM myapi_vertical_farm_10 WHERE idVf10 = '1'"

mycursor.execute(sql)

mydb.commit()

mycursor = mydb.cursor()

sql = "INSERT INTO myapi_vertical_farm_10 (idVf10, Available_capacity) VALUES (%s, %s)"
val = (1, (vf10capacity))
mycursor.execute(sql, val)

mydb.commit()


# In[4]:


# assign directory and itrate over files in directory
directory = 'files'

for filename in os.listdir('E:\Expeditor\Senior_Project_Sales_Data\One_year_dataset\customer_csvs'):
    filename_path = os.path.join('E:\Expeditor\Senior_Project_Sales_Data\One_year_dataset\customer_csvs', filename)
    #checking if it is a file
    if os.path.isfile(filename_path):
        # making data frame from csv file 
        expeditor_df = pd.read_csv((filename_path))
        
        #create a variable to use as input for assigning predictions to produce_orders table fields
        dir = (filename)
        current_filename = (dir.rsplit('.', 1)[0])
        
        #create a variable to assign correct produce type to past, present, or future order in produce_orders table
        dir1 = (current_filename)
        produce_type = (dir1.rsplit('_', 1)[1])
        
        #create variable to populate customer field in produce_orders table
        dir2 = (current_filename)
        customer = (dir2.rsplit('_', 1)[0])
        
        
        expeditor_df_processed = expeditor_df.iloc[:, 1:2].values
        
        #normalizing or scaling data
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler(feature_range = (0, 1))

        expeditor_df_scaled = scaler.fit_transform(expeditor_df_processed)
        
        #convert data to right shape
        features_set = expeditor_df.iloc[:, 0:1].values
        labels = expeditor_df_processed
        
        #convert feature_set and labels list to a numpy array
        features_set, labels = np.array(features_set), np.array(labels)
        
        #convert data into three-dimensional format
        features_set = np.reshape(features_set, (features_set.shape[0], features_set.shape[1], 1))
        
        #instantiate Sequential class
        model = Sequential()
        
        #Creating LSTM and Dropout Layers
        model.add(LSTM(units=52, return_sequences=True, input_shape= (features_set.shape[1], 1)))
        model.add(Dropout(0.2))

        model.add(LSTM(units=52, return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LSTM(units=52, return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LSTM(units=52))
        model.add(Dropout(0.2))
        
        #Creating Dense Layer with single value output
        model.add(Dense(units = 1))
        
        
        #compile model
        model.compile(optimizer = 'adam', loss = 'mean_squared_error')
        
        #Algorithm Training
        model.fit(features_set, labels, epochs = 35, batch_size =52)
        
        #testing the LSTM
        
        #importing dataset for testing
        expeditor_testing_complete = expeditor_df
        expeditor_testing_processed = expeditor_df.iloc[:, 1:2].values
        #all columns removed except 1 and 2
        #columns need to be modified for specific pertinent data
        
        #Converting Test Data to Right Format
        expeditor_total = pd.concat((expeditor_df['QUANTITY'], expeditor_testing_complete['QUANTITY']), axis=0)
        
        #prepare test inputs
        test_inputs = expeditor_total[len(expeditor_total) - len(expeditor_testing_complete) - 5:].values
        
        #scale test data
        test_inputs = test_inputs.reshape(-1,1)
        test_inputs = scaler.transform(test_inputs)
        
        #prepare final test input set
        test_features = []
        for i in range(1, 52):
            test_features.append(test_inputs[i-1:i, 0])
        
        #convert data into three-dimensional format
        test_features = np.array(test_features)
        test_features = np.reshape(test_features, (test_features.shape[0], test_features.shape[1], 1))
        
        #predict
        prediction = model.predict(test_features)
        
        #reverse the scaling
        prediction = scaler.inverse_transform(prediction)
        
        #visualize the prediction
        plt.figure(figsize=(10,6))
        plt.plot(expeditor_testing_processed, color='blue', label='Actual ordering data')
        plt.plot(prediction , color='red', label='Predicted Expeditor ordering data')
        plt.title('Expeditor ordering data')
        plt.xlabel('SHOP_WEEK')
        plt.ylabel('QUANTITY')
        plt.legend()
        plt.show()
        
        #create order prediction for vf for delivery 8 weeks in future
        vf_order = math.ceil(prediction[-1])
        
        #create orders for UI display
        order_past = math.ceil(prediction[-11])
        order_current = math.ceil(prediction[-10])
        order_future = math.ceil(prediction[-9])
        
        
        #create concatonated variables for use in sql queries
        past = "_past"
        current = "_current"
        future = "_future"
        
        produce_type_past = produce_type + past
        produce_type_current = produce_type + current
        produce_type_future = produce_type + future
        
        #create variables for use in sql queries
        email = "********@asu.edu"
        deliver_date = datetime.datetime.today() + datetime.timedelta(weeks=8)
        
        #delete data from past produce order to prep for transfer of current order data update
        import mysql.connector

        mydb = mysql.connector.connect(
          host="localhost",
          user="Paul",
          password="********",
          database="expeditor"
        )

        mycursor = mydb.cursor()

        sql = F"""DELETE FROM myapi_produce_orders WHERE Key_Value_Pair = '{current_filename}' AND Produce_type = '{produce_type_past}'"""

        mycursor.execute(sql)

        mydb.commit()
        
        
        #select current order data
        mycursor.execute(F"""SELECT Qty FROM myapi_produce_orders WHERE Key_Value_Pair = '{current_filename}' AND Produce_type = '{produce_type_current}'""")

        myresult = mycursor.fetchone()
        for x in myresult:
            order_past = x
            
        #and transfer to past order    
        mycursor = mydb.cursor()

        sql = "INSERT INTO myapi_produce_orders (Key_Value_Pair, Produce_type, Qty, Vf_Order, Customer, Customer_Email, Deliver_To, Deliver_Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = ((current_filename), (produce_type_past), (order_past), (vf_order), (customer), (email), (customer), (deliver_date))
        mycursor.execute(sql, val)

        mydb.commit()
        
        #create current order for UI display
        order = math.ceil(prediction[-10])
        
        #delete data from past produce order to prep for transfer of current order data update
        mycursor = mydb.cursor()

        sql = F"""DELETE FROM myapi_produce_orders WHERE Key_Value_Pair = '{current_filename}' AND Produce_type = '{produce_type_current}'"""

        mycursor.execute(sql)

        mydb.commit()
        
        #select future order data
        mycursor.execute(F"""SELECT Qty FROM myapi_produce_orders WHERE Key_Value_Pair = '{current_filename}' AND Produce_type = '{produce_type_future}'""")

        myresult = mycursor.fetchone()

        for x in myresult:
            order_current = x
            
        #and transfer to current order 
        mycursor = mydb.cursor()

        sql = "INSERT INTO myapi_produce_orders (Key_Value_Pair, Produce_type, Qty, Vf_Order, Customer, Customer_Email, Deliver_To, Deliver_Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = ((current_filename), (produce_type_current), (order_current), (vf_order), (customer), (email), (customer), (deliver_date))
        mycursor.execute(sql, val)

        mydb.commit()
        
        #create future order for UI display
        order_future = math.ceil(prediction[-9])
        
        #delete data from current produce order to prep for transfer of future order data update
        mycursor = mydb.cursor()

        sql = F"""DELETE FROM myapi_produce_orders WHERE Key_Value_Pair = '{current_filename}' AND Produce_type = '{produce_type_future}'"""

        mycursor.execute(sql)

        mydb.commit()
        
            
        #Future order for UI
        mycursor = mydb.cursor()

        sql = "INSERT INTO myapi_produce_orders (Key_Value_Pair, Produce_type, Qty, Vf_Order, Customer, Customer_Email, Deliver_To, Deliver_Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = ((current_filename), (produce_type_future), (order_future), (vf_order), (customer), (email), (customer), (deliver_date))
        mycursor.execute(sql, val)

        mydb.commit()
        
        #Select the closest vertical farm to the current customer order
        closest_vf = RestMatrix.cell_value(12, 2)
        
        #create an order for the vf 8 weeks out to allow time to grow and fulfill
        current_order = (vf_order)
        
        #create an array of vertical farms with capacity to fulfill order
        vf_with_capacity = []

        #search for closest available vertical farm with capacity
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_1 WHERE idVf1 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_1")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf1 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_2 WHERE idVf2 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_2")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf2 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_3 WHERE idVf3 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_3")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf3 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_4 WHERE idVf4 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_4")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf4 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_5 WHERE idVf5 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_5")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf5 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_6 WHERE idVf6 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_6")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf6 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_7 WHERE idVf7 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_7")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf7 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_8 WHERE idVf8 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_8")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf8 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_9 WHERE idVf9 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_9")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf9 = {}  New capacity = {}".format(available_capacity, new_capacity))

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Available_capacity FROM myapi_vertical_farm_10 WHERE idVf10 = '1'")
        myresult = mycursor.fetchone()

        for Available_capacity in myresult:
            available_capacity = Available_capacity
            if available_capacity > current_order:
                vf_with_capacity.append("myapi_vertical_farm_10")
            new_capacity = ((available_capacity) - (current_order))
            print("Available capacity for vf10 = {}  New capacity = {}".format(available_capacity, new_capacity))
        
        #select closest vertical farm with capacity to fulfill order
        closest_vf_with_capacity = "none"

        for closest in range(12,22):
            ((RestMatrix.cell_value)(closest, 2))
            for has_capacity in vf_with_capacity:
                if  has_capacity == ((RestMatrix.cell_value)(closest, 2)):
                    closest_vf_with_capacity = has_capacity
                    break
            else:
                continue
            break

        print("The closest vertical farm with capacity is: ", (closest_vf_with_capacity))
        
        # open TransMatrix workbook
        ExpeditorDistanceMatrix = xlrd.open_workbook(loc)
        TransMatrix = ExpeditorDistanceMatrix.sheet_by_index(2)
        
        # select closest transport to closest vertical farm with capacity
        transport = "none"

        for vertical_farm in range(12,22):
            ((TransMatrix.cell_value)(vertical_farm, 0))
            print((TransMatrix.cell_value)(vertical_farm, 0))
            print(closest_vf_with_capacity)
            if  ((TransMatrix.cell_value)(vertical_farm, 0)) == (closest_vf_with_capacity):
                transport = ((TransMatrix.cell_value)(vertical_farm, 2))
                print("match")
            else:
                print("no match")

        print("The closest transport is: ", transport)
        
        #generate year and week number and construct SHOP_WEEK column input for writing order to csv file
        year = datetime.datetime.today().year
        week_number = deliver_date.isocalendar()[1]
        shop_week = int(str(year) + str(week_number))
        
        #write the vf_order to the csv file
        shop_week_string = repr(shop_week)
        vf_order_string = repr(vf_order)
        order_write = open(filename_path, "a")
        order_write.write(shop_week_string + ",")
        order_write.write(vf_order_string + "\n")
        order_write.close()
        
        #send a confirmation email
        #port = 465
        #smtp_server = "smtp.gmail.com"
        #sender_email = "********@gmail.com"
        #receiver_email = "********@asu.edu"
        #password = "********"
        #message = f"""\
        #Your order is confirmed.
        #You will receive:
        #{vf_order}{produce_type}
        #on {deliver_date}"""

        #context = ssl.create_default_context()
        #with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            #server.login(sender_email, password)
            #server.sendmail(sender_email, receiver_email, message)
        
        #erase dataframe to begin new loop fresh
        expeditor_df.drop(['SHOP_WEEK', 'QUANTITY'], axis=1)
        break


# In[5]:


if produce_type == "Basil":
    plu = "4885"
    price = 0.5
elif produce_type == "Kale":
    plu = "4627"
    price = 1.25
elif produce_type == "Romaine":
    plu = "3097"
    price = 1
    
total_price = (price * order_current)

mycursor = mydb.cursor()

sql = "DELETE FROM myapi_rest1 WHERE id = '1'"

mycursor.execute(sql)

mydb.commit()

#and transfer to past order    
mycursor = mydb.cursor()

sql = "INSERT INTO myapi_rest1 (Nomenclature, Qty, Unit, Deliver, PLU, Price, Total) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = ((produce_type), (order_current), ('ea'), (deliver_date), (plu), (price), (total_price))
mycursor.execute(sql, val)

mydb.commit()


# In[6]:


#send a confirmation email
port = 465
smtp_server = "smtp.gmail.com"
sender_email = "ExpeditorASU@gmail.com"
receiver_email = "ppolsine@asu.edu"
password = "N3w5tart1%"
message = f"""Your order is confirmed.
You will receive:
{vf_order}{produce_type}
on {deliver_date}"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

