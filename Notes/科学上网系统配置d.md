### 1. 进入https://www.vultr.com/　注册

### 2. 充值10美元(微信和支付宝都可以,)

### 3.购买一台服务器

> 城市：可以自己选，东京、加拿大多伦多的ip容易被封，封了之后需要重新换服务器（换城市）
>
> 系统：ubuntu
>
> 规格：5刀/月，最低配置，注意是能够支持ipv4的, 这个价格和规格，其实非常适合3到5人拼团用

### 4.ssh 进入购买的服务器

```bash
ssh root@XXX.XXX.XXX.XXX   # 这里XXX代表你服务器的ip地址
```

> [Ubuntu 16.04下Shadowsocks服务器端安装及优化](https://www.polarxiong.com/archives/Ubuntu-16-04%E4%B8%8BShadowsocks%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%AB%AF%E5%AE%89%E8%A3%85%E5%8F%8A%E4%BC%98%E5%8C%96.html)

### 5.安装setuptools
```bash
apt install python3-pip
pip3 install --upgrade setuptools
pip3 install git+https://github.com/shadowsocks/shadowsocks.git@master
```

### 6. 新建一个文件 shadowsocks.json 并添加如下内容

> 这个用于自定义配置文件允许多用户使用
>
> 注意port_password里面是每个端口对应的密码,重要
>
> _comment里面是每个端口的备注，不重要

```
vim /etc/shadowsocks.json
{
    "server":"0.0.0.0",
    "server_ipv6":"[::]",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "timeout":300,
    "method":"aes-256-cfb",
    "port_password":
        {
            "80": "!t78Ttpb",
            "1001": "P!6j%3Dn",
            "1002": "5wOhq$Go",
            "1003": "UpGpHiN4",
            "1004": "9Jx9uDZr",
            "1005": "Nqq32Uqw",
            "1006": "KgTP&My5",
            "1007": "w#Sr7KWv",
            "1008": "lXKyc1d5",
            "1009": "OWUBu4%8"
        },
    "_comment":
        {
            "80": "commentof80",
            "1001": "commentof1001",
            "1002": "commentof1002",
            "1003": "commentof1003",
            "1004": "commentof1004",
            "1005": "commentof1005",
            "1006": "commentof1006",
            "1007": "commentof1007",
            "1008": "commentof1008",
            "1009": "commentof1009"
        },
    "protocol": "",
    "protocol_param": "",
    "obfs": "",
    "obfs_param": "",
    "redirect": "", 
    "dns_ipv6": false,
    "fast_open": false
} 
```

> [shadowsocks.json 配置文件各项说明](https://github.com/ssrarchive/shadowsocks-rss/wiki/config.json)

### 7.1  启动、关闭服务、

```bash
ssserver -c /etc/shadowsocks.json -d start   # 开启服务
ssserver -c /etc/shadowsocks.json -d restart # 重启服务
ssserver -c /etc/shadowsocks.json -d stop    # 停止服务
```

### 7.2 设置自动启动

```bash
sudo nano /etc/systemd/system/shadowsocks-server.service

[Unit]
Description=Shadowsocks Server
After=network.target

[Service]
ExecStart=/usr/local/bin/ssserver -c /etc/shadowsocks.json
Restart=on-abort

[Install]
WantedBy=multi-user.target
# Ctrl + O保存文件，Ctrl + X退出。

#启动Shadowsocks：
sudo systemctl start shadowsocks-server
#设置开机启动Shadowsocks：
sudo systemctl enable shadowsocks-server
```

### 8.1 查看日志

```bash
sudo tail -f /var/log/shadowsocks.log
```

### 9 防火墙

```bash
sudo vim /etc/firewalld/zones/public.xml
<?xml version="1.0" encoding="utf-8"?> <zone>
    <short>Public</short>
    <description>Shadowsocks port</description>
    <service name="dhcpv6-client"/>
    <service name="ssh"/>
    <port protocol="udp" port="80"/>
    <port protocol="tcp" port="80"/>
    <port protocol="udp" port="1001"/>
    <port protocol="tcp" port="1001"/>
    <port protocol="udp" port="1002"/>
    <port protocol="tcp" port="1002"/>
    <port protocol="udp" port="1003"/>
    <port protocol="tcp" port="1003"/>
    <port protocol="tcp" port="1004"/>
    <port protocol="udp" port="1004"/>
    <port protocol="tcp" port="1005"/>
    <port protocol="udp" port="1005"/>
    <port protocol="tcp" port="1006"/>
    <port protocol="udp" port="1006"/>
    <port protocol="tcp" port="1007"/>
    <port protocol="udp" port="1007"/>
    <port protocol="tcp" port="1008"/>
    <port protocol="udp" port="1008"/>
    <port protocol="tcp" port="1009"/>
    <port protocol="udp" port="1009"/>
</zone>
```

```bash
systemctl status firewalld.service # 状态
systemctl stop firewalld	# 停止防火墙
systemctl start firewalld	# 开启防火墙
```

### 10 客户端

> 以Ubuntu为例

```bash
sudo apt install shadowsocks
sslocal -c local.json
```

> local.json 是配置文件内容如下:

```
{
	"server": "xxx.xxx.xxx.xxx",
	"server_port": 1001, 
	"password": "Password",
	"method": "aes-256-cfb",
	"remarks": ""
}
```

> 注80端口不容易被封，用来救急用，平时不用，如果连80端口也被封了，可能需要换台服务器了