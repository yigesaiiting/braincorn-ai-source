---
title: Braincorn Daily Capture - 2026-W19
date: 2026-05-10
week: 2026-05-04_to_2026-05-10
type: daily-capture
status: captured
source: ChatGPT conversations
tags:
  - braincorn
  - daily-capture
  - trading-system
  - xingyu
  - writing
  - personal-methodology
  - obsidian
---

# Braincorn Daily Capture - 2026-W19

> 目标：只沉淀本周对话中具有长期复用价值的内容，不保留闲聊、不保留临时情绪、不保留一次性问答。  
> 写入原则：原始资料保留在 `10_Raw/`；抽象方法沉淀到 `20_Wiki/`；正在推进的项目进入 `30_Projects/`；明确的新判断进入 `40_Decisions/`；可交付成品进入 `50_Outputs/`；系统规则与 AI 工作流进入 `90_System/`。

---

## 0. 本周总摘要

本周最值得沉淀的主线有五条：

1. **交易系统**：从单票判断转向「题材—催化—盘口—财务/预期差—交易执行」的结构化模型，并开始形成盘前 30 分钟 SOP、扫描器优化规则与热度股判断框架。
2. **产品创业**：星与社区的定位从「饭圈社区 + 明星榜单工具」升级为「应援任务平台 + 粉丝资源解锁系统 + 商业空间粉丝经济解决方案」。
3. **写作素材**：围绕 `ww` 与「华南湿季」形成一套冷感、克制、带理论气质的关系叙事母题。
4. **个人方法论**：明确需要从「高认知 + 高情绪张力 + 低系统稳定性」转向「系统拥有者模式」。
5. **知识库系统**：Braincorn / Obsidian / GitHub / Codex 的协作方式开始成型，下一步应把每日对话自动沉淀为可检索、可回链、可复用的 Markdown。

---

# 1. 交易系统

## 1.1 可复用判断：AI / 高弹性成长股选股模型 V2

**核心公式**

```text
暴涨股 = 热门主线 × 预期差 × 业绩/订单验证 × 小中盘弹性 × 盘口确认
```

**模型解释**

- `热门主线`：AI 数据中心、光互联、AI 基础设施、半导体、机器人、核能、电力、云计算等。
- `预期差`：市场原先没有把公司归入主线，或仍按旧业务估值。
- `业绩/订单验证`：收入、毛利、订单、客户、指引、合同出现可验证变化。
- `小中盘弹性`：市值不宜过大，筹码更容易被重估推动。
- `盘口确认`：盘前成交额、RVOL、VWAP 承接、突破盘前高、回踩不破等。

**建议写入路径**

- `20_Wiki/Playbooks/AI高弹性成长股选股模型V2.md`
- `20_Wiki/Concepts/新身份重估.md`
- `40_Decisions/Investment_Decisions/2026-05-高弹性成长股模型升级.md`

---

## 1.2 可复用判断：热度股判断框架

本周反复出现的交易问题，不是「某只股票能不能买」，而是：

> 一只股票是否正在从普通股票变成市场共同叙事中的热度股？

可以沉淀成三个判断问题：

1. **这个题材是否刚被发现？**
   - 早期胜率高，但信息不充分。
   - 适合小仓试错，不能重仓幻想。

2. **这个题材是否已经大众化？**
   - 热度高，但容易进入追高阶段。
   - 需要看盘口承接和换手结构。

3. **这个题材是否还有接力叙事？**
   - 如果没有新催化，热度可能快速衰减。
   - 如果有财报、订单、政策、行业扩散，才可能继续上行。

**可复用表达**

```text
题材交易不是买“好公司”，而是买“市场正在共同相信的新身份”。
```

**建议写入路径**

- `20_Wiki/Concepts/题材潮流生命周期.md`
- `20_Wiki/Playbooks/热度股判断框架.md`
- `20_Wiki/Concepts/证券交易_vs_fashion_trends.md`

---

## 1.3 盘前 30 分钟可执行 SOP

**目标**

在美股开盘前 30 分钟内，从市场热度、催化、成交、风险和买点五个维度筛出当日可执行标的。

**SOP 结构**

### Step 1：市场环境判断

记录：

- Nasdaq 期货
- Russell 2000
- SOXX / SMH
- 10Y 美债
- VIX
- 今日主线

判断：

