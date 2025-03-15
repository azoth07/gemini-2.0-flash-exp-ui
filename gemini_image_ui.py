import os
import base64
import tempfile
import gradio as gr
from google import genai
from google.genai import types
from PIL import Image
import io

# 设置API密钥
def set_api_key(api_key):
    os.environ["GEMINI_API_KEY"] = api_key
    return "API密钥已设置！"

# 保存二进制文件
def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)
    return file_name

# 生成新图片（不需要输入图片）
def generate_new_image(api_key, prompt):
    return generate_or_modify_image(api_key, None, prompt)

# 使用多张图片生成
def generate_with_multiple_images(api_key, image1, image2, prompt):
    if not api_key:
        return None, "请先设置API密钥！"
    
    try:
        # 设置API密钥
        os.environ["GEMINI_API_KEY"] = api_key
        client = genai.Client(api_key=api_key)
        
        model = "gemini-2.0-flash-exp-image-generation"
        
        # 上传图片到Gemini API
        files = []
        temp_files = []
        
        # 处理上传的图片
        for idx, img in enumerate([image1, image2]):
            if img is not None:
                # 将图片保存为临时文件
                temp_file_path = os.path.join(tempfile.gettempdir(), f"temp_image_{idx}_{os.urandom(4).hex()}.jpg")
                img.save(temp_file_path)
                temp_files.append(temp_file_path)
                
                # 上传图片到Gemini API
                uploaded_file = client.files.upload(file=temp_file_path)
                files.append(uploaded_file)
        
        if not files:
            return None, "请至少上传一张图片！"
        
        # 准备API调用内容
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text="沙滩"),
                ],
            ),
            types.Content(
                role="model",
                parts=[
                    types.Part.from_uri(
                        file_uri=files[0].uri,
                        mime_type=files[0].mime_type,
                    ),
                ],
            ),
        ]
        
        # 添加用户输入的图片和提示
        user_parts = []
        for file in files[1:]:  # 跳过第一张已经使用的图片
            user_parts.append(
                types.Part.from_uri(
                    file_uri=file.uri,
                    mime_type=file.mime_type,
                )
            )
        user_parts.append(types.Part.from_text(text=prompt))
        
        contents.append(
            types.Content(
                role="user",
                parts=user_parts,
            )
        )
        
        # 配置生成参数
        generate_content_config = types.GenerateContentConfig(
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,
            response_modalities=["image", "text"],
            safety_settings=[
                types.SafetySetting(
                    category="HARM_CATEGORY_CIVIC_INTEGRITY",
                    threshold="OFF",  # Off
                ),
            ],
            response_mime_type="text/plain",
        )
        
        # 存储生成的文本和图片
        generated_text = ""
        output_image_path = None
        
        # 调用API并处理流式响应
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if not chunk.candidates or not chunk.candidates[0].content or not chunk.candidates[0].content.parts:
                continue
                
            if chunk.candidates[0].content.parts[0].inline_data:
                # 处理图片数据
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                output_image_path = os.path.join(tempfile.gettempdir(), f"gemini_output_{os.urandom(4).hex()}.png")
                save_binary_file(output_image_path, inline_data.data)
            else:
                # 处理文本数据
                generated_text += chunk.text if hasattr(chunk, 'text') else ""
        
        # 清理临时文件
        for temp_file in temp_files:
            try:
                os.unlink(temp_file)
            except:
                pass
        
        # 返回结果
        if output_image_path:
            return Image.open(output_image_path), "成功"
        else:
            return None, f"生成失败，没有返回图片。文本响应：{generated_text}"
            
    except Exception as e:
        return None, f"错误：{str(e)}"

# 生成或修改图片
def generate_or_modify_image(api_key, input_image, prompt):
    if not api_key:
        return None, "请先设置API密钥！"
    
    try:
        # 设置API密钥
        os.environ["GEMINI_API_KEY"] = api_key
        client = genai.Client(api_key=api_key)
        
        model = "gemini-2.0-flash-exp-image-generation"
        
        # 如果有输入图片，则进行修改，否则生成新图片
        if input_image is not None:
            # 将输入图片保存为临时文件
            temp_file_path = os.path.join(tempfile.gettempdir(), f"temp_image_{os.urandom(4).hex()}.jpg")
            input_image.save(temp_file_path)
            
            # 上传图片到Gemini API
            uploaded_file = client.files.upload(file=temp_file_path)
            
            # 准备API调用内容
            contents = [
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(text="沙滩"),  # 初始提示词，可以根据需要修改
                    ],
                ),
                types.Content(
                    role="model",
                    parts=[
                        types.Part.from_uri(
                            file_uri=uploaded_file.uri,
                            mime_type=uploaded_file.mime_type,
                        ),
                    ],
                ),
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(text=prompt),
                    ],
                ),
            ]
        else:
            # 如果没有输入图片，直接生成新图片
            contents = [
                types.Content(
                    role="user",
                    parts=[
                        types.Part.from_text(text=prompt),
                    ],
                ),
            ]
        
        # 配置生成参数
        generate_content_config = types.GenerateContentConfig(
            temperature=1,
            top_p=0.95,
            top_k=40,
            max_output_tokens=8192,
            response_modalities=["image", "text"],
            safety_settings=[
                types.SafetySetting(
                    category="HARM_CATEGORY_CIVIC_INTEGRITY",
                    threshold="OFF",  # Off
                ),
            ],
            response_mime_type="text/plain",
        )
        
        # 存储生成的文本和图片
        generated_text = ""
        output_image_path = None
        
        # 调用API并处理流式响应
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            if not chunk.candidates or not chunk.candidates[0].content or not chunk.candidates[0].content.parts:
                continue
                
            if chunk.candidates[0].content.parts[0].inline_data:
                # 处理图片数据
                inline_data = chunk.candidates[0].content.parts[0].inline_data
                output_image_path = os.path.join(tempfile.gettempdir(), f"gemini_output_{os.urandom(4).hex()}.png")
                save_binary_file(output_image_path, inline_data.data)
            else:
                # 处理文本数据
                generated_text += chunk.text if hasattr(chunk, 'text') else ""
        
        # 清理临时文件
        if input_image is not None:
            try:
                os.unlink(temp_file_path)
            except:
                pass
        
        # 返回结果
        if output_image_path:
            return Image.open(output_image_path), "成功"
        else:
            return None, f"生成失败，没有返回图片。文本响应：{generated_text}"
            
    except Exception as e:
        return None, f"错误：{str(e)}"

# 创建Gradio界面
def create_ui():
    with gr.Blocks(title="Gemini 图片修改工具") as app:
        gr.Markdown("# Gemini 图片修改工具")
        gr.Markdown("使用 Gemini AI 来生成新图片或修改现有图片")
        
        with gr.Row():
            with gr.Column():
                api_key_input = gr.Textbox(
                    label="Gemini API 密钥", 
                    placeholder="输入您的 Gemini API 密钥",
                    type="password"
                )
                set_key_btn = gr.Button("设置 API 密钥")
                api_status = gr.Textbox(label="API 状态", interactive=False)
                
                set_key_btn.click(
                    fn=set_api_key,
                    inputs=[api_key_input],
                    outputs=[api_status]
                )
        
        with gr.Tabs():
            with gr.TabItem("修改单张图片"):
                with gr.Row():
                    with gr.Column():
                        input_image = gr.Image(label="上传要修改的图片", type="pil")
                        prompt = gr.Textbox(
                            label="修改提示", 
                            placeholder="描述您想要对图片进行的修改，例如：'将背景改为海滩'",
                            lines=3
                        )
                        generate_btn = gr.Button("生成修改后的图片")
                    
                    with gr.Column():
                        output_image = gr.Image(label="修改后的图片")
                        output_text = gr.Textbox(label="Gemini 响应", interactive=False)
                
                generate_btn.click(
                    fn=generate_or_modify_image,
                    inputs=[api_key_input, input_image, prompt],
                    outputs=[output_image, output_text]
                )
            
            with gr.TabItem("多图片上传"):
                with gr.Row():
                    with gr.Column():
                        multi_image1 = gr.Image(label="上传图片1（必选）", type="pil")
                        multi_image2 = gr.Image(label="上传图片2（可选）", type="pil")
                        multi_prompt = gr.Textbox(
                            label="提示", 
                            placeholder="描述您想要生成的图片，例如：'汽车海边，旁边有一匹马'",
                            lines=3
                        )
                        multi_generate_btn = gr.Button("生成图片")
                    
                    with gr.Column():
                        multi_output_image = gr.Image(label="生成的图片")
                        multi_output_text = gr.Textbox(label="Gemini 响应", interactive=False)
                
                multi_generate_btn.click(
                    fn=generate_with_multiple_images,
                    inputs=[api_key_input, multi_image1, multi_image2, multi_prompt],
                    outputs=[multi_output_image, multi_output_text]
                )
            
            with gr.TabItem("生成新图片"):
                with gr.Row():
                    with gr.Column():
                        new_image_prompt = gr.Textbox(
                            label="图片描述", 
                            placeholder="描述您想要生成的图片，例如：'一只在海滩上奔跑的金毛犬'",
                            lines=3
                        )
                        new_generate_btn = gr.Button("生成新图片")
                    
                    with gr.Column():
                        new_output_image = gr.Image(label="生成的图片")
                        new_output_text = gr.Textbox(label="Gemini 响应", interactive=False)
                
                new_generate_btn.click(
                    fn=generate_new_image,
                    inputs=[api_key_input, new_image_prompt],
                    outputs=[new_output_image, new_output_text]
                )
        
        gr.Markdown("## 使用说明")
        gr.Markdown("""
        1. 首先输入您的 Gemini API 密钥并点击"设置 API 密钥"
        2. 选择功能标签页：
           - "修改单张图片"：上传一张图片并添加修改提示
           - "多图片上传"：上传两张图片（第一张必选，第二张可选）并添加提示
           - "生成新图片"：直接描述要生成的图片
        3. 点击相应的生成按钮，等待 Gemini AI 处理您的请求
        4. 生成的图片将显示在右侧，同时可能会有文本响应
        """)
        
    return app

# 主函数
if __name__ == "__main__":
    app = create_ui()
    app.launch()
