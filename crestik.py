import flet as ft 


def main(page: ft.Page):
    
    page.title = 'Крестики нолики'

    page.window.height = 1000
    page.window.width = 1000
    
    textus = ft.Text('Победил синий игрок')
    textus_20 = ft.Text('Победил красный игрок')

    def crest(e):

        btn.data = 1

        if btn1.data + btn2.data + btn3.data + btn4.data + btn5.data % 2 == 1:

            btn.icon = ft.Icons.STOP
            btn.icon_color = "#ff0000"
            btn.disabled = True


        elif btn.icon_color == btn1.icon_color and btn1.icon_color == btn2.icon_color and btn.icon_color == '#ff0000':

            page.add(textus_20)
                        
        else:

            btn.icon = ft.Icons.STOP
            btn.icon_color = "#1e01fb"
            btn.disabled = True

        page.update()

    def crest1(e):

        btn1.data = 1

        if btn.data + btn2.data + btn3.data + btn4.data + btn4.data % 2 == 1:

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

        if btn1.data + btn.data + btn3.data + btn4.data + btn5.data % 2 == 1:

            btn2.icon = ft.Icons.STOP
            btn2.icon_color = "#ff0000"
            btn2.disabled = True

        else:

            btn2.icon = ft.Icons.STOP
            btn2.icon_color = "#1e01fb"
            btn2.disabled = True

        page.update()

    def crest3(e):

        btn3.data = 1

        if btn1.data + btn2.data + btn.data + btn4.data + btn5.data% 2 == 1:

            btn3.icon = ft.Icons.STOP
            btn3.icon_color = "#ff0000"
            btn3.disabled = True

        else:

            btn3.icon = ft.Icons.STOP
            btn3.icon_color = "#1e01fb"
            btn3.disabled = True

        page.update()

    def crest4(e):

        btn4.data = 1

        if btn.data + btn2.data + btn3.data + btn1.data + btn5.data % 2 == 1:

            btn4.icon = ft.Icons.STOP
            btn4.icon_color = "#ff0000"
            btn4.disabled = True

        else:

            btn4.icon = ft.Icons.STOP
            btn4.icon_color = "#1e01fb"
            btn4.disabled = True

        page.update()

    def crest5(e):

        btn5.data = 1

        if btn1.data + btn.data + btn3.data + btn4.data + btn2.data % 2 == 1:

            btn5.icon = ft.Icons.STOP
            btn5.icon_color = "#ff0000"
            btn5.disabled = True

        else:

            btn5.icon = ft.Icons.STOP
            btn5.icon_color = "#1e01fb"
            btn5.disabled = True

        page.update()

    btn = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest)
    btn1 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest1)
    btn2 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest2)
    btn3 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest3)
    btn4 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest4)
    btn5 = ft.IconButton(icon=ft.Icons.CROP_SQUARE_SHARP, width=150, height=150, icon_size=100, data=0, on_click=crest5)

    column1 = ft.Row(
        controls=[
            btn,
            btn1,
            btn2
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )


    column2 = ft.Row(
        controls=[
            btn3,
            btn4,
            btn5
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    page.add(column1, column2)
    

ft.run(main=main)