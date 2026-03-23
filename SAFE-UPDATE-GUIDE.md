# SocienceAI 网站安全更新指南

> 🔴 **安全第一 - 验证通过才能上传**

**版本**: 1.0.0
**更新日期**: 2026-03-22

---

## ⚠️ 核心原则

### 三条红线

1. **未经验证，禁止上传**
   - 必须先运行 `python cli-anything.py verify`
   - 验证通过才能继续
   - 验证失败立即停止

2. **没有备份，禁止上传**
   - 上传前必须备份线上内容
   - 确保可以快速回滚
   - 备份文件妥善保存

3. **未经测试，禁止发布**
   - 本地测试通过
   - 样式正常
   - 链接正常
   - 路径正常

---

## 📋 完整流程

### Step 1: 本地构建

```bash
cd D:\socienceAI\agentskills
python cli-anything.py build
```

**输出**:
```
✅ 网站构建完成！
```

### Step 2: 验证（必须）

```bash
python cli-anything.py verify
```

**检查项**:
- ✅ 目录结构完整
- ✅ 文件完整性
- ✅ HTML 格式正确
- ✅ 链接无断链
- ✅ 相对路径正确
- ✅ 样式正常

**通过标准**:
```
✅ 通过：80+ 项
⚠️ 警告：0 项
❌ 错误：0 项
```

**如果验证失败**:
```
❌ 验证失败！禁止上传，请先修复错误

💡 建议：
  1. 查看上面的错误列表
  2. 修复所有错误
  3. 重新运行：python cli-anything.py verify
  4. 验证通过后再上传
```

### Step 3: 本地测试（推荐）

```bash
python cli-anything.py test
```

**启动本地服务器**: http://localhost:8080

**检查**:
- 首页显示正常
- 方法论页面正常
- 链接跳转正常
- 样式渲染正常

### Step 4: 备份线上内容（必须）

```bash
python cli-anything.py backup
```

**临时方案**（手动备份）:

1. 使用 FTP 客户端（如 FileZilla）
2. 连接服务器：
   - 主机：103.99.40.226
   - 端口：21
   - 用户名：3njf8mh28i222
   - 密码：4GrdQlUW38
3. 下载 `/htdocs/` 目录到本地 `backup/` 目录
4. 记录备份时间

### Step 5: 确认备份

系统会提示：
```
⚠️ 重要提醒：
  上传前请确保已备份线上内容
  如需备份，请先运行：python cli-anything.py backup

是否已备份？(y/n):
```

**必须输入**: `y`

**如果输入**: `n`
```
⚠️ 已取消上传
💡 请先备份：python cli-anything.py backup
```

### Step 6: 上传

```bash
python cli-anything.py upload ./website
```

或一键完成：
```bash
python cli-anything.py update all
```

### Step 7: 线上验证

访问 http://www.socienceai.com

**检查清单**:
- [ ] 首页正常显示
- [ ] 导航菜单正常
- [ ] 方法论页面正常
- [ ] 链接无 404
- [ ] 样式正常
- [ ] 移动端适配正常

### Step 8: 回滚准备

**如果线上有问题**:

```bash
python cli-anything.py rollback
```

**临时方案**（手动回滚）:
1. 从 `backup/` 目录选择要恢复的文件
2. 使用 FTP 客户端上传到服务器
3. 覆盖线上文件
4. 验证恢复

---

## 🔧 CLI 命令参考

### 验证命令

```bash
# 验证网站
python cli-anything.py verify

# 本地测试
python cli-anything.py test
```

### 备份命令

```bash
# 创建备份
python cli-anything.py backup
```

### 上传命令

```bash
# 上传文件
python cli-anything.py upload ./website

# 一键更新
python cli-anything.py update all
```

### 回滚命令

```bash
# 回滚到备份
python cli-anything.py rollback
```

---

## ⚠️ 禁止行为

### 绝对禁止

❌ **未验证直接上传**
```bash
# 错误示例
python cli-anything.py upload ./website  # 没有先 verify
```

❌ **没有备份就上传**
```bash
# 错误示例
python cli-anything.py update all  # 没有先 backup
```

❌ **跳过测试**
```bash
# 错误示例
# 本地不测试，直接上传
```

### 推荐做法

✅ **完整流程**
```bash
# 1. 构建
python cli-anything.py build

# 2. 验证
python cli-anything.py verify

# 3. 测试
python cli-anything.py test

# 4. 备份
python cli-anything.py backup

# 5. 上传
python cli-anything.py upload ./website

# 6. 线上验证
访问 http://www.socienceai.com
```

---

## 📊 验证检查清单

### 目录结构

- [ ] website/ 目录存在
- [ ] website/docs/ 目录存在
- [ ] website/docs/methodologies/ 目录存在
- [ ] website/docs/about/ 目录存在
- [ ] website/docs/blog/ 目录存在

### 文件完整性

- [ ] index.html 存在
- [ ] index.md 存在
- [ ] 方法论文件齐全（12+ 个）

### HTML 格式

- [ ] DOCTYPE 声明
- [ ] UTF-8 编码
- [ ] HTML 结构完整
- [ ] HEAD 标签完整
- [ ] BODY 标签完整

### 链接检查

- [ ] 无断链
- [ ] 相对路径正确
- [ ] 无绝对本地路径

### 样式检查

- [ ] 样式文件存在
- [ ] 样式正常渲染
- [ ] 无样式混乱

---

## 🚨 故障处理

### 验证失败

**错误**: 验证失败，禁止上传

**解决**:
1. 查看错误列表
2. 修复所有错误
3. 重新验证：`python cli-anything.py verify`
4. 通过后再上传

### 备份丢失

**错误**: 没有备份

**解决**:
1. 立即备份：`python cli-anything.py backup`
2. 或手动 FTP 下载备份

### 线上有问题

**错误**: 页面显示异常

**解决**:
1. 不要惊慌
2. 运行回滚：`python cli-anything.py rollback`
3. 或手动 FTP 上传备份文件
4. 验证恢复

---

## 📞 联系和支持

**项目负责人**: SocienceAI Team
**技术支持**: tech@socienceai.com

---

**安全更新，责任重大**

*验证通过才能上传 | 备份完成才能上传*

*2026-03-22*
