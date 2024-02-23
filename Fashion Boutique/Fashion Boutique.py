#used colors:
##a0569d => pink
#9abfd8 => light
#2a5b7f => dark
#e4e4e1 => back

from tkinter import *
from PIL import ImageTk, Image #for images

class Info:
    def print_title(self):
        print("Fashion Boutique")

    def print_name(self):

        list_students_name = ["Jana Alghamdi / 2230003268", "Areej Alamer/ 2230005275", "Wassayf Alqahtani/ 2230003360", "Fedaa alsabea / 2230003675"]
        for i in list_students_name:
            print(i)
info = Info()
info.print_name()
info.print_title()

class Application:
    def app(self):
        window1 = Tk()
        window1.title("Fashion Boutique")
        window1.geometry("1000x1000")
        window1.config(bg="#e4e4e1")

        frame1 = Frame(master=window1, width=1000, height=1000)
        frame1.pack()

        # lable of title
        lTitle = Label(master=frame1, text="Fashion Boutique", foreground="#2a5b7f", font=('Chiller', 50, 'bold'),
                       pady=15)
        lTitle.place(x=400, y=70)
        # load image file using PIL
        logo = Image.open("logo.png")
        # Resize the image to 300 by 200 pixels
        resized_image = logo.resize((160, 160))
        # convert to tkinter object:
        lolgo_convert = ImageTk.PhotoImage(resized_image)
        # or: to make a short story shorter:
        # Load, resize and convert an image file using PIL
        # lolgo_convert = ImageTk.PhotoImage(Image.open("logo.png").resize((300, 200)))
        # put our image in lable:
        logo_lable = Label(master=frame1, image=lolgo_convert)
        logo_lable.place(x=50, y=70)
# our names:
        name_lable = Label(master=frame1,
                           text="Jana Alghamdi/ 2230003268\nAreej Alamer/ 2230005275\nWassayf Alqahtani/ 2230003360\nFedaa alsabea / 2230003675\n under the supervision of:\nNAZNEEN BEGUM",
                           font=('Athelas', 18, 'bold'), foreground="#a0569d")
        name_lable.place(x=350, y=200)

