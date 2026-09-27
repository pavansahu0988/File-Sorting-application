from tkinter import *
import os,shutil
import tkinter as tk
from tkinter import ttk,filedialog 

class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")#WIDTHxHIEGHT
        self.root.title("File Sorter app by-Pawan sahu")#title
        self.logo_icon=PhotoImage(file="C:\\Users\\HP\\Desktop\\major\\images\\folder.png")
        bgcolor="red"
        title=Label(self.root,text="File Sorting Application",padx=10,image=self.logo_icon,compound=LEFT,font=("impact",30,"bold"),bd=12,bg="#023548",fg="white",anchor="w",pady=2).place(x=0,y=0,relwidth=1)#heading
    

        #section 1
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select folder",font=("times new roman",25),bg="white").place(x=50,y=100)
        text_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=220,y=100,height=40,width=600)

        btn_browse=Button(self.root,command=self.browse_function,text="BROWSE",font=("times new roman",15,"bold"),bg="white",activebackground="#262626",activeforeground="white",cursor="hand2")
        btn_browse.place(x=800,y=100)
        
        hr=Label(self.root,bg="lightgray").place(x=50,y=160,height=2,width=1250)


                #All extensions
        self.image_extensions=["Image Extensions",".png",".jpg",".jpeg"]
        self.audio_extensions=["Audio Extensions",".mp3",".amr"]
        self.video_extensions=["Video Extensions",".mp4",".mkv",".avi"]
        self.doc_extensions=["Document Extensions",".doc",".pdf",".ppt",".xlsx",".pptx",".xls",".rar",".zip"]
        self.exe_extensions=["Other Extensions",".exe"]

        self.folders={
                    'videos':self.video_extensions,
                    'audios':self.audio_extensions,
                    'images':self.image_extensions,
                    'documents':self.doc_extensions,
                 }
        
        #SELECTION BOX

        lbl_support_ext=Label(self.root,text="Various supported extension",font=("times new roman",25),bg="white").place(x=50,y=170)
        self.image_box=ttk.Combobox(self.root,state='readonly',values=self.image_extensions,font=("times new roman",15))       
        self.image_box.place(x=50,y=220)
        self.image_box.current(0) 
        
        self.doc_box=ttk.Combobox(self.root,state='readonly',values=self.doc_extensions,font=("times new roman",15))       
        self.doc_box.place(x=300,y=220)
        self.doc_box.current(0) 
        

        self.audio_box=ttk.Combobox(self.root,state='readonly',values=self.audio_extensions,font=("times new roman",15))       
        self.audio_box.place(x=550,y=220)
        self.audio_box.current(0) 
        

        self.video_box=ttk.Combobox(self.root,state='readonly',values=self.video_extensions,font=("times new roman",15))       
        self.video_box.place(x=800,y=220)
        self.video_box.current(0) 

        self.exe_box=ttk.Combobox(self.root,state='readonly',values=self.exe_extensions,font=("times new roman",15))       
        self.exe_box.place(x=1050,y=220)
        self.exe_box.current(0) 

      
        # All image icons

        self.image_icon=PhotoImage(file="./images/gallery.png")
        self.doc_icon=PhotoImage(file="./images/documents.png")
        self.audio_icon=PhotoImage(file="./images/audio.png")
        self.video_icon=PhotoImage(file="./images/vido.png")
        self.software_icon=PhotoImage(file="./images/software.png")
             
    # TOTAL SECTION

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=260,width=1250,height=300)
        self.lbl_total_files=Label(Frame1,text="Total files",font=("times new roman",20,"bold"),bg="white")
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_images=Label(Frame1,text="total images \n 250",image=self.image_icon,compound="top",relief=RAISED,bd=2,font=("times new roman",20),bg="#9A32CD",fg="white")
        self.lbl_total_images.place(x=10,y=50,width=200,height=220)

        self.lbl_total_images=Label(Frame1,text="total documents \n 277",image=self.doc_icon,compound="top",relief=RAISED,bd=2,font=("times new roman",20),bg="#DAA520",fg="white")
        self.lbl_total_images.place(x=250,y=50,width=200,height=220)

        self.lbl_total_images=Label(Frame1,text="total audio \n 120",image=self.audio_icon,compound="top",relief=RAISED,bd=2,font=("times new roman",20),bg="#EE7600",fg="white")
        self.lbl_total_images.place(x=500,y=50,width=200,height=220)

        self.lbl_total_images=Label(Frame1,text="total video \n 127",image=self.video_icon,compound="top",relief=RAISED,bd=2,font=("times new roman",20),bg="#FF4040",fg="white")
        self.lbl_total_images.place(x=750,y=50,width=200,height=220)

        self.lbl_total_images=Label(Frame1,text="total other file \n 197",image=self.software_icon,compound="top",relief=RAISED,bd=2,font=("times new roman",20),bg="#20B2AA",fg="white")
        self.lbl_total_images.place(x=1000,y=50,width=200,height=220)

