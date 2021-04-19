# coding=utf-8
"""
Created by 麋鹿君 on 2021/4/19.
"""
from handler.markit import mark_it
from handler.search_file import find_file

# path = "/Volumes/Jianan/Work Project/Work/myios/2021/Devote/Devote/"
path = input("Input your project file path：")
while True:
    all_file = []
    find_file(path=path, all_file=all_file)

    for fl in all_file:
        print(f'>> Now format {fl}')
        try:
            mark_it(fl)
            print(f'>> Succeed! Finish format {fl}')
        except:
            print(f'>> Failed! Format {fl} Failed')

    input("Finish~ Enter for recode")