```text
市场环境强 → 可以考虑高弹性标的
市场环境弱 → 只做最强主线，不追边缘票
VIX 高 / 10Y 上行 → 降低仓位，避免追高
```

### Step 2：扫描 Top 异动股

优先看：

- 盘前涨幅
- 盘前成交额
- RVOL
- 市值
- float
- short interest
- 是否有新闻 / 财报 / 订单 / 政策 / 并购 / FDA / 合作

### Step 3：催化分级

| 等级 | 催化类型 | 处理方式 |
|---|---|---|
| S | 财报超预期 + 上调指引 + 主线匹配 | 可进入重点观察 |
| A | 大订单 / 大客户 / 战略合作 / 政策直接受益 | 等盘口确认 |
| B | 行业热度扩散 / 主题关联 / 社区热炒 | 小仓试错 |
| C | 无明确催化，仅低价拉升 | 大多排除 |

### Step 4：排除条件

出现以下情况优先排除：

- 盘前涨幅巨大但成交额不足
- 无明确催化
- 刚完成增发或有明显稀释风险
- 已连续多日加速，开盘前一致性过强
- 盘前高开后不断跌破 VWAP
- 社区热度很高但财务/订单无法支撑

### Step 5：买点

优先级：

1. 开盘后突破盘前高，成交放大。
2. 回踩 VWAP 不破，出现二次上攻。
3. 首次强势分歧后快速收回。
4. 大盘强、板块强、个股强三者共振。

避免：

- 开盘第一根大阳线无脑追。
- 已涨 40% 以上但无新催化。
- 跌破 VWAP 后只因便宜而补仓。

### Step 6：止损与仓位

| 交易类型 | 仓位 | 止损 |
|---|---:|---|
| 观察试错 | 5% - 10% | 跌破 VWAP / 盘前关键位 |
| 高确认度 | 10% - 20% | 跌破结构位 |
| 妖股博弈 | 单票不超过 10% | 时间止损 + 价格止损 |
| 杠杆 ETF | 严格短线 | 不做无计划隔夜 |

**建议写入路径**

- `20_Wiki/Playbooks/盘前30分钟热度股SOP.md`
- `90_System/Templates/盘前交易面板模板.md`
- `40_Decisions/Investment_Decisions/2026-05-盘前SOP启用.md`

---

## 1.4 Python 扫描器优化方向

本周多次使用 Python 自动化工具扫 Top 股票，值得沉淀为扫描器迭代项。

**当前问题**

- 只看涨幅容易扫到噪音票。
- 缺少催化分类。
- 缺少稀释风险识别。
- 缺少盘前成交额优先级。
- 缺少社交热度与新闻质量打分。
- 缺少「主线匹配度」字段。

**建议新增字段**

```yaml
ticker:
premarket_change:
premarket_volume:
premarket_dollar_volume:
rvol:
market_cap:
float:
short_interest:
catalyst_type:
catalyst_quality:
sector_theme:
theme_fit_score:
dilution_risk:
news_source:
social_heat:
technical_position:
entry_plan:
risk_level:
```

**建议写入路径**

- `30_Projects/TradingScanner/盘前热度股扫描器需求.md`
- `90_System/Templates/热度股扫描器字段模板.md`
- `40_Decisions/Investment_Decisions/2026-05-扫描器字段升级.md`

---

## 1.5 个股复盘沉淀规则

本周涉及过的股票包括：

- IREN
- CRWV
- OSS
- MXL
- INOD
- PLTR
- BBAI
- TASK
- SOXL
- SENS
- ASRT
- AEHR
- NVTS
- AXSM
- AXTI

这些不适合全部写成零散聊天记录，而应按统一模板沉淀。

**建议模板**

```markdown
---
title: TICKER 复盘
ticker:
date:
type: stock-review
tags:
  - markets
  - stock-review
---

# TICKER 复盘

## 1. Facts
- 公司业务：
- 当日涨跌：
- 盘前/盘中表现：
- 财报/订单/新闻：
- 成交量/换手：

## 2. Inference
- 市场正在交易什么叙事？
- 是否发生新身份重估？
- 资金是否认可？

## 3. Catalysts
- 已发生催化：
- 潜在催化：
- 催化是否可持续：

## 4. Risks
- 估值风险：
- 稀释风险：
- 流动性风险：
- 追高风险：

## 5. Trade Plan
- 观察位：
- 买点：
- 止损：
- 止盈：
- 仓位：

## 6. Conditions Not Suitable For Entry
- 什么情况下不应该买：
```

