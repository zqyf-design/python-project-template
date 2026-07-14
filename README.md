# Python Project Template

一个基于 Python 的项目模板，包含完整的项目结构和最佳实践。

## 功能特性

- ✅ 模块化代码结构
- ✅ 配置管理
- ✅ 日志系统
- ✅ 单元测试
- ✅ 代码格式化

## 技术栈

- Python 3.10+
- pytest (测试)
- python-dotenv (配置)
- logging (日志)

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行项目

```bash
python src/main.py
```

### 运行测试

```bash
pytest tests/ -v
```

## 项目结构

```
.
├── src/                    # 源代码目录
│   ├── __init__.py
│   ├── main.py             # 入口文件
│   ├── config.py           # 配置管理
│   ├── logger.py           # 日志配置
│   └── utils.py            # 工具函数
├── tests/                  # 测试目录
│   ├── __init__.py
│   └── test_utils.py       # 单元测试
├── .env.example            # 环境变量示例
├── .gitignore              # Git 忽略文件
├── requirements.txt        # 依赖列表
└── README.md               # 项目文档
```

## 许可证

MIT License