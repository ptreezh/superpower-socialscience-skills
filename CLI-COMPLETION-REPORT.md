# SocienceAI CLI 完整指令集

> 🔴 **统一 CLI 工具 - 网站建设与更新**

**版本**: 1.0.0
**创建日期**: 2026-03-22

---

## 🎯 使命对齐

**通过 CLI 工具实现 socienceAI.com 网站的自动化建设和更新**

- ✅ 一键构建本地网站
- ✅ 一键上传到服务器
- ✅ 一键完整更新流程
- ✅ 自动化日常运维

---

## 📋 完整指令集

### 基础命令（6 个）

```bash
# 1. 查看帮助
python cli-anything.py --help

# 2. 构建网站
python cli-anything.py build

# 3. 上传文件
python cli-anything.py upload ./website

# 4. 完整更新
python cli-anything.py update all

# 5. 查看状态
python cli-anything.py status

# 6. 清理文件
python cli-anything.py clean
```

### 配置命令（3 个）

```bash
# 1. 设置配置
python cli-anything.py config set ftp_password YOUR_PASSWORD

# 2. 获取配置
python cli-anything.py config get ftp_password

# 3. 列出配置
python cli-anything.py config list
```

### 更新命令（4 个）

```bash
# 1. 更新所有内容
python cli-anything.py update all

# 2. 只更新内容
python cli-anything.py update content

# 3. 只更新方法论
python cli-anything.py update methods

# 4. 只更新博客
python cli-anything.py update blog
```

---

## 🚀 快速开始（5 分钟）

### Step 1: 配置 FTP 密码

```bash
cd D:\socienceAI\agentskills
python cli-anything.py config set ftp_password 4GrdQlUW38
```

### Step 2: 验证配置

```bash
python cli-anything.py config list
python cli-anything.py status
```

### Step 3: 构建网站

```bash
python cli-anything.py build
```

### Step 4: 上传到服务器

```bash
python cli-anything.py upload ./website
```

### Step 5: 验证

访问 http://www.socienceai.com

---

## 📊 完整工作流程

### 首次建站流程

```bash
# 1. 配置
python cli-anything.py config set ftp_password 4GrdQlUW38

# 2. 构建
python cli-anything.py build

# 3. 上传
python cli-anything.py upload ./website

# 4. 验证
访问 http://www.socienceai.com
```

### 日常更新流程

```bash
# 一键完成
python cli-anything.py update all
```

### 部分更新流程

```bash
# 只更新方法论
python cli-anything.py update methods

# 只上传博客
python cli-anything.py upload ./website/docs/blog --remote /htdocs/blog
```

---

## 📁 生成的文件结构

```
agentskills/
├── cli-anything.py              # CLI 主程序
├── CLI-USAGE-GUIDE.md           # 使用指南
├── CLI-COMPLETION-REPORT.md     # 本文档
│
├── website/                     # 构建输出
│   ├── docs/
│   │   ├── index.md            # 首页
│   │   ├── index.html          # 首页（HTML）
│   │   ├── methodologies/      # 方法论页面
│   │   ├── guide/              # 使用指南
│   │   ├── about/              # 关于页面
│   │   └── blog/               # 博客
│   └── build-state.json        # 构建状态
│
└── .cli-config.json            # CLI 配置
```

---

## 🔧 核心功能

### 1. 网站构建

**自动生成**:
- ✅ 首页（使命、价值主张、CTA）
- ✅ 12 种方法论页面
- ✅ 方法论索引页
- ✅ 关于页面
- ✅ 使用指南页面
- ✅ 博客页面

**自动转换**:
- Markdown → HTML
- 自动添加样式
- 响应式布局

### 2. FTP 上传

**功能**:
- ✅ 批量上传文件
- ✅ 自动创建远程目录
- ✅ 断点续传
- ✅ 错误重试
- ✅ 进度显示

**安全**:
- ✅ 密码加密存储
- ✅ 环境变量支持
- ✅ 不硬编码密码

### 3. 完整更新

**一站式流程**:
```
本地文件 → 构建 → HTML → 上传 → 服务器 → 验证
```

**自动化**:
- ✅ 自动构建
- ✅ 自动上传
- ✅ 自动验证
- ✅ 错误处理

### 4. 状态监控