**建议写入路径**

- `90_System/Templates/股票复盘模板.md`
- `10_Raw/Markets/2026-05-个股原始讨论/`
- `20_Wiki/Companies/`
- `40_Decisions/Investment_Decisions/`

---

# 2. 产品创业

## 2.1 星与社区核心定位升级

**原定位**

```text
饭圈社区 + 明星榜单工具
```

**新定位**

```text
明星应援活动任务平台
+ 粉丝资源解锁系统
+ 商业空间粉丝经济解决方案
```

**关键判断**

星与当前不应继续只做「流量入口」或「活动撮合方」，而应成为饭圈活动链条里的：

- 任务组织者
- 数据验证者
- 权益发放者
- 活动沉淀者
- 资源分配器

**核心转向**

```text
从“帮后援会找场地”
升级为
“帮商场、后援会、品牌设计一套可量化、可验证、可沉淀的粉丝任务系统”
```

**建议写入路径**

- `30_Projects/XingYu/星与产品定位升级.md`
- `40_Decisions/Product_Decisions/2026-05-星与从社区入口升级为任务中台.md`
- `20_Wiki/Products/星与应援任务平台.md`

---

## 2.2 星与新闭环

**旧闭环**

```text
后援会入驻星与 → 粉丝在星与报名 → 星与获得用户流量
```

问题：

- 商场要求粉丝去官方社媒互动。
- 粉丝注意力被导向外部平台。
- 星与只做撮合，容易被后援会和商场绕开。
- 小程序没有形成不可替代资产。

**新闭环**

```text
活动曝光 → 星与报名 → 商场互动任务 → 上传凭证 → 审核 → 解锁权益 → 现场核销 → 数据复盘
```

**星与必须掌握的关键节点**

- 任务发起权
- 凭证回流权
- 审核权
- 权益发放权
- 核销数据
- 活动报告
- 艺人主页沉淀
- 粉丝等级资产

**建议写入路径**

- `20_Wiki/Playbooks/饭圈活动任务闭环.md`
- `30_Projects/XingYu/应援任务解锁系统PRD.md`
- `40_Decisions/Product_Decisions/2026-05-星与新闭环.md`

---

## 2.3 应援任务解锁系统

**产品本质**

把商场社媒 KPI 包装成粉丝愿意参与的「为艺人解锁资源」任务。

**错误叙事**

```text
请粉丝去商场官方账号点赞、评论、收藏。
```

**正确叙事**

```text
完成任务，为艺人解锁更高规格应援资源。
```

**示例**

```text
已完成 328 / 500 人互动任务
距离解锁「商场大屏延长播放」还差 172 人
```

**任务链路**

```text
关注活动页
→ 去商场小红书/微博/抖音完成互动
→ 使用指定关键词评论
→ 截图上传星与
→ 审核通过
→ 获得礼包/积分/徽章/抽奖/留言上墙资格
```

**建议写入路径**

- `20_Wiki/Products/应援任务解锁系统.md`
- `30_Projects/XingYu/MVP/应援任务页.md`
- `30_Projects/XingYu/MVP/活动页_报名任务解锁结构.md`

---

## 2.4 应援资源解锁池

**资源池本质**

把商场资源产品化、等级化、门槛透明化。

| 等级 | 解锁条件 | 资源包 |
|---|---:|---|
| A 类基础资源包 | 300 人完成互动任务 | 中庭场地 / 基础桌椅 / 安保协助 / 官方账号基础露出 |
| B 类进阶资源包 | 800 人完成互动任务 | 打卡背景板 / 商场大屏播放 / 官方小红书发布 / 摄影支持 |
| C 类高规格资源包 | 1500 人完成互动任务 | 主题痛楼 / 社媒矩阵宣发 / 品牌联动礼品 / 舞台音响支持 |

**对后援会的表达**

```text
你不是来求场地，而是来星与为艺人解锁更高规格的应援资源。
```

**建议写入路径**

- `20_Wiki/Products/应援资源解锁池.md`
- `50_Outputs/XingYu/后援会资源等级表.md`
- `50_Outputs/XingYu/商场资源包招商页.md`

---

## 2.5 MVP 五个功能

本阶段不要过度复杂，先验证：

```text
任务发起 → 凭证回流 → 权益核销 → 数据交付
```

**MVP 五个模块**

