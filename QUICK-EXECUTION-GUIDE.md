# SocienceAI 网站更新 - 快速执行指南

> 🔴 **立即执行 - 本地内容发布到线上**

**制定日期**: 2026-03-22

---

## 🎯 目标

将本地已完成的新内容更新到 http://www.socienceai.com

---

## 📋 待发布内容清单

### 优先级 P0（今天发布）

| 内容 | 本地位置 | 目标位置 | 大小估算 |
|------|---------|---------|---------|
| Soul Agent Creator | `soul-agent-creator/README.md` | `/htdocs/agent-service/soul-agent-creator.html` | ~50KB |
| 质量保证宪章 | `QUALITY-ASSURANCE-CHARTER.md` | `/htdocs/whitepaper/quality-charter.html` | ~30KB |
| 项目宣言 | `MANIFESTO.md` | `/htdocs/about/manifesto.html` | ~40KB |
| 网站首页内容 | `website/docs/index.md` | `/htdocs/index.html` | ~20KB |
| 方法论页面（12 个） | `website/docs/methodologies/` | `/htdocs/methods/` | ~200KB |

### 优先级 P1（本周发布）

| 内容 | 本地位置 | 目标位置 |
|------|---------|---------|
| 自主进化系统 | `autonomous-evolution-engine.py` | `/htdocs/tools/autonomous-evolution.html` |
| 战略执行系统 | `strategic-execution-engine.py` | `/htdocs/about/strategy.html` |
| 博客文章（10 篇） | 待生成 | `/htdocs/blog/posts/` |

---

## 🚀 执行方式（3 选 1）

### 方式 1: WebFTP（推荐 - 最快）

**适用**: 小文件、快速更新

**步骤**:

1. **打开 WebFTP**
   - 使用 Edge 浏览器（已有 session）
   - URL: https://dedit1010n55-dedihosts-hk-control.topvps.top/vhost/?c=webftp&a=enter

2. **登录**
   - 应该自动登录（使用本地 cookie）
   - 如未登录，使用 VPSOR 账号

3. **导航到目标目录**
   - 进入 `/htdocs/`
   - 选择对应子目录

4. **上传文件**
   - 点击"上传"按钮
   - 选择本地文件
   - 等待完成

5. **验证**
   - 访问 http://www.socienceai.com 对应页面

**预计时间**: 30 分钟

---

### 方式 2: FTP 批量上传

**适用**: 大文件、批量上传

**步骤**:

1. **下载 FTP 客户端**（如 FileZilla）
   - https://filezilla-project.org/

2. **连接服务器**
   ```
   主机：103.99.40.226
   端口：21
   用户名：3njf8mh28i222
   密码：4GrdQlUW38
   ```

3. **导航到 `/htdocs/`**

4. **拖拽上传文件**

5. **验证**

**预计时间**: 1 小时

---

### 方式 3: Python 脚本

**适用**: 自动化、批量上传

**步骤**:

1. **设置环境变量**
   ```bash
   # Windows
   set FTP_PASSWORD=4GrdQlUW38
   
   # Linux/Mac
   export FTP_PASSWORD=4GrdQlUW38
   ```

2. **运行上传脚本**
   ```bash
   python ftp-upload.py ./website/docs
   ```

3. **验证**

**预计时间**: 30 分钟

---

## 📋 今日执行计划

### 上午（9:00-12:00）

**任务**: 准备和测试

- [ ] 9:00-9:30 测试 WebFTP 访问
- [ ] 9:30-10:00 备份线上现有内容
- [ ] 10:00-11:00 准备 P0 优先级文件
- [ ] 11:00-12:00 转换文件格式（md → html）

### 下午（13:00-18:00）

**任务**: 上传和验证

- [ ] 13:00-14:00 上传首页
- [ ] 14:00-15:00 上传 Agent 服务页面
- [ ] 15:00-16:00 上传方法论页面（12 个）
- [ ] 16:00-17:00 上传白皮书和关于页面
- [ ] 17:00-18:00 整体验证

---

## 🔧 文件格式转换

### Markdown 转 HTML 工具

**使用 Pandoc**:
```bash
# 安装 Pandoc
# https://pandoc.org/installing.html

# 转换单个文件
pandoc MANIFESTO.md -o manifesto.html --standalone

# 批量转换
for file in *.md; do
    pandoc "$file" -o "${file%.md}.html" --standalone
done
```

**使用 Python 脚本**:
```python
import markdown

def md_to_html(md_file, html_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html_text = markdown.markdown(md_text, extensions=['extra', 'codehilite'])
    
    html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SocienceAI</title>
</head>
<body>
{html_text}
</body>
</html>"""
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
```

---

## ✅ 验证检查清单

### 上传后验证

- [ ] 访问首页 http://www.socienceai.com
- [ ] 检查 Agent 服务页面
- [ ] 检查方法论页面（抽样 5 个）
- [ ] 检查白皮书页面
- [ ] 测试所有链接无 404
- [ ] 清除浏览器缓存后测试
- [ ] 移动端测试

### 功能验证

- [ ] 页面加载速度 < 3 秒
- [ ] 图片正常显示
- [ ] 链接正常跳转
- [ ] 表单正常提交（如有）
- [ ] 搜索功能正常（如有）

---

## ⚠️ 注意事项

### 上传前

1. **备份**
   - 下载线上所有文件到 `backup/` 目录
   - 记录备份时间

2. **测试**
   - 本地测试文件无错误
   - 转换后的 HTML 格式正确

3. **编码**
   - 确保 UTF-8 编码
   - 中文文件名注意兼容性

### 上传后

1. **验证**
   - 立即验证文件完整性
   - 测试关键功能

2. **监控**
   - 观察网站访问统计
   - 收集用户反馈

3. **回滚准备**
   - 保留备份文件
   - 知道如何快速回滚

---

## 📞 故障排查

### 问题 1: WebFTP 无法访问

**解决**:
1. 尝试清除浏览器缓存
2. 使用 Edge 浏览器
3. 从 VPSOR 管理面板重新进入

### 问题 2: 上传后页面 404

**解决**:
1. 检查文件路径是否正确
2. 检查文件名大小写
3. 检查文件权限（应为 644）

### 问题 3: 页面显示乱码

**解决**:
1. 检查文件编码（应为 UTF-8）
2. 检查 HTML meta charset
3. 重新上传文件

---

## 📊 成功标准

### 今日目标

- ✅ P0 优先级内容全部上线
- ✅ 首页正常访问
- ✅ 所有链接正常
- ✅ 无 404 错误

### 本周目标

- ✅ P1 优先级内容上线
- ✅ 博客系统启用
- ✅ 10 篇博客文章发布
- ✅ 网站访问量开始增长

---

**执行状态**: 准备中
*立即执行 | 2026-03-22*
