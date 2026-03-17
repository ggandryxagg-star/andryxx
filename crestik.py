import flet as ft 


def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 1000
    page.window.width = 1000
    
    def crest(e):

        btn.data = 1

        if btn1.data + btn2.data % 2 == 1:

            btn.icon = ft.Icons.STOP
            btn.icon_color = "#ff0000"
            btn.disabled = True

        else:

            btn.icon = ft.Icons.STOP
            btn.icon_color = "#1e01fb"
            btn.disabled = True

        page.update()

    def crest1(e):

        btn1.data = 1

        if btn.data + btn2.data % 2 == 1:

            btn1.icon = ft.Icons.STOP
            btn1.icon_color = "#ff0000"
            btn1.disabled = True

        else:

            btn1.icon = ft.Icons.STOP
            btn1.icon_color = "#1e01fb"
            btn1.disabled = True

        page.update()

    def crest2(e):

        btn2.data = 1

        if btn1.data + btn.data % 2 == 1:

            btn2.icon = ft.Icons.STOP
            btn2.icon_color = "#ff0000"
            btn2.disabled = True

        else:

            btn2.icon = ft.Icons.STOP
            btn2.icon_color = "#1e01fb"
            btn2.disabled = True

    btn = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest)
    btn1 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest1)
    btn2 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest2)

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