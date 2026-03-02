import flet as ft 


def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 900
    page.window.width = 900

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    btn = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn1 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn2 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn3 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn4 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn5 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn6 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn7 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    btn8 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100)
    

    column1 = ft.Column(
        controls=[
            btn, btn1, btn2
        ]
    )

    column2 = ft.Column(
        controls=[
            btn3, btn4, btn5
        ]
    )

    column3 = ft.Column(
        controls=[
            btn6, btn7, btn8
        ]
    )

    page.add(column1)
    page.add(column2)
    page.add(column3)

ft.app(target=main)