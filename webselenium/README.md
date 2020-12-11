# UI自动化
## 文件夹各功能

+-- UITest  
|+-- config 配置文件  
|+-- devops CI集成相关  
|+-- framework 页面基类，浏览器的选择  
|+-- logs 日志文件  
|+-- utils 工具方法  
|+-- pageobjects 页面对象，存放页面中的的动作函数  
|+-- screenshots 报错后的页面截图       **#需要自己手动新建**  
|+-- scripts  
|+-- test_reports 测试报告      **#需要自己手动新建**  
|+-- testsuites 测试用例，运行TestRunner则全部执行用例      **#文件名以test开头**  
|+-- tools 第三方工具       **#需要自己手动新建**  
||+-- drivers 各浏览器驱动      **#需要自己手动新建**  

### 安装依赖

chromedriver 对应地址和下载
https://chromedriver.chromium.org/downloads

需要手动把driver下载到tools/driver目录下。（后面会改成用shell脚本完成）

```
$ sh scripts/download_drivers.sh
```

### 运行测试

```
cd ./selenium
python -m testsuites.TestRunner
```
