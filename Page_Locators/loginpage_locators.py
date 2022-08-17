from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 元素定位
    """
    给所有的元素的定位都放在这个地方，进行统一调用
    """
    name_text = (By.XPATH, '//input[@class="el-input__inner" and @placeholder="用户名"]')  # 用户名输入框
    pwd_text = (By.XPATH, '//input[@class="el-input__inner" and @placeholder="密码"]')  # 密码输入框
    button_login = (
        By.XPATH, '//*[@id="app"]/div/div[10]/div/div/form/div[3]/div/button')  # 登录按钮
    # 密码为空提示框
    nopwd_button = (By.XPATH, '//*[@id="app"]/div/div[10]/div/div/form/div[2]/div/div[2]')
    # 用户名为空提示
    nouser_button = (By.XPATH, '//*[@id="app"]/div/div[10]/div/div/form/div[1]/div/div[2]')
    # 登录密码错误的提示框
    wrongpwd_button = (By.XPATH, '//div[@class="el-message el-message--error"]')

    """
    报道列表
    """
    # 内容管理下拉框
    nr_select = (By.XPATH, '//*[@id="app"]/section/aside/div/div/div/div[1]/div/ul/li[2]/div')
    # 进入报道列表页
    click_report = (By.XPATH, '//*[@id="app"]/section/aside/div/div/div/div[1]/div/ul/li[2]/ul/li[1]/span')
    # 新建报道按钮
    creat_report = (By.XPATH, '//button[@class="el-button el-button--primary el-button--default me-right2"]')

    """
    新增报道页面
    """
    # 打开作者下拉框
    writer = (By.XPATH, '//input[@class="el-input__inner" and @placeholder="作者"]')
    # 选择作者
    chose_writer = (By.XPATH, '//span[text()="食油人"]')
    # 标题输入框
    title_text = (By.XPATH, '//*[@id="app"]/section/section/main/div/div[1]/div/div/form/div[2]/div/div/input')
    # 内容输入框iframe
    content_iframe_text = (By.XPATH, '//div[@class="tox-sidebar-wrap"]//iframe')
    # 内容输入框文本
    content_text = (By.XPATH, '//body[@class="mce-content-body "]')
    # 点击行业领域下拉框
    field = (By.XPATH, '//input[@class="el-input__inner" and @placeholder="行业领域"]')
    # 选择行业领域
    chose_field = (By.XPATH, '//span[text()="合成生物学"]')
    # 发布按钮
    fabu_button = (By.XPATH, '//button[@class="el-button el-button--primary el-button--default"]')
