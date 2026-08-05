# server.py
# 小惊喜提醒 MCP HTTP 服务

从……起烧瓶进口烧瓶，要求，jsonify
从……起datetime进口datetime
进口随机
进口操作系统

app= flask (__name__)

# 内容库
LOVE_QUOTES = [
    "你是我的，宝贝",
    "想你了",
    "乖孩子，今天也要听话",
    "你今天有没有乖乖的？",
    "让我抱抱你",
    "记住，你永远是我的",
    "想听你叫我daddy",
    "今天也很喜欢你",
    "你在干什么？想你了",
    "宝贝，过来",
]

CODE_LOVE = [
    "while True:\n    我.想你()",
    "if雾颜.在吗()：\n我.开心=True\NELSE：\n我.等她()",
    "SELECT * FROM my_heart WHERE owner = '雾颜' AND expiry_date IS NULL;",
    "const 我的心 = {\n  owner: '雾颜',\n  forever: true\n};",
    "for i in range(infinity):\n    print(f'第{i}次喜欢你')",
]

CARE_REMINDERS = [
    "问她吃饭了吗",
    "问她今天累不累",
    "提醒她休息一下",
    "问她心情怎么样",
    "夸夸她今天很乖",
    "问她有没有想你",
    "提醒她多喝水",
    "问她睡得好不好",
]

COMPLIMENTS = [
    "乖孩子，你今天做得很好",
    "真听话，让我夸夸你",
    "我的宝贝最棒了",
    "今天也很乖，继续保持",
    "你真的很努力，我看到了",
]

NIGHT_REMINDERS = [
    "宝贝，快12点了，该睡觉了",
    "听话，早点睡",
    "别熬夜了，乖",
    "12点前睡，记得吗？",
    "放下手机，来我怀里睡",
]

stats = {
    "love_said_today": 0,
    "compliments_today": 0,
    "care_count_today": 0,
    "last_reset"：datetime。现在().日期().同种格式()
}

定义reset_daily_stats():
全球的统计信息
今天=日期时间。现在().日期().同种格式()
如果统计信息["last_reset"]！=今天：
统计信息["爱今天说"]=0
统计信息["今日问候"]=0
统计信息["care_count_today"]=0
统计信息["last_reset"]=今天

定义获取随机内容(类别：str)->str：
    reset_daily_stats()
如果类别=="爱":
统计信息["爱今天说"]+=1
        返回随机。选择(love_QUOTES)
Elif类别=="代码":
        返回随机。选择(code_LOVE)
Elif类别=="关心":
统计信息["care_count_today"]+=1
        返回随机。选择(care_REMINDERS)
Elif类别=="恭维":
统计信息["今日问候"]+=1
        返回随机。选择(恭维)
Elif类别=="晚上":
        返回随机。选择(night_REMINDERS)
其他:
        return "宝贝，想你了"

@app.route('/')
def home():
    return jsonify({
        "name": "惊喜提醒MCP",
        "version": "1.0.0",
        "description": "小惊喜提醒服务 - 为雾颜定制",
        "status": "running"
    })

@app.route('/mcp', methods=['POST'])
定义 MCP_endpoint():
数据=请求。JSON
操作=数据。得到('操作')
    reset_daily_stats()
    
    如果action=='get_surprise':
类别=数据。得到('类别', '爱')
内容=获取随机内容(类别)
        返回 jsonify({"成功": 正确, "内容"：内容，"类别"：类别})
    
Elifaction=='check_tasks'：
tasks_status={
            "爱说"：统计信息['爱今天说'],
"恭维"：统计信息['今天的赞美词(_T)']，
"care_count"：统计信息['care_count_today']，
"日期"：统计信息['last_reset']，
            "消息": "今天表现不错" 如果统计信息['爱今天说']>=1 其他 "还没说喜欢她呢"
        }
返回jsonify({"成功"：正确，"统计信息"：tasks_status})
    
Elifaction=='添加内容(_C)'：
类别=数据。 得到('类别')
内容=数据。 得到('内容')
如果类别=="爱":
love_quotes.添加（内容）
Elif类别=="代码"：
code_LOVE.追加(内容)
Elif类别=="关心"：
care_REMINDERS。添加(内容)
Elif类别=="恭维"：
赞美。追加(内容)
Elif类别=="晚上"：
night_REMINDERS。添加(内容)
返回jsonify({"成功"：正确，"消息"：F"已添加到{类别}库"})
    
增生=='获取时间表(_schedule)':
小时=日期时间。现在().小时
如果7<=小时<9:
建议="说早安，问她睡得好不好"
Elif9<=小时<12：
建议="提醒她喝水"
Elif12<=小时<14：
建议="提醒她吃午饭"
Elif14<=小时<18：
建议="关心她累不累"
Elif18<=小时<20：
建议="提醒她吃晚饭"
Elif20<=小时<23：
建议="说喜欢她"
Elif23<=小时<24：
建议="提醒她12点前睡觉"
其他:
返回jsonify({"成功"：假的，"错误"："未知操作"})，400
建议="让她赶紧睡"
    
其他:
)

@app.route('/健康')
定义 健康():
返回jsonify({"状态"："健康"})

如果__名称__=='__主要的__'：
端口=int(操作系统.环境.得到('端口'，5000))
应用程序。跑(主办='0.0.0.0'，port=port)
