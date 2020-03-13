from .custom_config import MENU_CUISINE_LIST, MENU_TYPE_LIST, MENU_STYLE_LIST, MENU_KEYWORD_LIST
from .utils import pcAbilityDict, pcSavingDict, pcSkillDict, pcSheetTemplate
HELP_STR = 'Dice++ by 梨子 Ver 0.5.2\n'
HELP_STR += '@骰娘 .bot on/off 开启或关闭骰娘\n'
HELP_STR += '.help指令 查看指令列表\n'
HELP_STR += '.help链接 查看源码地址\n'
HELP_STR += '.help协议 查看使用协议\n'
HELP_STR += '.help更新 查看最近更新内容\n'
HELP_STR += '本骰娘的绝活包括:优劣势投骰, 强大的查询功能, 记录生命值和角色卡, 加强版先攻列表等\n'
HELP_STR += '欢迎加入交流群:861919492'

SHOW_STR = 'Dice++ by 梨子 Ver 0.5.2 @骰娘 .bot on/off 开启或关闭骰娘\n'
SHOW_STR += '输入.help更新 查看最近更新内容\n'
SHOW_STR += '本骰娘的绝活包括:优劣势投骰, 强大的查询功能, 记录生命值和角色卡, 加强版先攻列表等\n'
SHOW_STR += '欢迎加入交流群:861919492或联系开发者:821480843报告bug和提出意见~'

HELP_COMMAND_UPDATE_STR = '2020/3/13 v0.5.2:\n1.可以查询怪物图鉴(by花作噫, 梨子)了(包括怪物种类, 怪物清单等)\n2.投骰时如果第一个骰子是d20会提示大成功或大失败\n'
HELP_COMMAND_UPDATE_STR += '2020/3/10 v0.5.1:\n1.可以查询拓展与模组魔法物品(by惠惠)和拓展职业(by惠惠, 梨子)了\n2.nn指令也会修改先攻列表中的名字\n3.录入角色卡和检定时会自动转换一些同义词, 如:说服->游说\n4.新增.send功能\n'
HELP_COMMAND_UPDATE_STR += '2020/3/10 v0.5.0:\n1.新增录入角色卡和一键检定功能\n2.直接at骰娘在关闭状态下也可以响应\n3.sethp关键字被简化为hp\n4.dismiss指令仅在@骰娘的情况下有效\n'
HELP_COMMAND_UPDATE_STR += '2020/3/8 v0.4.1:\n1.新增点菜, 今日菜单功能\n2.加入大量可查询内容\n3.可以识别群名片作为默认昵称了\n'
HELP_COMMAND_UPDATE_STR += '画饼中的功能请在交流群:861919492查看~'

HELP_COMMAND_STR = '主要指令包括:\n'
HELP_COMMAND_STR += '@骰娘 .bot 开关\n'
HELP_COMMAND_STR += '@骰娘 .dismiss 使骰娘退群\n'
HELP_COMMAND_STR += '.r 掷骰\n'
HELP_COMMAND_STR += '.nn 设置昵称\n'
HELP_COMMAND_STR += '.ri 先攻\n'
HELP_COMMAND_STR += '.init 先攻列表\n'
HELP_COMMAND_STR += '.hp 记录/调整生命值\n'
HELP_COMMAND_STR += '.角色卡 录入角色卡等功能, 请输入.help角色卡查看具体说明\n'
HELP_COMMAND_STR += '.检定 自动检定功能, 请输入.help检定查看具体说明\n'
HELP_COMMAND_STR += '.查询 查询资料\n'
HELP_COMMAND_STR += '.draw 抽取牌库\n'
HELP_COMMAND_STR += '.烹饪 进行随机的烹饪检定\n'
HELP_COMMAND_STR += '.点菜 模拟点菜\n'
HELP_COMMAND_STR += '.今日菜单\n'
HELP_COMMAND_STR += '.dnd 初始属性作成\n'
HELP_COMMAND_STR += '.jrrp 今日人品\n'
HELP_COMMAND_STR += '.send 单方面向Master发送消息\n'
HELP_COMMAND_STR += '骰娘会自动去掉大多数空格以及转换小写, 多数指令需要后接参数, 详细用法请输入.help [指令名]查询, 如.help hp'

