import os
import sys
import random

from log_base import log

import service_SmsOtp
import util_PhoneNumbers

"""
======================= MAIN
"""

URL_API_SMS = (
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


def banner():
    banner = f"""
     \033[1;93m
    ███████╗██████╗  █████╗ ███╗   ███╗     ██████╗ ████████╗██████╗
    ██╔════╝██╔══██╗██╔══██╗████╗ ████║    ██╔═══██╗╚══██╔══╝██╔══██╗
    ███████╗██████╔╝███████║██╔████╔██║    ██║   ██║   ██║   ██████╔╝
    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║    ██║   ██║   ██║   ██╔═══╝
    ███████║██║     ██║  ██║██║ ╚═╝ ██║    ╚██████╔╝   ██║   ██║
    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝    ╚═╝   ╚═╝
    """
    # banner = f"spam otp\n"
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()


os.system("cls" if os.name == "nt" else "clear")
banner()


def validPhone():
    phone = input(str('\033[1;33mPhone Number: '))
    # Validate input phone
    if (not len(phone.strip())):
        print("Bạn chưa nhập sdt !!!")
        return None

    log.info(f'phone input: {phone}')
    phone = phone.replace(' ', '')
    log.info(f'phone edited: {phone}')

    if (not phone.isnumeric()):
        log.warning(f'{phone} không là chuỗi số')
        print("Bạn nhập có ký tự không phải số !!!")
        return None

    if (not util_PhoneNumbers.is_valid_phone_number_VN(phone)):
        log.warning(f'{phone} không là sdt')
        print(f'{phone} không là sdt')
        return None
    return phone


def spamSmsOtp(phone, url):
    return service_SmsOtp.requestSpamSmsOtp(phone, url)


# Check input phone
phone = validPhone()
if (None == phone):
    input(str('Press any key to exit !!!'))
    sys.exit()

# Get random url
url = random.choice(URL_API_SMS)

# Request
resultRequest = spamSmsOtp(phone, url)
if (True == resultRequest):
    resultMessage = 'Gửi thành công'
    log.info(resultMessage)
else:
    resultMessage = 'Gửi thất bại'
    log.warning(resultMessage)

print(resultMessage)

input(str('Press any key to exit !!!'))
sys.exit()
