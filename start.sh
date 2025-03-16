#!/bin/bash

# 检查是否安装了Docker
if ! command -v docker &> /dev/null; then
    echo "错误: 未安装Docker。请先安装Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

# 检查是否安装了Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "错误: 未安装Docker Compose。请先安装Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# 检查.env文件是否存在，如果不存在则从示例创建
if [ ! -f .env ]; then
    echo "未找到.env文件，从.env.example创建..."
    cp .env.example .env
    echo "请编辑.env文件并设置您的Gemini API密钥"
    exit 1
fi

# 启动应用
echo "启动Gemini图片生成与修改工具..."
docker-compose up -d

echo "应用已启动！请访问 http://localhost:7860" 