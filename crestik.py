import flet as ft 

def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 900
    page.window.width = 900

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    btn = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn1 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn2 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn3 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn4 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn5 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn6 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn7 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    btn8 = ft.Button('', icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150)
    
    page.add(btn, btn1, btn2)



ft.app(target=main)