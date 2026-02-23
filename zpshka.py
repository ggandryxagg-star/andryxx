import flet as ft
import sqlite3 
from sqlite3 import * 
from flet.controls.material.switch import Switch
from datetime import * 
import datetime


prem = {'k10':300,
        'k12':400,
        'k15':600,
        'k17':800,
        'k19':1000,
        'k21':1200,
        'night':1700,
        'day': 1600
        }


def main(page: ft.Page):
    
    page.window.width = 768
    page.window.height = 1024

    page.title = 'Zpshitatel'
    page.theme_mode = 'dark'

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER


    class zps:
        
        def __init__(self, info ):
            
            self.info = info

            page.update()


    def zpia(e):
        
        smen = None

        if btn_day.value == 'День':

            smen = prem['day']

            page.add(smen)
            page.update


        elif btn_day.selected_suffix == 'Ночь':

            smen = prem['night']

            page.add(smen)
            page.update



    btn_day = ft.Dropdown(
        text='Выберете смену',
        width=250,
        options=[
            ft.dropdown.Option('День'),
            ft.dropdown.Option('Ночь')
        ]
    )

    btn_prem = ft.Dropdown(
        text='Выберете выручку',
        width=250,
        options=[
            ft.dropdown.Option('Больше 10к'),
            ft.dropdown.Option('Больше 12к'),
            ft.dropdown.Option('Больше 15к'),
            ft.dropdown.Option('Больше 17к'),
            ft.dropdown.Option('Больше 19к'),
            ft.dropdown.Option('Больше 21к')
        ]
    )

    btn_subm = ft.Button('Отправить', width=200, on_click=zpia)
    
    page.add(
        btn_day, btn_prem
    )

    page.add(btn_subm)
    


ft.run(main=main)
