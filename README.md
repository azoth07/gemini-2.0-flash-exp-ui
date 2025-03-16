# Gemini 图片生成与修改工具

这是一个使用Google Gemini AI进行图片生成和修改的Gradio应用程序。

## 使用Docker运行

### 方法1：使用Docker Compose（推荐）

1. 设置环境变量（可选）

```bash
# Linux/macOS
export GEMINI_API_KEY=your_api_key_here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_api_key_here"
```

2. 启动容器

```bash
docker-compose up -d
```

应用将在 http://localhost:7860 上运行。

### 方法2：使用Docker命令

1. 构建Docker镜像

```bash
docker build -t gemini-image-ui .
```

2. 运行Docker容器

```bash
docker run -p 8000:7860 gemini-image-ui
```

## 使用说明

1. 首先输入您的Gemini API密钥并点击"设置API密钥"
2. 选择功能标签页：
   - "修改单张图片"：上传一张图片并添加修改提示
   - "多图片上传"：上传两张图片（第一张必选，第二张可选）并添加提示
   - "生成新图片"：直接描述要生成的图片
3. 点击相应的生成按钮，等待Gemini AI处理您的请求
4. 生成的图片将显示在右侧，同时可能会有文本响应

## 获取Gemini API密钥

您需要从Google AI Studio获取Gemini API密钥：https://makersuite.google.com/app/apikey

## 功能

- 使用Gemini AI生成全新的图片
- 上传现有图片并使用Gemini AI进行修改
- 简洁直观的用户界面
- 实时显示生成结果

## 安装

1. 克隆此仓库或下载源代码

2. 安装所需依赖项：

```bash
pip install -r requirements.txt
```

## 使用方法

1. 运行应用程序：

```bash
python gemini_image_ui.py
```

2. 在浏览器中打开显示的URL（通常是 http://127.0.0.1:7860）

3. 在界面中输入您的Gemini API密钥并点击"设置API密钥"按钮

4. 使用应用程序：
   - 在"修改图片"标签页中，上传一张图片并输入修改提示
   - 在"生成新图片"标签页中，直接输入描述以生成全新图片
   - 点击相应的生成按钮，等待结果显示

## 注意事项

- 此应用程序需要有效的Gemini API密钥才能运行
- 生成的图片质量取决于您提供的提示和Gemini模型的能力
- 临时文件会存储在容器内的/tmp/gemini_images目录中

## 技术细节

- 前端界面：Gradio
- AI模型：Google Gemini 2.0 Flash
- 图片处理：PIL (Pillow)

## 许可证

[MIT](LICENSE) 