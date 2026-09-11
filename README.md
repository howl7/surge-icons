# Howl Surge Icons

个人定制高精 Retina 正圆策略组图标库，供 [Surge](https://nssurge.com/) / Loon 等客户端订阅使用。

- 画布：256×256 px，RGBA 透明通道，圆形外部 100% 纯透明
- 圆形几何：居中 `cx=128, cy=128`，半径 `r=118`（四周留 10px 安全边距）
- 国旗：统一 2.5px 黑色细边框 `#1A1A1A`
- 非国旗（流媒体 / AI / 品牌 / 工具）：一律纯净无描边
- 分类：`Country` `Media` `AI` `Brand` `Tool`，共 31 枚

---

## 在 Surge 中订阅

### 推荐：版本化直链（即时生效，杜绝 CDN 与客户端缓存）

由于 jsDelivr CDN 与 iOS 网络栈对 `@main` 分支有较长时间的强缓存，**强烈推荐使用 Git Tag 版本化链接订阅**：

```text
https://cdn.jsdelivr.net/gh/howl7/surge-icons@v1.0.1/surge-icon.json
```

### 备用：滚动更新直链（随 main 分支更新，受 CDN 缓存约 12h-7d 影响）

```text
https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/surge-icon.json
```

也可以用 GitHub raw 直链（无 CDN 加速，需代理支持）：

```text
https://raw.githubusercontent.com/howl7/surge-icons/main/surge-icon.json
```

订阅成功后，编辑策略组时即可在图标选择器中按分类（Country / Media / AI / Brand / Tool）浏览并点选。

> ⚠️ **客户端缓存注意**：Surge iOS 主界面上已经绑定的策略组卡片，在图标库更新后不会自动热重载，需在策略组设置中重新点选一次该图标。

---

## 图标索引

### Country

| 预览 | 名称 | 直链 |
|:---:|:---|:---|
| ![America](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/America.png) | America | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/America.png` |
| ![China](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/China.png) | China | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/China.png` |
| ![HongKong](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/HongKong.png) | HongKong | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/HongKong.png` |
| ![Japan](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Japan.png) | Japan | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Japan.png` |
| ![Korea](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Korea.png) | Korea | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Korea.png` |
| ![Singapore](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Singapore.png) | Singapore | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Singapore.png` |
| ![Taiwan](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Taiwan.png) | Taiwan | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/Taiwan.png` |
| ![UnitedKingdom](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/UnitedKingdom.png) | UnitedKingdom | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Country/UnitedKingdom.png` |

### Media

| 预览 | 名称 | 直链 |
|:---:|:---|:---|
| ![Disney](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Disney.png) | Disney | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Disney.png` |
| ![HBOMax](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/HBOMax.png) | HBOMax | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/HBOMax.png` |
| ![Hulu](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Hulu.png) | Hulu | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Hulu.png` |
| ![Netflix](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Netflix.png) | Netflix | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Netflix.png` |
| ![Peacock](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Peacock.png) | Peacock | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Peacock.png` |
| ![PrimeVideo](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/PrimeVideo.png) | PrimeVideo | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/PrimeVideo.png` |
| ![Spotify](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Spotify.png) | Spotify | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/Spotify.png` |
| ![TVB](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/TVB.png) | TVB | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/TVB.png` |
| ![TVB_ball](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/TVB_ball.png) | TVB_ball | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/TVB_ball.png` |
| ![TVB_frame](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/TVB_frame.png) | TVB_frame | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/TVB_frame.png` |
| ![YouTube](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/YouTube.png) | YouTube | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Media/YouTube.png` |

### AI

| 预览 | 名称 | 直链 |
|:---:|:---|:---|
| ![Antigravity](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/AI/Antigravity.png) | Antigravity | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/AI/Antigravity.png` |
| ![Claude](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/AI/Claude.png) | Claude | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/AI/Claude.png` |
| ![Codex](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/AI/Codex.png) | Codex | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/AI/Codex.png` |

### Brand

| 预览 | 名称 | 直链 |
|:---:|:---|:---|
| ![Apple](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Brand/Apple.png) | Apple | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Brand/Apple.png` |
| ![Google](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Brand/Google.png) | Google | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Brand/Google.png` |
| ![Nintendo](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Brand/Nintendo.png) | Nintendo | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Brand/Nintendo.png` |

### Tool

| 预览 | 名称 | 直链 |
|:---:|:---|:---|
| ![Mitaka](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/Mitaka.png) | Mitaka | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/Mitaka.png` |
| ![PayPal](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/PayPal.png) | PayPal | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/PayPal.png` |
| ![Speedtest](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/Speedtest.png) | Speedtest | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/Speedtest.png` |
| ![Surge](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/Surge.png) | Surge | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/Surge.png` |
| ![YToo](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/YToo.png) | YToo | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/YToo.png` |
| ![YToo_blue](https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/YToo_blue.png) | YToo_blue | `https://cdn.jsdelivr.net/gh/howl7/surge-icons@main/icons/Tool/YToo_blue.png` |

---

## 维护与版本发布 SOP
 
新增或调整图标后，推荐使用 Git Tag 方式发布，彻底避免 CDN 与客户端缓存滞后：
 
```bash
# 1. 放入符合规范的 PNG 文件至 icons/<分类>/<名称>.png
 
# 2. 生成对应 Tag 的图标库 JSON（例如发布 v1.0.2）
python3 generate-icon-json.py --repo howl7/surge-icons --branch v1.0.2 \
  --name "Howl-Surge-Icons" \
  --desc "个人定制高精 Retina 正圆策略组图标库 · 256x256 · 国旗细黑边 / 非国旗无描边" \
  --icons-dir icons --out surge-icon.json
 
# 3. 提交并打 Git Tag 推送
git add -A
git commit -m "feat(icons): release v1.0.2"
git tag -a v1.0.2 -m "release v1.0.2"
git push origin main
git push origin v1.0.2
```
 
图标设计规约：256×256 px、RGBA、圆形外部纯透明、国旗 2.5px 黑边 `#1A1A1A`、非国旗无描边。

---

## 免责声明

本仓库仅收录用于 Surge/Loon 策略组显示的图标图形，均为个人二次绘制/加工用于私人网络工具配置展示，不涉及任何品牌官方发布内容，不含任何节点凭据、订阅链接或个人隐私信息。若涉及版权问题，请提交 issue，将第一时间处理。
