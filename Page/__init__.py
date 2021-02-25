from selenium.webdriver.common.by import By
#元素文件
#登录
login = [(By.ID,"tenantCode"),(By.ID,'username'),(By.ID,'password')]
#获取登录后的断言内容的元素
obtain_login = [(By.CSS_SELECTOR,".menu___1xeJi li"),(By.CSS_SELECTOR,"#errorspan")]
#登录页的登录文本
login_safe = (By.CSS_SELECTOR,"#bgImgBom .b_title")
#安全设置修改密码
safe_setting = [(By.CSS_SELECTOR,"[placeholder='原密码']"),(By.CSS_SELECTOR,"[placeholder='新密码']"),
          (By.CSS_SELECTOR,"[placeholder='确认新密码']"),(By.CSS_SELECTOR,"[type='submit']")]
#验证密码修改成功
text_checking = (By.CSS_SELECTOR,".userInfo___1LYfa span b")
#管理
management = (By.CSS_SELECTOR,'.menu___1xeJi li:nth-child(3)')
#管理中心
management_centre_el = (By.CSS_SELECTOR,'.link___1BNhq')
#点击管理后获取姓名
management_obtain = (By.CSS_SELECTOR,'.name___3USxA')
#获取组织数量
num_el = [(By.CSS_SELECTOR,'.down___18Q54 .item___2VSxG:nth-child(1) .count___39_OH'),
          (By.CSS_SELECTOR,'.down___18Q54 .item___2VSxG:nth-child(2) .count___39_OH')]
#点击头像
head_portrait = (By.CSS_SELECTOR,'.profile___1KV7B img')
setting = [(By.CSS_SELECTOR,"[href='/setting/personal']"),(By.CSS_SELECTOR,"[href='/setting/security']"),
                    (By.CSS_SELECTOR,"[href='/mypermission']"),(By.CSS_SELECTOR,"[role='menu'] li:nth-child(5)")]
personal_setting = [(By.CSS_SELECTOR,'.footer___YtN64 button.ant-btn-primary'),(By.CSS_SELECTOR,'.ant-message-custom-content span')]
logout_define = (By.CSS_SELECTOR,'.ant-modal-footer .ant-btn-primary')
#点击我的权限后获取文本
my_authority_obtain = (By.CSS_SELECTOR,".tabs___arsVC [role='tab']:nth-child(1)")
#点击消息
view_news = [(By.CSS_SELECTOR,'.ant-badge span'),(By.CSS_SELECTOR,".overlayContainer___1DTHV [role='tab']")]
#点击帮助
help =  [(By.CSS_SELECTOR,'.dropdown___1ZzvZ'),(By.CSS_SELECTOR,"a[download='']")]
#创建组织输入框
create_send = [(By.ID,'orgmodal_orgname'),(By.ID,'orgmodal_orgcode'),(By.ID,'orgmodal_remark')]
#创建组织确定按钮
org_define = (By.CSS_SELECTOR,'.ant-modal-footer div button:nth-child(2)')
#更新组织按钮
update_org = (By.CSS_SELECTOR,'[data-row-key="werr"]  span a:nth-child(1)')
#更新组织名称输入框
update_org_send = (By.ID,'orgmodal_orgname')
#删除组织
delete_org = [(By.CSS_SELECTOR,'[data-row-key="werr"] span a:nth-child(3)'),(By.CSS_SELECTOR,"[data-row-key='qqq'] span a:nth-child(3)")
    ,(By.CSS_SELECTOR,'.ant-modal-confirm-btns button:nth-child(2)')]
#获取新增组织的组织名称
obtain_org = [(By.CSS_SELECTOR,".ant-message-success span"),(By.CSS_SELECTOR,".ant-form-explain"),
              (By.CSS_SELECTOR,".ant-form-explain"),(By.CSS_SELECTOR,".ant-form-explain")]