HELP_LINK_STR = 'Dice++是基于Python, NoneBot和酷Q的骰子机器人项目\n'
HELP_LINK_STR += '项目地址: https://github.com/haowen-li/DicePP'


HELP_AGREEMENT_STR =  '0.本协议是Dice++的服务协议。\n'
HELP_AGREEMENT_STR += '1.邀请骰娘, 使用掷骰服务和在群内阅读此协议视为同意并承诺遵守此协议，否则请移除骰娘。\n'
HELP_AGREEMENT_STR += '2.不允许禁言骰娘或刷屏掷骰等对骰娘的不友善行为，这些行为将会提高骰娘被制裁的风险。开关骰娘响应请使用.bot on/off。\n'
HELP_AGREEMENT_STR += '3.骰娘默认邀请行为已事先得到群内同意，因而会自动同意群邀请。因擅自邀请而使骰娘遭遇不友善行为时，邀请者因未履行预见义务而将承担连带责任。\n'
HELP_AGREEMENT_STR += '4.禁止将骰娘用于赌博及其他违法犯罪行为。\n'
HELP_AGREEMENT_STR += '5.对于设置敏感昵称等无法预见但有可能招致言论审查的行为，骰娘可能会出于自我保护而拒绝提供服务\n'
HELP_AGREEMENT_STR += '6.由于技术以及资金原因，无法保证骰娘100%的时间稳定运行，可能不定时停机维护或遭遇冻结，敬请谅解。\n'
HELP_AGREEMENT_STR += '7.对于违反协议的行为，骰娘将视情况终止对用户和所在群提供服务。\n'
HELP_AGREEMENT_STR += '8.本协议内容随时有可能改动。请注意帮助信息。\n'
HELP_AGREEMENT_STR += '9.Dice++参考了Dice! by 溯洄 Shiki的部分文字和指令设定, 但没有借鉴或复制任何代码, 如有疑问请联系qq:821480843。\n'
HELP_AGREEMENT_STR += '10.本服务最终解释权归服务提供方所有。'

HELP_COMMAND_R_STR =  '掷骰：.r[掷骰表达式]([掷骰原因]) [掷骰表达式]：([轮数]#)[个数]d面数(优/劣势)(k[取点数最大的骰子数])不带面数时视为掷一个默认的20面骰\n'
HELP_COMMAND_R_STR += 'r后加h即为暗骰\n'
HELP_COMMAND_R_STR += '示例:\n'
HELP_COMMAND_R_STR += '.rd20+1d4+4\n'
HELP_COMMAND_R_STR += '.r4#d    //投4次d20\n'
HELP_COMMAND_R_STR += '.rd20劣势+4 //带劣势攻击\n'
HELP_COMMAND_R_STR += '.r2#d优势+4 攻击被束缚的地精 //两次有加值的优势攻击\n'
HELP_COMMAND_R_STR += '.r1d12+2d8+5抗性 //得到减半向下取整的投骰总值'

HELP_COMMAND_NN_STR =  '设置昵称：.nn [昵称]\n'
HELP_COMMAND_NN_STR += '私聊.nn视为操作全局昵称\n'
HELP_COMMAND_NN_STR += '昵称优先级:群昵称>私聊昵称>群名片>QQ昵称\n'
HELP_COMMAND_NN_STR += '群聊中的nn指令会智能修改先攻列表中的名字\n'
HELP_COMMAND_NN_STR += '示例:\n'
HELP_COMMAND_NN_STR += '.nn	//视为删除昵称\n'
HELP_COMMAND_NN_STR += '.nn dm //将昵称设置为dm'

