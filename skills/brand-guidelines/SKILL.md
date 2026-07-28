---
name: brand-guidelines
description: 将 Anthropic 官方品牌色、字体和视觉规范应用到各类产物。用户提到 Anthropic 品牌、品牌色、视觉格式、企业识别或设计规范时使用。
license: Complete terms in LICENSE.txt
---

# Anthropic 品牌样式（中文执行导读）

使用本 skill 为演示文稿、文档和其他视觉产物应用 Anthropic 官方风格：

- 主色为深色 `#141413`、浅色 `#faf9f5`、中灰 `#b0aea5`、浅灰 `#e8e6dc`。
- 强调色依次使用橙色 `#d97757`、蓝色 `#6a9bcc`、绿色 `#788c5d`。
- 标题使用 Poppins，缺失时回退 Arial；正文使用 Lora，缺失时回退 Georgia。
- 24pt 及以上文本视为标题；非文本形状循环使用三种强调色。
- 根据背景选择可读的文本颜色，保留原有层级和格式；无需自动安装字体。

下面保留上游英文正文，作为颜色与字体契约的权威来源。

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems
