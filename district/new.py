import sqlite3
import pandas as pd

# value=int(input("Enter:\n1 for District data \n2 for Municipality data\n3 for Province data\n "))
# print(f"selected value is {value}")
value=input("Which level of data you need:\n Province? or District? Or Municipality?\n")
print(f"selected value is {value}")


if value.lower()=='district':
    district=input("Enter name of district: ")
    connection = sqlite3.connect("covid.db")
    # cursor=connection.cursor()
    # query1 = f"SELECT * FROM 'District' where title = '{district}'  "
    query1=f"SELECT Covid.currentState as Current_State,count(*) as Total FROM 'Covid','District' on Covid.district=District.id where District.title='{district}' group by currentState"
    df1=pd.read_sql_query(query1,connection)
    print(df1.head())
    f = open('district.txt', 'a')
    f.write(f"\n\nData of {district} district:\n\n----------------------Total Data of covid cases----------------------\n\n")
    f.close()
    # df1.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('district.txt', 'a') as f: df1.to_string(f, col_space=10,index=False,justify=True)
    query2=f"SELECT Covid.gender as Gender,Covid.currentState as Current_State,count(*) as Total FROM 'Covid','District' on Covid.district=District.id where District.title='{district}' group by lower(Covid.gender),Covid.currentState"
    f = open('district.txt', 'a')
    f.write("\n\n----------------------Total Data by Gender----------------------\n\n")
    f.close()
    df2=pd.read_sql_query(query2,connection)
    print(df2.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('district.txt', 'a') as f: df2.to_string(f, col_space=10,index=False,justify=True)
    query3=f"""  SELECT currentState,SUM(CASE WHEN Covid.age < 18 THEN 1 ELSE 0 END) AS [Under 18],
        SUM(CASE WHEN Covid.age BETWEEN 18 AND 30 THEN 1 ELSE 0 END) AS [18-30],
        SUM(CASE WHEN Covid.age BETWEEN 31 AND 50 THEN 1 ELSE 0 END) AS [31-50],
        SUM(CASE WHEN Covid.age > 50 THEN 1 ELSE 0 END) AS [ Above 50]
        FROM Covid,District on Covid.district=District.id where District.title='{district}' group by Covid.currentState """
    f = open('district.txt', 'a')
    f.write("\n\n----------------------Total Data by Age Group----------------------\n\n")
    f.close()
    df3=pd.read_sql_query(query3,connection)
    print(df3.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('district.txt', 'a') as f: df3.to_string(f, col_space=10,index=False,justify=True)
    query4=f"Select count(*) as Total_Death from Covid,District on Covid.district=District.id where currentState='death' and District.title='{district}' "
    f = open('district.txt', 'a')
    f.write("\n\n----------------------Total Number of death----------------------\n\n")
    f.close()
    df4=pd.read_sql_query(query4,connection)
    print(df4.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('district.txt', 'a') as f: df4.to_string(f, col_space=10,index=False,justify=True)


if value.lower()=='municipality':
    municipality=input("Enter name of Municipality: ")
    connection = sqlite3.connect("covid.db")
    # cursor=connection.cursor()
    # query1 = f"SELECT * FROM 'District' where title = '{district}'  "
    query1=f"SELECT Covid.currentState as Current_State,count(*) as Total FROM 'Covid','Municipal' on Covid.municipality=Municipal.id where Municipal.title='{municipality}' group by currentState"
    df1=pd.read_sql_query(query1,connection)
    print(df1.head())
    f = open('municipality.txt', 'a')
    f.write(f"\n\nData of {municipality} :\n\n----------------------Total Data of covid cases----------------------\n\n")
    f.close()
    # df1.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('municipality.txt', 'a') as f: df1.to_string(f, col_space=10,index=False,justify=True)
    query2=f"SELECT Covid.gender as Gender,Covid.currentState as Current_State,count(*) as Total FROM 'Covid','Municipal' on Covid.municipality=Municipal.id  where Municipal.title='{municipality}' group by lower(Covid.gender),Covid.currentState"
    f = open('municipality.txt', 'a')
    f.write("\n\n----------------------Total Data by Gender----------------------\n\n")
    f.close()
    df2=pd.read_sql_query(query2,connection)
    print(df2.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('district.txt', 'a') as f: df2.to_string(f, col_space=10,index=False,justify=True)
    query3=f"""  SELECT currentState,SUM(CASE WHEN Covid.age < 18 THEN 1 ELSE 0 END) AS [Under 18],
        SUM(CASE WHEN Covid.age BETWEEN 18 AND 30 THEN 1 ELSE 0 END) AS [18-30],
        SUM(CASE WHEN Covid.age BETWEEN 31 AND 50 THEN 1 ELSE 0 END) AS [31-50],
        SUM(CASE WHEN Covid.age > 50 THEN 1 ELSE 0 END) AS [ Above 50]
        FROM Covid,Municipal on Covid.municipality=Municipal.id where Municipal.title='{municipality}' group by Covid.currentState """
    f = open('municipality.txt', 'a')
    f.write("\n\n----------------------Total Data by Age Group----------------------\n\n")
    f.close()
    df3=pd.read_sql_query(query3,connection)
    print(df3.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('district.txt', 'a') as f: df3.to_string(f, col_space=10,index=False,justify=True)
    query4=f"Select count(*) as Total_Death from Covid,Municipal on Covid.municipality=Municipal.id where currentState='death' and Municipal.title='{municipality}' "
    f = open('municipality.txt', 'a')
    f.write("\n\n----------------------Total Number of death----------------------\n\n")
    f.close()
    df4=pd.read_sql_query(query4,connection)
    print(df4.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('municipality.txt', 'a') as f: df4.to_string(f, col_space=10,index=False,justify=True)

if value.lower()=='province':
    province=int(input("Enter province number [1-7]: "))
    connection = sqlite3.connect("covid.db")
    # cursor=connection.cursor()
    # query1 = f"SELECT * FROM 'District' where title = '{district}'  "
    query1=f"SELECT Covid.currentState as Current_State,count(*) as Total FROM 'Covid' where Covid.province='{province}' group by currentState"
    df1=pd.read_sql_query(query1,connection)
    print(df1.head())
    f = open('province.txt', 'a')
    f.write(f"\n\nData of province {province} :\n\n----------------------Total Data of covid cases----------------------\n\n")
    f.close()
    # df1.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('province.txt', 'a') as f: df1.to_string(f, col_space=10,index=False,justify=True)
    query2=f"SELECT Covid.gender as Gender,Covid.currentState as Current_State,count(*) as Total FROM 'Covid' where Covid.province='{province}' group by lower(Covid.gender),Covid.currentState"
    f = open('province.txt', 'a')
    f.write("\n\n----------------------Total Data by Gender----------------------\n\n")
    f.close()
    df2=pd.read_sql_query(query2,connection)
    print(df2.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('province.txt', 'a') as f: df2.to_string(f, col_space=10,index=False,justify=True)
    query3=f"""  SELECT currentState,SUM(CASE WHEN Covid.age < 18 THEN 1 ELSE 0 END) AS [Under 18],
        SUM(CASE WHEN Covid.age BETWEEN 18 AND 30 THEN 1 ELSE 0 END) AS [18-30],
        SUM(CASE WHEN Covid.age BETWEEN 31 AND 50 THEN 1 ELSE 0 END) AS [31-50],
        SUM(CASE WHEN Covid.age > 50 THEN 1 ELSE 0 END) AS [ Above 50]
        FROM Covid where Covid.province='{province}' group by Covid.currentState """
    f = open('province.txt', 'a')
    f.write("\n\n----------------------Total Data by Age Group----------------------\n\n")
    f.close()
    df3=pd.read_sql_query(query3,connection)
    print(df3.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('province.txt', 'a') as f: df3.to_string(f, col_space=10,index=False,justify=True)
    query4=f"Select count(*) as Total_Death from Covid where currentState='death' and Covid.province='{province}' "
    f = open('province.txt', 'a')
    f.write("\n\n----------------------Total Number of death----------------------\n\n")
    f.close()
    df4=pd.read_sql_query(query4,connection)
    print(df4.head())
    # df2.to_csv(r'district.txt', index=None, sep='\t', mode='a')
    with open('province.txt', 'a') as f: df4.to_string(f, col_space=10,index=False,justify=True)