1. **活动报名页**
   - 艺人
   - 活动名称
   - 时间地点
   - 主办后援会
   - 合作商场
   - 报名按钮
   - 入群入口
   - 核销二维码

2. **应援任务页**
   - 关注
   - 点赞
   - 评论
   - 收藏
   - 转发
   - 上传截图
   - 审核状态
   - 任务完成进度条

3. **解锁进度条**
   - 已完成人数
   - 下一档权益
   - 距离解锁还差多少人

4. **现场核销**
   - 扫码核销
   - 礼包领取
   - 积分 / 徽章 / 抽奖 / 留言上墙资格

5. **活动数据后台**
   - 报名人数
   - 任务完成人数
   - 截图审核数
   - 到场核销数
   - 粉丝来源
   - 社群转化
   - 活动照片
   - 数据报告导出

**建议写入路径**

- `30_Projects/XingYu/MVP/星与应援任务平台MVP.md`
- `30_Projects/XingYu/PRD/活动报名页PRD.md`
- `30_Projects/XingYu/PRD/应援任务页PRD.md`
- `30_Projects/XingYu/PRD/活动数据后台PRD.md`

---

## 2.6 给商场的合作话术

**不要再说**

```text
我们帮你引流粉丝到商场。
```

**应该说**

```text
星与帮你把粉丝应援活动拆成线上互动任务 + 线下核销任务，
并交付一份可用于内部汇报和二次招商的活动数据报告。
```

**商场真正关心**

- 官方账号互动
- 现场人流
- 活动照片
- 领导汇报
- 可复用案例素材
- 下次招商 / 品牌联动

**报告应包含**

- 活动报名人数
- 实际到场核销人数
- 商场官方账号互动量
- 相关笔记 / 微博传播量
- 粉丝打卡照片数量
- 后援会参与人数
- 现场人流照片
- 二次合作建议

**建议写入路径**

- `50_Outputs/XingYu/星与商业空间粉丝应援活动增长解决方案.md`
- `50_Outputs/XingYu/商场合作话术.md`
- `20_Wiki/Playbooks/商场粉丝经济数据报告模型.md`

---

# 3. 写作素材

## 3.1 核心文本资产：华南湿季 / ww

本周写作主线围绕以下开头展开：

```text
这个季节的华南，总是不体面的。
```

这句话已经具备长期复用价值，建议作为一个独立写作项目的母题入口。

**核心氛围**

- 华南
- 湿气
- 黏腻
- 阴晴之间的误判
- 半年关系
- 旧账
- 合拍
- 预感关系结束
- 提前抽离
- 克制但没有放下

**建议写入路径**

- `30_Projects/Writing/华南湿季与ww.md`
- `10_Raw/Writing/2026-05-ww原始片段.md`
- `20_Wiki/Concepts/湿气作为情绪结构.md`

---

## 3.2 可复用写作母题

### 母题一：气候不是背景，是心理结构

```text
湿气不是环境描写，而是关系里无法干脆结束的状态。
```

可发展方向：

- 华南的湿气 = 情绪的黏连
- 阴晴不定 = 关系判断的不稳定
- 风 = 误以为事情还能变好的瞬间
- 不体面 = 情绪无法被整洁地处理

**建议写入路径**

- `20_Wiki/Concepts/气候作为心理结构.md`

---

### 母题二：关系中的提前撤退

```text
她几乎在提前预知到一段关系即将结束时，就开始提前抽离。
```

可发展方向：

- 不是背叛，而是自保。
- 不是冷漠，而是提前处理失去。
- 不是不在乎，而是不相信关系能稳定存在。
- 叙述者的痛点不是失去，而是发现对方比自己更早接受失去。

**建议写入路径**

- `20_Wiki/Concepts/关系中的提前撤退.md`

---

### 母题三：男性冷感叙述

**写法规则**

- 不直接哭诉。
- 不求理解。
- 不把情绪解释完整。
- 用具体细节承载未说出口的部分。
- 用句子的空白制造余震。
- 不把对方写成坏人。

**建议写入路径**

- `20_Wiki/Playbooks/冷感男性叙事方法.md`
- `90_System/Templates/关系散文修改检查表.md`

---

## 3.3 “加布噜咕里咕咕”作为私人语言资产

**当前定义**

```text
加布噜咕里咕咕 = 我不太会说温柔的话，但我在学。
```

这个短句可以作为关系文本里的私人语言，不宜过度解释。