#STATUS BAR
        
        self.lbl_status=Label(self.root,text="STATUS",font=("times new roman",20),bg="white",fg="black")
        self.lbl_status.place(x=50,y=580)

        self.lbl_st_total=Label(self.root,text="TOTAL:971",font=("times new roman",18),bg="white",fg="green")
        self.lbl_st_total.place(x=250,y=580)

        self.lbl_st_moved=Label(self.root,text="MOVED:928",font=("times new roman",18),bg="white",fg="blue")
        self.lbl_st_moved.place(x=450,y=580)

        self.lbl_st_left=Label(self.root,text="LEFT:43",font=("times new roman",18),bg="white",fg="orange")
        self.lbl_st_left.place(x=650,y=580)
        
        
        #button

        self.btn_clear=Button(self.root,text="CLEAR" ,command=lambda:self.var_foldername.set(''),bd=4,relief=RAISED,font=("times new roman",15,"bold"),bg="#607d8b",activebackground="#262626",activeforeground="white",cursor="hand2")
        self.btn_clear.place(x=820,y=580,height=45,width=200)

        self.btn_start=Button(self.root,text="START", command=self.organize_files,bd=4,relief=RAISED,font=("times new roman",15,"bold"),bg="#ff5722",activebackground="#262626",activeforeground="white",cursor="hand2")
        self.btn_start.place(x=1050,y=580,height=45,width=200)

    # end of GUI

    
    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        for i in self.all_files:
           if os.path.isfile(os.path.join(self.selected_directory,i))==True:
                count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                #    print(folder_name)
                   if ext in folder_name[1]and folder_name[0]=="images":
                       images+=1
                   if ext in folder_name[1]and folder_name[0]=="audio":
                       audios+=1
                   if ext in folder_name[1]and folder_name[0]=="video":
                       videos+=1
                   if ext in folder_name[1]and folder_name[0]=="documents":
                       documents+=1
        #for other files
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.selected_directory,i))==True:
                ext = "."+i.split(".")[-1]
                # if ext.lower() not in cmbine_list:
                #     others+=1


        self.lbl_total_images.config(text="Total Image\n"+str(images))
        self.lbl_total_files.config(text="total :"+str(count))
        
    #     # take input from user
    def browse_function(self):
        self.selected_directory=filedialog.askdirectory(title="Select a file")
       
        if self.selected_directory!=None:
            self.var_foldername.set(str(self.selected_directory))
            self.directry=self.var_foldername.get()
            self.other_name="others"
            self.self.self.self.self.self.self.self.rename_folder()
            self.all_files=os.listdir(self.directry)
            length=len(self.all_files)
            count=1
            self.Total_count()
            
            
     
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                    pass
                    # self.create_move(i.split(".")[-1],i)
                print(f'Total:{length}|Done:{count}|left:{length-count}')
                count+=1

    def organize_files(self):
        if not hasattr(self, 'selected_directory') or not self.selected_directory:
            tk.messagebox.showinfo("Error", "Please select a directory first.")
            return

        try:
            for filename in os.listdir(self.selected_directory):
                source_path = os.path.join(self.selected_directory, filename)

                if os.path.isfile(source_path):
                    # Get the file extension
                    _, file_extension = os.path.splitext(filename)

                    # Create a directory for the extension if it doesn't exist
                    destination_folder = os.path.join(self.selected_directory, file_extension[1:])
                    os.makedirs(destination_folder, exist_ok=True)

                    # Move the file to the destination folder
                    destination_path = os.path.join(destination_folder, filename)
                    shutil.move(source_path, destination_path)

            result = tk.messagebox.askyesno("Success", "Files organized successfully!\n Do you want to open ?")

            # Process the result
            if result:
                os.startfile(self.selected_directory)
            else:
                print("User clicked No.")
                

        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

        

    # def rename_folder(self):
    #     for folder in os.listdir(self.directry):
    #         if os.path.isdir(os.path.join(self.directry,folder))==True:
    #             os.rename(os.path.join(self.directry,folder)),os.path.join(self.directry,folder)        

    # def create_move(self,ext,file_name):
    #     find=False
    #     for folder_name in self.folders:
    #         if "."+ext in self.folders[folder_name]:
    #             if folder_name not in os.listdir(self.directry):
    #                 os.mkdir(os.path.join(self.directry,folder_name))
    #             shutil.move(os.path.join(self.directry,file_name)),os.path.join(self.directry,folder_name)  
    #             find=True
    #             break
    #     if find!=True:
    #         if self.other_name not in os.listdir(self.directry):
    #             os.mkdir(os.path.join(self.directry,self.other_name))
    #         shutil.move(os.path.join(self.directry,file_name)),os.path.join(self.directry,folder_name)





root=Tk()
object=Sorting_App(root)
root.mainloop()


