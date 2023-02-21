#when this error appears
#FutureWarning: The frame.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.


#convert
# df = pd.DataFrame(columns=['a','b','c','d'])
# list1 = ['n1','n2','n3']
# for counter in range(0,len(list1)):
#      df_temp={'a':a, 'b': a, 'c':c,'d': d}   
#      # append the result of the site to the data frame
#      df=df.append(df_temp, ignore_index = True)
# print(df)


#to 
# df = pd.DataFrame()
# list1 = ['n1','n2','n3']
# for counter in range(0,len(list1)):
#      df_temp={'a':a, 'b': a, 'c':c,'d': d}   
#      # append the result of the site to the data frame
#      df_scale = pd.concat([df_scale, new_df], axis=0, ignore_index=True)
# print(df)
