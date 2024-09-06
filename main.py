import tkinter
from tkinter import IntVar
import customtkinter
import dataCollection
import os
from PIL import Image
from trainData import train_data
from Inference import inference
from InferenceDefault import inferenceDefault

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    n = 0

    def __init__(self):
        super().__init__()
        self.title("Media Controller Using Hand Gestures")
        self.geometry("1366x768")
        self.resizable(width=True, height=True)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
       

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "handgesture.png")), size=(40, 40))
        
        self.one_image_display = customtkinter.CTkImage(Image.open(os.path.join(image_path, "oneimg.png")), size=(60, 60))
        self.two_image_display = customtkinter.CTkImage(Image.open(os.path.join(image_path, "twoimg.png")), size=(60, 60))
        self.three_image_display = customtkinter.CTkImage(Image.open(os.path.join(image_path, "threeimg.png")), size=(60, 60))
        self.four_image_display = customtkinter.CTkImage(Image.open(os.path.join(image_path, "fourimg.png")), size=(60, 60))
        self.five_image_display = customtkinter.CTkImage(Image.open(os.path.join(image_path, "fiveimg.png")), size=(60, 60))


        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))



        self.data_collection = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "data_collection.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "data_collection.png")), size=(40, 40))
        self.training_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "training.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "training.png")), size=(40, 40))
        self.test_data_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "test.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "test.png")), size=(40, 40))

        self.one_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "oneimg.png")),dark_image=Image.open(os.path.join(image_path, "oneimg.png")), size=(40, 40))
        
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Hand Gesture", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

 
        self.data_collection_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Collect Data",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.data_collection, anchor="w", command=self.Collectdata)
        self.data_collection_button.grid(row=1, column=0, sticky="ew")

        self.train_data_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Train Data",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.training_image, anchor="w", command=self.Traindata)
        self.train_data_button.grid(row=2, column=0, sticky="ew")

        # self.radio_var = tkinter.StringVar(value="Default")
        #
        # self.radio_button_1 = customtkinter.CTkRadioButton(self.navigation_frame, variable=self.radio_var, value="Default", text="Defualt", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.radio_button_1.grid(row=4, column=0, pady=10, padx=20, sticky="s")
        #
        # self.radio_button_3 = customtkinter.CTkRadioButton(self.navigation_frame, variable=self.radio_var, value="Custom", text="Custom", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.radio_button_3.grid(row=5, column=0, pady=10, padx=20,sticky="s")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


        self.update_main_frame()



    def update_main_frame(self):

        if App.n == 0:



            self.label_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.label_frame.grid(row=0, column=1, rowspan=6, sticky="nsew" ,columnspan=5)
            self.label_frame.grid_rowconfigure(4, weight=1)

            self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")  
            self.main_frame.grid(row=0, column=1,rowspan=10)
            self.main_frame.grid_columnconfigure(0, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.label_frame, text="Start",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=10,sticky="nsew")

            self.radiobutton_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.radiobutton_frame.grid(row=1, column=1, rowspan=10, padx=20, pady=0,sticky="nsew")

            self.radio_var = tkinter.StringVar(value="Default")

            self.radio_button_1 = customtkinter.CTkRadioButton(self.radiobutton_frame, variable=self.radio_var, value="Default", text="Defualt", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

            self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="Custom", text="Custom", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_3.grid(row=2, column=4, pady=10, padx=20, sticky="nsew")

            self.main_frame1 = customtkinter.CTkFrame(self.main_frame, corner_radius=0, fg_color="transparent")  
            self.main_frame1.grid(row=0, column=5,rowspan=10)
            self.main_frame1.grid_columnconfigure(5, weight=1)

            #help box##########################

            self.help_box = customtkinter.CTkFrame(self.main_frame1, border_width=1, border_color="gray50", corner_radius=5)
            self.help_box.grid(row=1, column=5, padx=20, sticky="nsew")

            self.one_image_label = customtkinter.CTkLabel(self.help_box, text="", image=self.one_image_display)
            self.one_image_label.grid(row=2, column=2, padx=20, pady=10)
            self.one_label = customtkinter.CTkLabel(self.help_box, text="Play/Pause", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.one_label.grid(row=3, column=2, padx=20, pady=10)

            self.two_image_label = customtkinter.CTkLabel(self.help_box, text="", image=self.two_image_display)
            self.two_image_label.grid(row=5, column=2, padx=20, pady=10)
            self.two_label = customtkinter.CTkLabel(self.help_box, text="Volume Up", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.two_label.grid(row=6, column=2, padx=20, pady=10)
            
            self.three_image_label = customtkinter.CTkLabel(self.help_box, text="", image=self.three_image_display)
            self.three_image_label.grid(row=2, column=5, padx=20, pady=10)
            self.three_label = customtkinter.CTkLabel(self.help_box, text="Fast Forward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.three_label.grid(row=3, column=5, padx=20, pady=10)

            
            self.four_image_label = customtkinter.CTkLabel(self.help_box, text="", image=self.four_image_display)
            self.four_image_label.grid(row=5, column=5, padx=20, pady=10)
            self.four_label = customtkinter.CTkLabel(self.help_box, text="Backward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.four_label.grid(row=6, column=5, padx=20, pady=10)

            
            self.five_image_label = customtkinter.CTkLabel(self.help_box, text="", image=self.five_image_display)
            self.five_image_label.grid(row=11, column=2, padx=20, pady=10)
            self.five_label = customtkinter.CTkLabel(self.help_box, text="Volume Down", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.five_label.grid(row=12, column=2, padx=20, pady=10)
            ###############################


            # Add button to move to start page from other pages
            self.start_button = customtkinter.CTkButton(self.main_frame, text="Start", command=self.start,width=200,height=90,font=customtkinter.CTkFont(size=30, weight="bold"),fg_color="green",text_color="white")
            self.start_button.grid(row=1, column=1, padx=350, pady=250)

            
            
        elif App.n == 1:
            self.main_frame = customtkinter.CTkFrame(self, width=240, corner_radius=0)
            self.main_frame.grid(row=0, column=1, rowspan=20, sticky="nsew")
            self.main_frame.grid_rowconfigure(4, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.main_frame, text="Data Collection",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=4, columnspan=10, padx=50, pady=(20, 10), sticky="w")
            
            # Back to start button
            self.start_button = customtkinter.CTkButton(self.main_frame, text="Back to Start", command=self.start_page)
            self.start_button.grid(row=1, column=0, padx=20, pady=10)

            self.radiobutton_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
            self.radiobutton_frame.grid(row=0, column=1, rowspan=10, padx=20, pady=0,sticky="nsew")
            # self.radio_var = tkinter.IntVar(value=0)
            self.radio_var = tkinter.StringVar(value="Up")

            
            self.one_image_label = customtkinter.CTkLabel(self.radiobutton_frame, text="", image=self.one_image_display)
            self.one_image_label.grid(row=2, column=2, padx=20, pady=10)
            self.one_label = customtkinter.CTkLabel(self.radiobutton_frame, text="PlayOrPause", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.one_label.grid(row=3, column=2, padx=20, pady=10)
            
            self.two_image_label = customtkinter.CTkLabel(self.radiobutton_frame, text="", image=self.two_image_display)
            self.two_image_label.grid(row=5, column=2, padx=20, pady=10)
            self.two_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Down", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.two_label.grid(row=6, column=2, padx=20, pady=10)
            
            self.three_image_label = customtkinter.CTkLabel(self.radiobutton_frame, text="", image=self.three_image_display)
            self.three_image_label.grid(row=2, column=5, padx=20, pady=10)
            self.three_label = customtkinter.CTkLabel(self.radiobutton_frame, text="FastForward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.three_label.grid(row=3, column=5, padx=20, pady=10)

            
            self.four_image_label = customtkinter.CTkLabel(self.radiobutton_frame, text="", image=self.four_image_display)
            self.four_image_label.grid(row=5, column=5, padx=20, pady=10)
            self.four_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Backward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.four_label.grid(row=6, column=5, padx=20, pady=10)

            
            self.five_image_label = customtkinter.CTkLabel(self.radiobutton_frame, text="", image=self.five_image_display)
            self.five_image_label.grid(row=11, column=2, padx=20, pady=10)
            self.five_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Up", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.five_label.grid(row=12, column=2, padx=20, pady=10)



            self.rowspace=customtkinter.CTkLabel(self.radiobutton_frame, text="", text_color="green")
            self.rowspace.grid(row=4, column=2, padx=20, pady=30)
            self.colspace=customtkinter.CTkLabel(self.radiobutton_frame, text="", text_color="green")
            self.colspace.grid(column=3, padx=100)

            self.rowspace=customtkinter.CTkLabel(self.radiobutton_frame, text="", text_color="green")
            self.rowspace.grid(row=7, column=2, padx=20, pady=30)
            self.colspace=customtkinter.CTkLabel(self.radiobutton_frame, text="", text_color="green")
            self.colspace.grid(column=3, padx=100)
           



            self.logo_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Collect Data", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            
            # Add button to move to start page from other pages

            self.start_button = customtkinter.CTkButton(self.radiobutton_frame, text="Back to Start", command=self.start_page)
            self.start_button.grid(row=1, column=0, padx=20, pady=10)

            self.radio_button_1 = customtkinter.CTkRadioButton(self.radiobutton_frame, variable=self.radio_var,value="PlayOrPause", text="PlayOrPause", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_1.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

            self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="Down", text="Down", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_2.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")

            self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="FastForward", text="FastForward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_3.grid(row=2, column=4, pady=10, padx=20, sticky="nsew")
            
            self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="Backward", text="Backward", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_4.grid(row=5, column=4, pady=10, padx=20, sticky="nsew")

            self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value="Up", text="Up", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.radio_button_4.grid(row=12, column=0, pady=10, padx=20, sticky="nsew")

            self.save_button = customtkinter.CTkButton(self.radiobutton_frame, text="Collect and Save",command=self.save, font=customtkinter.CTkFont(size=20, weight="bold"))

            self.save_button.grid(row=15, column=0, padx=10, pady=25)

        elif App.n == 2:

            self.label_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.label_frame.grid(row=0, column=1, rowspan=6, sticky="nsew")
            self.label_frame.grid_rowconfigure(4, weight=1)     
            self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
              
            self.main_frame.grid(row=0, column=1,rowspan=10)
            self.main_frame.grid_columnconfigure(0, weight=1)
            self.logo_label = customtkinter.CTkLabel(self.label_frame, text="Train Data",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=10,sticky="nsew")

            self.start_button = customtkinter.CTkButton(self.label_frame, text="Back to Start", command=self.start_page)
            self.start_button.grid(row=1, column=0, padx=20, pady=10)
            # Add button to move to start page from other pages
            self.start_button = customtkinter.CTkButton(self.main_frame, text="Train Data", command=self.train,width=200,height=90,font=customtkinter.CTkFont(size=30, weight="bold"),fg_color="green",text_color="white")
            self.start_button.grid(row=1, column=0, padx=20, pady=10)
            

       


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def start_page(self):
        App.n = 0
        self.update_main_frame()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Welcome to Hand Gesture Media Controller", title="CTkInputDialog")
        print("Welcome to Hand Gesture Media Controller")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def Traindata(self):
        App.n = 2
        self.update_main_frame()

    def start(self):
        if self.radio_var.get() == "Default":
            inferenceDefault()
        elif self.radio_var.get() == "Custom":
            inference()

    
    def Collectdata(self):
        App.n = 1
        self.update_main_frame()

    def test(self):
        App.n = 3
        self.update_main_frame()

    def train(self):
        result = train_data()
        if result == 1:
            self.start_page()
        else:
            App.n=2

    def save(self):
        dataCollection.datacollection(self.radio_var.get())
        print(self.radio_var.get(),"Media Collected")
        App.n = 1
        self.update_main_frame()


if __name__ == "__main__":
    app = App()
    app.mainloop()
