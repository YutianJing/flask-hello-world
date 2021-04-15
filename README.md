1. Create a Linux VM on azure

   - VM name: YutianVM
     VM username: Yutian
     OS: Linux (ubuntu 18.04 LTS)
   - Settings -> Networking -> Inbound port rules
     Allow public inbound at port 22 (ssh), 80 (http), 443 (https)

   - ```
     ssh-keygen YutianVM_key
     ssh Yutian@13.72.106.225
     ```

   - ```
     # install nginx
     sudo apt-get update
     sudo apt-get install nginx
     ```

   - ```
     # install azure cli
     curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
     ```

2. Run a web service on port 80

3. Create a shell script to start/stop the web service and integrate it with OS startup/shutdown procedure

   - ```
     sudo systemctl start nginx
     ```

4. Create a Python micro-service application on port 8080

1） 通过该服务可以新建一个用户。

    要求：提交条件包含 first name 和 last name，返回 user id（可以随机生成，也可以是数据库id，取决于是否使用数据库来存储用户信息）。提交格式为 json，例如:
    {
     "first_name": "Jason",
     "last_name": "Obama"
    }
    
    返回格式为 json：
    {
     "status": "success",
     "result": {
      "id": "1"
     }
    }
    
    或错误:
    {
     "status": "failure",
     "result": {
      "reason": "User is existing."
     }
    }

2） 通过该服务访问这个用户的时候返回这个用户的问候语。

    要求：访问该用户（通过 user id），返回该用户的问候语。 提交格式为 json，例如：
    {
     "command": "greeting",
    }
    
    返回格式为 json，例如：
    {
     "status": "success",
     "result": {
      "user": {
       "id": "1",
       "first_name": "Jason",
       "last_name": "Obama"
      },
      "greeting": "Hello, World!"
     }
    }
    
    或失败：
    {
     "status": "failure",
     "result": {
      "reason": "User id 1 is not existing."
     }
    }

提示：
1） 用户可以存储在内存中，id 可以随机，id 类型可以是 integer 或 uuid
2） 微服务框架任选





```
cd /home/Yutian
git clone https://github.com/YutianJing/test
cd test

az login
az webapp up --sku B1 --name Yutian-test

{
  "URL": "http://yutian-flask-hello-world.azurewebsites.net",
  "appserviceplan": "yutian.jing_asp_Linux_centralus_0",
  "location": "centralus",
  "name": "Yutian-flask-hello-world",
  "os": "Linux",
  "resourcegroup": "yutian.jing_rg_Linux_centralus",
  "runtime_version": "python|3.7",
  "runtime_version_detected": "-",
  "sku": "BASIC",
  "src_path": "//home//Yutian//flask-hello-world"
}

# after changing app.py
az webapp up

az webapp config appsettings set --resource-group <group-name> --name <app-name> --settings WEBSITES_PORT=8080
```

Above not working since Azure App Service only expose port 80 and 443



Retry using WSGI server

```
gunicorn -b 127.0.0.1:8080 app:app

uwsgi --http :8080 --wsgi-file /home/Yutian/test/app.py --master --processes 4 --threads 2
uwsgi --http 127.0.0.1:8080 --module app:app

# working on localhost but not remote VM ip

sudo systemctl start nginx
```



```
# /etc/nginx/sites-enabled/default
server {
    listen 80;
    server_name 13.72.106.225;

    location /api/ {
       proxy_pass http://127.0.0.1:8080;
    }
}
```


```
# test on localhost using "rest clint" (vs code)
POST http://127.0.0.1:5000/users
content-type: application/json

{
     "first_name": "Jason",
     "last_name": "Obama"
}

###

GET http://127.0.0.1:5000/
```






