# import pandas, numpy
# Create the required data frames by reading in the files

# Q1 Find least sales amount for each item
# has been solved as an example
def least_sales(df):
    # write code to return pandas dataframe
	ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls

# Q2 compute total sales at each year X region
def sales_year_region(df):
    # write code to return pandas dataframe

# Q3 append column with no of days difference from present date to each order date
def days_diff(df):
    # write code to return pandas dataframe

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    # write code to return pandas dataframe

# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    # write code to return pandas dataframe


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    # write code to return pandas dataframe
    return q10

# Q7 get imdb rating for fifth movie of dataframe
def fifth_movie(df):
	# write code here

# Q8 return titles of movies with shortest and longest run time
def movies(df):
	# write code here

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
	# write code here

# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
def subset_df(df):
	# write code here

# Q11 count the duplicate rows of diamonds DataFrame.
def dupl_rows(df):
	# write code here

# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
	# write code here

# Q13 subset only numeric columns
def sub_numeric(df):
	# write code here

# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
	# write code here

# Q15 impute missing price values with mean
def impute(df):
	# write code here
