#!/usr/bin/env python

import random

from tkinter import *
from tkinter import ttk

from log_base import log

import service_SmsOtp
import util_PhoneNumbers

"""
======================= MAIN
"""


class App(Frame):

    countSpam = 0
    countSuccess = 0
    countFail = 0
    urlApiSms = (
        'https://api-sms-v2.herokuapp.com/nhap-hang-247?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/elines?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/meta-vn?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/bach-hoa-xanh?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/grab-food?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/tiki?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/gojoy?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/vntrip?phone={sdt}',
        'https://api-sms-v2.herokuapp.com/the-gioi-di-dong?phone={sdt}',
    )

    def __init__(self, master=None):
        Frame.__init__(self, master)

        # UI options
        paddings = {'padx': 64, 'pady': 25}
        entry_font = {'font': ('Helvetica', 11)}

        # Configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.master = master

        # Phone
        self.l_phone = ttk.Label(text="Phone")
        self.l_phone.grid(row=2, column=0, **paddings)

        self.e_phone = ttk.Entry(width=30, **entry_font)
        self.e_phone.grid(row=2, column=1, padx=10, pady=10, ipadx=2, ipady=2)

        # Buttons
        self.b_clear = ttk.Button(text="Clear")
        self.b_clear['command'] = self.clearSpamOtp
        self.b_clear.grid(row=3, column=0, columnspan=2, ipadx=10)

        self.b_spam = ttk.Button(text="Spam")
        self.b_spam['command'] = self.submitSpamOtp
        self.b_spam.grid(row=3, column=1, columnspan=2, ipadx=10)

        # Result message
        self.l_result = ttk.Label(
            text='', foreground="#FA7905", wraplength=300, justify="left")
        self.l_result.grid(row=4, column=0, columnspan=3, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', **entry_font)
        self.style.configure('TEntry', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11), width=6)

    def submitSpamOtp(self):
        phone = self.e_phone.get()

        # Validate input phone
        if (not len(phone.strip())):
            self.l_result.config(text="Bạn chưa nhập sdt !!!")
            return

        log.info(f'phone input: {phone}')
        phone = phone.replace(' ', '')
        log.info(f'phone edited: {phone}')

        if (not phone.isnumeric()):
            log.warning(f'{phone} không là chuỗi số')
            self.l_result.config(text="Bạn nhập có ký tự không phải số !!!")
            return

        if (not util_PhoneNumbers.is_valid_phone_number_VN(phone)):
            log.warning(f'{phone} không là sdt')
            self.l_result.config(text="Bạn nhập sai sdt !!!")
            return

        # Get random url
        url = random.choice(self.urlApiSms)
        brand = url[33:len(url)]
        brand = brand[:len(brand)-12]
        log.debug(f'url: {url}, brand: {brand}')

        # Request
        result = service_SmsOtp.requestSpamSmsOtp(phone, url)
        msgResult = ''
        if result:
            self.countSuccess += 1
            msgResult = 'thành công'
        else:
            self.countFail += 1
            msgResult = 'thất bại'

        # Display messages
        self.countSpam += 1
        msgResult = f"count: {self.countSpam}, success: {self.countSuccess}, fail: {self.countFail}\nphone: {phone}\nbrand: {brand}\nmessage: {msgResult}"
        log.info(repr(msgResult))
        self.l_result.config(text=msgResult)

    def clearSpamOtp(self):
        log.info(self.e_phone.get())
        self.e_phone.delete(0, END)
        self.l_result.config(text='')


root = Tk()
app = App(root)
root.wm_title("Spam SMS OTP")
root.geometry("500x250")
root.eval('tk::PlaceWindow . center')
# root.config(bg="#447c84")
root.attributes('-fullscreen', False)
root.mainloop()
