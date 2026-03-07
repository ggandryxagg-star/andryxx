import flet as ft 


def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 900
    page.window.width = 900

    def crest(e):
        pass

    btn = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn1 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn2 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn3 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn4 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn5 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn6 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn7 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn8 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)

    page.add(btn, btn1, btn2)
    

ft.run(main=main)