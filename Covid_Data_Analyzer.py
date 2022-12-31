import os
from district import district_covid_data
from municipality import municipality_covid_data
from province import province_covid_data
from dump_to_pdf import PdfConverter


class CovidDataAnalyzer:
    def __init__(self):
        self.value=input("Which level of data you need:\n Province? or District? Or Municipality? or All?\n")
        
    def check_value(self):
        if self.value.lower()=='district':
            district_data=input("Enter name of district: ")
            district_covid_data.district(district_data)
            PdfConverter.pdf_converter_district()

        elif self.value.lower()=='municipality':
            municipality_data=input("Enter name of Municipality: ")
            municipality_covid_data.municipality(municipality_data)
            PdfConverter.pdf_converter_municipality()

        elif self.value.lower()=='province':
            province_data=int(input("Enter province number [1-7]: "))
            province_covid_data.province(province_data)
            PdfConverter.pdf_converter_province()
            `       `````````````````````````````                                                                                                                               ``````````````
        elif self.value.lower()=='all':

            district_data=input("Enter name of district: ")
            municipality_data=input("Enter name of Municipality: ")
            province_data=int(input("Enter province number [1-7]: "))
            district_covid_data.district(district_data)
            municipality_covid_data.municipality(municipality_data)
            province_covid_data.province(province_data)
            PdfConverter.pdf_converter_district()
            PdfConverter.pdf_converter_municipality()
            PdfConverter.pdf_converter_province()
        else:
            print("Invalid data! Provide valid data!!")

obj1=CovidDataAnalyzer()
obj1.check_value()






