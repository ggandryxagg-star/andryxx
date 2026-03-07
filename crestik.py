import flet as ft 


def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 900
    page.window.width = 900

    btn = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=100, height=100, icon_size=100)
    btn1 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn2 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn3 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn4 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn5 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn6 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn7 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn8 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)

    page.add(btn, btn1, btn2)
    page.add(btn3, btn4, btn5)

ft.run(main=main)