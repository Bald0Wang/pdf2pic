# PDF to Image Converter

## 安装依赖
```bash
pip install -r requirements.txt
```

## 使用方法
```bash
python pdf_to_images.py input.pdf \
  --output ./images \
  --dpi 300 \
  --format png
```

## 参数说明
- `input_pdf`: 必填，输入PDF文件路径
- `-o/--output`: 输出目录（默认：output）
- `--dpi`: 图像分辨率（默认：200）
- `--format`: 输出格式 png/jpg（默认：png）
- `--split-height`: 垂直切割高度（像素）（默认：None）

## PDF 文件切分工具

### 安装依赖
```bash
pip install PyPDF2
```

### 使用方法
```bash
python pdf_splitter.py input.pdf
```

### 参数说明
- `input_pdf`: 必填，输入PDF文件路径
- `-o/--output_prefix`: 输出文件前缀（默认：page）
- `-p/--pages`: 指定要提取的页码，逗号分隔（例如：1,3,5）。如果不指定，默认提取所有页面

### 示例
1. 提取所有页面：
```bash
python pdf_splitter.py input.pdf
```

2. 提取指定页面：
```bash
python pdf_splitter.py input.pdf -p 1,3,5
```

3. 自定义输出文件前缀：
```bash
python pdf_splitter.py input.pdf -o output_prefix
```

## 图片转 PDF 工具

### 安装依赖
```bash
pip install Pillow reportlab
```

### 使用方法
```bash
python img_to_pdf.py input_path [output.pdf]
```

### 参数说明
- `input_path`: 必填，包含图片的输入目录路径或单个图片文件路径
- `output_pdf`: 可选，输出 PDF 文件路径。如果不指定，将在输入路径的同一目录下生成默认文件名

### 示例
1. 将 `images` 目录中的所有图片转换为 `output.pdf`：
```bash
python img_to_pdf.py images output.pdf
```

2. 将单个图片文件 `image.jpg` 转换为 `output.pdf`：
```bash
python img_to_pdf.py image.jpg output.pdf
```

3. 将单个图片文件 `image.jpg` 转换为默认文件名的 PDF（生成 `image.pdf`）：
```bash
python img_to_pdf.py image.jpg
```

4. 将 `images` 目录中的所有图片转换为默认文件名的 PDF（生成 `images/images.pdf`）：
```bash
python img_to_pdf.py images
```

python pdf_to_images.py xiumi.pdf --dpi 300 --format jpg --split-height 800