**可复用方向**

- 作为一段关系里的暗号。
- 作为人物不会表达温柔的替代说法。
- 作为冷叙述中突然出现的柔软断点。
- 作为标题或章节名。

**建议写入路径**

- `10_Raw/Writing/私人语言词典.md`
- `20_Wiki/Concepts/亲密关系中的私人语言.md`

---

# 4. 个人方法论

## 4.1 从高认知个体到系统拥有者

**本周核心判断**

```text
你不是缺洞察，而是缺稳定复利结构。
```

当前模式可概括为：

```text
高认知 + 高情绪张力 + 低系统稳定性
```

需要转向：

```text
系统拥有者模式
```

**系统拥有者模式包含**

- 稳定现金流
- 稳定睡眠
- 稳定训练
- 稳定交易规则
- 稳定知识沉淀
- 稳定输出机制
- 稳定关系边界

**建议写入路径**

- `30_Projects/Personal_System/稳定复利底盘.md`
- `20_Wiki/Concepts/系统拥有者模式.md`
- `40_Decisions/Personal_Decisions/2026-05-从机会捕捉转向系统复利.md`

---

## 4.2 Obsidian / Braincorn / Codex 工作流

**Braincorn 定位**

```text
Obsidian = 本地知识前端
GitHub = 版本管理与 AI 可读取仓库
Codex = 自动整理 / 编译 / 维护
ChatGPT = 研究、判断、结构化与输出
```

**分层写入规则**

| 层级 | 用途 |
|---|---|
| `00_Inbox/` | 临时捕获，未整理内容 |
| `10_Raw/` | 原始资料，尽量少改写 |
| `20_Wiki/` | 概念、模型、方法论 |
| `30_Projects/` | 进行中的项目 |
| `40_Decisions/` | 明确判断与决策 |
| `50_Outputs/` | 可交付成品 |
| `90_System/` | 系统规则、模板、AI 工作流 |

**AI 处理规则**

- 优先读索引页，再读具体页面。
- 原始资料不覆盖。
- 新判断写入 `40_Decisions/`。
- 交易内容必须拆成：
  - facts
  - inference
  - catalysts
  - risks
  - trade plan
  - conditions not suitable for entry
- 不确定内容标注 `需要验证` 或 `资料不足`。
- 使用 YAML frontmatter。
- 使用 Obsidian wiki-link。
- 关键决策必须反链到相关概念和项目。

**建议写入路径**

- `90_System/Knowledge_Rules/Braincorn写入规则.md`
- `90_System/AI_Workflows/ChatGPT_to_Obsidian_Daily_Capture.md`
- `90_System/AI_Workflows/Codex_Obsidian协作规范.md`
- `90_System/Templates/Daily_Capture_Template.md`

---

## 4.3 每日对话自动沉淀工作流

**目标**

把每天和 ChatGPT 的高价值对话自动沉淀进 Obsidian，而不是让洞察散落在聊天窗口里。

**推荐流程**

```text
当天对话
→ ChatGPT 生成 Daily Capture
→ 写入 00_Inbox/Daily_Capture/
→ 每周整理到 20_Wiki / 30_Projects / 40_Decisions
→ 更新 INDEX.md
→ Git 提交
```

**每日沉淀模板**

```markdown
---
title:
date:
type: daily-capture
source: ChatGPT
status: captured
tags:
---

# Daily Capture

## 1. 今日高价值判断

## 2. 可复用模型

## 3. 项目推进

## 4. 写入路径建议

## 5. 待办

## 6. INDEX.md 更新项
```

**建议写入路径**

- `90_System/Templates/Daily_Capture_Template.md`
- `90_System/AI_Workflows/每日对话沉淀到Obsidian.md`
- `00_Inbox/Daily_Capture/2026-05-10.md`

---

## 4.4 身体底盘：增肌训练系统

**已知条件**

- 男
- 35 岁
- 身高 172cm
- 体重 51kg
- 目标：增肌
- 训练频率：每周 4-5 天
- 单次训练：约 1 小时
- 训练地点：健身房
- 连续健身约 8 个月
- 曾被教练提醒：长短脚可能影响硬拉动作

**长期规则**

- 增肌优先于刷重量。
- 硬拉类动作需谨慎，不强行追求传统硬拉。
- 关注动作稳定、左右平衡和核心控制。
- 记录 RPE、reps、组数、重量，形成训练日志。

