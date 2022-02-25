from requests import post
from random import choice
from secrets import token_hex
from string import ascii_letters
from time import sleep as sp, time
from sty import fg, bg, ef, rs
from os import system, get_terminal_size, name
from httpx_socks import SyncProxyTransport
from concurrent.futures import ThreadPoolExecutor as tp
from httpx import Client
from hcapt import bypass, setup
from json import loads, dumps, load
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('Discord Member Boost Tool | VojtasL#9848')
def make_c(c, msg):
    return f'''{fg(int(c))}{msg}{fg.rs}'''


def printc(text, textm = ('',)):
    pass


def printc2(text):
    wi = (get_terminal_size().columns - 3) // 5


def clear():
    if name == 'nt':
        pass
    1('clear')


def inputc(text):
    return input(f'''{''.center(get_terminal_size().columns // 4)}{text}''')

bar = bg.magenta + ' Mode [v1 or v2] :' + bg.rs
print('\n\n\n')
mode_gen = input(f'''                                               {bar} ''')
if mode_gen == 'v1':
    ctypes.windll.kernel32.SetConsoleTitleW('Loading... | Discord Member Boost Tool | VojtasL#9848')
elif mode_gen == 'v2':
    ctypes.windll.kernel32.SetConsoleTitleW('Loading... | Discord Member Boost Tool | VojtasL#9848')
else:
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW('Error | Close program in 5 sec')
    ttr = 'Please type [ v1 | v2 ]'
    errr = '[Error]'
    printc2(f'''\n\n\n\n\n\n\n\n                                         {make_c(196, errr)} {make_c(254, ttr)}''')
    five = '5'
    printc(f'''\n\n\n\n\n        Close the program in {make_c(196, five)} sec''')
    exit()
captcha__text = '[Captcha]'
token__text = '[Finish]'
config = load(open('config.json', 'utf-8', **('encoding',)))
key = config['key_cap']
hc_a = 'wAHi1MOKSosBLK6HVeeBzfbaQknsYZOOkIB/s3TXYK3NzxiIzJ3HzV6uQOMlyTSI1GIVz9AazrmLIgl7NAufVofFaQDhnTL9CNyhqVwlaibJmi6mQrr377HrCaTI7VCWxo1kniMjJDOEz4X29+NH5awd4jH6hPyKIOZhNjWuMrNSKu6ZFLuRSgOiy4c+0idoOSRYiOiX9HK8KkQaHk8EfkR05vRrjPBkaNVKqg1RcpcfREQ06gIS9YzkItTt+2z/aHHZU1rAdJTyJ8oijsq2Mis23zqp9EWQ52H4oWEstionkOct9Z8NgybESmrdNsowi3NXNOoVwWoU4ZEwGCbjG8eO+2HnSP1vPKUi6tT7Z39E2eCMAJJDn9dyenkOuFRcOMmFiMIIIFsTUniyM7EhvSWxWDFvI+4zbx/+TP5pQClZJcLbXinpw1SMk3GVT3S6EG2n/DyLQ0/p3+/CJYbr7sVjdeRLQBGyCMvaOPy+dvaRH+mszz58EoV35sq9835SPRD17jNym9E=UCa12gEu9VIPScd9'
ec = tp(int(100000), **('max_workers',))
pro_list = [
    '-',
    '\\',
    '|',
    '/']
pro_num = 0
cap_done = 0
token_done = 0
msg_list = [
    '\n[*] Token generator v2']
proxy_list = list()
proxy_num = 0
proxy_name = [
    config['proxy_file'] + '.txt']
setup(proxy_list, hc_a)

def register(captcha, invite):
Unsupported opcode: WITH_EXCEPT_START
    if config['username_ascii'] == True:
        username = f'''{config['username']} ''' + f''' {''.join((lambda .0: [ choice(ascii_letters) for _ in .0 ])(range(3)))}'''
    else:
        username = config['username']
    data = {
        'captcha_key': captcha,
        'consent': True,
        'date_of_birth': '2001-03-05',
        'fingerprint': '',
        'gift_code_sku_id': None,
        'invite': invite,
        'username': username }
    p = f'''socks4://{choice(proxy_list)}'''
# WARNING: Decompyle incomplete


def reg(invite, tt):
    global cap_done
    c = post('http://api.capmonster.cloud/createTask', {
        'clientKey': key,
        'task': {
            'type': 'HCaptchaTaskProxyless',
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
            'websiteURL': f'''https://discord.com/invite/{invite}''',
            'websiteKey': 'f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34' } }, **('json',)).json()['taskId']
    sp(0.5)
    d = post('http://api.capmonster.cloud/getTaskResult', {
        'clientKey': key,
        'taskId': c }, **('json',)).json()
    if d['status'] == 'ready':
        msg_list.append(f'''\n{make_c(226, captcha__text)} Available | Waiting for generator''')
        cap_done += 1
        if tt <= int(time()):
            pass
        else:
            sp(0.5)
        register(d['solution']['gRecaptchaResponse'], invite)



def reg_free(invite, tt):
    global cap_done
    cap = bypass()
    msg_list.append(f'''\n              {make_c(226, captcha__text)} Available | Waiting for generator''')
    cap_done += 1
    if tt <= int(time()):
        pass
    else:
        sp(0.5)
    register(cap, invite)

gi = '0'
ci = '0'
i = config['invite']
j = config['amount_bot']
t = '0'

def a():
    tt = int(time() + int(t))
    if mode_gen == 'v1':
        pass
    if mode_gen == 'v2':
        pass

ec.submit(a)
clear()
oo0o0o0o0o0o = f'''               [*] Gen mode : {make_c(51, mode_gen)} | [*] discord.gg/{make_c(51, i)} | [*] Amount gen {make_c(51, j)} users | [*] {make_c(51, len(proxy_list))} proxy\n '''
printc('\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\xe2\x96\x85\n ')
dfks0idgfid = f'''{make_c(15, oo0o0o0o0o0o)}'''
printc(dfks0idgfid)

def update():
Unsupported opcode: RERAISE
    global pro_num
    pass
# WARNING: Decompyle incomplete

update()
if token_done >= j:
    pass
else:
    sp(0.5)
