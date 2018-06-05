#Merge two csv file

The script combines two CSV files by key

Example:

_First csv file_
```csv
id_product,reference,id_category_default,price,description_short,description,name_product
3,00100,22,0,,,"Фляжка (береста, металл)"
4,00100-1,22,0,,,"Шкатулка (дерево, лазерная гравировка)"
5,00100-10,22,0,,,"Магнит (береста)"
6,00100-11,22,0,,,"Шкатулка (береста, дерево)"
7,00100-12,22,0,,,"Шкатлука под формат А4 (береста, дерево)"
8,00100-13,22,0,,,"Шкатулка под бутылку (береста, дерево)"
9,00100-14,22,0,,,"Набор: фляжка+стопки+зажигалка (береста, дерево)"
10,00100-15,22,0,,,"Шкатулка под бутылку верт. (береста, дерево)"
```
_Second csv file_
```csv
id_product,src
3,"souvenires.ru/18462/flyazhka-beresta-metall.jpg"
4,"souvenires.ru/18469/shkatulka-derevo-lazernaya-gravirovka.jpg"
5,"souvenires.ru/18478/magnit-beresta.jpg"  
6,"souvenires.ru/18477/shkatulka-beresta-derevo.jpg"
7,"souvenires.ru/18472/shkatluka-pod-format-a4-beresta-derevo.jpg"
8,"souvenires.ru/18489/shkatulka-pod-butylku-beresta-derevo.jpg"
9,"souvenires.ru/18475/nabor-flyazhkastopkizazhigalka-beresta-derevo.jpg"
10,"souvenires.ru/18468/shkatulka-pod-butylku-vert-beresta-derevo.jpg"
```
_Output file_
```csv
id_product,reference,id_category_default,price,description_short,description,name_product,src
3,00100,22,0,,,"Фляжка (береста, металл)",souvenires.ru/18462/flyazhka-beresta-metall.jpg
4,00100-1,22,0,,,"Шкатулка (дерево, лазерная гравировка)",souvenires.ru/18469/shkatulka-derevo-lazernaya-gravirovka.jpg
5,00100-10,22,0,,,Магнит (береста),souvenires.ru/18478/magnit-beresta.jpg  
6,00100-11,22,0,,,"Шкатулка (береста, дерево)",souvenires.ru/18477/shkatulka-beresta-derevo.jpg
7,00100-12,22,0,,,"Шкатлука под формат А4 (береста, дерево)",souvenires.ru/18472/shkatluka-pod-format-a4-beresta-derevo.jpg
8,00100-13,22,0,,,"Шкатулка под бутылку (береста, дерево)",souvenires.ru/18489/shkatulka-pod-butylku-beresta-derevo.jpg
9,00100-14,22,0,,,"Набор: фляжка+стопки+зажигалка (береста, дерево)",souvenires.ru/18475/nabor-flyazhkastopkizazhigalka-beresta-derevo.jpg
10,00100-15,22,0,,,"Шкатулка под бутылку верт. (береста, дерево)",souvenires.ru/18468/shkatulka-pod-butylku-vert-beresta-derevo.jpg
```


#How to use

The script requires the installed Python interpreter version 3.6 To call the help, run the script with the -h or --help option.
```Bash
python merge_two_csv_in_one.py -h
usage: merge_two_csv_in_one.py [-h] [csv_first] [csv_second] [csv_output]

positional arguments:
  csv_first   File path to first csv file
  csv_second  File path to second csv file
  csv_output  File path to output csv file

optional arguments:
  -h, --help  show this help message and exit
```