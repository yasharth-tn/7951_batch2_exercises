library(dplyr)    
library(readxl)
library(lubridate)
library(imputeTS)
install.packages("readxl")
install.packages("dplyr")
install.packages("imputeTS")

my_data= read_excel('C:\\Users\\yasharth.tandon\\Desktop\\Tiger\\SaleData.xlsx')
#1st
#head(filter(my_data,Item,min(Sale_amt)))
itemsale <- group_by(my_data,Item)
minsale <- summarise(itemsale, min_sale=min(Sale_amt))
print(minsale)

#2nd Question

my_data %>% group_by(Region,year(my_data$OrderDate)) %>% summarise(sum(my_data$Sale_amt))
#print(my_)

#3rd
x= now()
#print(x)
x2=date(x)
#print(date(my_data$OrderDate))
x1=dim(my_data)
#print(x1)
#print(x1[1])
for(i in 1:x1[1]){
  my_data$days_diff = x2-date((my_data$OrderDate))
}
print(my_data$days_diff)

#4th Question

uni_manager= unique(my_data$Manager)
df6<- my_data %>% group_by(Manager) %>% summarise(list_of_salesman = list(unique(SalesMan)))
print(df6)


# 5th Question 
my_data %>% group_by(Region) %>% summarise(sales_man_count=n_distinct(SalesMan),total_sales=sum(Sale_amt))


#6th
cc1 <- sum(df5$Sale_amt)
ss6 <-df5 %>% group_by(Manager) %>% summarise(percent_sale= ((sum(Sale_amt)/cc1)*100))
print(ss6)

df1<-read.csv("C:\\Users\\yasharth.tandon\\Desktop\\Tiger\\movie_metadata.csv")
#7th
df2<-df1[5,]
df2<-df2$movie_title
print(df2)
#8
min_val<-min(df1[,"duration"],na.rm=TRUE)
max_val<-max(df1[,"duration"],na.rm=TRUE)
m1<-filter(df1,duration==min_val)
#print(m1)
m2 <- filter(df1,duration==max_val)
#print(m2)
#m1<-m1$movie_titlemin_val<-min(df1[,"duration"],na.rm=TRUE)
#max_val<-max(df1[,"duration"],na.rm=TRUE)
#m1<-filter(df1,duration==min_val)
m2 <- m2$movie_title
m2 <- m$movie_title
print(m2)
print(m1)

#nrow(df4)
#10

q1<- subset(df1,gross>2000000 & budget<1000000 &(duration >=30 & duration <=180))
print(q1)
dim(q1)

#9th
df4<-read.csv("C:\\Users\\yasharth.tandon\\Desktop\\Tiger\\imdb.csv",delim = ',',escape_backslash = T,escape_double = F)
q2 <- df4[order(df4[,24]),-(df4[,26]),]
print(q2)
#q2 <- df1 %>% arrange(title_year) %>% arrange(desc(imdb_score))
#q3 <- df4 %>% arrange(year)
#?filter

df3= read.csv("C:\\Users\\yasharth.tandon\\Desktop\\Tiger\\diamonds.csv")
#dia1<-df3 %>% distinct()
#11th
sc1 =distinct(df3)
ss1= nrow(df3)- nrow(sc1)
print(ss1)

#12th
#df3 %>% drop_na(carat,cut)
drop_rows <- function(df3){
  df3 %>% drop_na(carat,cut)
}
print(df3)
#13th


new_df<-na.omit(df3)
Filter(is.numeric,new_df)

#15th
for(i in nrow(df3))
{
  df3[is.na(df3[,i]), i] <- mean(df3[,i], na.rm = TRUE)
  
}
na_mean(df3$price)


fd=data.frame(x=df3$x)
fd[,'y']<-df3[,'y']
fd[,'depth']<-df3[,'depth']
fd[,'zfloat']<-as.numeric(as.character(df3[,'z']))
fd[,'volume']<-fd$x*fd$y*fd$zfloat
for(i in 1:nrow(fd)){
  if(fd[i,'depth']<60 & !is.na(fd[i,'depth'])){
    fd[i,'volume']=8
  }
}

print(fd$volume)
