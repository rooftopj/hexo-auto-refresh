from selenium import webdriver
import time
import pickle


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

