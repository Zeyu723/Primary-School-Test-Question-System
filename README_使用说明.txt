📘 使用说明（交付文档）

✅ 项目简介：
该系统使用 Python Flask 制作，内嵌 Google 表单供不同年级学生答题，页面风格统一，可部署在学校网站或作为独立页面。

📁 项目结构：
- app.py：Flask 主程序
- templates/：每个年级+科目的页面模板（共8个）
- static/logo.png：可替换为学校 LOGO
- requirements.txt：依赖安装文件

🚀 启动方法（本地部署）：
1. 安装 Python 3.10+
2. 运行命令：
   pip install -r requirements.txt
   python app.py
3. 浏览器访问：
   http://127.0.0.1:5000/

🛠 如何替换 Google 表单链接：
- 打开 templates/ 文件夹
- 找到对应的页面（如 grade3_math.html）
- 修改 iframe 中的 src 链接，换成你自己的 Google 表单嵌入地址

📤 如何让老师修改题目：
- 用他们自己的 Gmail 登录 Google 表单
- 在你发的表单上点击“复制”
- 新建的表单链接发给你，用来替换 iframe 即可

如有其他需求可联系制作者继续支持
