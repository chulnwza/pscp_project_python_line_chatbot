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