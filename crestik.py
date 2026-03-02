import flet as ft 

def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 900
    page.window.width = 900

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    btn = ft.Button(icon=ft.Icons.ARROW_CIRCLE_DOWN)

    page.add(btn)



ft.app(target=main)