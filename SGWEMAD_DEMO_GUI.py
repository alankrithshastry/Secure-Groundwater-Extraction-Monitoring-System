# groundwater_gui_v2.py
# Professional Dashboard Version 2.1

import serial
import tkinter as tk
from tkinter import ttk, messagebox
import random
from datetime import datetime

COM_PORT = "COM4"
MAX_HEIGHT = 15

fake_mode = False
fake_counter = 0
previous_percentage = 0
recent_readings = []

arduino = serial.Serial(COM_PORT, 9600)

def add_log(log_widget, msg):
    ts = datetime.now().strftime("%H:%M:%S")
    log_widget.insert("end", f"[{ts}] {msg}\n")
    log_widget.see("end")

login = tk.Tk()
login.title("Secure Login")
login.geometry("500x350")
login.configure(bg="#eef4f8")

tk.Label(login,text="GROUNDWATER MONITORING LOGIN",
         font=("Arial",18,"bold"),
         bg="#eef4f8",fg="#0b3d5c").pack(pady=30)

user = tk.Entry(login,font=("Arial",14),width=25)
user.pack(pady=10)
user.insert(0,"admin")

pwd = tk.Entry(login,font=("Arial",14),width=25,show="*")
pwd.pack(pady=10)

def open_dashboard():
    global previous_percentage,recent_readings
    previous_percentage = 0
    recent_readings = []
    arduino.reset_input_buffer()
    login.destroy()

    root = tk.Tk()
    root.title("Groundwater Monitoring V2.1")
    root.state("zoomed")
    root.configure(bg="#eef4f8")

    header = tk.Frame(root,bg="#0b3d5c",height=80)
    header.pack(fill="x")
    tk.Label(header,
             text="SECURE GROUNDWATER EXTRACTION MONITORING WITH ANOMALY DETECTION",
             bg="#0b3d5c",fg="white",
             font=("Arial",20,"bold")).pack(pady=20)

    body = tk.Frame(root,bg="#eef4f8")
    body.pack(fill="both",expand=True,padx=15,pady=15)

    left = tk.Frame(body,bg="white",bd=2,relief="ridge")
    left.pack(side="left",fill="both",expand=True,padx=10)

    canvas = tk.Canvas(left,width=500,height=350,bg="#dff4ff")
    canvas.pack(padx=10,pady=10)

    canvas.create_rectangle(220,40,280,500,fill="#efefef",width=2)
    canvas.create_rectangle(190,5,310,45,fill="black")
    canvas.create_text(250,25,text="ULTRASONIC SENSOR",fill="white")

    water_rect = canvas.create_rectangle(223,500,277,500,fill="#00bfff")

    right = tk.Frame(body,bg="#eef4f8")
    right.pack(side="right",fill="y",padx=10)

    card1 = tk.Frame(right,bg="white",bd=2,relief="ridge")
    card1.pack(fill="x",pady=8)

    tk.Label(card1,text="WATER LEVEL",font=("Arial",16,"bold"),
             bg="white").pack(pady=5)

    water_lbl = tk.Label(card1,text="0%",font=("Arial",30,"bold"),
                         bg="white",fg="#0077b6")
    water_lbl.pack()

    prog = ttk.Progressbar(card1,length=280,maximum=100)
    prog.pack(pady=12)

    card2 = tk.Frame(right,bg="white",bd=2,relief="ridge")
    card2.pack(fill="x",pady=8)

    tk.Label(card2,text="SYSTEM STATUS",font=("Arial",16,"bold"),
             bg="white").pack(pady=5)
    status_lbl = tk.Label(card2,text="NORMAL",font=("Arial",22,"bold"),
                          bg="white",fg="green")
    status_lbl.pack(pady=10)

    card3 = tk.Frame(right,bg="white",bd=2,relief="ridge")
    card3.pack(fill="x",pady=8)

    tk.Label(card3,text="CYBER SECURITY",font=("Arial",16,"bold"),
             bg="white").pack(pady=5)
    cyber_lbl = tk.Label(card3,text="DATA SECURE",font=("Arial",14,"bold"),
                         bg="white",fg="blue")
    cyber_lbl.pack(pady=10)
        # Allowed Extraction Card
    card4 = tk.Frame(right,bg="white",bd=2,relief="ridge")
    card4.pack(fill="x",pady=8)

    tk.Label(card4,
             text="ALLOWED EXTRACTION",
             font=("Arial",16,"bold"),
             bg="white").pack(pady=5)

    allowed_lbl = tk.Label(card4,
                           text="30%",
                           font=("Arial",22,"bold"),
                           bg="white",
                           fg="green")

    allowed_lbl.pack(pady=10)
    allowed = 30
    def force_extraction():
        try:
            req = float(req_entry.get())
        except:
            result_lbl.config(
                text="INVALID INPUT",
                fg="red"
            )
            return        

        
        result_lbl.config(
            text="FORCE APPROVED",
            fg="orange"
        )

        status_lbl.config(
            text="ANOMALY",
            fg="red"
        )

        cyber_lbl.config(
            text="POLICY VIOLATION",
            fg="red"
        )

        add_log(
            log,
            f"FORCE EXTRACTION USED : {req}%"
        )

        add_log(
            log,
            "POLICY VIOLATION DETECTED"
        )
        root.after(
    10000,
    lambda: (
        status_lbl.config(text="NORMAL",fg="green"),
        cyber_lbl.config(text="DATA SECURE",fg="blue"),
        add_log(log,"SYSTEM RESTORED")
    )
)
    def submit_request():

        try:
            req = float(req_entry.get())

            if req <= int(allowed_lbl.cget("text").replace("%","")):
                result_lbl.config(
                    text="REQUEST APPROVED",
                    fg="green"
                )

                add_log(
                    log,
                    f"Request Approved : {req}%"
                )

            else:
                result_lbl.config(
                    text="LIMIT EXCEEDED",
                    fg="red"
                )

                add_log(
                    log,
                    f"Request Rejected : {req}%"
                )

        except:
            result_lbl.config(
                text="INVALID INPUT",
                fg="red"
            )
        # Extraction Request Panel
    request_frame = tk.Frame(left,bg="white",bd=2,relief="ridge")
    request_frame.pack(fill="x", padx=20, pady=10)

    tk.Label(request_frame,
             text="GROUNDWATER EXTRACTION REQUEST",
             font=("Arial",14,"bold"),
             bg="white").pack(pady=5)

    req_entry = tk.Entry(request_frame,font=("Arial",12))
    req_entry.pack(pady=5)
    result_lbl = tk.Label(request_frame,
                          text="",
                          font=("Arial",14,"bold"),
                          bg="white")
    result_lbl.pack(pady=5)
    submit_btn = tk.Button(
        request_frame,
        text="SUBMIT REQUEST",
        command=submit_request,
        bg="#0052cc",
        fg="white",
        font=("Arial",11,"bold")
    )
    submit_btn.pack(pady=5)
    force_btn = tk.Button(
    request_frame,
    text="FORCE EXTRACTION",
    bg="red",
    fg="white",
    font=("Arial",11,"bold"),
    command=force_extraction
)

    force_btn.pack(pady=5)
        
    log_frame = tk.Frame(left,bg="white",bd=2,relief="ridge")
    log_frame.pack(fill="x",padx=20,pady=10)

    tk.Label(log_frame,text="EVENT LOG",font=("Arial",15,"bold"),
             bg="white").pack()

    log = tk.Text(log_frame,height=6)
    log.pack(fill="x",padx=10,pady=10)

    add_log(log,"System Started")
    
    def inject():
        global fake_mode,fake_counter
        fake_mode = True
        fake_counter = 10
        btn.config(state="disabled")
        add_log(log,"Fake Data Injection Started")

    btn = tk.Button(card3,text="INJECT FAKE DATA",
                    bg="red",fg="white",
                    font=("Arial",12,"bold"),
                    command=inject)
    btn.pack(pady=10)

    def update():
        global allowed 
        global fake_mode,fake_counter,previous_percentage,recent_readings

        try:
            data = arduino.readline().decode().strip()

            if "Water Level:" in data:
                level = float(data.replace("Water Level:","").replace("cm",""))

                if level < 2:
                    level = 0

                recent_readings.append(level)
                if len(recent_readings) > 5:
                    recent_readings.pop(0)

                level = sum(recent_readings)/len(recent_readings)

                level = max(0,min(MAX_HEIGHT,level))

                pct = (level/MAX_HEIGHT)*100

                if pct < 3:
                    pct = 0
                if pct > 97:
                    pct = 100

                pct = previous_percentage*0.4 + pct*0.6
                previous_percentage = pct

                if fake_mode:
                    pct = random.randint(5,100)
                    cyber_lbl.config(text="DATA TAMPERING DETECTED",fg="red")
                    status_lbl.config(text="ANOMALY",fg="red")

                    fake_counter -= 1
                    if fake_counter <= 0:
                        fake_mode = False
                        btn.config(state="normal")
                        cyber_lbl.config(text="DATA SECURE",fg="blue")
                        status_lbl.config(text="NORMAL",fg="green")
                        add_log(log,"System Restored")
                if pct > 75:
                    allowed = 30
                elif pct > 50:
                    allowed = 20
                elif pct > 25:
                    allowed = 10
                else:
                    allowed = 5     
                allowed_lbl.config(text=f"{allowed}%")    
                water_lbl.config(text=f"{pct:.1f}%")
                prog["value"] = pct

                h = 420*(pct/100)
                canvas.coords(water_rect,223,500-h,277,500)

        except:
            pass

        root.after(1000,update)

    update()
    root.mainloop()

def do_login():
    if user.get().strip() == "admin" and pwd.get().strip() == "admin123":
        open_dashboard()
    else:
        messagebox.showerror("Login Failed","Invalid Username or Password")

tk.Button(login,text="LOGIN",command=do_login,
          bg="#0b3d5c",fg="white",
          font=("Arial",14,"bold")).pack(pady=20)

login.mainloop()