**检查项**:
- ✅ 本地文件数量
- ✅ 配置完整性
- ✅ FTP 连接测试
- ✅ 服务器响应

---

## 📈 更新场景

### 场景 1: 新内容发布

```bash
# 1. 准备新内容（Markdown 文件）
# 2. 放到 website/docs/ 目录
# 3. 运行更新
python cli-anything.py update all

# 4. 验证
访问 http://www.socienceai.com/new-content
```

### 场景 2: 方法论页面更新

```bash
# 更新方法论
python cli-anything.py update methods

# 或上传特定目录
python cli-anything.py upload ./website/docs/methodologies
```

### 场景 3: 博客文章发布

```bash
# 1. 创建博客文章
echo "# 文章标题" > website/docs/blog/new-post.md

# 2. 更新博客
python cli-anything.py update blog
```

### 场景 4: 紧急修复

```bash
# 1. 修复文件
# 2. 直接上传
python cli-anything.py upload ./website/docs/index.html

# 3. 验证
```

---

## ⚠️ 注意事项

### 安全提醒

1. **密码保护**
   - ✅ 使用 `config set` 命令
   - ✅ 或使用环境变量
   - ❌ 不要硬编码

2. **备份**
   - ✅ 更新前备份线上内容
   - ✅ 保留回滚能力

3. **验证**
   - ✅ 上传后验证文件
   - ✅ 检查网站功能

### 最佳实践

1. **小步快跑**
   - 频繁小更新
   - 避免大批量变更

2. **测试**
   - 本地测试后再上传
   - 先上传测试环境

3. **文档**
   - 记录每次更新
   - 编写更新日志

---

## 📞 故障排查

### 常见问题

**Q: 命令未找到？**
```bash
# 确保在正确目录
cd D:\socienceAI\agentskills

# 检查 Python 版本
python --version  # 需要 Python 3.6+
```

**Q: FTP 密码错误？**
```bash
# 重新设置密码
python cli-anything.py config set ftp_password 4GrdQlUW38

# 验证配置
python cli-anything.py config get ftp_password
```

**Q: 上传失败？**
```bash
# 检查网络连接
ping 103.99.40.226

# 检查服务器状态
python cli-anything.py status

# 查看详细错误
python cli-anything.py upload ./website --verbose
```

### 调试模式

```bash
# 启用调试
set DEBUG=1  # Windows
export DEBUG=1  # Linux/Mac

# 运行命令
python cli-anything.py update all
```

---

## 📚 相关文档

| 文档 | 说明 |
|------|------|
| [CLI-USAGE-GUIDE.md](CLI-USAGE-GUIDE.md) | 详细使用指南 |
| [WEBSITE-UPDATE-PLAN.md](WEBSITE-UPDATE-PLAN.md) | 更新计划 |
| [QUICK-EXECUTION-GUIDE.md](QUICK-EXECUTION-GUIDE.md) | 快速执行指南 |
| [VPS-ACCOUNT-INFO.md](VPS-ACCOUNT-INFO.md) | 账户信息 |

---

## ✅ 完成检查清单

### CLI 工具完成

- [x] CLI 主程序 (`cli-anything.py`)
- [x] 使用指南 (`CLI-USAGE-GUIDE.md`)
- [x] 完成报告 (`CLI-COMPLETION-REPORT.md`)
- [x] 配置管理
- [x] 错误处理

### 功能完成

- [x] 网站构建
- [x] FTP 上传
- [x] 完整更新流程
- [x] 状态监控
- [x] 配置管理

### 文档完成

- [x] 快速开始指南
- [x] 完整命令参考
- [x] 使用场景示例
- [x] 故障排查指南

---

## 🎯 下一步行动

### 立即执行

```bash
# 1. 配置 FTP 密码
python cli-anything.py config set ftp_password 4GrdQlUW38

# 2. 验证配置
python cli-anything.py status

# 3. 构建网站
python cli-anything.py build

# 4. 上传到服务器
python cli-anything.py upload ./website

# 5. 验证
访问 http://www.socienceai.com
```

### 日常使用

```bash
# 每日更新
python cli-anything.py update all

# 查看状态
python cli-anything.py status
```

---

**CLI 工具版本**: 1.0.0
**创建日期**: 2026-03-22
**维护**: SocienceAI Team

*让社会科学研究人人可为*
