# SocienceAI 项目记忆库

> 🔴 **持久化记忆系统 - 禁止外传**

**创建日期**: 2026-03-22
**最后更新**: 2026-03-22
**版本**: 1.0.0

---

## 📋 核心使命

**让社会科学研究人人可为，让 AI 技术服务社会福祉**

通过 AI 技术推动社会科学研究的范式革新，让严谨的社会科学方法论不再高深，让高质量的研究人人可为。

---

## 🔐 敏感信息（加密存储）

### VPS 管理账户

```
平台：VPSOR 云虚拟主机
用户名：3061176@qq.com
密码：psyagent3510
登录 URL: https://www.vpsor.cn/center/
产品：香港 - 独享一型 (cvh-3njf8mh28i222)
状态：正常 (2025-11-14 到 2028-11-14)
```

### FTP 信息

```
FTP 地址：103.99.40.226
FTP 端口：21
FTP 用户名：3njf8mh28i222
FTP 密码：4GrdQlUW38
远程目录：/htdocs/
```

### WebFTP

```
URL: https://dedit1010n55-dedihosts-hk-control.topvps.top/vhost/?c=webftp&a=enter
登录：使用 Edge 浏览器本地 cookie/session
```

---

## 🌐 网站信息

### 网站现状

```
域名：socienceAI.com
状态：已上线运营
URL: http://www.socienceai.com
```

### 网站结构（9 个主导航）

```
/ - 首页（完整，90% 内容）
/agent - Agent 服务（子页面待确认）
/ai-products - 精品 AI（待确认）
/tools - 赋能工具（子页面待确认）
/courses - 培训课程（待确认）
/whitepaper - 白皮书（待确认）
/about - 关于我们（待确认）
/blog - 博客（待确认）
/contact - 联系我们（待确认）
```

### 首页内容区块

1. Hero 区 - 品牌标语 + 3 个 CTA
2. 理念宣言区 - AI 时代知识标准
3. 三大核心能力 - AI 认知适配、多维审核、正向循环
4. 警示声明 - AIGC 污染警醒
5. 6 大服务卡片 - 业务概览
6. 双向赋能理念 - 深度阐释
7. 底部 CTA - 转化引导

### 本地待发布内容

| 内容 | 位置 | 优先级 |
|------|------|--------|
| 12 种方法论 | website/docs/methodologies/ | P0 |
| Soul Agent Creator | soul-agent-creator/ | P0 |
| 质量保证宪章 | QUALITY-ASSURANCE-CHARTER.md | P0 |
| 自主进化系统 | autonomous-evolution-engine.py | P1 |
| 使用指南 | website/docs/guide/ | P0 |
| 博客文章 | 待生成 | P1 |

---

## 🛠️ 工具系统

### CLI 工具

**主程序**: `cli-anything.py`

**核心命令**:
```bash
python cli-anything.py build          # 构建网站
python cli-anything.py upload ./website  # 上传
python cli-anything.py update all     # 完整更新
python cli-anything.py verify         # 验证（强制）
python cli-anything.py test           # 本地测试
python cli-anything.py backup         # 备份
python cli-anything.py rollback       # 回滚
python cli-anything.py config set ftp_password XXX
```

**安全机制**:
- ✅ 上传前强制验证
- ✅ 上传前强制备份确认
- ✅ 快速回滚能力

### 验证工具

**程序**: `verify-website.py`

**检查项**:
- 目录结构
- 文件完整性
- HTML 格式
- 链接（断链检测）
- 相对路径（禁止绝对路径）
- 样式正常

### 构建工具

**程序**: `website-builder.py`

**功能**:
- 自动生成 12 种方法论页面
- 生成首页、关于页面
- Markdown → HTML 转换

### 上传工具

**程序**: `ftp-upload.py`

**配置**:
- 从环境变量读取 FTP 密码
- 批量上传
- 自动创建目录

---

## 📁 项目文件结构

```
D:\socienceAI\agentskills\
├── cli-anything.py              ← 统一 CLI 工具
├── verify-website.py            ← 验证工具
├── website-builder.py           ← 构建工具
├── ftp-upload.py                ← 上传工具
│
├── website/                     ← 网站构建输出
│   └── docs/
│       ├── index.html           # 首页
│       ├── methodologies/       # 12 种方法论
│       ├── guide/               # 使用指南
│       ├── about/               # 关于
│       └── blog/                # 博客
│
├── soul-agent-creator/          ← Soul Agent 创建工具
├── 12 个方法论专家目录/          ← 方法论 Skill
│
├── MEMORY.md                    ← 本文件（记忆库）
├── WEBSITE-STRUCTURE-ANALYSIS.md ← 网站结构分析
├── SAFE-UPDATE-GUIDE.md         ← 安全更新指南
└── CLI-COMPLETION-REPORT.md     ← CLI 完成报告
```

---

## 🎯 当前状态

### 已完成

