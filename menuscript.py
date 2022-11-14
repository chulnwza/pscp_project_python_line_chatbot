"""menuscript"""
import csv

def menuscript(menutype):
    """menuscript"""
    if menutype == 'ปู':
        with open('ingredient/crab.csv', mode='r', newline='', encoding='utf8') as mycsv:
            reader = csv.reader(mycsv)
            recommend_menu = []
            first_row = 0
            for row in reader:
                if first_row != 0 and len(row[2]) == 0:
                    recommend_menu.append((row[0], row[1].split(' ,')))
                first_row += 1
    elif menutype == 'ปลา':
        with open('ingredient/fish.csv', mode='r', newline='', encoding='utf8') as mycsv:
            reader = csv.reader(mycsv)
            recommend_menu = []
            first_row = 0
            for row in reader:
                if first_row != 0 and len(row[2]) == 0:
                    recommend_menu.append((row[0], row[1].split(' ,')))
                first_row += 1
    elif menutype == 'ปลาหมึก':
        with open('ingredient/octopus.csv', mode='r', newline='', encoding='utf8') as mycsv:
            reader = csv.reader(mycsv)
            recommend_menu = []
            first_row = 0
            for row in reader:
                if first_row != 0 and len(row[2]) == 0:
                    recommend_menu.append((row[0], row[1].split(' ,')))
                first_row += 1
    elif menutype == 'กุ้ง':
        with open('ingredient/pawn.csv', mode='r', newline='', encoding='utf8') as mycsv:
            reader = csv.reader(mycsv)
            recommend_menu = []
            first_row = 0
            for row in reader:
                if first_row != 0 and len(row[2]) == 0:
                    recommend_menu.append((row[0], row[1].split(' ,')))
                first_row += 1
    elif menutype == 'หอย':
        with open('ingredient/shellfish.csv', mode='r', newline='', encoding='utf8') as mycsv:
            reader = csv.reader(mycsv)
            recommend_menu = []
            first_row = 0
            for row in reader:
                if first_row != 0 and len(row[2]) == 0:
                    recommend_menu.append((row[0], row[1].split(' ,')))
                first_row += 1
    return recommend_menu

def show_menuscript(ing_type):
    """test menuscript"""
    output = ''
    buf = menuscript(ing_type)
    for i in buf:
        ing = i[0]
        rec = ' ,'.join(i[1])
        output += '%s เมนูแนะนำ : %s\n'%(ing, rec)
    return output

def check_table():
    """table"""
    with open('table.csv', mode='r', newline='', encoding='utf8') as mycsv:
        reader = csv.reader(mycsv)
        count = 0
        table_z = []
        for i in reader:
            if count != 0 and len(i[1])==0:
                table_z.append(i[0])
            count += 1
    output = 'โต๊ะว่าง :' + '\n'
    for j in table_z:
        output += '%s \n' %j
    return output
