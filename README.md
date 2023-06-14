# 项目说明

pid监控程序，当指定pid结束时，发送邮件提醒，及下一步操作

## 使用说明

### 1. 配置文件

配置文件为`config.ini`，配置项说明如下：

```ini

[mail]
# 邮件服务器地址
server = smtp.163.com
# 邮件服务器端口
port = 25
# 发件人邮箱
sender =
# 发件人邮箱密码
password =
# 收件人邮箱
receiver =
# 邮件标题
subject = pid监控程序
# 邮件内容
content = pid监控程序
```