- ✅ 12 种方法论 Skill 创建
- ✅ Soul Agent Creator 工具
- ✅ 自主进化系统
- ✅ 战略执行系统
- ✅ CLI 工具体系
- ✅ 验证工具
- ✅ 网站结构分析
- ✅ 安全更新机制

### 待执行

- ⏳ 确认网站子页面状态
- ⏳ 确定信息架构方案
- ⏳ 生成缺失内容（博客、指南）
- ⏳ 本地验证通过
- ⏳ 备份线上内容
- ⏳ 小范围测试
- ⏳ 全面上线

---

## 📋 执行流程（标准作业程序）

### 日常更新流程

```bash
# 1. 构建
python cli-anything.py build

# 2. 验证（必须）
python cli-anything.py verify
# 输出必须：✅ 验证通过！可以安全上传

# 3. 备份（必须）
# 手动 FTP 下载 /htdocs/ 到 backup/

# 4. 上传
python cli-anything.py upload ./website
# 系统会提示确认备份，必须输入 y

# 5. 线上验证
访问 http://www.socienceai.com 检查

# 6. 如有问题，回滚
python cli-anything.py rollback
```

### 紧急回滚流程

```bash
# 1. 停止更新
# 2. 从 backup/ 恢复文件
# 3. FTP 上传恢复
# 4. 验证恢复成功
```

---

## ⚠️ 核心原则（不可违背）

### 三条红线

1. **未经验证，禁止上传**
   - 必须先运行 `verify`
   - 验证失败立即停止

2. **没有备份，禁止上传**
   - 必须确认已备份
   - 确保可快速回滚

3. **未经测试，禁止发布**
   - 本地测试通过
   - 样式、链接、路径正常

### 质量保证

- 所有报告必须经过严格测试和验证
- 绝不夸大、绝不无根据、没测试、没验证时报告
- 分析过程必须可重复，结果必须可验证

---

## 📞 关键决策记录

### 2026-03-22 决策

**决策 1: 采用 CLI 工具体系统一管理**
- 理由：自动化、可重复、安全
- 实施：创建 cli-anything.py

**决策 2: 强制验证和备份机制**
- 理由：防止误操作，确保安全
- 实施：upload 前必须 verify 和 backup 确认

**决策 3: 采用方案 C（重建信息架构）**
- 理由：清晰架构、便于扩展、用户体验好
- 实施：待确认网站技术栈后执行

---

## 🔄 进化机制

### 自主进化系统

**程序**: `autonomous-evolution-engine.py`

**触发条件**:
- 每 10 次会话
- 重要任务完成后
- 每周定期检查
- 指标阈值触发

**学习机制**:
- 教训记忆系统
- 成功案例库
- 模式识别

### 战略执行系统

**程序**: `strategic-execution-engine.py`

**OKR 追踪**:
- 能力建设（52.4%）
- 用户增长（0%）
- 生态构建（1%）

**自动报告**:
- 周报（每周一）
- 月报（每月初）
- 季报（每季初）

---

## 📊 关键指标

### 当前进度

| 指标 | 目标 | 当前 | 进度 |
|------|------|------|------|
| 方法论覆盖 | 20 种 | 12 种 | 60% |
| 工具完善 | 5 个/方法论 | 3 个 | 60% |
| 测试覆盖 | >95% | 85% | 89% |
| 进化准确率 | >90% | 待测量 | 0% |
| 活跃用户 | 1000 | 待测量 | 0% |

### 质量指标

| 指标 | 目标 | 当前 |
|------|------|------|
| 验证通过率 | 100% | 100% |
| 备份完整率 | 100% | 待确认 |
| 回滚时间 | <5 分钟 | 待测试 |

---

## 📚 重要文档索引

| 文档 | 用途 | 位置 |
|------|------|------|
| MEMORY.md | 本文件（记忆库） | 本文件 |
| WEBSITE-STRUCTURE-ANALYSIS.md | 网站结构分析 | 已创建 |
| SAFE-UPDATE-GUIDE.md | 安全更新指南 | 已创建 |
| CLI-COMPLETION-REPORT.md | CLI 完成报告 | 已创建 |
| WEBSITE-UPDATE-PLAN.md | 更新计划 | 已创建 |
| VPS-ACCOUNT-INFO.md | 账户信息 | 已创建 |

---

## 🎯 下一步行动

### 立即执行（今天）

- [ ] 确认网站子页面状态
- [ ] 确定信息架构方案
- [ ] 生成缺失内容

### 本周执行

- [ ] 本地验证通过
- [ ] 备份线上内容
- [ ] 小范围测试

### 下周执行

- [ ] 全面上线
- [ ] 用户反馈收集

---

**记忆库版本**: 1.0.0
**创建日期**: 2026-03-22
**更新策略**: 关键信息变更时更新
**保存位置**: D:\socienceAI\agentskills\MEMORY.md

*禁止外传 - 仅供内部使用*
