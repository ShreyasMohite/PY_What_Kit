from tkinter import *
from tkinter.ttk import Notebook,Progressbar,Combobox
import pywhatkit as kit
import tkinter.messagebox
import threading



class Allpywhatkit:
    def __init__(self,root):
        self.root=root
        self.root.title("PY WTF ")
        self.root.geometry("500x510")
        self.root.iconbitmap("logo188.ico")
        self.root.resizable(0,0)

        youtube=StringVar()
        google=StringVar()
        wikipedia=StringVar()
        lines=StringVar()


        def on_enter1(e):
            but_youtube_search['background']="black"
            but_youtube_search['foreground']="cyan"  
        def on_leave1(e):
            but_youtube_search['background']="SystemButtonFace"
            but_youtube_search['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_google_search['background']="black"
            but_google_search['foreground']="cyan"  
        def on_leave2(e):
            but_google_search['background']="SystemButtonFace"
            but_google_search['foreground']="SystemButtonText"
            


        def on_enter3(e):
            but_wikiinfo_search['background']="black"
            but_wikiinfo_search['foreground']="cyan"  
        def on_leave3(e):
            but_wikiinfo_search['background']="SystemButtonFace"
            but_wikiinfo_search['foreground']="SystemButtonText"

        def on_enter4(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave4(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def clear():
            youtube.set("")
            google.set("")
            wikipedia.set("")
            lines.set("Select lines")
            text.delete("1.0","end")

        def search_youtube():
            try:
                if youtube.get()!="":
                    kit.playonyt(youtube.get())
                else:
                    tkinter.messagebox.showerror("ERROR","Please youtube Name")
            except:
                tkinter.messagebox.showerror("ERROR","Network Error")

        def thread_sy():
            t1=threading.Thread(target=search_youtube)
            t1.start()

        def search_google():
            try:
                if google.get()!="":
                    kit.search(google.get())
                else:
                    tkinter.messagebox.showerror("Eroor","Please Enter Search Name")
            except:
                tkinter.messagebox.showerror("Error","Network Error")

        def thread_sg():
            t1=threading.Thread(target=search_google)
            t1.start()


        def search_wikipedia():
            try:
                if wikipedia.get()!="":
                    if lines.get()!="Select lines":
                        with open("C:/TEMP/wiks.txt","w") as f:
                            x=kit.info(wikipedia.get(),lines.get())
                            f.write(x)
                        with open("C:/TEMP/wiks.txt","r") as f:
                            text.insert("end",f.read())

                    else:
                        tkinter.messagebox.showerror("Error","Please Select Lines")
                else:
                    tkinter.messagebox.showerror("Error","Please Enter Wikipedia Search Name")
            except:
                tkinter.messagebox.showerror("Error","Please Enter wikipedia search name")

       
        
        def thread_sw():
            t1=threading.Thread(target=search_wikipedia)
            t1.start()



#-----------------------------------------------------------------#
        mainframe=Frame(self.root,width=500,height=510,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)


        firstframe=Frame(mainframe,width=494,height=320,relief="ridge",bd=3,bg="#b53512")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=184,relief="ridge",bd=3)
        secondframe.place(x=0,y=320)

#==================================================================#
        lab_youtube_search=Label(firstframe,text="Youtube Search",font=('times new roman',13),bg="#b53512",fg="white")
        lab_youtube_search.place(x=10,y=3)

        ent_youtube_search=Entry(firstframe,width=37,font=('times new roman',13),relief="ridge",bd=3,textvariable=youtube)
        ent_youtube_search.place(x=125,y=3)

        but_youtube_search=Button(firstframe,width=17,text="Search",font=('times new roman',12),cursor="hand2",command=thread_sy)
        but_youtube_search.place(x=180,y=50)
        but_youtube_search.bind("<Enter>",on_enter1)
        but_youtube_search.bind("<Leave>",on_leave1)


        lab_google_search=Label(firstframe,text="Google Search",font=('times new roman',13),bg="#b53512",fg="white")
        lab_google_search.place(x=10,y=113)

        ent_google_search=Entry(firstframe,width=37,font=('times new roman',13),relief="ridge",bd=3,textvariable=google)
        ent_google_search.place(x=125,y=113)

        but_google_search=Button(firstframe,width=17,text="Search",font=('times new roman',12),cursor="hand2",command=thread_sg)
        but_google_search.place(x=180,y=160)
        but_google_search.bind("<Enter>",on_enter2)
        but_google_search.bind("<Leave>",on_leave2)



        lab_wikiinfo_search=Label(firstframe,text="Wiki Search",font=('times new roman',13),bg="#b53512",fg="white")
        lab_wikiinfo_search.place(x=10,y=213)

        ent_wikiinfo_search=Entry(firstframe,width=20,font=('times new roman',13),relief="ridge",bd=3,textvariable=wikipedia)
        ent_wikiinfo_search.place(x=125,y=213)


        list_health=list(range(1,51))
        list_health_combo=Combobox(firstframe,values=list_health,font=('arial',12),width=10,state="readonly",textvariable=lines)
        list_health_combo.set("Select lines")
        list_health_combo.place(x=340,y=213)

        but_wikiinfo_search=Button(firstframe,width=17,text="Search",font=('times new roman',12),cursor="hand2",command=thread_sw)
        but_wikiinfo_search.place(x=60,y=260)
        but_wikiinfo_search.bind("<Enter>",on_enter3)
        but_wikiinfo_search.bind("<Leave>",on_leave3)

        but_clear=Button(firstframe,width=17,text="Clear All",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=270,y=260)
        but_clear.bind("<Enter>",on_enter4)
        but_clear.bind("<Leave>",on_leave4)




#-============================================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=10,width=66,font=('times new roman',11),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
        


if __name__ == "__main__":
    root=Tk()
    app=Allpywhatkit(root)
    root.mainloop()