import json


SITES = [
    {
        "url": "https://webs-mahjonghu.com",
        "keyword": "麻将胡了",
        "tags": ["麻将", "棋牌", "娱乐", "胡牌"],
        "description": "一个提供在线麻将胡牌玩法的游戏平台，支持多种经典和变体规则。"
    },
    {
        "url": "https://webs-mahjonghu.com/classic",
        "keyword": "经典麻将",
        "tags": ["麻将", "经典", "四人"],
        "description": "经典四人麻将模式，适合传统麻将爱好者。"
    },
    {
        "url": "https://webs-mahjonghu.com/speed",
        "keyword": "极速胡了",
        "tags": ["麻将", "极速", "快节奏"],
        "description": "快节奏麻将玩法，每局时间缩短，适合碎片时间娱乐。"
    }
]


def generate_summary(site):
    """为单个站点生成结构化摘要"""
    summary = {
        "title": site["keyword"],
        "url": site["url"],
        "tags": site["tags"],
        "description": site["description"]
    }
    return summary


def format_summary(summary):
    """将摘要格式化为易读字符串"""
    lines = []
    lines.append(f"【站点标题】{summary['title']}")
    lines.append(f"【访问地址】{summary['url']}")
    lines.append(f"【标签】{'、'.join(summary['tags'])}")
    lines.append(f"【简要说明】{summary['description']}")
    return "\n".join(lines)


def generate_all_summaries(sites):
    """对所有内置站点生成摘要并返回列表"""
    result = []
    for site in sites:
        summ = generate_summary(site)
        result.append(summ)
    return result


def print_summaries(sites):
    """打印所有站点的完整结构化摘要"""
    summaries = generate_all_summaries(sites)
    for idx, summ in enumerate(summaries, start=1):
        print(f"========== 站点 {idx} ==========")
        print(format_summary(summ))
        print()


def main():
    print("内置站点资料结构化摘要（共 {} 个站点）\n".format(len(SITES)))
    print_summaries(SITES)


if __name__ == "__main__":
    main()