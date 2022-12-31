
import requests
import sqlite3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from requests.exceptions import HTTPError
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

class DumpToDatabase:
    def make_get_request(self,url):

        try:
            disable_warnings(InsecureRequestWarning)
            response = requests.get(url,verify=False)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP Error occured: {http_err}')
        except Exception as err:
            print(f'Other error occured: {err}')
        else:
            print('Successful get request', response)
            return response


    def dump_district_to_database(self):
        url='https://data.askbhunte.com/api/v1/districts'
        response_district=self.make_get_request(url)
        connection = sqlite3.connect("covid.db")
        cursor=connection.cursor()
        cursor.execute('Create Table if not exists District (id Int PRIMARY KEY,title Text,title_en Text,title_ne Text,code Text,province Int)')

        district_data = response_district.json()
        columns = ['id','title','title_en','title_ne','code','province']

        for row in district_data:
            keys= tuple(row[c] for c in columns)
            cursor.execute('insert into District values(?,?,?,?,?,?)',keys)
            print(f'{row["title"]} data inserted Succefully')

        connection.commit()

    def dump_covid_data_to_database(self):
        url='https://data.askbhunte.com/api/v1/covid'
        response_covid=self.make_get_request(url)
        connection = sqlite3.connect("covid.db")
        cursor=connection.cursor()
        cursor.executescript(
            """
             DROP TABLE IF EXISTS Covid;
            create table Covid ( id Int PRIMARY KEY,
            province Int,district Int,municipality Int, createdOn Text,modifiedOn Text,label Text,gender TEXT,
            age Int,occupation Text,reportedOn Text, recoveredOn Text,deathOn Text,currentState Text,
            isReinfected Text, source Text,comment Text, type Text, nationality Text,ward Int,
            FOREIGN KEY(district) REFERENCES District(id),
            FOREIGN KEY(municipality) REFERENCES Municipal(id)
            );"""
            )
        covid_data = response_covid.json()
        columns = ['id' ,
        'province','district','municipality' ,
        'createdOn',
        'modifiedOn',
        'label',
        'gender',
        'age' ,'occupation',
        'reportedOn' , 
        'recoveredOn',
        'deathOn',
        'currentState',
        'isReinfected',
        'source',
        'comment',
        'type',
        'nationality',
        'ward']
        for row in covid_data:
            keys= tuple(row[c] for c in columns)
            cursor.execute('insert into Covid values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',keys)
            print(f'Province {row["province"]} data inserted Succefully')
        connection.commit()


    def dump_municipal_to_database(self):
        url='https://data.askbhunte.com/api/v1/municipals'
        response_municipal=self.make_get_request(url)
        connection = sqlite3.connect("covid.db")
        cursor=connection.cursor() 
        cursor.executescript(
        """
        DROP TABLE IF EXISTS Municipal;
        create table Municipal ( id Int PRIMARY KEY,title Text,title_en Text,title_ne Text,type Text,
        code Text,district Int
        );"""
        )
        municipal_data = response_municipal.json()
        columns = ['id','title','title_en','title_ne','type','code','district']
        for row in municipal_data:
            keys= tuple(row[c] for c in columns)
            cursor.execute('insert into Municipal values(?,?,?,?,?,?,?)',keys)
            print(f'{row["title"]} data inserted Succefully')

        connection.commit()  



obj1=DumpToDatabase()
obj1.dump_district_to_database()
obj1.dump_municipal_to_database()
obj1.dump_covid_data_to_database()
                
      

    
            


            

