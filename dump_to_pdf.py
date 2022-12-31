
from fpdf import FPDF

class PdfConverter():
   @staticmethod
   def pdf_converter_district():
      pdf = FPDF()
      imagelist=['district_total.png','district_male_data.png','district_female_data.png','district_age_group_data.png']
      x,y,w,h = 0,0,200,200
      for image in imagelist:
         pdf.add_page()
         pdf.image(image,x,y,w,h)
      pdf.output("district.pdf", "F")

   @staticmethod
   def pdf_converter_municipality():
      pdf = FPDF()
      imagelist=['municipality_total.png','municipality_male_data.png','municipality_female_data.png','municipality_age_group_data.png']
      x,y,w,h = 0,0,200,200
      for image in imagelist:
         pdf.add_page()
         pdf.image(image,x,y,w,h)
      pdf.output("municipality.pdf", "F")

   @staticmethod
   def pdf_converter_province():
      pdf = FPDF()
      imagelist=['province_total.png','province_male_data.png','province_female_data.png','province_age_group_data.png']
      x,y,w,h = 0,0,200,200
      for image in imagelist:
         pdf.add_page()
         pdf.image(image,x,y,w,h)
      pdf.output("province.pdf", "F")


