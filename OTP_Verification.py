from tkinter import *
from twilio.rest import Client
import random
from tkinter import  messagebox
import time

print("***************************OTP VERIFICATION SYSTEM*****************")

class otp_verifier(Tk) :
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg = "#FFFFFF")
        self.resizable(False, False)
        self.n = str(self.OTP())
        self.client = Client("ACc9bc34fa07102336a1791a2ac4ac7b29", "ee0dcfe341f504033ec851c5f8c65e2d")
        self.client.messages.create(to=("+918851715010"),
                                    from_="+18318513498",
                                    body = self.n
                                    )
        self.minuteString = StringVar()
        self.secondString = StringVar()

        self.minuteString.set("10")
        self.secondString.set("00")

    def Labels(self):
            self.c = Canvas(self, bg= "#808080", width=400, height=280)
            self.c.place(x=290, y=120)

            self.minuteTextbox = Entry(self, width=2, bg="#808080", font=("Calibri", 20, ""),
                                       textvariable=self.minuteString)
            self.secondTextbox = Entry(self, width=2, bg="#808080", font=("Calibri", 20, ""),
                                       textvariable=self.secondString)

            self.minuteTextbox.place(x=460, y=270)
            self.secondTextbox.place(x=500, y=270)

            self.c = Canvas(self, bg = "#0000FF", width = 400, height = 280)
            self.c.place(x = 290, y=120 )

            self.upper_frame =  Frame(self, bg = "#FFA500", width=3000, height= 200 )
            self.upper_frame.place(x=0 , y=0)

            self.picture = PhotoImage(file = "LOGO.png")
            self.k = Label(self.upper_frame, image= self.picture, bg = "#FFA500").place(x = 50 , y= 20)

            self.j = Label(self.upper_frame, text = "Verify OTP", font = "TimesNewRoman 38 bold", bg = "#FFA500", fg="white" ).place(x = 350, y = 50)


    def Entry(self):
         self.User_name = Text(self, font="Calibre 20", borderwidth= 2, wrap= WORD, width= 23, height=1)
         self.User_name.place(x=315, y= 250)

    def OTP(self) :
        return random.randrange(1000, 10000)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file= "output-onlinepngtools.png")
        self.submitButton = Button(self, image = self.submitButtonImage, command= lambda:[self.checkOTP(), self.runTimer()], border=0)
        self.submitButton.place(x = 445, y= 300)

        self.resendOTPImage = PhotoImage(file="resend_otp.png")
        self.resendOTP = Button(self, image= self.resendOTPImage, command = self.resendOTP, border= 0)
        self.resendOTP.place(x= 410, y=450)

    def resendOTP(self):
        self.n = str(self.OTP())
        self.client = Client("ACc9bc34fa07102336a1791a2ac4ac7b29", "ee0dcfe341f504033ec851c5f8c65e2d")
        self.client.messages.create(to=("+918851715010"),
                                    from_="+18318513498",
                                    body=self.n)

    def checkOTP(self):
        try:
            self.userInput = int(self.User_name.get(1.0, "end-1c"))
            if self.userInput == int(self.n) :
                  messagebox.showinfo(":showinfo", "Verification Successful")
                  self.n = "done"
            else :
                  messagebox.showinfo("showinfo", "Wrong OTP")

        except :
            messagebox.showinfo("showinfo", "INVALID OTP")

    def runTimer(self):

        self.clockTime = int(self.minuteString.get())*60 + int(self.secondString.get())

        while (self.clockTime > -1):

            totalMinutes, totalSeconds = divmod(self.clockTime, 60)

            self.minuteString.set("{0:2d}".format(totalMinutes))
            self.secondString.set("{0:2d}".format(totalSeconds))

            self.update()
            time.sleep(1)


            if (self.clockTime == 0):
                messagebox.showinfo("", "Your time has expired!")

            self.clockTime -= 1

if __name__ == "__main__" :
    window =  otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.OTP()
    window.update()
    window.mainloop()