import flet as ft 


def main(page: ft.Page):
    
    hods = ft.Text('Синие', color="#3700ff")

    hods1 = ft.Text('Красные', color="#ff0808")

    page.title = 'Крестики нолики'

    page.window.height = 1000
    page.window.width = 1000
    
    def crest(e):
        
        if btn.on_click == crest:
            btn.icon_color = "#3700ff"
            btn.icon = ft.Icons.STOP
            btn.icon_size = 150
            hodi.value = f'Ходят: {hods1}'
            btn.disabled = True
            page.update

    btn = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn1 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn2 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn3 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn4 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn5 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn6 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn7 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
    btn8 = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN, width=150, height=150, icon_size=100, on_click=crest)
        
    hodi = ft.Text(value=f'Ходят: {hods}', size=100, height=200)

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

    column3 = ft.Row(
        controls=[
            btn6,
            btn7,
            btn8
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )   

    page.add(hodi, column1, column2, column3)
    

ft.run(main=main)