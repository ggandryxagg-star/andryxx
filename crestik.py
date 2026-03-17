import flet as ft 


def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 1000
    page.window.width = 1000
    
    def crest(e):

        pass

    btn = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, data=0, on_click=crest)
    btn1 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, data=0, on_click=crest)
    btn2 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest)

    column1 = ft.Row(
        controls=[
            btn,
            btn1,
            btn2
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    page.add(column1)
    

ft.run(main=main)