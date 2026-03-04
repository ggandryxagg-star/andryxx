import flet as ft 


def main(page: ft.Page):
    
    page.title = 'Крестики_нолики'

    page.window.height = 900
    page.window.width = 900

    

    btn = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.START)
    btn1 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.CENTER)
    btn2 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.END)
    btn3 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.START)
    btn4 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.CENTER)
    btn5 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.END)
    btn6 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.START)
    btn7 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.CENTER)
    btn8 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, alignment=ft.MainAxisAlignment.END)

    page.add(btn, btn1, btn2)
    page.add(btn3, btn4, btn5)

ft.run(main=main)