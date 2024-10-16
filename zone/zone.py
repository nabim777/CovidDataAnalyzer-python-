# import DumpToDatabase
import sqlite3
import pandas as pd

class CovidDataAnalyzer:
   
    # query = "SELECT * FROM 'zone' where title = 'Kaski' "
    # df=pd.read_sql_query(query,connection)
    # print(df.head())
#         print(df.head())
#         self.connection.close()
#         # return self.cursor.execute(query).fetchall()
#         df=pd.read_sql_query(query,self.connection)
#         print(df.head())
#         self.connection.close()

    def __init__(self,municipality,district,province):
        self.municipality=municipality
        self.district=district
        self.province=province

    def print_data(self):
        print(f"Given data:\n Municipality: {self.municipality}\n District: {self.district}\n Province:{self.province}")
    
   
        
    def query_district(self):
        connection = sqlite3.connect("covid.db")
        # cursor=connection.cursor()
        query = f"SELECT * FROM 'District' where title = '{self.district}' "
        df=pd.read_sql_query(query,connection)
        print(df.head())
        df.to_csv(r'district.txt', index=None, sep=' ', mode='a')

    def query_municipality(self):
        connection = sqlite3.connect("covid.db")
        query = f"SELECT * FROM 'Municipal' where title = '{self.municipality}';"
        df=pd.read_sql_query(query,connection)
        print(df.head())
        df.to_csv(r'municipality.txt', index=None, sep=' ', mode='a')

    def query_province(self):
        connection = sqlite3.connect("covid.db")
        query = f"SELECT * FROM 'Covid' where province = '{self.province}';"
        df=pd.read_sql_query(query,connection)
        print(df.head())
        df.to_csv(r'province.txt', index=None, sep=' ', mode='a')




obj1=CovidDataAnalyzer('Pokhara','Kaski',4)
obj1.print_data()
obj1.query_district()
obj1.query_municipality()
obj1.query_province()

