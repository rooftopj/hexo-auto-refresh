## hexo-auto-refresh
![](https://img.shields.io/badge/python-3.8-orange)&nbsp;&nbsp;![](https://img.shields.io/badge/python-selenium-brightgreen)&nbsp;&nbsp;![](https://img.shields.io/badge/Node-%3E%3D8.1.0-orange)&nbsp;&nbsp;![](https://img.shields.io/badge/ChromeDriver-%3Dversion--Browser-red)<br>
![](https://img.shields.io/badge/release-v1.0.0-blue)&nbsp;&nbsp;![](https://img.shields.io/badge/license-MIT-green)<br>
hexo博客自动部署工具。每次部署，都要输入重复的指令，本着懒惰是第一生产力的原则，制作了hexo-auto-fresh这个小工具，简化我们对于hexo的一些操作。除一些基本功能外，还可自动刷新七牛云cdn缓存。

### 使用方法

将本项目 `clone` 至你的博客根目录下。

### 使用步骤

打开hexo-auto-refresh.exe文件。

![hexo-auto-refresh界面图](https://i.loli.net/2020/07/15/OZYG5HFgpnExVqi.png)

- User name：你的七牛云账号。
- Password：你的七牛云账号所对应的密码。
- updateSite1：你要刷新的文件目录。注意最后需要一个 / 。
- updateSite2：你要刷新的文件目录。注意最后需要一个 / 。

以上四条个人信息在第一次使用时需要自己手动输入，往后每一次打开该工具，会自动导入上次输入的信息。

`Create post:`创建博文，文件名为newPost中的内容。

`Local deployment:`本地部署。停止该服务时不要直接关闭对应的窗口，应按 crtl+C 退出，否则会造成关闭失败使得下次本地部署时发现端口号已被占用，若发现该问题，应主动kill node.js 进程。

`Remote deployment with gulp:`压缩静态文件并部署到远端，需要先配置 gulp 插件。并自动刷新七牛云cdn文件缓存。中断该服务时不要直接关闭对应的窗口，应按 crtl+C 退出。

`Remote deployment without gulp:`不经压缩部署到远端（不使用gulp插件）。并自动刷新七牛云cdn文件缓存。中断该服务时不要直接关闭对应的窗口，应按 crtl+C 退出。
