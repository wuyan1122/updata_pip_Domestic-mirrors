
import os



qh=['https://pypi.tuna.tsinghua.edu.cn/simple','pypi.tuna.tsinghua.edu.cn','清华大学']   # 清华源
al=['https://mirrors.aliyun.com/pypi/simple/','mirrors.aliyun.com','阿里']           # 阿里源
zkd= ['https://pypi.mirrors.ustc.edu.cn/simple/','pypi.mirrors.ustc.edu.cn','中国科技大学' ] # 中科大源
hzlgf=['http://pypi.hustunique.com/','pypi.hustunique.com','华中理工大学']     # 华中理工
sdlg=['http://pypi.sdutlinux.org/','pypi.sdutlinux.org','山东理工大学']        #山东理工
dp=['http://pypi.douban.com/simple/','pypi.douban.com','豆瓣']         # 豆瓣


yum_yuan='''下载源:
   1 清华：https://pypi.tuna.tsinghua.edu.cn/simple
   2 阿里云：https://mirrors.aliyun.com/pypi/simple/
   3 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
   4 华中理工大学：http://pypi.hustunique.com/
   5 山东理工大学：http://pypi.sdutlinux.org/
   6 豆瓣：http://pypi.douban.com/simple/
    '''

yum_yuan_dict={
    '1':qh,
    '2':al,
    '3':zkd,
    '4':hzlgf,
    '5':sdlg,
    '6':dp
}


def create_pip_yum():
    print(yum_yuan)
    input_num = input('请输入要选择的源:')

    pip_ini = f'''
    [global]
    timeout = 6000
    index-url = {yum_yuan_dict.get(input_num)[0]}
    trusted-host = {yum_yuan_dict.get(input_num)[1]}
    '''

    pip_path=f"{os.getenv('SystemDrive')}//Users//{os.environ['USERNAME']}//AppData//Roaming//pip" # 获取当前系统用户配置文件夹
    isexists= os.path.exists(pip_path)
    print(isexists)
    if not isexists:
        os.mkdir(pip_path)
        with open(pip_path+'//pip.ini','w+') as fp:  #	覆盖写入
            fp.write(pip_ini)

        print(f'pip_yum源更新完成-->{yum_yuan_dict.get(input_num)[2]}源')
        fp.close()
    else: 
        with open(pip_path+'//pip.ini','w+') as fp:  #	覆盖写入
            fp.write(pip_ini)

    input("please input any key to exit!")
if __name__ == '__main__':
    create_pip_yum()