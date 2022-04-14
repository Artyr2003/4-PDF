import pandas as pd 
import matplotlib.pyplot as plt 
import os
dataset = pd.DataFrame({ 
    'Fname':['Harry','Sally','Paul','Abe','June','Mike','Tom'], 
    'Age':[21,34,42,18,24,80,22], 
    'Weight': [180, 130, 200, 140, 176, 142, 210], 
    'Gender':['M','F','M','M','F','M','M'], 
    'State':['Washington','Oregon','California','Washington','Nevada','Texas','Nevada'],
    'Children':[4,1,2,3,0,2,0],
    'Pets':[3,2,2,5,0,1,5] ,
    'uytuty':['M','F','M','M','F','M','M'], 
    'ytitye':['Washington','Oregon','California','Washington','Nevada','Texas','Nevada'],
    'Cyturen':[4,1,2,3,0,2,0],
    'Pytus':[3,2,2,5,0,1,5] 
}) 
print (dataset) 

#Создание графика 
#--------------->
ase=[]
fig= plt.figure(figsize=(5.5,3.5))
ax = plt.gca() 

dataset.plot(kind='line',x=str(dataset.columns[0]),y=str(dataset.columns[5]), color='green',ax=ax) 
dataset.plot(kind='line',x=str(dataset.columns[0]),y=str(dataset.columns[6]), color='red',ax=ax) 

ase.append('Kost1.png')
plt.savefig('Kost1.png')
ax = plt.gca() 

dataset.plot(kind='line',x=str(dataset.columns[0]),y=str(dataset.columns[5]), color='red',ax=ax) 
dataset.plot(kind='line',x=str(dataset.columns[0]),y=str(dataset.columns[6]), color='green',ax=ax) 

#Сохронение графика
#------------->
ase.append('Kost2.png')
plt.savefig('Kost2.png')
#-------------<
#---------------<
def installer_png_to_pdf(list_name_png):
    size=len(list_name_png)
    for nom in range(size):
        pdf.image(list_name_png[nom], x = None, y = None, w = 0, h = 0, type = '', link = '')
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), list_name_png[nom])
        os.remove(path)


def output_df_to_pdf(pdf, df):
    #Ширини и высота ячейки таблицы данных
    #------------->
    table_cell_width = 25
    table_cell_height = 6
    #-------------<
    #Шрифт таблицы данных
    #------------->
    pdf.set_font('Arial', 'B', 8)
    #-------------<
    #Получение таблицы данных в виде массива
    #------------->
    cols = df.columns
    #-------------<
    #Заполнение таблицы данных
    #--------------->
    #Максемальное количество столбиков в одной строке
    #------------->
    kol=7
    #-------------<
    #Количество строк
    #------------->
    cols_kol=len(cols)//kol+(len(cols)%kol!=0)
    #-------------<
    #Цикол для перехода на новую строку в нужном месте и в нужном каличестве
    #------------->
    for nam in range(cols_kol):
    #-------------<
        for col in cols[nam*kol:kol*nam+kol]:
           pdf.cell(table_cell_width, table_cell_height, col, align='C', border=1)
        pdf.ln(table_cell_height)
        
        for row in df.itertuples():
            for col in cols[nam*kol:kol*nam+kol]:
                value = str(getattr(row,col))
                pdf.cell(table_cell_width, table_cell_height, value, align='C', border=1)
            pdf.ln(table_cell_height)  
        pdf.ln(table_cell_height)
        
    pdf.ln(table_cell_height)
    #---------------<
from fpdf import FPDF
#Создание и заполнение pdf
#------------>
pdf = FPDF()
pdf.add_page()
#Добавление графика в pdf 
#---------->
#pdf.image('Kost.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
installer_png_to_pdf(ase)
#----------<
#Отступ на 20 пикселей
#---------->
pdf.ln(20)
#----------<
#Добавление index в таблицу данных
#---------->
dataset_pdf = dataset.reset_index()
#----------<
#Запись таблицы данных
#---------->
output_df_to_pdf(pdf, dataset_pdf)
#----------<
#------------<
#Сохронение pdf файла
#---------->
pdf.output('simple_demo.pdf', 'F')
#----------<

#Удаление картинку графика
#---------->

#----------<