**建议写入路径**

- `30_Projects/Body/增肌训练系统.md`
- `90_System/Templates/训练日志模板.md`
- `40_Decisions/Personal_Decisions/2026-05-增肌优先于极限重量.md`

---

# 5. 待办

## 5.1 交易系统待办

- [ ] 建立 `盘前30分钟热度股SOP.md`
- [ ] 建立 `AI高弹性成长股选股模型V2.md`
- [ ] 建立 `题材潮流生命周期.md`
- [ ] 建立 `股票复盘模板.md`
- [ ] 给 Python 扫描器新增字段：
  - [ ] catalyst_type
  - [ ] catalyst_quality
  - [ ] premarket_dollar_volume
  - [ ] dilution_risk
  - [ ] social_heat
  - [ ] theme_fit_score
- [ ] 对 INOD 做一次完整复盘，重点提炼为什么当时没有提前识别。
- [ ] 对 IREN / CRWV / MXL / OSS 建立统一复盘文件。
- [ ] 将交易计划统一拆成：
  - [ ] facts
  - [ ] inference
  - [ ] catalysts
  - [ ] risks
  - [ ] trade plan
  - [ ] conditions not suitable for entry

---

## 5.2 产品创业待办

- [ ] 建立 `星与产品定位升级.md`
- [ ] 建立 `应援任务解锁系统PRD.md`
- [ ] 建立 `应援资源解锁池.md`
- [ ] 把活动页改成 `报名 + 任务 + 解锁` 结构。
- [ ] 做一版 `商场资源解锁方案` 招商页。
- [ ] 做一版 `后援会应援资源等级表`。
- [ ] 设计活动数据后台字段。
- [ ] 评估 `应援定制 H5` 最低可行模板：
  - [ ] 活动主视觉
  - [ ] 艺人信息
  - [ ] 解锁任务
  - [ ] 进度条
  - [ ] 截图上传
  - [ ] 核销二维码
  - [ ] 战报页
- [ ] 找一个真实活动试跑 `任务发起 → 凭证回流 → 权益核销 → 数据交付` 闭环。

---

## 5.3 写作待办

- [ ] 建立 `华南湿季与ww.md`
- [ ] 整理当前所有 `ww` 片段，保留原始版本。
- [ ] 建立 `湿气作为情绪结构.md`
- [ ] 建立 `关系中的提前撤退.md`
- [ ] 建立 `冷感男性叙事方法.md`
- [ ] 把「加布噜咕里咕咕」写入私人语言词典。
- [ ] 产出一版中篇结构：
  - [ ] 现在的我
  - [ ] 回忆中的我
  - [ ] ww 的提前抽离
  - [ ] 华南湿季作为结构线
  - [ ] 未说出口的结尾

---

## 5.4 个人方法论待办

- [ ] 建立 `稳定复利底盘.md`
- [ ] 建立 `系统拥有者模式.md`
- [ ] 建立 `每日对话沉淀到Obsidian.md`
- [ ] 建立 `Daily_Capture_Template.md`
- [ ] 建立 `训练日志模板.md`
- [ ] 每天结束后做一次 Daily Capture。
- [ ] 每周末更新一次 INDEX.md。
- [ ] 把重要决策写入 `40_Decisions/`，不要只留在聊天记录中。

---

# 6. 应该更新的 INDEX.md 条目

## 6.1 根目录 `INDEX.md`

建议新增：

```markdown
## Trading System
- [[20_Wiki/Playbooks/盘前30分钟热度股SOP]]
- [[20_Wiki/Playbooks/AI高弹性成长股选股模型V2]]
- [[20_Wiki/Playbooks/热度股判断框架]]
- [[20_Wiki/Concepts/题材潮流生命周期]]
- [[90_System/Templates/股票复盘模板]]

## XingYu / Product
- [[30_Projects/XingYu/星与产品定位升级]]
- [[30_Projects/XingYu/应援任务解锁系统PRD]]
- [[20_Wiki/Products/应援资源解锁池]]
- [[50_Outputs/XingYu/星与商业空间粉丝应援活动增长解决方案]]

## Writing
- [[30_Projects/Writing/华南湿季与ww]]
- [[20_Wiki/Concepts/湿气作为情绪结构]]
- [[20_Wiki/Concepts/关系中的提前撤退]]
- [[20_Wiki/Playbooks/冷感男性叙事方法]]

## Personal System
- [[30_Projects/Personal_System/稳定复利底盘]]
- [[20_Wiki/Concepts/系统拥有者模式]]
- [[30_Projects/Body/增肌训练系统]]

## Braincorn System
- [[90_System/Knowledge_Rules/Braincorn写入规则]]
- [[90_System/AI_Workflows/ChatGPT_to_Obsidian_Daily_Capture]]
- [[90_System/Templates/Daily_Capture_Template]]
```

