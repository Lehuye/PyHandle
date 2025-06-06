import os
from PIL import Image

def convert_image(input_path, output_path, format):
    """转换图片格式"""
    try:
        with Image.open(input_path) as img:
            format = format.lower()

            if format == 'jpg':
                # 确保 jpg 不包含透明度
                if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                    img = img.convert("RGB")

            elif format == 'icns':
                # ICNS 需要正方形，推荐尺寸：512x512
                size = max(img.size)
                img = img.resize((size, size))
                output_path = os.path.splitext(output_path)[0] + ".icns"
                img.save(output_path, format='ICNS')
                return True

            # 默认保存
            img.save(output_path, format=format.upper())
        return True

    except Exception as e:
        print(f"转换失败: {e}")
        return False