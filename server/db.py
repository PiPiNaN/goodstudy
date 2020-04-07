import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        conn = sqlite3.connect('hanzi.db')
        return conn
    except Error:
        print(Error)


def sql_table(conn):
    c = conn.cursor()
    c.execute(
        "CREATE TABLE hanzis(id integer PRIMARY KEY, hanzi text, type text, learned integer, passed integer)")
    conn.commit()

def sql_drop_table(conn):
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS hanzis")
    conn.commit()

def insert_top1000hanzi(conn):
    data = [
        "的", "一", "是", "在", "了", "人", "有", "不", "中", "大", "国", "年", "为", "上", "和", "这", "个", "会", "到", "时", "行", "出", "来", "发", "以", "我", "公", "对", "市", "生", "日", "要", "业", "家", "地", "成", "作", "能", "后", "他", "多", "者", "新", "也", "经", "现", "就", "于", "学", "们", "方", "开", "月", "过", "本", "法", "下", "动", "前", "场", "进", "分", "自", "全", "工", "可", "高", "用", "说", "实", "将", "部", "车", "民", "理", "得", "报", "都", "主", "天", "区", "子", "体", "小", "资", "事", "同", "关", "等", "机", "面", "还", "力", "与", "之", "长", "而", "记", "定", "最", "通", "产", "员", "金", "重", "所", "合", "其", "心", "比", "好", "化", "元", "司", "次", "政", "文", "加", "度", "当", "点", "期", "名", "目", "务", "间", "道", "表", "建", "展", "内", "但", "里", "电", "外", "品", "平", "从", "如", "制", "提", "安", "看", "第", "入", "保", "位", "没", "着", "美", "起", "三", "此", "网", "利", "已", "手", "情", "两", "相", "交", "明", "很", "被", "并", "因", "万", "意", "然", "更", "正", "去", "路", "信", "球", "队", "赛", "据", "管", "设", "及", "性", "些", "任", "海", "示", "股", "东", "城", "社", "北", "水", "价", "活", "今", "门", "问", "院", "题", "老", "特", "种", "基", "数", "应", "量", "西", "商", "近", "系", "解", "无", "强", "代", "联", "收", "持", "计", "向", "至", "受", "打", "常", "样", "总", "教", "调", "果", "么", "改", "式", "规", "让", "投", "件", "京", "接", "只", "处", "项", "华", "广", "立", "回", "权", "费", "各", "身", "台", "房", "想", "女", "程", "二", "由", "达", "做", "增", "那", "认", "南", "先", "组", "己", "局", "案", "少", "影", "科", "物", "格", "你", "议", "张", "给", "服", "证", "企", "斯", "导", "办", "视", "深", "推", "告", "查", "结", "战", "该", "委", "山", "专", "传", "统", "周", "运", "马", "书", "标", "或", "放", "线", "每", "原", "单", "求", "十", "治", "风", "共", "首", "布", "消", "级", "口", "集", "气", "世", "知", "决", "节", "别", "感", "创", "济", "领", "转", "指", "未", "息", "选", "军", "直", "众", "整", "术", "头", "育", "她", "把", "需", "取", "流", "非", "完", "省", "医", "王", "责", "再", "四", "考", "续", "师", "变", "造", "客", "话", "尔", "观", "使", "户", "州", "界", "团", "带", "支", "站", "参", "微", "儿", "亚", "校", "称", "几", "乐", "技", "反", "博", "步", "演", "见", "李", "警", "际", "克", "何", "营", "质", "型", "走", "难", "确", "超", "德", "号", "士", "府", "准", "注", "色", "份", "环", "片", "购", "易", "款", "真", "供", "才", "游", "快", "始", "空", "显", "限", "监", "较", "清", "亿", "施", "银", "包", "村", "获", "又", "预", "约", "研", "况", "条", "依", "源", "形", "晚", "备", "讯", "拉", "则", "究", "率", "住", "江", "具", "举", "引", "足", "友", "票", "爱", "销", "孩", "低", "望", "光", "论", "益", "职", "值", "照", "势", "优", "米", "排", "热", "某", "升", "习", "助", "越", "根", "精", "协", "类", "速", "花", "构", "仅", "均", "青", "牌", "效", "党", "图", "随", "存", "革", "农", "险", "什", "容", "历", "防", "群", "义", "段", "边", "音", "连", "居", "五", "划", "干", "财", "字", "买", "采", "往", "态", "林", "太", "即", "复", "神", "负", "审", "融", "售", "配", "季", "巴", "维", "属", "终", "官", "境", "检", "护", "落", "除", "候", "料", "百", "诉", "病", "园", "响", "积", "便", "策", "罗", "装", "严", "试", "奖", "言", "评", "双", "极", "失", "钱", "功", "英", "纪", "范", "半", "觉", "许", "黄", "红", "满", "争", "剧", "媒", "男", "请", "模", "律", "版", "宝", "亲", "白", "象", "致", "县", "断", "控", "置", "声", "火", "像", "必", "离", "养", "批", "星", "店", "刘", "央", "曾", "停", "验", "且", "兰", "思", "艺", "志", "史", "识", "食", "底", "午", "河", "互", "域", "卡", "它", "却", "违", "降", "岁", "介", "送", "春", "早", "额", "算", "执", "陈", "景", "楼", "层", "阿", "列", "远", "副", "港", "希", "织", "旅", "录", "普", "核", "阳", "访", "按", "汽", "围", "善", "班", "讲", "承", "余", "继", "卫", "追", "故", "板", "初", "突", "土", "兴", "铁", "击", "龙", "福", "另", "命", "健", "读", "富", "鲁", "留", "例", "油", "破", "担", "修", "充", "坚", "找", "宣", "刚", "石", "切", "够", "眼", "昨", "胜", "听", "货", "夫", "尽", "频", "轻", "愿", "伤", "仍", "判", "念", "庭", "镇", "辆", "盘", "飞", "待", "吃", "占", "药", "届", "拿", "申", "跟", "器", "航", "香", "察", "写", "康", "虽", "闻", "欧", "轮", "补", "语", "否", "奥", "酒", "救", "席", "绍", "临", "独", "喜", "状", "露", "紧", "角", "招", "压", "假", "括", "谈", "素", "减", "室", "圳", "免", "登", "拍", "测", "疑", "套", "帮", "播", "古", "温", "卖", "齐", "择", "止", "涉", "波", "付", "欢", "适", "死", "授", "载", "八", "彩", "券", "训", "云", "络", "纳", "练", "移", "幅", "遇", "细", "涨", "画", "略", "韩", "疗", "短", "街", "馆", "稳", "左", "钟", "罪", "杨", "千", "母", "湖", "洲", "族", "戏", "换", "冠", "右", "六", "乡", "差", "派", "尼", "索", "黑", "智", "奇", "武", "含", "味", "宁", "培", "令", "甚", "苏", "密", "激", "怎", "父", "浪", "座", "歌", "障", "妈", "币", "绩", "犯", "退", "签", "印", "摄", "威", "启", "块", "害", "端", "须", "绝", "竞", "简", "材", "托", "贷", "透", "急", "血", "述", "吸", "亮", "似", "俄", "乎", "编", "课", "岛", "良", "庆", "享", "借", "松", "秀", "津", "困", "税", "厂", "租", "促", "守", "征", "错", "背", "哪", "顺", "朋", "缺", "川", "杯", "汉", "泰", "抓", "患", "董", "冲", "础", "乌", "婚", "挥", "纷", "绿", "丽", "呢", "梦", "雷", "田", "督", "惠", "幕", "迎", "丰", "刻", "尚", "析", "逐", "章", "巨", "攻", "败", "召", "措", "菜", "久", "朝", "笔", "沙", "礼", "峰", "顾", "诺", "舞", "染", "驾", "童", "餐", "陆", "罚", "序", "稿", "针", "综", "净", "永", "靠", "雨", "污", "延", "悉", "吴", "拥", "迷", "损", "鲜", "禁", "厅", "毒", "伊", "贵", "孙", "输", "皮", "予", "七", "私", "佳", "码", "毕", "跌", "木", "笑", "乘", "般", "兵", "汇", "坐", "典", "树", "伟", "倒", "危", "爆", "跑", "阶", "债", "束", "贸", "探", "润", "刑", "叫", "玩", "休", "截", "谢", "夜", "异", "烟", "询", "雪", "荣", "附", "夏", "裁", "吗", "抢", "映", "哈", "晓", "赵", "库", "订", "贴", "曲", "桥", "答", "归", "遭"
    ]
    c = conn.cursor()
    i = 0
    for h in data:
        entity = (i, h, "top1000", 0, 0)
        i+=1
        c.execute("INSERT INTO hanzis VALUES(?, ?, ?, ?, ?)", entity)
    conn.commit()

def update_data(conn, d):
    c = conn.cursor()
    c.execute("UPDATE hanzis SET hanzi = ?, type= ?, learned=?, passed=? WHERE id = ?", d)
    conn.commit()

def get_data(conn, id):
    c = conn.cursor()
    d = c.execute("SELECT * FROM hanzis WHERE id = ?", id)
    #for r in d:
    #    print(r)
    result = d.fetchall()
    print(result)
    return result
        

con = sql_connection()
#sql_drop_table(con)
#sql_table(con)
#insert_top1000hanzi(con)
get_data(con, (0,))
d = ('的', 'top1000', 2, 3, 0)
update_data(con, d)
get_data(con, (0,))