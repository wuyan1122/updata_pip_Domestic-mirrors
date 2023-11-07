import PySimpleGUI  as sg
import re
import os
class CreateGui():
    
    def __init__(self):
        self.selects = {
            'Rx1' :   'https://pypi.tuna.tsinghua.edu.cn/simple/',           # 清华
            'Rx2' :   'https://mirrors.aliyun.com/pypi/simple/',             # 阿里
            'Rx3' :   'https://pypi.mirrors.ustc.edu.cn/simple/',            # 中科大
            'Rx4' :   'http://pypi.douban.com/simple/',                      # 豆瓣
            'Rx5' :   'http://mirrors.cloud.tencent.com/pypi/simple/',       # 腾讯
            'Rx6' :   'https://repo.huaweicloud.com/repository/pypi/simple', # 华为
            'Rx7' :   'https://mirrors.pku.edu.cn/pypi/web/simple/',         # 北大 
            'Rx8' :   'https://mirrors.hit.edu.cn/pypi/web/simple/',         # 哈工大
            'Rx9' :   'https://mirrors.neusoft.edu.cn/pypi/web/simple/'      # 大连东软
        }

        self.show_str ={
            'Rx1' :    '清华源',
            'Rx2' :    '阿里源',
            'Rx3' :    '中科大源',
            'Rx4' :    '豆瓣',
            'Rx5' :    '腾讯',
            'Rx6' :    '华为',
            'Rx7' :    '北大 ',
            'Rx8' :    '哈工大',
            'Rx9' :    '大连东软',
        }


    # 创建选选择源的一级ggui
    def create_select_gui(self):
         # 定义每个界面元素的样式
        sg.theme("DefaultNoMoreNagging")  
        one_layout = [[ 
            sg.Radio     ('清华'    , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx1'),
            sg.Radio     ('阿里'    , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx2'),
            sg.Radio     ('中科大'  , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx3'),
            sg.Radio     ('豆瓣'    , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx4'),
            sg.Radio     ('腾讯'    , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx5'),
            sg.Radio     ('华为'    , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx6'),
            sg.Radio     ('北大'    , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx7'),
            sg.Radio     ('哈工大'  , group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx8'),
            sg.Radio     ('大连东软', group_id =1,font=('Helvetica',12),enable_events=True, key=f'Rx9'), 
            sg.Button('确定',tooltip = '选择镜像源', button_color=('white', 'black'),size=5 ,key='select'  )  
        ]]
         # 够建一级页面
        window = sg.Window('Resizable Window', one_layout, resizable=True)
        while True:
            event, values = window.read(timeout=100)
            if event == 'Exit' or event == sg.WIN_CLOSED:
                window.close()
                break
            if event =='select':
                pip_url = next((key for key, val in values.items() if val == True), None) # 是否选择了源 
                if pip_url :
                      self.create_error_or_succeed_gui(pip_url)  
                else:
                     self.create_error_or_succeed_gui(pip_url)  

    # 创建错误or成功 gui界面
    def create_error_or_succeed_gui(self,radio_key):
        if  radio_key:
            trusted_host = re.search(r"//(.*?)/", self.selects[radio_key])  # 商品价格
            pip_ini = f'''[global]
timeout = 6000
index-url = {self.selects[radio_key]}
trusted-host = {trusted_host.group(1)}'''
            
            pip_path=f"{os.getenv('SystemDrive')}//Users//{os.environ['USERNAME']}//AppData//Roaming//pip" # 获取当前系统用户配置文件夹
            os.makedirs(pip_path,exist_ok='True')   # 创建存放pip.ini的文件夹 
            with open(pip_path+'//pip.ini','w+') as fp:  #	覆盖写入
                fp.write(pip_ini)

            ll3 = [
            [ sg.Text(f'pip源更新完成-->{self.show_str[radio_key]}镜像源', font=('Helvetica',13)), ],
            [ sg.Button('OK', button_color=('white', 'black'),size=3 ,key='-exit-'  )   ]
            ]

            win3 = sg.Window('Window 3', ll3,resizable=True)
            while True:
                ev2, vals2 = win3.read(timeout=100)
                if ev2 == sg.WIN_CLOSED or ev2 == '-exit-':  # 关闭三级gui
                    win3 .close()
                    break
        else:
            ll3 = [
            [ sg.Text(f'至少选择一个源', font=('Helvetica',13)), ],
            [ sg.Button('OK', button_color=('white', 'black'),size=3 ,key='-exit-'  )   ]
            ]

            win3 = sg.Window('Window 3', ll3,resizable=True)
            while True:
                ev2, vals2 = win3.read(timeout=100)
                if ev2 == sg.WIN_CLOSED or ev2 == '-exit-':  # 关闭三级gui
                    win3 .close()
                    break                







if __name__ == '__main__':

    CreateGui().create_select_gui()   























