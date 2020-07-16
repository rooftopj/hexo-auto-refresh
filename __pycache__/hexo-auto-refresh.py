# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle
import os

window = tk.Tk()
window.title('Welcome to rooftopj\'s hexo-auto-refresh')
window.geometry('476x450')

canvas = tk.Canvas(window, height=200, width=476)
image_file = tk.PhotoImage(file='emblemmatic-rooftopj-logo-9.png')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

tk.Label(window, text='User name: ').place(x=5, y= 150)
tk.Label(window, text='七牛云账号').place(x=260, y= 150)
tk.Label(window, text='Password: ').place(x=5, y= 190)
tk.Label(window, text='七牛云密码').place(x=260, y= 190)
tk.Label(window, text='updateSite1: ').place(x=5, y= 230)
tk.Label(window, text='https://wwww.example.com/').place(x=260, y= 230)
tk.Label(window, text='updateSite2: ').place(x=5, y= 270)
tk.Label(window, text='https://example.com/').place(x=260, y= 270)
tk.Label(window, text='newPost: ').place(x=5, y= 300)

# input
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=105, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd) # , show='*'
entry_usr_pwd.place(x=105, y=190)

var_update_site1 = tk.StringVar()
update_site1 = tk.Entry(window, textvariable=var_update_site1)
update_site1.place(x=105, y=230)

var_update_site2 = tk.StringVar()
update_site2 = tk.Entry(window, textvariable=var_update_site2)
update_site2.place(x=105, y=270)

var_newPost = tk.StringVar()
newPost = tk.Entry(window, textvariable=var_newPost)
newPost.place(x=105, y=300)

try:
    with open('usrs_info.pickle', 'rb') as usr_file:
        usrs_info = pickle.load(usr_file)
        var_usr_name.set(usrs_info['var_usr_name_input'])
        var_usr_pwd.set(usrs_info['var_usr_pwd_input'])
        var_update_site1.set(usrs_info['var_update_site_input1'])
        var_update_site2.set(usrs_info['var_update_site_input2'])
except FileNotFoundError:
    pass

def newPostFunction():
    newPost_command = 'cd .. && hexo n ' + newPost.get()
    os.system(newPost_command)

def local():
    os.system('local.sh')

def deploy_gulp():
    exist_usr_info={}
    exist_usr_info['var_usr_name_input']=var_usr_name.get()
    exist_usr_info['var_usr_pwd_input']=var_usr_pwd.get()
    exist_usr_info['var_update_site_input1']=update_site1.get()
    exist_usr_info['var_update_site_input2']=update_site2.get()
    with open('usrs_info.pickle', 'wb') as usr_file:
        pickle.dump(exist_usr_info, usr_file)
    os.system('deploy_gulp.sh')

def deploy():
    exist_usr_info={}
    exist_usr_info['var_usr_name_input']=var_usr_name.get()
    exist_usr_info['var_usr_pwd_input']=var_usr_pwd.get()
    exist_usr_info['var_update_site_input1']=update_site1.get()
    exist_usr_info['var_update_site_input2']=update_site2.get()
    with open('usrs_info.pickle', 'wb') as usr_file:
        pickle.dump(exist_usr_info, usr_file)
    os.system('deploy.sh')

# button
btn_sign_up = tk.Button(window, text='Create post', command=newPostFunction)
btn_sign_up.place(x=260, y=300)

btn_sign_up = tk.Button(window, text='Local deployment', command=local)
btn_sign_up.place(x=170, y=340)

btn_sign_up = tk.Button(window, text='Remote deployment with gulp', command=deploy_gulp)
btn_sign_up.place(x=10, y=390)

btn_sign_up = tk.Button(window, text='Remote deployment without gulp', command=deploy)
btn_sign_up.place(x=250, y=390)

window.mainloop()