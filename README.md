```plaintext
flask_project/
│
├── app/                     # 应用程序目录
│   ├── __init__.py          # 应用初始化文件，包含Flask实例
│   ├── routes.py            # 路由定义文件
│   ├── models.py            # 数据库模型文件
│   ├── forms.py             # 表单定义文件
│   ├── templates/           # 模板目录（HTML文件）
│   │   ├── base.html        # 基础模板
│   │   └── index.html       # 首页模板
│   ├── static/              # 静态文件目录（CSS、JS、图片等）
│   │   ├── css/
│   │   └── js/
│   └── utils/               # 工具函数目录（可选）
│       └── helper.py        # 一些辅助函数
│
├── config.py                # 配置文件，定义不同环境的配置
├── run.py                   # 启动文件，用于运行Flask应用
├── requirements.txt         # 项目依赖文件，用于pip安装依赖
└── README.md                # 项目说明文件
```