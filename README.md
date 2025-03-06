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


python pdf_to_images.py xiumi.pdf --dpi 300 --format jpg --split-height 800