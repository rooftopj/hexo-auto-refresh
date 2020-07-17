import tkinter as tk
from tkinter import messagebox  # import this to fix messagebox error
import pickle
import os
from selenium import webdriver
import time
import pickle


window = tk.Tk()
window.title('Welcome to rooftopj\'s hexo-auto-refresh')
window.geometry('476x470')

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

def CDNrefresh():
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)

            # 创建Chrome对象，已配置环境变量
            driver = webdriver.Chrome()     

            # 访问七牛云
            driver.get('https://sso.qiniu.com/')

            # 登录
            driver.find_element_by_id('email').send_keys(usrs_info['var_usr_name_input'])
            driver.find_element_by_id('password').send_keys(usrs_info['var_usr_pwd_input'])
            driver.find_element_by_id('login-button').click()

            # 确保刷新出来了，访问CDN
            driver.implicitly_wait(20)
            while len(driver.find_elements_by_class_name('sidebar-item')) < 3:
                time.sleep(0.2)
            driver.find_elements_by_class_name('sidebar-item')[3].click()

            # 访问刷新预取
            driver.implicitly_wait(20)
            driver.find_elements_by_class_name('sub-sidebar-link')[2].click()

            # 访问刷新目录
            driver.implicitly_wait(20)
            driver.find_elements_by_class_name('ant-tabs-tab')[2].click()
            driver.implicitly_wait(20)
            driver.find_elements_by_class_name('ant-tabs-tab')[1].click()

            # 输入目录
            driver.implicitly_wait(20)
            driver.find_elements_by_class_name('ant-input')[1].send_keys(usrs_info['var_update_site_input1'] + '\n' + usrs_info['var_update_site_input2'])

            # 提交
            driver.implicitly_wait(20)
            driver.find_elements_by_class_name('ant-btn')[1].click()
    except FileNotFoundError:
        print('请输入信息！')

def newPostFunction():
    newPost_command = 'cd .. && hexo n ' + newPost.get()
    os.system(newPost_command)

def local():
    local = 'cd .. && hexo clean && hexo s'
    os.system(local)

def deploy_gulp():
    deploy_gulp_cmd = 'cd .. && rd/s/q .deploy_git & hexo clean && hexo g && gulp && hexo d'
    os.system(deploy_gulp_cmd)

def deploy():
    deploy_cmd = 'cd .. && rd/s/q .deploy_git & hexo clean && hexo g && hexo d'
    os.system(deploy_cmd)


def refreshCDN():
    exist_usr_info={}
    exist_usr_info['var_usr_name_input']=var_usr_name.get()
    exist_usr_info['var_usr_pwd_input']=var_usr_pwd.get()
    exist_usr_info['var_update_site_input1']=update_site1.get()
    exist_usr_info['var_update_site_input2']=update_site2.get()
    with open('usrs_info.pickle', 'wb') as usr_file:
        pickle.dump(exist_usr_info, usr_file)
    CDNrefresh()

def deploy_cdn_gulp():
    exist_usr_info={}
    exist_usr_info['var_usr_name_input']=var_usr_name.get()
    exist_usr_info['var_usr_pwd_input']=var_usr_pwd.get()
    exist_usr_info['var_update_site_input1']=update_site1.get()
    exist_usr_info['var_update_site_input2']=update_site2.get()
    with open('usrs_info.pickle', 'wb') as usr_file:
        pickle.dump(exist_usr_info, usr_file)
    deploy_gulp()
    CDNrefresh()


def deploy_cdn():
    exist_usr_info={}
    exist_usr_info['var_usr_name_input']=var_usr_name.get()
    exist_usr_info['var_usr_pwd_input']=var_usr_pwd.get()
    exist_usr_info['var_update_site_input1']=update_site1.get()
    exist_usr_info['var_update_site_input2']=update_site2.get()
    with open('usrs_info.pickle', 'wb') as usr_file:
        pickle.dump(exist_usr_info, usr_file)
    deploy()
    CDNrefresh()

# button
btn_sign_up = tk.Button(window, text='Create post', command=newPostFunction)
btn_sign_up.place(x=260, y=300)

tk.Label(window, text='---------------------------------------Without CDN---------------------------------------').place(x=0, y= 335)

btn_sign_up = tk.Button(window, text='Local deployment', command=local)
btn_sign_up.place(x=5, y=360)

btn_sign_up = tk.Button(window, text='Remote deployment(gulp)', command=local)
btn_sign_up.place(x=140, y=360)

btn_sign_up = tk.Button(window, text='Remote deployment', command=deploy)
btn_sign_up.place(x=330, y=360)

tk.Label(window, text='-----------------------------------------With CDN-----------------------------------------').place(x=0, y= 405)

btn_sign_up = tk.Button(window, text='Refresh CDN', command=refreshCDN)
btn_sign_up.place(x=5, y=430)

btn_sign_up = tk.Button(window, text='Remote deployment(gulp, CDN)', command=deploy_cdn_gulp)
btn_sign_up.place(x=100, y=430)

btn_sign_up = tk.Button(window, text='Remote deployment(CDN)', command=deploy_cdn)
btn_sign_up.place(x=307, y=430)

window.mainloop()