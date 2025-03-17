# Gemini Image Generation and Modification Tool
# Gemini 图片生成与修改工具

This is a Gradio application that uses Google Gemini AI for image generation and modification.

这是一个使用Google Gemini AI进行图片生成和修改的Gradio应用程序。


## Instructions | 使用说明

1. First, enter your Gemini API key and click "Set API Key"
2. Choose a function tab:
   - "Modify Single Image": Upload one image and add modification prompts
   - "Multiple Image Upload": Upload two images (first one required, second optional) and add prompts
   - "Generate New Image": Directly describe the image you want to generate
3. Click the corresponding generation button and wait for Gemini AI to process your request
4. The generated image will display on the right side, along with possible text responses

1. 首先输入您的Gemini API密钥并点击"设置API密钥"
2. 选择功能标签页：
   - "修改单张图片"：上传一张图片并添加修改提示
   - "多图片上传"：上传两张图片（第一张必选，第二张可选）并添加提示
   - "生成新图片"：直接描述要生成的图片
3. 点击相应的生成按钮，等待Gemini AI处理您的请求
4. 生成的图片将显示在右侧，同时可能会有文本响应

## Get Gemini API Key | 获取Gemini API密钥

You need to obtain a Gemini API key from Google AI Studio: https://makersuite.google.com/app/apikey

您需要从Google AI Studio获取Gemini API密钥：https://makersuite.google.com/app/apikey

## Features | 功能

- Generate brand new images using Gemini AI
- Upload existing images and modify them using Gemini AI
- Clean and intuitive user interface
- Real-time display of generation results

- 使用Gemini AI生成全新的图片
- 上传现有图片并使用Gemini AI进行修改
- 简洁直观的用户界面
- 实时显示生成结果

## Installation | 安装

1. Clone this repository or download the source code

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

1. 克隆此仓库或下载源代码

2. 安装所需依赖项：

```bash
pip install -r requirements.txt
```

## Usage | 使用方法

1. Run the application:

```bash
python gemini_image_ui.py
# or
python gemini_image_ui_base64.py
```

2. Open the displayed URL in your browser (typically http://127.0.0.1:7860)

3. Enter your Gemini API key in the interface and click the "Set API Key" button

4. Use the application:
   - In the "Modify Image" tab, upload an image and enter modification prompts
   - In the "Generate New Image" tab, directly input descriptions to generate brand new images
   - Click the corresponding generation button and wait for the results to display

1. 运行应用程序：

```bash
python gemini_image_ui.py
# or
python gemini_image_ui_base64.py
```

2. 在浏览器中打开显示的URL（通常是 http://127.0.0.1:7860）

3. 在界面中输入您的Gemini API密钥并点击"设置API密钥"按钮

4. 使用应用程序：
   - 在"修改图片"标签页中，上传一张图片并输入修改提示
   - 在"生成新图片"标签页中，直接输入描述以生成全新图片
   - 点击相应的生成按钮，等待结果显示

## Notes | 注意事项

- This application requires a valid Gemini API key to run
- The quality of generated images depends on the prompts you provide and the capabilities of the Gemini model
- Temporary files are stored in the /tmp/gemini_images directory within the container

- 此应用程序需要有效的Gemini API密钥才能运行
- 生成的图片质量取决于您提供的提示和Gemini模型的能力
- 临时文件会存储在容器内的/tmp/gemini_images目录中

## Technical Details | 技术细节

- Frontend Interface: Gradio
- AI Model: Google Gemini 2.0 Flash
- Image Processing: PIL (Pillow)

- 前端界面：Gradio
- AI模型：Google Gemini 2.0 Flash
- 图片处理：PIL (Pillow)

## Demo
https://gemini.finleye.ai/

## Experimental Results | 实验效果
Prompt: Draw a picture of a girl wearing accessories
prompt：绘制一张图中女孩佩戴饰品的照片
![Screenshot 2025-03-15 212001.png](https://s2.loli.net/2025/03/15/VxEz3Rrg2AdYIZ5.png)