#获取修改后的组织名称
obtain_org02 = (By.CSS_SELECTOR,"[title='组织0101']")
#获取删除组织后弹框信息
obtain_org03 = [(By.CSS_SELECTOR,".ant-message-success span"),(By.CSS_SELECTOR,".ant-message-error span")]
#点击人员数量
number_personnel = [(By.CSS_SELECTOR,"[data-row-key='qqq'] td:nth-child(2) a"),(By.CSS_SELECTOR,".title___2_88l")]
#点击单位tab
company = (By.CSS_SELECTOR,'.tabs____iMBm span:nth-child(2)')
#创建单位
create_com_click = (By.CSS_SELECTOR,'.operation___1HLO8 .ant-btn-primary')
create_com_send = [(By.CSS_SELECTOR,'.ant-modal-body #name'),(By.ID,'shortName'),(By.ID,'desc')]
#创建单位确定按钮
com_define = (By.CSS_SELECTOR,'.ant-modal-footer div button:nth-child(2)')
#编辑单位
update_com_send = (By.CSS_SELECTOR,'.ant-modal-body #name')
#删除单位
delete_com  = (By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary")
#获取新增单位的单位名称
obtain_com = [(By.CSS_SELECTOR,"[title='单位01']"),(By.CSS_SELECTOR,".ant-message-error span"),(By.CSS_SELECTOR,'div.ant-form-explain')]
#修改单位名称
update_com = (By.CSS_SELECTOR,".ant-table-tbody a:nth-child(1)")
#获取修改后的单位名称
obtain_com02 = (By.CSS_SELECTOR,"[title='阿里巴巴']")
#获取删除单位后弹框信息
obtain_com03 = [(By.CSS_SELECTOR,".ant-message-custom-content span"),(By.CSS_SELECTOR,".ant-message-error span")]
#搜索功能验证
search_com = [(By.CSS_SELECTOR,"[placeholder='请输入']"),(By.CSS_SELECTOR,".btnsWrapper___M2BE1 .ant-btn-primary"),(By.CSS_SELECTOR,"[title='单位02xasas']")]
#验证重置功能
reset_com = [(By.CSS_SELECTOR,"[placeholder='请输入']"),(By.CSS_SELECTOR,".resetBtn___5FRYQ")]
#创建人员按钮
create_per_el = (By.CSS_SELECTOR,".operation___1HLO8 button:nth-child(1)")
#创建人员页面shur
per_send_el = [(By.CSS_SELECTOR,'#userName'),(By.CSS_SELECTOR,'#accountName'),(By.CSS_SELECTOR,'#email'),(By.CSS_SELECTOR,'#mobileNo')]
per_click_el = [(By.CSS_SELECTOR,'#companyId'),(By.XPATH,"//ul/li[contains(text(),'单位02xasas')]"),
                 (By.CSS_SELECTOR,"[aria-disabled='false']"),(By.CSS_SELECTOR,"[data-icon='caret-down']"),(By.CSS_SELECTOR,"[role='group'] li span span"),
                (By.CSS_SELECTOR,'.ant-select-selection--multiple'),(By.XPATH,"//ul/li[contains(text(),'租户管理员')]"),
                (By.XPATH,"//ul/li[contains(text(),'普通用户')]")]
per_define_el = (By.CSS_SELECTOR,'.footer___1Ykjp .ant-btn-primary')
per_define1_el = (By.CSS_SELECTOR,'.footer___FeeIm .ant-btn-primary')
#创建人员返回箭头点击
per_fallback_el = (By.CSS_SELECTOR,'.iconback')
#验证下拉框数据正确性
per_select_el = [(By.CSS_SELECTOR,"[role='option']"),(By.CSS_SELECTOR,'.ant-select-tree-title')]
#获取新增人员的人员姓名
per_obtain_el = [(By.CSS_SELECTOR,"[title='人员04'] a"),(By.XPATH,'//*[@id="root"]/section/main/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/div/div'),
                 (By.CSS_SELECTOR,'.ant-message-custom-content span')]
#修改人员信息
per_update_el = (By.CSS_SELECTOR,"[title='test修改功能'] a")
#人员页面的操作按钮
per_opers_el = (By.CSS_SELECTOR,"[data-row-key='13455'] button span")
#停用操作确定按钮
stop_define_el = (By.CSS_SELECTOR,'.ant-modal-footer .ant-btn-primary')
#登录解锁确定按钮
resetpassword_define_el = [(By.CSS_SELECTOR,'.ant-popover-buttons .ant-btn-primary'),(By.CSS_SELECTOR,'.ant-message-success span')]
#搜索点击启用操作，点击搜索
start_per_el = [(By.CSS_SELECTOR,'#status'),(By.XPATH,"//ul/li[contains(text(),'停用')]"),
                (By.CSS_SELECTOR,'.btnsWrapper___M2BE1 button.ant-btn-primary')]
#启用操作确定按钮
start_define_el = (By.CSS_SELECTOR,'.ant-modal-footer .ant-btn-primary')
#验证人员管理页面的搜索功能/[title='yuedantestadmin']
search_per_el = [(By.CSS_SELECTOR,'#status'),(By.XPATH,"//ul/li[contains(text(),'正常')]"),(By.CSS_SELECTOR,'#userId'),
                 (By.CSS_SELECTOR,'.btnsWrapper___M2BE1 button.ant-btn-primary'),(By.CSS_SELECTOR,"[title='yuedantestadmin']")]
#验证查看导入结果按钮
results_per_el = [(By.CSS_SELECTOR,'.operation___1HLO8 button:nth-child(4)'),(By.CSS_SELECTOR,'.title___2_88l a'),
                 (By.CSS_SELECTOR,'.title___2_88l')]
#查看人员详情
details_per_el = [(By.CSS_SELECTOR,"[title='乐丹'] a"),(By.CSS_SELECTOR,'.tabs____iMBm .active___phwF4'),
                  (By.CSS_SELECTOR,'.title___2_88l span')]
#人员详情页编辑信息
details_edit_el = [(By.CSS_SELECTOR,'.operation___1HLO8 .ant-btn-primary'),(By.CSS_SELECTOR,'.footer___FeeIm .ant-btn-primary'),
                 (By.CSS_SELECTOR,'.tabs____iMBm .active___phwF4'), (By.CSS_SELECTOR,"[title='test修改功能'] a")]

#人员详情页修改人员状态
details_status_el = [(By.CSS_SELECTOR,'.operation___1HLO8 button:nth-child(2)'),(By.CSS_SELECTOR,'.ant-modal-footer .ant-btn-primary')]
#查看日志数量
details_log_el = [(By.CSS_SELECTOR,'.tabs____iMBm span:nth-child(2)'),(By.CSS_SELECTOR,'.total___3ssc9 span:nth-child(1)')]
#重置密码
details_resetpassword_el = [(By.CSS_SELECTOR,'.operation___1HLO8 button:nth-child(3)'),(By.CSS_SELECTOR,'.ant-modal-footer .ant-btn-primary'),
                            (By.CSS_SELECTOR,'.ant-message-success span'),
                            (By.CSS_SELECTOR,"[title='test修改功能'] a")]
#重置密码登录验证
text_checking_el = (By.CSS_SELECTOR,".ant-form-horizontal h3")
#初始密码修改
initial_password_el = [(By.CSS_SELECTOR,"[placeholder='新密码']"),(By.CSS_SELECTOR,"[placeholder='确认新密码']"),
                       (By.CSS_SELECTOR,".ant-btn-primary"),(By.CSS_SELECTOR,"#bgImgBom .b_title")]
#修改组织
btch_org_el =  [(By.CSS_SELECTOR,"[data-row-key='13455'] [type='checkbox']"),(By.CSS_SELECTOR,''),
                (By.CSS_SELECTOR,''),(By.CSS_SELECTOR,'')]
#创建功能角色
create_role_el = (By.CSS_SELECTOR,'.operation___1HLO8 .ant-btn-primary')
role_send_el = [(By.CSS_SELECTOR,'.ant-modal-body #name'),(By.CSS_SELECTOR,'.ant-modal-body #code'),
                (By.CSS_SELECTOR,"#privList [role='combobox']"),(By.CSS_SELECTOR,"[role='listbox'] [role='option']:nth-child(8)"),
                (By.CSS_SELECTOR,'#rcDialogTitle2'),(By.CSS_SELECTOR,"[placeholder='请输入角色描述']"),
                (By.CSS_SELECTOR,'.ant-modal-footer .ant-btn-primary')]

#获取创建功能角色后的提示信息
obtain_pri_el = [(By.CSS_SELECTOR,"[title='功能角色01'] a"),(By.CSS_SELECTOR,'.ant-message-error span'),
                (By.CSS_SELECTOR,".ant-form-explain"),(By.CSS_SELECTOR,".ant-form-explain")]

#修改角色
pri_update_el = [(By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(1) td:nth-child(6) a:nth-child(1)"),
                 (By.CSS_SELECTOR,'.ant-modal-content #name'),
                (By.CSS_SELECTOR,"[title='功能角色02'] a")]

#查询角色
search_role_el = [(By.CSS_SELECTOR,"[placeholder='请输入角色名称']"),(By.CSS_SELECTOR,".ant-form-item-children .ant-btn-primary"),
                  (By.CSS_SELECTOR,"[title='普通用户'] a"),(By.CSS_SELECTOR,".ant-form-horizontal button:nth-child(2)")]

#添加人员
add_people_el = [(By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(1) a:nth-child(5)"),
                 (By.CSS_SELECTOR,".ant-select-selection__placeholder"),
                 (By.XPATH,"//ul/li[contains(text(),'人员04')]"),
                 (By.CSS_SELECTOR,".ant-modal-title"), (By.CSS_SELECTOR,"[title='第一个组织']"),
                 (By.CSS_SELECTOR,".contentContainer___dD3jy .ant-tree-icon-hide.ant-tree:nth-child(3) li:nth-child(1) span:nth-child(2) span"),
                 (By.CSS_SELECTOR,".contentContainer___dD3jy .ant-tree-icon-hide.ant-tree:nth-child(3) li:nth-child(6) span:nth-child(2) span"),
                 (By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                 (By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(1) td:nth-child(3) a"),
                 (By.CSS_SELECTOR,".contentLeft___30H76 [focusable='false']")]

#人员详情页面批量移除人员
details_delete_el = [(By.CSS_SELECTOR,".container___3VQKy .ant-checkbox-inner"),(By.CSS_SELECTOR,"[data-row-key='13455'] .ant-checkbox-inner"),
                     (By.CSS_SELECTOR,".container___3VQKy button:nth-child(2)"),(By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                     (By.CSS_SELECTOR,".ant-message-success span")]

#人员详情页面搜索人员
details_search_el = [(By.CSS_SELECTOR,"#name"),(By.CSS_SELECTOR,"#accountName"),
                     (By.CSS_SELECTOR,".ant-form-item-children .ant-btn-primary"), (By.CSS_SELECTOR,"[title='人员04']"),
                     (By.CSS_SELECTOR,".ant-form-item-children button:nth-child(2)"),(By.CSS_SELECTOR,".icon___24c46")]

#点击角色详情
role_details_el = [(By.CSS_SELECTOR,"[title='功能角色02'] a"),(By.CSS_SELECTOR,".body___cA1b4 div:nth-child(4)"),
                   (By.CSS_SELECTOR,'.iconback')]

#移除人员
remove_people_el = [(By.CSS_SELECTOR,'.ant-table-tbody .ant-table-row:nth-child(1) a:nth-child(7)'),
                    (By.CSS_SELECTOR,".ant-modal-body [unselectable='on']"),(By.XPATH,"//ul/li[contains(text(),'test修改功能')]"),
                    (By.CSS_SELECTOR,"[placeholder='请输入移除原因']"),(By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                    (By.CSS_SELECTOR,".ant-message-success span")]
#删除角色（不存在人员）
delete_role01_el = [(By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(1) a:nth-child(3)"),
                  (By.CSS_SELECTOR,".ant-modal-confirm-btns .ant-btn-primary"),
                  (By.CSS_SELECTOR,".ant-message-success span")]


#删除角色（存在人员）
delete_role02_el = [(By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(2) a:nth-child(3)"),
                  (By.CSS_SELECTOR,".ant-modal-confirm-btns .ant-btn-primary"),
                  (By.CSS_SELECTOR,".ant-message-error span")]


#移除admin账号
remove_admin_el = [(By.CSS_SELECTOR,"[data-row-key='817'] span a:nth-child(7)"),
                    (By.CSS_SELECTOR,".ant-modal-body [unselectable='on']"),(By.XPATH,"//ul/li[contains(text(),'乐丹')]"),
                    (By.CSS_SELECTOR,"[placeholder='请输入移除原因']"),(By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                    (By.CSS_SELECTOR,".ant-message-error span")]

#批量删除角色
delete_roles_el = [(By.CSS_SELECTOR,".container___3VQKy .ant-checkbox-inner"),
                  (By.CSS_SELECTOR,".container___3VQKy .ant-btn:nth-child(2)"),
                   (By.CSS_SELECTOR,".ant-modal-confirm-btns .ant-btn-primary"),
                  (By.CSS_SELECTOR,".ant-message-error span")]

#验证功能角色添加的人员，对应人员人员权限显示正确
checking_el = [(By.CSS_SELECTOR,".menu___1vDQf li"),(By.CSS_SELECTOR,".iconmenu")]

#点击数据权限tab
data_authority_el = (By.CSS_SELECTOR,".tabs____iMBm span:nth-child(2)")

#添加数据权限
add_authority_el = [(By.CSS_SELECTOR,"[data-row-key='846'] span a:nth-child(1)"),(By.CSS_SELECTOR,".selectContainer___3Uf04 .ant-select"),
                    (By.XPATH,"//ul/li[contains(text(),'人员04')]"),(By.CSS_SELECTOR,"[title='第一个组织']"),
                    (By.CSS_SELECTOR,".contentContainer___dD3jy .ant-tree-icon-hide.ant-tree:nth-child(3) li:nth-child(3) span:nth-child(2) span"),
                    (By.CSS_SELECTOR,".contentContainer___dD3jy .ant-tree-icon-hide.ant-tree:nth-child(3) li:nth-child(6) span:nth-child(2) span"),
                    (By.CSS_SELECTOR,".ant-modal-content .ant-btn-primary"),(By.CSS_SELECTOR,"[data-row-key='846'] td:nth-child(4) a")]

#成员列表添加人员
details_add_el = [(By.CSS_SELECTOR,".operation___1HLO8 .ant-btn-primary"),(By.CSS_SELECTOR,".selectContainer___3Uf04 .ant-select"),
                  (By.XPATH,"//ul/li[contains(text(),'test修改功能')]"),(By.CSS_SELECTOR,".ant-modal-content .ant-btn-primary"),
                  (By.CSS_SELECTOR,"[title='test修改功能']")]
#成员列表验证搜索
details_search_aut_el = [(By.CSS_SELECTOR,"#name"),(By.CSS_SELECTOR,"#accountName"),
                         (By.CSS_SELECTOR,".ant-form-item-children .ant-btn-primary"),(By.CSS_SELECTOR,"[title='人员04']"),
                         (By.CSS_SELECTOR,".ant-form-item-children .ant-btn:nth-child(2)")]

#成员列表批量移除
details_removes_el = [(By.CSS_SELECTOR,".ant-table-tbody tr:nth-child(1) td:nth-child(1) span:nth-child(2)"),
                      (By.CSS_SELECTOR,".ant-table-tbody tr:nth-child(2) td:nth-child(1) span:nth-child(2)"),
                      (By.CSS_SELECTOR,".ant-table-tbody tr:nth-child(3) td:nth-child(1) span:nth-child(2)"),
                      (By.CSS_SELECTOR,".container___3VQKy button:nth-child(2)"),(By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                      (By.CSS_SELECTOR,".ant-list-items .ant-list-item:nth-child(1) ul i"),(By.CSS_SELECTOR,".total___3ssc9 span:nth-child(1)")]

#成员列表修改角色
details_modify_role_el = [(By.CSS_SELECTOR,".ant-table-tbody tr:nth-child(1) td:nth-child(1) span:nth-child(2)"),
                          (By.CSS_SELECTOR,".container___3VQKy button:nth-child(3)"),(By.CSS_SELECTOR,".ant-modal-body .ant-select-selection__rendered"),
                          (By.XPATH,"//ul/li[contains(text(),'开发者')]"),(By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                          (By.CSS_SELECTOR,".total___3ssc9 span:nth-child(1)"), (By.CSS_SELECTOR,".iconback")]
#批量授权
add_authoritys_el = [(By.CSS_SELECTOR,".selectBox___2kNY5 .ant-btn-primary"), (By.CSS_SELECTOR,"#roleId .ant-select-selection__placeholder"),
                     (By.XPATH,"//ul/li[contains(text(),'管理员')]"), (By.CSS_SELECTOR,".ant-select-search__field__placeholder"),
                     (By.CSS_SELECTOR,".ant-select-tree-checkbox-inner"), (By.CSS_SELECTOR,".selectContainer___3Uf04 .ant-select"),
                     (By.XPATH,"//ul/li[contains(text(),'人员04')]"),(By.CSS_SELECTOR,".ant-modal-content .ant-btn-primary"),
                     (By.CSS_SELECTOR,"[data-row-key='846'] td:nth-child(4) a")]

#移除人员  test修改功能
remove_authority_el = [(By.CSS_SELECTOR,"[data-row-key='846'] span a:nth-child(3)"),(By.CSS_SELECTOR,".ant-select-selection__placeholder"),
                       (By.XPATH,"//ul/li[contains(text(),'test修改功能')]"),(By.XPATH,"//ul/li[contains(text(),'人员04')]"),
                       (By.CSS_SELECTOR,"[title='test修改功能'] .anticon"),(By.CSS_SELECTOR,"[placeholder='请输入移除原因']"),
                       (By.CSS_SELECTOR, ".ant-modal-footer .ant-btn-primary"),(By.CSS_SELECTOR, "[data-row-key='846'] td:nth-child(4) a"),
                       (By.XPATH,"//ul/li[contains(text(),'乐丹')]"),(By.CSS_SELECTOR,"[title='乐丹'] .anticon")]

#移除系统的唯一管理员
remove_only_el = [(By.CSS_SELECTOR,"[data-row-key='846'] span a:nth-child(3)"),(By.CSS_SELECTOR,".ant-select-selection__placeholder"),
                  (By.XPATH,"//ul/li[contains(text(),'乐丹')]"),(By.CSS_SELECTOR,"[placeholder='请输入移除原因']"),
                  (By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),(By.CSS_SELECTOR,".ant-message-error span")]


#创建公告栏目
create_column_el = [(By.CSS_SELECTOR,".operation___1HLO8 button:nth-child(2)"),(By.CSS_SELECTOR,".ant-drawer-body .ant-btn-primary"),
                    (By.CSS_SELECTOR,"#columnName"),(By.CSS_SELECTOR,"#isActive"),
                    (By.CSS_SELECTOR,"#remark"),(By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                    (By.CSS_SELECTOR,".ant-drawer-body .ant-table-tbody tr:nth-child(1) td:nth-child(1)")]

#创建公告栏目异常获取
create_column_unusual_el = [(By.CSS_SELECTOR,".ant-message-error span"),(By.CSS_SELECTOR,".ant-form-explain")]

#修改公告
update_column_el = [(By.CSS_SELECTOR,".ant-drawer-body .ant-table-tbody tr:nth-child(1) td:nth-child(6) a:nth-child(1)"),
                    (By.CSS_SELECTOR,"#columnName"),(By.CSS_SELECTOR,"#isActive"),(By.CSS_SELECTOR,"#remark"),
                    (By.CSS_SELECTOR, ".ant-modal-footer .ant-btn-primary"),
                    (By.CSS_SELECTOR, ".ant-drawer-body .ant-table-tbody tr:nth-child(1) td:nth-child(1)")]
#启用分类
start_using_el = [(By.CSS_SELECTOR,".ant-drawer-body .ant-table-tbody tr:nth-child(1) td:nth-child(6) a:nth-child(1)"),
                  (By.CSS_SELECTOR,".ant-modal-confirm-btns .ant-btn-primary")]

#删除栏目
delete_column_el = [(By.CSS_SELECTOR,".ant-drawer-body .ant-table-tbody tr:nth-child(1) td:nth-child(6) a:nth-child(3)"),
                    (By.CSS_SELECTOR,".ant-modal-confirm-btns .ant-btn-primary"),(By.CSS_SELECTOR,".titleWrapper___10H-X span")]


#创建公告
create_notice_el = [(By.CSS_SELECTOR,".operation___1HLO8 .ant-btn-primary"),(By.CSS_SELECTOR,"[placeholder='请输入标题']"),
                    (By.CSS_SELECTOR,".DraftEditor-root .DraftEditor-editorContainer"),(By.CSS_SELECTOR,"[role='combobox']"),
                    (By.XPATH,"//ul/li[contains(text(),'分类01')]"),(By.CSS_SELECTOR,"#noticeTargets"),
                    (By.CSS_SELECTOR,"[role='group'] li:nth-child(2) span.ant-tree-checkbox:nth-child(2) span"),
                    (By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),(By.CSS_SELECTOR,"[role='switch']"),
                    (By.CSS_SELECTOR,".footer___1ivCr .ant-btn-primary"),[By.CSS_SELECTOR,".current.ant-scroll-number-only-unit"]]


#编辑并发送公告
edit_send_el = [(By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(1) td:nth-child(9) .ant-btn-link:nth-child(1) span"),
                (By.CSS_SELECTOR,"[placeholder='请输入标题']"),
                (By.CSS_SELECTOR,"[role='switch']"),(By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),
                (By.CSS_SELECTOR,".ant-modal-content [focusable='false']")]
#撤回公告
recall_notice_el = [(By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(1) td:nth-child(9) .ant-btn-link:nth-child(5) span"),
                    (By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),(By.CSS_SELECTOR,".ant-message-success span")]
#删除公告
delete_notice_el = [(By.CSS_SELECTOR,".ant-table-tbody .ant-table-row:nth-child(1) td:nth-child(9) .ant-btn-link:nth-child(3) span"),
                    (By.CSS_SELECTOR,".ant-modal-footer .ant-btn-primary"),(By.CSS_SELECTOR,".ant-message-success span")]