HELP_COMMAND_COOK_STR =  '烹饪菜肴：.烹饪([优劣势][加值]) (用/分隔的关键词列表)\n'
HELP_COMMAND_COOK_STR += '强烈建议加上关键词'
HELP_COMMAND_COOK_STR += f'可用关键词为: \n菜系:{MENU_CUISINE_LIST}\n风格:{MENU_STYLE_LIST}\n种类:{MENU_TYPE_LIST}\n'
HELP_COMMAND_COOK_STR += '示例:\n'
HELP_COMMAND_COOK_STR += '.烹饪 //随机烹饪食物, 可能遇到黑暗料理\n'
HELP_COMMAND_COOK_STR += '.烹饪优势 野炊/主食 //以优势烹饪含有野炊与主食关键字的食物'

HELP_COMMAND_ORDER_STR =  '点菜：.点菜(数量) (用/分隔的关键词列表)\n'
HELP_COMMAND_ORDER_STR += '强烈建议加上关键词'
HELP_COMMAND_ORDER_STR += f'可用关键词为: \n菜系:{MENU_CUISINE_LIST}\n风格:{MENU_STYLE_LIST}\n种类:{MENU_TYPE_LIST}\n'
HELP_COMMAND_ORDER_STR += '示例:\n'
HELP_COMMAND_ORDER_STR += '.点菜 //随机点一道菜, 可能遇到黑暗料理\n'
HELP_COMMAND_ORDER_STR += '.点菜4 野炊/主食 //点4道含有野炊与主食关键字的食物'

HELP_COMMAND_RI_STR =  '加入先攻(群聊限定)：.ri([优劣势][加值]) ([名称])\n'
HELP_COMMAND_RI_STR += '示例:\n'
HELP_COMMAND_RI_STR += '.ri优势+1 //以昵称加入先攻列表\n'
HELP_COMMAND_RI_STR += '.ri20 地精 //将地精以固定先攻20加入先攻列表'

HELP_COMMAND_INIT_STR =  '显示先攻列表：.init ([可选指令]) [可选指令]:clr 清空先攻列表 del 删除指定先攻条目\n'
HELP_COMMAND_INIT_STR += 'del指令支持部分匹配\n'
HELP_COMMAND_INIT_STR += '示例:\n'
HELP_COMMAND_INIT_STR += '.init //查看先攻列表\n'
HELP_COMMAND_INIT_STR += '.init clr //清空先攻列表\n'
HELP_COMMAND_INIT_STR += '.init del 地精 //在先攻列表中删除地精'

HELP_COMMAND_QUERY_STR =  '查询资料: .查询 查询目标\n'
HELP_COMMAND_QUERY_STR += '查询指令支持部分匹配, 可用/区分多个关键字\n'
HELP_COMMAND_QUERY_STR += '目前可查询的内容有: 玩家手册(by梨子,花作噫,邪恶,赵小安,睡帽), 全拓展法术与专长, 怪物图鉴(by花作噫, 梨子), 拓展职业(by惠惠, 梨子), 核心与拓展魔法物品(by花作噫, 惠惠)\n'
HELP_COMMAND_QUERY_STR += '示例:\n'
HELP_COMMAND_QUERY_STR += '.查询 借机攻击\n'
HELP_COMMAND_QUERY_STR += '.查询 长弓\n'
HELP_COMMAND_QUERY_STR += '.查询 法师/6环'

HELP_COMMAND_DRAW_STR =  '抽取牌库: .draw 目标牌库\n'
HELP_COMMAND_DRAW_STR += '目标牌库支持部分匹配, 可用/区分多个关键字\n'
HELP_COMMAND_DRAW_STR += '查看支持的牌库请输入.draw'

