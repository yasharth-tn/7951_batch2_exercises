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
df=pd.read_csv(r'C:\Users\yasharth.tandon\Desktop\Tiger\imdb.csv',escapechar='\\')		       
def non_zero(row, columns):
    return list(set(list(columns[~(row == 0)])))
		       
#1st Bonus Question
def Ist_Bonus(df):
	df['duration']=df['duration']/60
	df2=df[['year','title','wordsInTitle','type','imdbRating','duration','Action','Adult','Adventure','Animation','Biography','Crime','Documentary','Documentary','Drama','Family','Fantasy','FilmNoir','GameShow','History','Horror','Music','Musical','Mystery','News','RealityTV','Romance','SciFi','Short','Sport','TalkShow','Thriller','War','Western']]	      
	df2.sort_values(by=['year'])	       
	df2.dropna(subset=['type', 'year'],inplace=True)	      
	df2.sort_values(by=['year'],inplace=True)
	df2['Genere_combo']=df2.iloc[:,6:].apply(lambda x: non_zero(x, df2.iloc[:,6:].columns), axis=1)	       
	df3=df2.groupby(['year','type']).agg({'imdbRating': ['mean','min','max'],'duration':'sum'})
	return df3	       

df=pd.read_csv(r'C:\Users\yasharth.tandon\Desktop\Tiger\imdb.csv',escapechar='\\')
def 2nd_bonus(df):
    	df['duration']=df['duration']/60
	df2=df[['year','title','wordsInTitle','type','imdbRating','duration','Action','Adult','Adventure','Animation','Biography','Crime','Documentary','Documentary','Drama','Family','Fantasy','FilmNoir','GameShow','History','Horror','Music','Musical','Mystery','News','RealityTV','Romance','SciFi','Short','Sport','TalkShow','Thriller','War','Western']]	       
	df2['length_of_title']=df2['wordsInTitle'].map(str).apply(len)	       
	x1=df2['length_of_title'].corr(df2['imdbRating'])
	df2.groupby(['year'])['length_of_title'].sum()	       
	per=np.percentile(df2['length_of_title'],[25,50,75])	       
	per1=[]	       
	for i in df2['length_of_title']:
    		if(i<per[0]):
        		per1.append('1st percentile')
    		elif(i>=per[0] and i<per[1]):
       			per1.append('2nd percentile')
    		elif(i>=per[1] and i< per[2]):
        		per1.append('3rd percentile')
    		elif(i>=per[2] ):
        		per1.append('4th percentile')	       
	  df2['percentile']=per1
          df7=pd.crosstab(df2.year,df2.percentile)
	  df8=df2.groupby(['year'])['length_of_title'].min().to_frame().reset_index()
	  df7['min_length']=df8['length_of_title'].values	       
	  df8=df2.groupby(['year'])['length_of_title'].max().to_frame().reset_index()	       
	  df7['max_length']=df8['length_of_title'].values	       
          return x1,df7
		       
#Bonus_3rd
df = pd.read_csv(r'C:\Users\yasharth.tandon\Desktop\Tiger\diamonds.csv',escapechar='\\')
def Bonus_3rd(df):		 		       
    	df1=df[df['z']!='None']
	df1['vol']=np.where(df1['depth']>60,df1['x']*df1['y']*pd.to_numeric(df1['z']),8)	       
	df1['equal_bins']=pd.qcut(df1['vol'],q=4)	       
	df5=pd.crosstab(df1.equal_bins,df1.cut,margins=True)
	x2=df5['All'].iloc[-1]	       
	df5.apply(lambda x: (x*100)/x2,axis=1)	       
	return df5
		       
df=pd.read_csv(r'C:\Users\yasharth.tandon\Desktop\Tiger\imdb.csv',escapechar='\\')
def Bonus_5th(df):
	df['duration_deciles']=pd.cut(df['duration'],bins=10)
	df2=df.groupby(['duration_deciles']).agg({'nrOfWins':['sum'],'nrOfNominations':['sum'],'title':['count']})
	df2.columns=df2.columns.droplevel()	       
	df6=df.groupby(['duration_deciles'])[df.columns.to_list()[16:-1]].sum()	       
	df6 = pd.DataFrame(df6.columns.values[np.argsort(-df6.values, axis=1)[:, :3]], index=df6.index, columns = ['Top_1_genre','Top_2_genre','Top_3_genre']).reset_index()	       
	df6.set_index(['duration_deciles'],inplace=True)	       
	df7 = pd.concat([df2, df6], axis=1)
	return df7
		      

		       
