from pypresence import Presence # Python wrapper for discord rich presence
from ast import literal_eval # Allows to turn strings into lists
from pprint import pprint # Basic Debugging
import tkinter as tk # GUI Package
import configparser # Reading config
import datetime # Time
import time # Time
import os




parser = configparser.SafeConfigParser()
config = configparser.ConfigParser()


parser.read("data.ini")
config.read("data.ini")




class interface(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.client_id = tk.StringVar()

        if int(config.get('client', 'firstStartUp')):
            self.client_id.set(config.get('client', 'id'))
            self.init_window()
        else:
            self.firstWindow()
    
    def firstWindow(self):
        
        root.title("Start Up" +  " - Beautiful Rich Presence")

        self.firstFrame = tk.Frame(self.master, background="#525760", relief='raised')

        firstLabel = tk.Label(self.firstFrame, text='Insert your client ID here:', font=("Helvetica", 13), justify=tk.CENTER, anchor=tk.N, background='#525760', foreground='#ededed', highlightbackground='#525760', borderwidth=0)
        firstEntry = tk.Entry(self.firstFrame, text='clientid', borderwidth=0.8, width=35, font=("Helvetica", 9), justify=tk.CENTER, textvariable=self.client_id, background='#484B51', foreground='#ffffff', insertbackground='#ffffff')

        firstButton = tk.Button(self.firstFrame, text="SAVE & EXUCUTE", font=("Helvetica", 11, "bold"),  state=tk.ACTIVE, bd=0, background="#7289da", activebackground="#7289da", foreground="#ededed", activeforeground="#ededed", command=self.firstExucute)

        self.firstErrorLabel = tk.Label(self.firstFrame, text='', font=("Helvetica", 8), justify=tk.CENTER, anchor=tk.N, background='#525760', foreground='#ededed', highlightbackground='#525760', borderwidth=0)

        self.firstFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

        firstLabel.pack(side=tk.TOP, pady=15, fill=tk.X)
        firstEntry.pack(side=tk.TOP, ipady=3)
        firstButton.pack(side=tk.TOP, pady=10)
        self.firstErrorLabel.pack(side=tk.TOP, pady=5)

        

    
    def firstExucute(self):
        
        try:
            int(self.client_id.get())
            if self.client_id.get() != "" and not self.client_id.get().isspace():
                self.client_id.set("".join(self.client_id.get().split()))
                parser.set('client', 'id', str(self.client_id.get()))
                parser.set('client', 'firststartup', str(1))
                with open('data.ini', 'w') as configfile:
                    parser.write(configfile) 
                self.firstFrame.pack_forget()
                self.init_window() 
            else:
                self.firstErrorLabel.config(text='ERROR: Client ID is not valid \n Entry is blank')
        except:
            self.firstErrorLabel.config(text='ERROR: Client ID is not valid \n Entry is not a number')

    
    def init_window(self):
        

        topframe = tk.Frame(self.master, background="#525760", relief='raised') # Full Window Frame
        statusframe = tk.Frame(self.master, background="#525760", borderwidth=1, relief="sunken") # Frame of status bar
        self.widgetframe = tk.Frame(self.master, background="#36393F", relief='flat') # Frame for all widgets
        
        self.tab_Topframe= tk.Frame(topframe, background="#525760", relief='raised') # Frame for all of the Tabs
        
        # Tab Buttons
        self.main_Tab = tk.Button(self.tab_Topframe, text="Main",  state=tk.DISABLED, bd=0, background="#36393F", activebackground="#36393F", foreground="#ededed", activeforeground="#ededed", command=self.mainTab)
        self.asset_Tab = tk.Button(self.tab_Topframe, text="Assets",  state=tk.ACTIVE, bd=0, background="#4a4d54", activebackground="#4a4d54", foreground="#ededed", activeforeground="#ededed", command=self.assetsTab)
        self.config_Tab = tk.Button(self.tab_Topframe, text="Config",  state=tk.ACTIVE, bd=0, background="#4a4d54", activebackground="#4a4d54", foreground="#ededed", activeforeground="#ededed", command=self.configTab)
        self.refresh_Button = tk.Button(self.tab_Topframe, text="Refresh", font=("Helvetica", 9, "bold"),  state=tk.ACTIVE, bd=0, background="#4a4d54", activebackground="#4a4d54", foreground="#ededed", activeforeground="#ededed", command=self.refresh)
       
        self.status_Status = tk.Label(statusframe, text="", font=("Helvetica", 8), anchor=tk.W, background='#525760', foreground='#ededed', highlightbackground='#525760', borderwidth=0)
        
        # NEVER UNPACKS #
        topframe.pack(fill=tk.X, side=tk.TOP, expand=False)
        statusframe.pack(fill=tk.X, side=tk.BOTTOM, expand=False)
        self.widgetframe.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        

        self.tab_Topframe.pack(fill=tk.X, side=tk.TOP, anchor=tk.N)

        self.status_Status.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        


        self.main_Tab.pack(side=tk.LEFT, ipadx=6)
        self.asset_Tab.pack(side=tk.LEFT, ipadx=6)
        self.config_Tab.pack(side=tk.LEFT, ipadx=6)
        self.refresh_Button.pack(side=tk.RIGHT, ipadx=6)
        

        
        #################

        # MAIN TAB #
        
        # Variables

        self.assetList = literal_eval(config.get('config', 'assets'))
        xassetList = ['None', ] + self.assetList

        self.topVar = tk.StringVar()
        self.bottomVar = tk.StringVar()
        self.largeVar = tk.StringVar()
        self.largeVar.set(xassetList[0])
        self.largehoverVar = tk.StringVar()
        self.smallVar = tk.StringVar()
        self.smallVar.set(xassetList[0])
        self.smallhoverVar = tk.StringVar()
        self.timerVar = tk.IntVar()
        self.timerEntryVar = tk.StringVar()
        self.timerEntryVar.set('0')
        self.rememberVar = tk.IntVar()

        self.topVar.set(config.get('lastpresence', 'top'))
        self.bottomVar.set(config.get('lastpresence', 'bottom'))
        self.largeVar.set(config.get('lastpresence', 'largeasset'))
        self.largehoverVar.set(config.get('lastpresence', 'largeassethovertext'))
        self.smallVar.set(config.get('lastpresence', 'smallasset'))
        self.smallhoverVar.set(config.get('lastpresence', 'smallassethovertext'))
        self.timerVar.set(config.get('lastpresence', 'time'))
        self.timerEntryVar.set(config.get('lastpresence', 'timevalue'))
        self.rememberVar.set(config.get('lastpresence', 'remember'))

        if self.largeVar.get() not in self.assetList:
            self.largeVar.set(xassetList[0])
        if self.smallVar.get() not in self.assetList:
            self.smallVar.set(xassetList[0])

                
        ##########

        self.topLabel = tk.Label(self.widgetframe, text='Top:', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.topEntry = tk.Entry(self.widgetframe, text='top', borderwidth=0.8, width=22, textvariable=self.topVar, background='#484B51', foreground='#ffffff', insertbackground='#ffffff')

        self.bottomLabel = tk.Label(self.widgetframe, text='Bottom:', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.bottomEntry = tk.Entry(self.widgetframe, text='bottom', borderwidth=0.8, width=22, textvariable=self.bottomVar, background='#484B51', foreground='#ffffff', insertbackground='#ffffff')

        self.largeLabel = tk.Label(self.widgetframe, text='Large Image:', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.largeOptMenu = tk.OptionMenu(self.widgetframe, self.largeVar, *xassetList)
        self.largeOptMenu.config(background="#2F3136", foreground='#ffffff', activebackground="#7289da", activeforeground="#ffffff", font=("Helvetica", 9), borderwidth=0, highlightthickness=0)
        self.largeOptMenu["menu"].config(background="#2F3136", foreground='#ffffff', activebackground="#7289da", font=("Helvetica", 9), borderwidth=0)
        self.largehoverLabel = tk.Label(self.widgetframe, text='Large Image Hover:', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.largehoverEntry = tk.Entry(self.widgetframe, text='large image hover', borderwidth=0.8, width=22, textvariable=self.largehoverVar, background='#484B51', foreground='#ffffff', insertbackground='#ffffff')

        self.smallLabel = tk.Label(self.widgetframe, text='Small Image:', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.smallOptMenu = tk.OptionMenu(self.widgetframe, self.smallVar, *xassetList)
        self.smallOptMenu.config(background="#2F3136", foreground='#ffffff', activebackground="#7289da", activeforeground="#ffffff", font=("Helvetica", 9), borderwidth=0, highlightthickness=0)
        self.smallOptMenu["menu"].config(background="#2F3136", foreground='#ffffff', activebackground="#7289da", font=("Helvetica", 9), borderwidth=0)
        self.smallhoverLabel = tk.Label(self.widgetframe, text='Small Image Hover:', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.smallhoverEntry = tk.Entry(self.widgetframe, text='small image hover', borderwidth=0.8, width=22, textvariable=self.smallhoverVar, background='#484B51', foreground='#ffffff', insertbackground='#ffffff')

        self.timerBox = tk.Checkbutton(self.widgetframe, text="time", variable=self.timerVar, fg='#AEB7C1', bg='#36393F', activebackground="#7289da", activeforeground="#ffffff")
        self.timerEntry = tk.Entry(self.widgetframe, text='timeset', borderwidth=0.8, width=10, textvariable=self.timerEntryVar, font=("Helvetica", 10), background='#484B51', foreground='#ffffff', insertbackground='#ffffff' )
        self.timerLabel = tk.Label(self.widgetframe, text='*Set to 0 to use elapse time \n **Time goes in seconds', font=("Helvetica", 7), background='#36393F', foreground='#AEB7C1')

        self.rememberBox = tk.Checkbutton(self.widgetframe, text="remember", variable=self.rememberVar, fg='#AEB7C1', bg='#36393F', activebackground="#7289da", activeforeground="#ffffff")

        self.buttonRP = tk.Button(self.widgetframe, text='SET', font=("Helvetica", 10), width=20, command=self.setRP, background="#7289da", foreground='#ffffff', activebackground="#7289da", activeforeground="#ffffff", highlightbackground="#7289da")
        
        #################

        # ASSETS TAB #
        
        

        # Variables


        self.assetVar = tk.StringVar()

        ##########

        self.assetLabel = tk.Label(self.widgetframe, text='Asset Name: ', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.assetEntry = tk.Entry(self.widgetframe, text='assetentry', state=tk.DISABLED, borderwidth=0.8, width=21, textvariable=self.assetVar, font=("Helvetica", 10), background='#484B51', foreground='#ffffff', insertbackground='#ffffff', disabledbackground='#34363a', disabledforeground='#b7b3b3')

        self.assetScrollbar = tk.Scrollbar(self.widgetframe, orient=tk.VERTICAL, width=3, relief=tk.FLAT, activerelief=tk.FLAT, troughcolor='#7289da', highlightbackground='#7289da')
        self.assetListbox = tk.Listbox(self.widgetframe, height=10, yscrollcommand=self.assetScrollbar.set, bd=0, background="#282a2d", highlightbackground="#282a2d", highlightcolor='#282a2d', selectbackground='#7289da', foreground='#ededed')
        self.assetScrollbar.config(command=self.assetListbox.yview)

        self.assetSelectButton = tk.Button(self.widgetframe, text='SELECT', font=("Helvetica", 10),  width=14, command=self.assetSelect)
        self.assetFinishedButton = tk.Button(self.widgetframe, text='', font=("Helvetica", 10), width=14)

        #################

        # CONFIG TAB #

        # Variables

        # ALREADY DEFINED self.client_id

        ##########

        self.configClientIDLabel = tk.Label(self.widgetframe, text='Client ID: ', font=("Helvetica", 9), background='#36393F', foreground='#ededed')
        self.configClientIDEntry = tk.Entry(self.widgetframe, text='clientid', state=tk.NORMAL, borderwidth=0.8, width=21, textvariable=self.client_id, font=("Helvetica", 10), background='#484B51', foreground='#ffffff', insertbackground='#ffffff', disabledbackground='#34363a', disabledforeground='#b7b3b3')

        self.configSaveButton = tk.Button(self.widgetframe, text='SAVE & REFRESH', font=("Helvetica", 10), width=20, command=self.configSave, background="#4d915b", foreground='#ffffff', activebackground="#4d915b", activeforeground="#ffffff", highlightbackground="#4d915b")

        #################

        root.protocol('WM_DELETE_WINDOW', self.endprogram)



        self.tabName = "startup"
        self.initializepresence()
        self.updatestatus()
        self.mainTab()

    def endprogram(self):
        try:
            self.rp.clear()
            self.rp.close()
        except:
            pass
        root.destroy()
        exit("Program closed by user")

    def update_option_menu(self, optionMenu, var):
        menu = optionMenu["menu"]
        menu.delete(0, "end")
        xassetList = ['None',] + self.assetList
        for string in xassetList:
            menu.add_command(label=string, 
                             command=lambda value=string: var.set(value))
        
        if self.largeVar.get() not in self.assetList:
            self.largeVar.set(xassetList[0])
        if self.smallVar.get() not in self.assetList:
            self.smallVar.set(xassetList[0])

    def refresh(self):
        if self.isconnected:
            if self.opened:
                self.rp.clear()
            self.rp.close()
        self.rp = None
        config.read('data.ini')
        self.client_id.set(config.get('client', 'id'))
        self.initializepresence()
        if self.isconnected:
            parser.read("data.ini")
            config.read("data.ini")
            self.assetList = literal_eval(config.get('config', 'assets'))
            self.update_option_menu(self.smallOptMenu, self.smallVar)
            self.update_option_menu(self.largeOptMenu, self.largeVar)
            self.buttonRP.configure( text='ON COOLDOWN', state=tk.DISABLED, background='#3B3E44', foreground='#ffffff' )
            self.refresh_Button.configure( state=tk.DISABLED, background='#3B3E44', foreground='#b7b7b7' )
            self.configClientIDEntry.configure(state=tk.DISABLED)
            self.configSaveButton.configure(state=tk.DISABLED, background='#3B3E44', foreground='#b7b7b7')
            self.updatestatus(text="| Refreshed config  | COOLDOWN (10)", color="#202225")
            self.status_Status.after(1000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (9)", color="#202225"))
            self.status_Status.after(2000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (8)", color="#202225"))
            self.status_Status.after(3000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (7)", color="#202225"))
            self.status_Status.after(4000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (6)", color="#202225"))
            self.status_Status.after(5000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (5)", color="#202225"))
            self.status_Status.after(6000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (4)", color="#202225"))
            self.status_Status.after(7000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (3)", color="#202225"))
            self.status_Status.after(8000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (2)", color="#202225"))
            self.status_Status.after(9000, lambda: self.updatestatus(text="| Refreshed config  | COOLDOWN (1)", color="#202225"))
            self.status_Status.after(10000, lambda: self.updatestatus(text="| Refreshed config | COOLDOWN (DONE)", color="#202225"))
            self.buttonRP.after(10000, lambda: self.buttonRP.config(text='SET', state=tk.ACTIVE, background='#7289da', foreground='#ffffff', activebackground="#7289da", activeforeground="#ffffff", highlightbackground="#7289da"))
            self.refresh_Button.after(10000, lambda: self.refresh_Button.configure(state=tk.ACTIVE, background="#4a4d54", activebackground="#4a4d54", foreground="#ededed", activeforeground="#ededed"))        
            self.refresh_Button.after(10000, lambda: self.configClientIDEntry.configure(state=tk.NORMAL))
            self.refresh_Button.after(10000, lambda: self.configSaveButton.configure(state=tk.ACTIVE, background='#4d915b', foreground='#ffffff', activebackground="#4d915b"))
            self.status_Status.after(14000, lambda: self.updatestatus())
        else:
            self.updatestatus()

    def initializepresence(self):
        try:
            if self.client_id.get() != "":
                self.rp = Presence(self.client_id.get(), pipe=0)
                self.rp.connect()
                print("Connected to DiscordApp")
                self.isconnected = True
                self.opened = False
            else:
                self.isconnected = False
                self.opened = False
                self.startuperror = "| Client ID is empty! |"
        except:
            print("Error while connecting to DiscordApp")
            self.isconnected = False
            self.opened = False
            self.startuperror = "| Client ID is empty! |"
        

    def updatestatus(self, text:str=None, color:str="#525760"):
        if self.isconnected == True and text == None:
            self.status_Status.configure(text='| Connected to DiscordApp! |', background='#525760', highlightbackground='#525760')
        elif self.isconnected == False and self.startuperror == "Client ID is empty!":
             self.status_Status.configure(text=self.startuperror, background='#da7272', highlightbackground='#da7272')
        elif self.isconnected == False and text == None:
            self.status_Status.configure(text='| Not connected DiscordApp |', background='#da7272', highlightbackground='#da7272')
        else:
            self.status_Status.configure(text=text, background=color, highlightbackground=color)

    def unpack(self):
        self.configAll()
        if self.tabName == 'main':
            
            self.topLabel.place_forget()
            self.topEntry.place_forget()
            self.bottomLabel.place_forget()
            self.bottomEntry.place_forget()
            self.largeLabel.place_forget()
            self.largeOptMenu.place_forget()
            self.largehoverLabel.place_forget()
            self.largehoverEntry.place_forget()
            self.smallLabel.place_forget()
            self.smallOptMenu.place_forget()
            self.smallhoverLabel.place_forget()
            self.smallhoverEntry.place_forget()
            self.timerBox.place_forget()
            self.timerEntry.place_forget()
            self.timerLabel.place_forget()

            self.rememberBox.place_forget()

            self.buttonRP.pack_forget()
        elif self.tabName == 'assets':
            
            self.assetLabel.place_forget()
            self.assetEntry.place_forget()

            self.assetListbox.pack_forget()
            self.assetScrollbar.place_forget()
            self.assetSelectButton.pack_forget()

            self.assetFinishedButton.place_forget()

        elif self.tabName == 'config':
            
            self.configClientIDEntry.place_forget()
            self.configClientIDLabel.place_forget()

            self.configSaveButton.pack_forget()

        elif self.tabName == 'credits':
            pass
    
    def configAll(self):
        self.main_Tab.configure(activebackground="#4a4d54", background="#4a4d54", foreground="#ededed", state=tk.ACTIVE)
        self.asset_Tab.configure(activebackground="#4a4d54", background="#4a4d54", foreground="#ededed", state=tk.ACTIVE)
        self.config_Tab.configure(activebackground="#4a4d54", background="#4a4d54", foreground="#ededed", state=tk.ACTIVE)

    def mainTab(self):
        self.unpack()
        self.configAll()
        self.main_Tab.configure(activebackground="#36393F", background="#36393F",  foreground="#ededed", state=tk.DISABLED)
        self.tabName = str('main') # Tab name - All lowercase (Helps with minmization)
        root.title(self.tabName +  " - Beautiful Rich Presence")

        self.topLabel.place(y=23, x=25)
        self.topEntry.place(y=24.2, x=60)

        self.bottomLabel.place(y=53, x=13)
        self.bottomEntry.place(y=54.2, x=60)

        self.largeLabel.place(y=93, x=13)
        self.largeOptMenu.place(y=91.5, x=95)
        self.largehoverLabel.place(y=127, x=13)
        self.largehoverEntry.place(y=127, x=132)

        self.smallLabel.place(y=163, x=13)
        self.smallOptMenu.place(y=161.5, x=95)
        self.smallhoverLabel.place(y=197, x=13)
        self.smallhoverEntry.place(y=197, x=132)

        self.timerBox.place(y=23, x=250)
        self.timerEntry.place(y=50, x=239)
        self.timerLabel.place(y=35, x=331)

        self.rememberBox.place(y=170, x=425)

        self.buttonRP.pack(side=tk.BOTTOM, anchor=tk.E, padx=7, pady=7)

    def assetsTab(self):
        self.unpack()
        self.configAll()
        self.asset_Tab.configure(activebackground="#36393F", background="#36393F",  foreground="#ededed", state=tk.DISABLED)
        self.tabName = str('assets') # Tab name
        root.title(self.tabName +  " - Beautiful Rich Presence")

        self.assetVar.set('')

        self.assetEntry.config(font=("Helvetica", 10, "italic") ,state=tk.DISABLED)
        self.assetLabel.config(text='Asset Name:')
        self.assetSelectButton.config(background="#35363a", foreground='#ffffff', activebackground="#2c2d30", activeforeground="#ffffff", highlightbackground="#35363a")

        self.assetLabel.place(y=15, x=25)
        self.assetEntry.place(y=35, x=25)

        self.assetSelectButton.pack(side=tk.BOTTOM, anchor=tk.E, padx=7, pady=7)

        self.assetListbox.pack(side=tk.BOTTOM, anchor=tk.E, padx=7, pady=7)
        

        self.assetListbox.delete(0, tk.END)

        try:
            self.assetListbox.insert(tk.END, "ADD")
            for item in self.assetList:
                self.assetListbox.insert(tk.END, item)
        except: pass
    
    def assetSelect(self):

        self.assetSelectButton.config(background="#7289da", foreground='#ffffff', activebackground="#7289da", activeforeground="#ffffff", highlightbackground="#7289da")
        if self.assetListbox.get(tk.ACTIVE) == "ADD":
            self.assetVar.set('')
            self.assetLabel.config(text='New Asset Name:')
            self.assetEntry.config(font=("Helvetica", 10, "normal"), state=tk.NORMAL)
            self.assetFinishedButton.config(text='ADD', width=0, background="#5baf66", foreground='#ffffff', activebackground="#5baf66", activeforeground="#ffffff", highlightbackground="#5baf66", command=self.assetAdd)
        else:
            self.assetLabel.config(text='Asset Name:')
            self.assetEntry.config(font=("Helvetica", 10, "italic"), state=tk.DISABLED)
            self.assetVar.set(self.assetListbox.get(tk.ACTIVE))
            self.assetFinishedButton.config(text='DELETE', width=0, background="#e07676", foreground='#ffffff', activebackground="#e07676", activeforeground="#ffffff", highlightbackground="#e07676", command=self.assetDelete)
        self.assetFinishedButton.place(y=32, x=200)
     
    def assetAdd(self):
        
        if self.assetVar.get() != "" or not self.assetVar.get().isspace():
            self.assetList.append(self.assetVar.get())
            parser.set('config', 'assets', str(self.assetList))
            self.assetSelectButton.config(background="#35363a", foreground='#ffffff', activebackground="#2c2d30", activeforeground="#ffffff", highlightbackground="#35363a")
            with open('data.ini', 'w') as configfile:
                parser.write(configfile)
            self.assetListbox.insert(tk.END, self.assetVar.get())
            self.assetVar.set('')
            self.assetListbox.selection_clear(0)
            self.assetFinishedButton.place_forget()
            config.read("data.ini")
            self.assetList = literal_eval(config.get('config', 'assets'))
            self.update_option_menu(self.smallOptMenu, self.smallVar)
            self.update_option_menu(self.largeOptMenu, self.largeVar)
    
    def assetDelete(self):
        self.assetList.remove(self.assetVar.get())
        parser.set('config', 'assets', str(self.assetList))
        self.assetSelectButton.config(background="#35363a", foreground='#ffffff', activebackground="#2c2d30", activeforeground="#ffffff", highlightbackground="#35363a")
        self.assetFinishedButton.place_forget()
        with open('data.ini', 'w') as configfile:
            parser.write(configfile)
        self.assetListbox.delete(self.assetListbox.curselection())
        self.assetVar.set('')
        self.assetListbox.selection_clear(0)
        self.assetFinishedButton.place_forget()
        config.read("data.ini")
        self.assetList = literal_eval(config.get('config', 'assets'))
        self.update_option_menu(self.smallOptMenu, self.smallVar)
        self.update_option_menu(self.largeOptMenu, self.largeVar)

    def configTab(self):
        self.unpack()
        self.configAll()
        self.config_Tab.configure(activebackground="#36393F", background="#36393F",  foreground="#ededed", state=tk.DISABLED)
        self.tabName = str('config') # Tab name
        root.title(self.tabName +  " - Beautiful Rich Presence")

        self.configClientIDLabel.place(y=15, x=25)
        self.configClientIDEntry.place(y=35, x=25)
        
        self.configSaveButton.pack(side=tk.BOTTOM, anchor=tk.E, padx=7, pady=7)


    def configSave(self):
        try:
            int(self.client_id.get())
            if self.client_id.get() != "" and not self.client_id.get().isspace():
                self.client_id.set("".join(self.client_id.get().split()))
                parser.set('client', 'id', str(self.client_id.get()))
                parser.set('client', 'firststartup', str(1))
                with open('data.ini', 'w') as configfile:
                    parser.write(configfile)
                self.refresh()
        except:
            self.updatestatus(text="Client ID has to be numbers only", color="#da7272") 

    def creditsTab(self):
        self.unpack()
        self.tabName = str('credits') # Tab name
        root.title(self.tabName +  " - Beautiful Rich Presence")
    
    def setRP(self):
        # Variables
        # self.topVar = tk.StringVar()
        # self.bottomVar = tk.StringVar()
        # self.largeVar = tk.StringVar()
        # self.largeVar.set(largeList[0])
        # self.largehoverVar = tk.StringVar()
        # self.smallVar = tk.StringVar()
        # self.smallVar.set(smallList[0])
        # self.smallhoverVar = tk.StringVar()
        ##########
        self.updatestatus
        if self.topVar.get() != "" and not self.topVar.get().isspace():
            if self.bottomVar.get() != "" and not self.bottomVar.get().isspace():
                if self.timerEntryVar.get() != "" and not self.timerEntryVar.get().isspace():
                    details = self.topVar.get()
                    state = self.bottomVar.get()
                    large_image = self.largeVar.get()
                    large_text = self.largehoverVar.get()
                    small_image = self.smallVar.get()
                    small_text = self.smallhoverVar.get()
                    timeron = self.timerVar.get()
                    timer_seconds = int(self.timerEntryVar.get())
                    if large_image == 'None':
                        large_image = None
                        large_text = None
                    if small_image == 'None':
                        small_image = None
                        small_text = None
                    if large_text == '' and not large_text.isspace():
                        large_text = None
                    if small_text == '' and not small_text.isspace():
                        small_text = None
                    if timeron:
                            if timer_seconds > 0:
                                start = int(datetime.datetime.now().timestamp())
                                end = int((datetime.datetime.now() + datetime.timedelta(seconds=timer_seconds)).timestamp())
                            else:
                                start = int(time.time())
                                end = None
                    else:
                        start = None
                        end = None

                    try:
                        self.returnObject = self.rp.update(
                            state=state,
                            details=details,
                            large_image=large_image,
                            large_text=large_text,
                            small_image=small_image,
                            small_text=small_text,
                            end=end,
                            start=start
                        )
                        self.opened = True
                        self.buttonRP.configure( text='ON COOLDOWN', state=tk.DISABLED, background='#3B3E44', foreground='#ffffff' )
                        self.refresh_Button.configure( state=tk.DISABLED, background='#3B3E44', foreground='#b7b7b7' )
                        self.configClientIDEntry.configure(state=tk.DISABLED)
                        self.configSaveButton.configure(state=tk.DISABLED, background='#3B3E44', foreground='#b7b7b7')
                        self.updatestatus(text="| Presence is set  | COOLDOWN (15)", color="#202225")
                        self.status_Status.after(1000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (14)", color="#202225"))
                        self.status_Status.after(2000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (13)", color="#202225"))
                        self.status_Status.after(3000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (12)", color="#202225"))
                        self.status_Status.after(4000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (11)", color="#202225"))
                        self.status_Status.after(5000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (10)", color="#202225"))
                        self.status_Status.after(6000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (9)", color="#202225"))
                        self.status_Status.after(7000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (8)", color="#202225"))
                        self.status_Status.after(8000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (7)", color="#202225"))
                        self.status_Status.after(9000, lambda: self.updatestatus(text="| Presence is set  | COOLDOWN (6)", color="#202225"))
                        self.status_Status.after(10000, lambda: self.updatestatus(text="| Presence is set | COOLDOWN (5)", color="#202225"))
                        self.status_Status.after(11000, lambda: self.updatestatus(text="| Presence is set | COOLDOWN (4)", color="#202225"))
                        self.status_Status.after(12000, lambda: self.updatestatus(text="| Presence is set | COOLDOWN (3)", color="#202225"))
                        self.status_Status.after(13000, lambda: self.updatestatus(text="| Presence is set | COOLDOWN (2)", color="#202225"))
                        self.status_Status.after(14000, lambda: self.updatestatus(text="| Presence is set | COOLDOWN (1)", color="#202225"))
                        self.status_Status.after(15000, lambda: self.updatestatus(text="| Presence is set | COOLDOWN (DONE)", color="#202225"))
                        self.status_Status.after(17000, lambda: self.updatestatus(text="| Presence is set |", color="#202225"))
                        self.refresh_Button.after(15000, lambda: self.refresh_Button.configure(state=tk.ACTIVE, background="#4a4d54", activebackground="#4a4d54", foreground="#ededed", activeforeground="#ededed"))
                        self.buttonRP.after(15000, lambda: self.buttonRP.config(text='SET', state=tk.ACTIVE, background='#7289da', foreground='#ffffff', activebackground="#7289da", activeforeground="#ffffff", highlightbackground="#7289da"))
                        self.refresh_Button.after(15000, lambda: self.configClientIDEntry.configure(state=tk.NORMAL))
                        self.refresh_Button.after(15000, lambda: self.configSaveButton.configure(state=tk.ACTIVE, background='#4d915b', foreground='#ffffff', activebackground="#4d915b"))
                        parser.read('data.ini')
                        parser.set('lastpresence', 'remember', str(self.rememberVar.get()))
                        if str(self.rememberVar.get()) == '1':
                            parser.set('lastpresence', 'top', str(self.topVar.get()))
                            parser.set('lastpresence', 'bottom', str(self.bottomVar.get()))
                            parser.set('lastpresence', 'largeasset', str(self.largeVar.get()))
                            parser.set('lastpresence', 'largeassethovertext', str(self.largehoverVar.get()))
                            parser.set('lastpresence', 'smallasset', str(self.smallVar.get()))
                            parser.set('lastpresence', 'smallassethovertext', str(self.smallhoverVar.get()))
                            parser.set('lastpresence', 'time', str(self.timerVar.get()))
                            parser.set('lastpresence', 'timevalue', str(self.timerEntryVar.get()))
                        with open('data.ini', 'w') as configfile:
                            parser.write(configfile)                     
                    except:
                       self.updatestatus(text="| Error while updating presence | Is discord open? | Image name correct?", color="#da7272")
                else:
                    self.updatestatus(text="| Timer's entry needs to be filled", color="#da7272")
            else:
                self.updatestatus(text="| Bottom text box must be filled", color="#da7272")
        else:
            self.updatestatus(text="| Top text box must be filled", color="#da7272")

            
                


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("525x275+500+200")
    root.resizable(False, False)
    window = interface(root)
    root.mainloop()



        