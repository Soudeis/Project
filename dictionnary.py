import flet as ft
#from larousse-api import larousse

def Dpage(page:ft.page):
    page.margin=0
    page.padding=0
    

    def clean(e):
        searchbar.value=""
        page.update()





    def search(e):
        definition=larousse.get_definition(searchbar.value)
        li=[]
        for i in definition:
            meaning="".join(i.strip())
            li.append(meaning)

            for k in li:
                t=ft.Text(k,font_family="Robot",size=14)
                s=ft.VerticalDivider()
                co.controls.append(t)
                co.controls.append(s)
        page.update()
    
    
    searchbar=ft.CupertinoTextField(placeholder_text="  Recherche...",on_submit=search,border_radius=8,width=400,height=40,prefix=ft.Icon(ft.icons.SEARCH),suffix=ft.IconButton(icon=ft.icons.CLEAR,on_click=clean),suffix_visibility_mode=ft.VisibilityMode.EDITING)
    S_=ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[searchbar])
    ap=ft.AppBar(adaptive=True,bgcolor=ft.colors.TRANSPARENT)
    #col=ft.Container(width=1000,height=100,border_radius=ft.border_radius.only(0,0,20,20),blur=ft.Blur(10,0.1,ft.BlurTileMode.REPEATED),padding=0)
    x=ft.Text("  DICTIONAIRE",italic=True,size=26,font_family="Arial",weight=ft.FontWeight.BOLD,color=ft.colors.BLUE)
    co=ft.Column(scroll="always",controls=[x,S_],alignment=ft.MainAxisAlignment.START)
    page.add(ap,co)
    page.update()

