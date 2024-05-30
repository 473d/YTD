
import re
from pytube import YouTube
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown




from kivy.core.window import Window
Window.size = (500,600)

from functools import partial


class MyApp(MDApp):
    def GetLinkInfo(self, event, layout):
        self.link = self.linkinput.text

        self.checkLink =re.match("^https://www.youtube.com/.*",self.link)
        print(self.checkLink)

        if self.checkLink:

            self.errorLabel.text=""
            self.errorLabel.pos_hint={'center_x': 0.5, 'center_y': 20}

            try:

                self.yt = YouTube(self.link)

                self.title = str(self.yt.title)
                self.views = str(self.yt.views)
                self.length = str(self.yt.length)
    # ...........................................................................................................
                self.titlelabel.text= "TITLE : "+self.title
                self.titlelabel.pos_hint={'center_x': 0.5, 'center_y': 0.4}

                self.viewslabel.text = "VIEWS : "+self.views
                self.viewslabel.pos_hint = {'center_x': 0.5, 'center_y': 0.35}

                self.lengthlabel.text = "LENGTH : "+self.length
                self.lengthlabel.pos_hint = {'center_x': 0.5, 'center_y': 0.30}

    # ...........................................................................................................
                self.downloadbutton.text = "DOWNLOAD"
                self.downloadbutton.pos_hint = {'center_x': 0.5, 'center_y': 0.15}
                self.downloadbutton.size_hint = (0.3,0.1)
    #...........................................................................................................
                self.video = self.yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
                print(self.video)

                self.dropDown = DropDown()

                for video in self.video:
                    btton=Button(text=video.resolution, size_hint_y=None, height= 30)

                    btton.bind(on_release=lambda btton:self.dropDown.select(btton.text))

                    self.dropDown.add_widget(btton)

                self.main_button =Button(text='144p',size_hint=(None,None),pos=(420,75),height=50)

                self.main_button.bind(on_release=self.dropDown.open)

                self.dropDown.bind(on_select=lambda instance, x:setattr(self.main_button,'text',x))

                layout.add_widget(self.main_button)

    #.................................................................................................................

                print("TITLE : "+self.title)
                print("VIEWS : "+self.views)
                print("LENGTH : "+self.length)
            except:
                self.errorLabel.text = "NETWORK OR UNKNOWN ISSUE.. PLZ CHECK UR INTERNET CONNECTION "
                self.errorLabel.pos_hint = {'center_x': 0.5, 'center_y': 0.40}

        else:
            print("Invalid Link . plz put here the right link for Youtube ONLY. ")
            self.errorLabel.text = "Invalid Link . plz put here the right link for Youtube ONLY. "
            self.errorLabel.pos_hint ={'center_x': 0.5, 'center_y': 0.40}
# ..............................................................................................................

    def download(self, event, window):
        self.ys = self.yt.streams.filter(file_extension='mp4').filter(res=self.main_button.text).first()
        print("Downloding")
        self.ys.download("D:\cdLcd")
        print("Downlod Complete")
# ..............................................................................................................
    def build(self):

        layout = MDRelativeLayout(md_bg_color= [248/255,200/255,220/255])
# ..............................................................................................................
        self.img = Image(source='ytlogo.JPG',size_hint = (0.5,0.5),
                                             pos_hint = {'center_x':0.5 ,'center_y':0.90})
        layout.add_widget(self.img)
#..............................................................................................................
        self.youtubelink = Label(text="Please enter youtube link to download it ",
                                 size_hint=(1,1),
                                 font_size=20,
                                 color=(1,0,0),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.75})
        layout.add_widget(self.youtubelink)
# ..............................................................................................................
        self.linkinput = TextInput(text="",
                                 size_hint=(1, None),
                                 height=48,
                                 font_size=29,
                                 foreground_color=(0, 0.5, 0),
                                 font_name="comic",
                                 pos_hint={'center_x': 0.5, 'center_y': 0.65})

        layout.add_widget(self.linkinput)
# ..............................................................................................................
        self.linkbutton = Button(text="GetLink",
                                   size_hint=(0.2, 0.1),
                                   height=48,
                                   font_size=24,
                                   background_color=[0, 1, 0],
                                   font_name="comic",
                                   pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.linkbutton.bind(on_press= partial(self.GetLinkInfo,layout))
        layout.add_widget(self.linkbutton)
# ..............................................................................................................
        self.titlelabel = Label(text="",
                                 size_hint=(1, 1),
                                 font_size=20,
                                 pos_hint={'center_x': 0.5, 'center_y': 20})
        self.viewslabel = Label(text="",
                                size_hint=(1, 1),
                                font_size=20,
                                pos_hint={'center_x': 0.5, 'center_y': 20})
        self.lengthlabel = Label(text="",
                                size_hint=(1, 1),
                                font_size=20,
                                pos_hint={'center_x': 0.5, 'center_y': 20})

        layout.add_widget(self.titlelabel)
        layout.add_widget(self.viewslabel)
        layout.add_widget(self.lengthlabel)
# ..............................................................................................................
        self.downloadbutton = Button(text="GetLink",
                                 size_hint=(0.2, 0.1),
                                 height=48,
                                 font_size=24,
                                 size= (75,75),
                                 bold=(True),
                                 background_color=[0, 1, 0],
                                 font_name="comic",
                                 pos_hint={'center_x': 0.5, 'center_y': 20})
        self.downloadbutton.bind(on_press=partial(self.download , layout))
        layout.add_widget(self.downloadbutton)
# ..............................................................................................................
# ..............................................................................................................
        self.errorLabel=Label(text="",
                                 size_hint=(1, 1),
                                 color=(1,0,0),
                                 font_size=20,
                                 bold=(True),
                                 pos_hint={'center_x': 0.5, 'center_y': 20})
        layout.add_widget(self.errorLabel)
# ..............................................................................................................

# ..............................................................................................................

        return layout

if __name__ == "__main__":
    MyApp().run()
