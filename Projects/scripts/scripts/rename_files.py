import os
import re
import yaml

# 指定文件夹路径
folder_path = "blog-content/blog"

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # 跳过非 Markdown 文件
    if not filename.endswith(".md"):
        continue
    
    # 检查文件名是否以日期格式（yyyy-MM-dd）开头
    if re.match(r"^\d{4}-\d{2}-\d{2}", filename):
        continue  # 如果文件名已经以日期开头，则跳过

    # 读取文件内容
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 提取 YAML 信息
    match = re.match(r"(?s)^---\n(.*?)\n---", content)
    if not match:
        print(f"文件 {filename} 缺少 YAML 信息，跳过处理")
        continue

    yaml_content = match.group(1)
    yaml_data = yaml.safe_load(yaml_content)

    # 提取 date 字段
    date = yaml_data.get("date")
    print(f"文件 {filename} 的 date 字段为: {date}")

    # 检查 date 是否为字符串
    if not isinstance(date, str):
        print(f"文件 {filename} 的 date 字段不是字符串，尝试转换为字符串")
        date = str(date) if date is not None else None

    # 如果 date 仍然无效，跳过处理
    if not date or not re.match(r"^\d{4}-\d{2}-\d{2}", date):
        print(f"文件 {filename} 的 date 字段不存在或格式不正确，跳过处理")
        continue

    # 提取日期部分（忽略时间）
    date_match = re.match(r"^\d{4}-\d{2}-\d{2}", date)
    date = date_match.group(0)  # 提取匹配的日期部分

    # 在文件名开头插入日期
    new_filename = re.sub(r"^\d+-", "", filename)  # 删除文件名开头的数字
    new_filename = f"{date}-{new_filename}"
    new_file_path = os.path.join(folder_path, new_filename)
    os.rename(file_path, new_file_path)

    print(f"已重命名文件：{filename} -> {new_filename}")