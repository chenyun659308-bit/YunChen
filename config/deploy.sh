#!/bin/bash
# 久友电器 Django 后端部署脚本 (适用于 1Panel / Ubuntu / CentOS)
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "=== 久友电器后端部署 ==="
echo "项目目录: $PROJECT_DIR"

# 1. 进入后端目录
cd "$PROJECT_DIR"

# 2. 创建虚拟环境
if [ ! -d "venv" ]; then
    echo ">>> 创建 Python 虚拟环境..."
    python3 -m venv venv
fi
source venv/bin/activate

# 3. 安装依赖
echo ">>> 安装 Python 依赖..."
pip install -r requirements.txt

# 4. 复制环境配置
if [ ! -f ".env" ]; then
    echo ">>> 创建 .env 配置文件，请修改数据库信息..."
    cp .env.example .env
    echo "!!! 请编辑 .env 填写正确的数据库连接信息，然后重新运行此脚本"
    exit 1
fi

# 5. 数据库迁移
echo ">>> 执行数据库迁移..."
python manage.py migrate

# 6. 收集静态文件
echo ">>> 收集静态文件..."
python manage.py collectstatic --noinput

# 7. 启动 Gunicorn
echo ">>> 启动 Gunicorn 服务..."
echo "服务运行在 http://0.0.0.0:8000"
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4 --daemon

echo "=== 部署完成 ==="