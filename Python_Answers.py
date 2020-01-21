# import pandas, numpy
import pandas as pd
import numpy as np
# Create the required data frames by reading in the files

#df=pd.read_excel("SaleData.xlsx")
df1 = pd.read_excel(r"C:\Users\yasharth.tandon\Desktop\Tiger\SaleData.xlsx")
df=pd.read_csv(r'C:\Users\yasharth.tandon\Desktop\Tiger\diamonds.csv',escapechar='\\')
df2=pd.read_csv('C:\Users\yasharth.tandon\Desktop\Tiger\imdb.csv',escapechar='\\')
# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
	ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls

# Q2 compute total sales at each year X region
def sales_year_region(df):
    # write code to return pandas dataframe
    ls=df1.groupby(['Region',df1.OrderDate.dt.year])['Sale_amt'].sum().reset_index()
    return ls

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    # write code to return pandas dataframe
    df1['days_diff']=[x.days for x in dt.datetime.now()-df1.OrderDate]
    return df1


# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    # write code to return pandas dataframe
    ls=df1.groupby(['Manager'])
    ['SalesMan'].apply(np.hstack).to_frame().reset_index().rename(columns={"SalesMan":'list_of_salesmen','Manager':'manager'})
    return ls


# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe
    ls=df1.groupby(['Region']).agg({'SalesMan':[('Count',len)],'Units':[('count of       units',sum)]})
    ls.columns=ls.columns.droplevel(0)
    return ls



# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    # write code to return pandas dataframe
    ls=df1.groupby(['Manager'])['Sale_amt'].sum().to_frame().reset_index()
    ls['percent_sales']=(ls['Sale_amt']/ls['Sale_amt'].sum())*100
    ls.drop('Sale_amt',axis=1,inplace=True)   
    return ls.round({'percent_sales':2}) 

#___________________________________________________________

#df=pd.read_csv("imdb.csv",error_bad_lines=False)

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	# write code here
	return df2.iloc[4]['imdbRating']

# Q8 return titles of movies with shortest and longest run time
def movies(df):
	# write code here
    shortest=df2.loc[df2['duration']==df2['duration'].min()]['title']
    longest=df2.loc[df2['duration']==df2['duration'].max()]['title']
    return shortest,longest


# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
    ls=df2.sort_values(['year','imdbRating'],ascending=[True,False]).reset_index()
    return ls


# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	# write code here
    result_1 = df[(df['gross'] > 20000000) & (df['budget'] < 10000000) & (df['duration'] >= 30) & (df['duration'] <= 180)]
    return result_1

#____________________________________

#df=pd.read_csv('diamonds.csv',error_bad_lines=False)

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	# write code here
	return len(df)-(len(df.drop_duplicates()))

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here
	return df.dropna(subset=['cut','carat'])

# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here
	return df.select_dtypes(include =np.number)

# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	# write code here
    df3=df[df['z']!='None']
    df['vol']=np.where(df1['depth']>60,df1['x']*df1['y']*pd.to_numeric(df1['z'],8)
    df1.fillna({'vol':8},inplace=True)
    return df1[‘vol’]

	

# Q15 impute missing price values with mean
def impute(df):
	# write code here
    df['price'].fillna((df['price'].mean()), inplace=True)
    return df
