# 允许的文件扩展名
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'ico'}

def allowed_file(filename, allowed_types=None):
    """检查文件是否是允许的类型"""
    if not filename:
        return False
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    
    if allowed_types is None:
        return ext in ALLOWED_EXTENSIONS
    else:
        return ext in allowed_types