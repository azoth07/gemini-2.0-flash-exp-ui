# Gemini 图片修改工具

这是一个基于Gradio的UI界面，用于使用Google的Gemini AI模型生成和修改图片。

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

## 获取Gemini API密钥

要使用此应用程序，您需要一个有效的Gemini API密钥。您可以通过以下步骤获取：

1. 访问 [Google AI Studio](https://makersuite.google.com/)
2. 登录您的Google账户
3. 创建一个新项目或使用现有项目
4. 在API部分获取您的API密钥

## 注意事项

- 此应用程序需要互联网连接以访问Gemini API
- 图片生成和修改可能需要一些时间，请耐心等待
- 生成的图片质量和准确性取决于您提供的描述/提示的质量

## 技术细节

- 前端界面：Gradio
- AI模型：Google Gemini 2.0 Flash
- 图片处理：PIL (Pillow)

## 许可证

[MIT](LICENSE) 