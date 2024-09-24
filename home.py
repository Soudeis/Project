import flet as ft 
import culture

def Hpage(page):
    page.padding=0
    page.scroll=ft.ScrollMode.HIDDEN
    
    def f1(e):
        global cc
        text=""
        page.go('/Cul')
        cc.content=ft.Text(text)
        page.update()

    def f2(e):
        global cc
        text=""
        page.go('/Cul')
        cc.content=ft.Text(text)
        page.update()
        

    def f3(e):
        global cc
        text=""
        page.go('/Cul')
        cc.content=ft.Text(text)
        page.update()

    def f4(e):
        global cc
        text=""
        page.go('/Cul')
        cc.content=ft.Text(text)
        page.update()

    def f5(e):
        global cc
        text=""
        page.go('/Cul')
        cc.content=ft.Text(text)
        page.update()

    def f6(e):
        global cc
        text=""
        page.go('/Cul')
        cc.content=ft.Text(text)
        page.update()

    def f7(e):
        global cc
        text=""
        page.go('/Cul')
        cc.content=ft.Text(text)
        page.update()





    
    R1=ft.Row(scroll=ft.ScrollMode.HIDDEN,alignment=ft.MainAxisAlignment.START)
    Cquote=ft.Container(margin=5,alignment=ft.alignment.center,ink=True,content=ft.Text("Quote",size=25,italic=True),width=180,height=180,
    border_radius=20,on_click=lambda _:page.go('/Quote'),bgcolor=ft.colors.INDIGO_200)
    Cwomen=ft.Container(margin=5,alignment=ft.alignment.center,ink=True,content=ft.Text("Shorten",size=25,italic=True),width=180,height=180,
    border_radius=20,on_click=lambda _:page.go('/Short'),bgcolor=ft.colors.INDIGO_200)
    C=ft.Container(margin=5,alignment=ft.alignment.center,content=ft.Text("Third container",size=25,italic=True),width=180,height=180,bgcolor=ft.colors.INDIGO_200,
    border_radius=20,on_click=lambda _:page.go())
    
    R1.controls.append(Cquote)
    R1.controls.append(Cwomen)
    R1.controls.append(C)

    

    B1=ft.TextButton(style=ft.ButtonStyle(alignment=ft.Alignment(-1.0,0.0),bgcolor=ft.colors.BLUE_300,shape=ft.RoundedRectangleBorder(radius=10)),content=ft.Text("Premiere histoire",size=20),on_click=f1,height=50)
    B2=ft.TextButton(style=ft.ButtonStyle(alignment=ft.Alignment(-1.0,0.0),bgcolor=ft.colors.BLUE_300,shape=ft.RoundedRectangleBorder(radius=10)),content=ft.Text(""),on_click=f2,height=50)
    B3=ft.TextButton(style=ft.ButtonStyle(alignment=ft.Alignment(-1.0,0.0),bgcolor=ft.colors.BLUE_300,shape=ft.RoundedRectangleBorder(radius=10)),content=ft.Text(""),on_click=f3,height=50)
    B4=ft.TextButton(style=ft.ButtonStyle(alignment=ft.Alignment(-1.0,0.0),bgcolor=ft.colors.BLUE_300,shape=ft.RoundedRectangleBorder(radius=10)),content=ft.Text(""),on_click=f4,height=50)
    B5=ft.TextButton(style=ft.ButtonStyle(alignment=ft.Alignment(-1.0,0.0),bgcolor=ft.colors.BLUE_400,shape=ft.RoundedRectangleBorder(radius=10)),content=ft.Text(""),on_click=f5,height=50)
    B6=ft.TextButton(style=ft.ButtonStyle(alignment=ft.Alignment(-1.0,0.0),bgcolor=ft.colors.BLUE_400,shape=ft.RoundedRectangleBorder(radius=10)),content=ft.Text(""),on_click=f6,height=50)
    B7=ft.TextButton(style=ft.ButtonStyle(alignment=ft.Alignment(-1.0,0.0),bgcolor=ft.colors.BLUE_400,shape=ft.RoundedRectangleBorder(radius=10)),content=ft.Text(""),on_click=f7,height=50)

    LS=ft.ListView(spacing=10,padding=5,auto_scroll=True,controls=[B1,B2,B3,B4,B5,B6,B7])
    

    
    appbar=ft.AppBar(center_title=True,
    leading=ft.IconButton(style=ft.ButtonStyle(padding=5),icon_size=25,icon_color=ft.colors.BLUE,
    icon=ft.icons.MENU,
    on_click=lambda _:page.open(drawer)),
    adaptive=True,
    bgcolor=ft.colors.TRANSPARENT,
    title=ft.Text("~Alfa",font_family='Roboto', size=20,color=ft.colors.BLUE,italic=True
    ))

    drawer=ft.NavigationDrawer(controls=[])
    page.drawer=drawer

    

    C=ft.Column(controls=[ft.Container(height=20),R1,LS])

    page.add(C,appbar)
    page.update()
