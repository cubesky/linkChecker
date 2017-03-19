# Hexo-Material-Theme 友链检测后端
利用 Github Pages 和 Travis CI 运行的友链存活检查后端

# 如何使用
1. 先 fork 这个仓库  
2. 进入 Github 的 `Setting` ，选择左侧的 `Personal Access Token` ，勾选 `repo` 创建
3. 到 TravisCI 中开启这个仓库的自动构建，然后设置这个项目，`Environment Variables` 中设置 `GITHUB_TOKEN` 值为你刚刚创建的 `Token`
4. 自己修改 `main.py` 中的网址为自己域名友链页的地址  
5. 正常的话这会让 TravisCI 进行首次构建  
6. 将 `linkChecker.js` 复制到你的博客中，并修改 `linkChecker.js` 中的网址为自己 Github Pages 的地址
7. 想办法让这个脚本在友链页加载
8. 确认无误后，到 TravisCI 的项目设置页添加 `Cron Jobs` ，分支为 `master` ，时间为 `daily` ，并选择 `Always Run`

Enjoy!