# description:
        desc_lable = Label(master=frame1, fg="#9abfd8",
                           text="Fashion Boutique is your online destination for high-end bags at great prices.\n You can customize your bag by selecting the size and color that suit your style and pay securely online.\n Experience the convenience and luxury of Fashion Boutique today!",
                           font=('Athelas', 15))
        desc_lable.place(x=28, y=400)

        # button next with function:
        def toPage2():
            # page2
            p2 = Tk()
            p2.geometry("660x900")
            p2.title("Shop now!")

            # page2 title:
            shop_now = Label(p2, text="Shop now!", font=('Tahoma', 20))
            shop_now.place(x=30, y=20)

            # iamges:
            # big bags:
            # 1
            big1 = ImageTk.PhotoImage(file="big1.png", master=p2)
            b1image = Button(p2, image=big1, width=100, height=100)
            b1image.image = big1
            b1image.place(x=100, y=70)
            code1 = Label(p2, text="code: AAS4", fg="#2a5b7f", font=('Tahoma', 17))
            code1.place(x=105, y=180)
            price1 = Label(p2, text="price: 120 SAR", fg="#2a5b7f", font=('Tahoma', 16))
            price1.place(x=95, y=210)
            # 2
            big2 = ImageTk.PhotoImage(file="big3.png", master=p2)
            b2image = Button(p2, image=big2, width=100, height=100)
            b2image.image = big2
            b2image.place(x=100, y=250)
            code2 = Label(p2, text="code: AA43", fg="#2a5b7f", font=('Tahoma', 17))
            code2.place(x=105, y=365)
            price2 = Label(p2, text="price: 150 SAR", fg="#2a5b7f", font=('Tahoma', 16))
            price2.place(x=95, y=393)
            # 3
            big3 = ImageTk.PhotoImage(file="big4.png", master=p2)
            b3image = Button(p2, image=big3, width=100, height=100)
            b3image.image = big3
            b3image.place(x=100, y=445)
            code3 = Label(p2, text="code: Ze34", fg="#2a5b7f", font=('Tahoma', 17))
            code3.place(x=105, y=555)
            price3 = Label(p2, text="price: 170 SAR", fg="#2a5b7f", font=('Tahoma', 16))
            price3.place(x=95, y=585)

            # small bags:
            # 1
            small1 = ImageTk.PhotoImage(file="small1.png", master=p2)
            s1image = Button(p2, image=small1, width=100, height=100)
            s1image.image = small1
            s1image.place(x=370, y=70)
            codes1 = Label(p2, text="code: eW97", fg="#2a5b7f", font=('Tahoma', 17))
            codes1.place(x=360, y=180)
            prices1 = Label(p2, text="price: 170 SAR", fg="#2a5b7f", font=('Tahoma', 16))
            prices1.place(x=355, y=210)
            # 2
            small2 = ImageTk.PhotoImage(file="small2.png", master=p2)
            s2image = Button(p2, image=small2, width=100, height=100)
            s2image.image = small2
            s2image.place(x=370, y=250)
            codes2 = Label(p2, text="code: M345", fg="#2a5b7f", font=('Tahoma', 17))
            codes2.place(x=360, y=365)
            prices2 = Label(p2, text="price: 120 SAR", fg="#2a5b7f", font=('Tahoma', 16))
            prices2.place(x=355, y=393)
            # 3
            small3 = ImageTk.PhotoImage(file="small3.png", master=p2)
            s3image = Button(p2, image=small3, width=100, height=100)
            s3image.image = small3
            s3image.place(x=370, y=445)
            codes3 = Label(p2, text="code: 6224", fg="#2a5b7f", font=('Tahoma', 17))
            codes3.place(x=360, y=555)
            prices3 = Label(p2, text="price: 120 SAR", fg="#2a5b7f", font=('Tahoma', 16))
            prices3.place(x=355, y=585)

            # button go page3
            def toPage3():
                p3 = Tk()
                p3.geometry("450x900")
                p3.title("Info")

                # order details:
                order_code = Label(p3, text="Bag CODE:", fg="#2a5b7f", font=('Gungsuh', 13, 'italic'))
                order_code.place(x=40, y=50)
                order_quantity = Label(p3, text="How many?", fg="#2a5b7f", font=('Gungsuh', 13, 'italic'))
                order_quantity.place(x=40, y=120)
                # Entry:
                code_entry = Entry(p3, width=10, font=('Kefa', 15), fg="#a0569d")
                code_entry.place(x=270, y=50)
                quantity_entry = Entry(p3, width=10, font=('Kefa', 15), fg="#a0569d")
                quantity_entry.place(x=270, y=120)


               #client info:
                client_name = Label(p3, text="Name:", fg="#2a5b7f", font=('Gungsuh', 13, 'italic'))
                client_name.place(x=40, y=190)
                client_email = Label(p3, text="email:", fg="#2a5b7f", font=('Gungsuh', 13, 'italic'))
                client_email.place(x=40, y=260)
                client_adress = Label(p3, text="adress:", fg="#2a5b7f", font=('Gungsuh', 13, 'italic'))
                client_adress.place(x=40, y=330)
                phone_number = Label(p3, text="phone:", fg="#2a5b7f", font=('Gungsuh', 13, 'italic'))
                phone_number.place(x=40, y=400)

                #entry:
                client_name_entry = Entry(p3, width=10, font=('Kefa', 15), fg="#a0569d")
                client_name_entry.place(x=270, y=190)
                client_email_entry = Entry(p3, width=10, font=('Kefa', 15), fg="#a0569d")
                client_email_entry.place(x=270, y=260)
                client_adress_entry = Entry(p3, width=10, font=('Kefa', 15), fg="#a0569d")
                client_adress_entry.place(x=270, y=330)
                phone_entry = Entry(p3, width=10, font=('Kefa', 15), fg="#a0569d")
                phone_entry.place(x=270, y=400)



                def toPage4():
                    p4 = Tk()
                    p4.geometry("600x900")
                    p4.title("Pay")

                    bill_details = Label(master=p4, text="---------------------Bill Details:---------------------", font=(20))
                    bill_details.place(x = 80, y = 50)

                    d_name = Label(p4, text= "Name: ", font=(18))
                    d_name.place(x = 50, y = 100)
                    qq = client_name_entry.get()
                    p_name = Label(p4, text= qq, font=(18))
                    p_name.place(x = 150, y = 100 )

                    d_email = Label(p4, text="email: ", font=(18))
                    d_email.place(x=50, y=150)
                    ww = client_email_entry.get()
                    p_email = Label(p4, text=ww, font=(18))
                    p_email.place(x=150, y=150)

                    d_adress = Label(p4, text="adress: ", font=(18))
                    d_adress.place(x=50, y=200)
                    ee = client_adress_entry.get()
                    p_adress = Label(p4, text=ee, font=(18))
                    p_adress.place(x=150, y=200)

                    d_phone = Label(p4, text="phone: ", font=(18))
                    d_phone.place(x=50, y=250)
                    rr = phone_entry.get()
                    p_phone = Label(p4, text=rr, font=(18))
                    p_phone.place(x=150, y=250)





                    # get the code and quantity as integers
                    code_get = code_entry.get()
                    code_get_slice = code_get[-4:]  # use negative indexing to get the last four characters
                    quantity_get = int(quantity_entry.get())  # convert the quantity to an integer
                    # create a label to display the price
                    price_is = Label(p4, text="price is: ", font=('Kefa', 20, 'bold'))
                    price_is.place(x=140, y=400)
                    bill = Label(p4, text="", font=('Kefa', 20, 'bold'))
                    bill.place(x=320, y=400)
                    # use if-elif-else statements to check the code and calculate the price
                    if code_get_slice == "AAAS4" or code_get_slice == "M345" or code_get_slice == "6224":
                        x = 120 * quantity_get
                        bill.config(text=x)
                    elif code_get_slice == "AA43":
                        x = 150 * quantity_get
                        bill.config(text=x)
                    elif code_get_slice == "Ze34" or code_get_slice == "eW97":
                        x = 170 * quantity_get
                        bill.config(text=x)
                    else:
                        x = "Invalid code"
                        bill.config(text=x)

                    # good buy:
                    good_buy = Label(p4, fg="#2a5b7f", font=("Nyala", 16),
                                     text="Thank you for buying from Fashion Boutique.\n You’ll love our bags. They are stylish and comfortable.\n Please visit us again soon. Have a great day!")
                    good_buy.place(x=17, y=500)

                    def close():
                        p4.destroy()

                    closebtn = Button(master=p4, text="close", fg="#a0569d", font=(20), pady=15, padx=20,
                                      command=close)
                    closebtn.place(x=230, y=670)

                    p4.mainloop()




                go_page2 = Button(master=p3, text="NEXT", fg="#a0569d", font=(20), pady=15, padx=20,
                                  command=toPage4)
                go_page2.place(x=190, y=550)















                p3.mainloop()

            go_page3 = Button(master=p2, text="NEXT", fg="#a0569d", font=(20), pady=15, padx=20,
                              command=toPage3)
            go_page3.place(x=550, y=500)

            p2.mainloop()

        go_page2 = Button(master=frame1, text="NEXT", fg="#a0569d", font=(20), pady=15, padx=20,
                          command=toPage2)
        go_page2.place(x=450, y=500)

        window1.mainloop()
application = Application()
application.app()




