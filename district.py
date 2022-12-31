import sqlite3
import pandas as pd
class district_covid_data:
    @staticmethod
    def district(district):
            connection = sqlite3.connect("covid.db")

            #*********Query to get total data*********
            query1=f"SELECT Covid.currentState as Current_State,count(*) as Total FROM 'Covid','District' on Covid.district=District.id where District.title='{district}' group by currentState"
            df1=pd.read_sql_query(query1,connection)
            total_bargraph=df1.plot.bar(title='Total covid data Districtwise:',x='Current_State', rot=0).get_figure()
            total_bargraph.savefig('district_total.png')
            print(df1.head())
            f = open('district.txt', 'a')
            f.write(f"\n\nData of {district} district:\n\n----------------------Total Data of covid cases----------------------\n\n")
            f.close()
            with open('district.txt', 'a') as f: df1.to_string(f, col_space=10,index=False,justify=True)
            

            #*********Query to get total data gender-male*********
            query2=f"SELECT Covid.currentState as Current_State,count(*) as Total FROM 'Covid','District' on Covid.district=District.id where District.title='{district}' and lower(Covid.gender)='male' group by Covid.currentState "
            f = open('district.txt', 'a')
            f.write("\n\n----------------------Total Data by Gender----------------------\n")
            f.write("\n----------------------Total Data of Male----------------------\n\n")
            f.close()
            df2=pd.read_sql_query(query2,connection)
            total_bargraph_male=df2.plot.bar(title='Total covid data of male Districtwise:',x='Current_State', rot=0).get_figure()
            total_bargraph_male.savefig('district_male_data.png')
            
            print(df2.head())
            with open('district.txt', 'a') as f: df2.to_string(f, col_space=10,index=False,justify=True)

            #*********Query to get total data of gender-female*********
            query2_1=f"SELECT Covid.currentState as Current_State,count(*) as Total FROM 'Covid','District' on Covid.district=District.id where District.title='{district}' and lower(gender)='female' group by Covid.currentState "
            f = open('district.txt', 'a')
            f.write("\n\n----------------------Total Data of Female----------------------\n\n")
            f.close()
            df2_1=pd.read_sql_query(query2_1,connection)
            total_bargraph_female=df2_1.plot.bar(title='Total covid data of female Districtwise:',x='Current_State', rot=0).get_figure()
            total_bargraph_female.savefig('district_female_data.png')
            with open('district.txt', 'a') as f: df2_1.to_string(f, col_space=10,index=False,justify=True)


            #*********Query to get total data of different Age group*********
            query3=f"""  SELECT currentState,SUM(CASE WHEN Covid.age < 18 THEN 1 ELSE 0 END) AS [Under 18],
                SUM(CASE WHEN Covid.age BETWEEN 18 AND 30 THEN 1 ELSE 0 END) AS [18-30],
                SUM(CASE WHEN Covid.age BETWEEN 31 AND 50 THEN 1 ELSE 0 END) AS [31-50],
                SUM(CASE WHEN Covid.age > 50 THEN 1 ELSE 0 END) AS [ Above 50]
                FROM Covid,District on Covid.district=District.id where District.title='{district}' group by Covid.currentState """
            f = open('district.txt', 'a')
            f.write("\n\n----------------------Total Data by Age Group----------------------\n\n")
            f.close()
            df3=pd.read_sql_query(query3,connection)
            total_bargraph_age_group=df3.plot.bar(title='Total covid data of Agegroup Districtwise:',x='currentState', rot=0).get_figure()
            total_bargraph_age_group.savefig('district_age_group_data.png')
            print(df3.head())
            with open('district.txt', 'a') as f: df3.to_string(f, col_space=10,index=False,justify=True)



            query4=f"Select count(*) as Total_Death from Covid,District on Covid.district=District.id where currentState='death' and District.title='{district}' "
            f = open('district.txt', 'a')
            f.write("\n\n----------------------Total Number of death----------------------\n\n")
            f.close()
            df4=pd.read_sql_query(query4,connection)
            print(df4.head())
            with open('district.txt', 'a') as f: df4.to_string(f, col_space=10,index=False,justify=True)
            