---

## 6.2 `20_Wiki/Index.md`

建议新增：

```markdown
## Concepts
- [[20_Wiki/Concepts/新身份重估]]
- [[20_Wiki/Concepts/题材潮流生命周期]]
- [[20_Wiki/Concepts/证券交易_vs_fashion_trends]]
- [[20_Wiki/Concepts/湿气作为情绪结构]]
- [[20_Wiki/Concepts/关系中的提前撤退]]
- [[20_Wiki/Concepts/系统拥有者模式]]

## Playbooks
- [[20_Wiki/Playbooks/盘前30分钟热度股SOP]]
- [[20_Wiki/Playbooks/热度股判断框架]]
- [[20_Wiki/Playbooks/AI高弹性成长股选股模型V2]]
- [[20_Wiki/Playbooks/饭圈活动任务闭环]]
- [[20_Wiki/Playbooks/冷感男性叙事方法]]

## Products
- [[20_Wiki/Products/星与应援任务平台]]
- [[20_Wiki/Products/应援资源解锁系统]]
- [[20_Wiki/Products/应援资源解锁池]]
```

---

## 6.3 `30_Projects/Index.md`

建议新增：

```markdown
## XingYu
- [[30_Projects/XingYu/星与产品定位升级]]
- [[30_Projects/XingYu/应援任务解锁系统PRD]]
- [[30_Projects/XingYu/MVP/星与应援任务平台MVP]]
- [[30_Projects/XingYu/MVP/活动页_报名任务解锁结构]]

## Trading Scanner
- [[30_Projects/TradingScanner/盘前热度股扫描器需求]]

## Writing
- [[30_Projects/Writing/华南湿季与ww]]

## Personal System
- [[30_Projects/Personal_System/稳定复利底盘]]

## Body
- [[30_Projects/Body/增肌训练系统]]
```

---

## 6.4 `40_Decisions/Index.md`

建议新增：

```markdown
## Investment Decisions
- [[40_Decisions/Investment_Decisions/2026-05-高弹性成长股模型升级]]
- [[40_Decisions/Investment_Decisions/2026-05-盘前SOP启用]]
- [[40_Decisions/Investment_Decisions/2026-05-扫描器字段升级]]

## Product Decisions
- [[40_Decisions/Product_Decisions/2026-05-星与从社区入口升级为任务中台]]
- [[40_Decisions/Product_Decisions/2026-05-星与新闭环]]

## Personal Decisions
- [[40_Decisions/Personal_Decisions/2026-05-从机会捕捉转向系统复利]]
- [[40_Decisions/Personal_Decisions/2026-05-增肌优先于极限重量]]
```

---

## 6.5 `90_System/Index.md`

建议新增：

```markdown
## Knowledge Rules
- [[90_System/Knowledge_Rules/Braincorn写入规则]]

## AI Workflows
- [[90_System/AI_Workflows/ChatGPT_to_Obsidian_Daily_Capture]]
- [[90_System/AI_Workflows/Codex_Obsidian协作规范]]
- [[90_System/AI_Workflows/每日对话沉淀到Obsidian]]

## Templates
- [[90_System/Templates/Daily_Capture_Template]]
- [[90_System/Templates/盘前交易面板模板]]
- [[90_System/Templates/热度股扫描器字段模板]]
- [[90_System/Templates/股票复盘模板]]
- [[90_System/Templates/训练日志模板]]
- [[90_System/Templates/关系散文修改检查表]]
```

---

# 7. 本周最重要的 5 条长期资产

1. `暴涨股 = 热门主线 × 预期差 × 业绩/订单验证 × 小中盘弹性 × 盘口确认`
2. `题材交易不是买好公司，而是买市场正在共同相信的新身份`
3. `星与不要做流量入口，要做饭圈活动里的任务中台和利益分配器`
4. `湿气不是环境描写，而是关系里无法干脆结束的状态`
5. `你不是缺洞察，而是缺稳定复利结构`