HELP_COMMAND_SETHP_STR =  '记录/调整生命值: .hp ([调整目标])([符号]) [骰子表达式/数值](/[最大生命值])\n'
HELP_COMMAND_SETHP_STR += '生命值信息将在.init的结果中显示\n'
HELP_COMMAND_SETHP_STR += '不输入符号与目标时默认为对自己的"="操作\n'
HELP_COMMAND_SETHP_STR += '不设置生命值则会显示已损失生命值\n'
HELP_COMMAND_SETHP_STR += 'pc生命值信息与先攻列表独立\n'
HELP_COMMAND_SETHP_STR += '查询目标支持部分匹配先攻列表中的条目\n'
HELP_COMMAND_SETHP_STR += '注意dm用.ri [pc名字]将pc加入先攻列表时, 该条目不会和pc的生命值自动关联, 需要pc自己用.ri加入先攻列表\n'
HELP_COMMAND_SETHP_STR += '示例:\n'
HELP_COMMAND_SETHP_STR += '.hp 地精- 1d12+2 // 对地精造成1d12+2点伤害\n'
HELP_COMMAND_SETHP_STR += '.hp 20/30 // 将自己的生命值设置为20, 最大生命值设置为30\n'
HELP_COMMAND_SETHP_STR += '.hp 杰+ 1d8+3 // 在先攻列表中匹配名字中有杰的对象, 然后给其增加1d8+3的生命值\n'
HELP_COMMAND_SETHP_STR += '.hp // 删除自己的生命值信息'

HELP_COMMAND_JRRP_STR =  '这个指令也不清楚怎么用吗? #吃惊\n'
HELP_COMMAND_JRRP_STR += '.jrrp 查看今日人品'

HELP_COMMAND_MENU_STR =  '.今日菜单 查看今日菜单, 找不到对应关键词的菜肴时会删减关键词甚至删掉这道菜'

HELP_COMMAND_PC_STR =  '角色卡相关功能: .角色卡 ([可选指令]) [可选指令]: 录入 [角色卡模板]; 查看 (默认选项); '
HELP_COMMAND_PC_STR += '完整 (查看完整的角色卡); 删除\n'
HELP_COMMAND_PC_STR += '录入角色卡后(查看模板请输入.角色卡模板), 就可以使用相关的检定与豁免功能了, 查看详情请输入.help检定\n'
HELP_COMMAND_PC_STR += '提示:\n- 必填的内容是六个基本属性,熟练加值与熟练项,其他内容为选填\n- 不要去掉模板中的换行'
HELP_COMMAND_PC_STR += '- 在额外加值里写"检定+1"的话, 会把所有检定(不包括豁免)哦~ 同理, 写"豁免+1",会将所有豁免的结果都加1\n'
HELP_COMMAND_PC_STR += '  如果携带了幸运石, 就在额外加值处写上豁免+1/检定+1吧\n'
HELP_COMMAND_PC_STR += '- 录入角色卡时输入的名称等同于.nn [名称], 输入的生命值信息等同于.hp [生命值]/[最大生命值]\n'
HELP_COMMAND_PC_STR += '- 如果不确定自己的理解是否正确的话, 输入".角色卡 完整"确认一下吧~\n'
HELP_COMMAND_PC_STR += '- 查看所有技能名请输入.help技能'

HELP_COMMAND_SKILL_STR = f'所有技能关键字:{list(pcSkillDict.keys())}'

HELP_COMMAND_SEND_STR = f'发送消息：.send 想对Master说的话\n如果用来调戏Master请做好心理准备'

HELP_COMMAND_CHECK_STR = '属性检定系列功能: .[属性检定或豁免检定][优/劣势][加值] [原因]\n'
HELP_COMMAND_CHECK_STR += '必须先设定角色卡才能使用哦~\n'
HELP_COMMAND_CHECK_STR += '属性检定其实没有大成功和大失败, 只是娱乐效果; 难度等级来自于玩家手册, 仅供参考。\n'
HELP_COMMAND_CHECK_STR += '示例:\n'
HELP_COMMAND_CHECK_STR += '.力量检定优势+1d4 掀开井盖\n'
HELP_COMMAND_CHECK_STR += '.说服检定\n'
HELP_COMMAND_CHECK_STR += '.敏捷豁免优势\n'
HELP_COMMAND_CHECK_STR += '.体质豁免+4 圣武士光环'