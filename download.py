import flet as ft
#import lyricsgenius

def Dopage(page:ft.page):
    #genius=lyricsgenius.Genius("gdkvfYLGtBo4du6dhJu464WVJAncrfyZeEUmr1fBHGiKu6QGbnYCX1AiJyeY3wLb")     
    def Che (e):
        t=artiste.value
        S=title.value
      #  try:
        #    t=""
           # if t:
              #  lyrics=genius.search_song(S,t)
               # Titre.value=lyrics.title
               # Paroles.value=lyrics.lyrics
          # else:
             #  lyrics=genius.search_song(S)
             #  Titre.value=lyrics.title
              # Paroles.value=lyrics.lyrics
      #  else:
          #   Paroles.value="Veuillez verifier le titre ou le nom de l'artiste."
        page.update()


    def clean(e):
        title.value=""
        page.update()
    
    def clean1(e):
        artiste.value=""
        page.update()
        
  
    

    artiste=ft.CupertinoTextField(placeholder_text="Artiste…",width=400,height=40,border_radius=8,suffix=ft.IconButton(icon=ft.icons.CLEAR,on_click=clean1),suffix_visibility_mode=ft.VisibilityMode.EDITING)

    title=ft.CupertinoTextField(placeholder_text="Titre...",width=400,height=40,border_radius=8,suffix=ft.IconButton(icon=ft.icons.CLEAR,on_click=clean),suffix_visibility_mode=ft.VisibilityMode.EDITING)

    ap=ft.AppBar(adaptive=True,bgcolor="indigo",title=ft.Text("~ALFA",italic=True,color=ft.colors.BLUE,size=20)


    B=ft.ElevatedButton("Chercher",on_click=Che,adaptive=True)
    
    Titre=ft.Text(value="",font_family="Arial", size=22,selectable=True)
  
    Paroles=ft.Text(font_family="Arial",size=20,selectable=True)

    c=ft.Column(scroll="always",controls=[ft.Container(height=5),title,artiste,B,ft.Container(height=100),Titre,ft.Text(),Paroles],horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    page.add(ap,c)
    page.update()

