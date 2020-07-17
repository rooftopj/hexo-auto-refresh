## hexo-auto-refresh
![](https://img.shields.io/badge/python-3.8-orange)&nbsp;&nbsp;![](https://img.shields.io/badge/python-selenium-brightgreen)&nbsp;&nbsp;![](https://img.shields.io/badge/Node-%3E%3D8.1.0-orange)&nbsp;&nbsp;![](https://img.shields.io/badge/ChromeDriver-%3Dversion--Browser-red)<br>
![](https://img.shields.io/badge/release-v1.0.0-blue)&nbsp;&nbsp;![](https://img.shields.io/badge/license-MIT-green)<br>
hexo博客自动部署工具。每次部署，都要输入重复的指令，本着懒惰是第一生产力的原则，制作了hexo-auto-fresh这个小工具，简化我们对于hexo的一些操作。除一些基本功能外，还可自动刷新七牛云cdn目录缓存。

### 使用方法

将本项目 `clone` 至你的博客根目录下。

### 使用步骤

打开hexo-auto-refresh.exe文件。

![hexo-auto-refresh界面图](https://i.loli.net/2020/07/17/874ksSuhDQnE6RP.png)

- User name：你的七牛云账号。
- Password：你的七牛云账号所对应的密码。
- updateSite1：你要刷新的文件目录。注意最后需要一个 / 。
- updateSite2：你要刷新的文件目录。注意最后需要一个 / 。

以上四条个人信息在第一次使用时需要自己手动输入，运行`With CDN`下的功能后，会保存个人数据。往后每一次打开该工具，会自动导入上次输入的信息。

`Create post:`创建博文，文件名为newPost中的内容。

1. Without CDN，以下三个功能不会自动刷新七牛云CDN目录。

- `Local deployment:`本地部署。停止该服务时不要直接关闭对应的窗口，应按 crtl+C 退出。

- `Remote deploymen(gulp):`采用gulp插件压缩文件（需要先配置 gulp 插件），并部署至远端。

- `Remote deploymen:`不经压缩部署到远端（不使用gulp插件）。

2. With CDN，以下三个功能会自动刷新七牛云CDN目录。

- `Refresh CDN:`自动刷新七牛云cdn目录缓存。

- `Remote deployment(gulp, CDN):`采用gulp插件压缩文件（需要先配置 gulp 插件），部署至远端。并自动刷新七牛云cdn目录缓存。

- `Remote deployment(CDN):`不经压缩部署到远端（不使用gulp插件）。并自动刷新七牛云cdn目录缓存。