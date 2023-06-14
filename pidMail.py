import argparse
import time
import zmail


USERNAME = ""
PASSWORD = ""
SERVER = "smtp.qq.com"
PORT = 465
SMTP_SSL = True
SMTP_TLS = False


# pid监控程序，当指定pid结束时，发送邮件提醒，及下一步操作

def pidMail(pid, mail, title, content):
    # pid: 要监控的pid
    # mail: 要发送的邮箱
    # title: 邮件标题
    # content: 邮件内容
    if pid is None:
        print("pid is None")
        return
    if mail is None:
        print("mail is None")
        return
    if title is None:
        print("title is None")
        return
    if content is None:
        print("content is None")
        return
    while True:
        if pid is None:
            print("pid is None")
            return
        if mail is None:
            print("mail is None")
            return
        if title is None:
            print("title is None")
            return
        if content is None:
            print("content is None")
            return
        try:
            with open("/proc/" + str(pid) + "/status") as _:
                time.sleep(1)
                pass
        except Exception as e:
            print("pid is over")
            print(e)
            # 发送邮件
            try:
                server = zmail.server(username=USERNAME,
                                      password=PASSWORD,
                                      smtp_host=SERVER,
                                      smtp_port=PORT,
                                      smtp_ssl=SMTP_SSL,
                                      smtp_tls=SMTP_TLS)
                server.send_mail(
                    mail, {
                        "subject": title, "content_text": content
                    })
            except Exception as e:
                print(e)
            return


if __name__ == "main":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("-p", "--pid", help="pid", type=int)
    argparse.add_argument("-m", "--mail", help="mail", type=str)
    argparse.add_argument("-t", "--title", help="title", type=str)
    argparse.add_argument("-c", "--content", help="content", type=str)
    args = argparse.parse_args()
