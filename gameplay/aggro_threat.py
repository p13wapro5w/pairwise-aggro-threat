import math


def heal_threat(heal, factor):
    """治疗威胁：有效治疗量按威胁系数折算。"""
    return heal * factor


def taunt_locked(now, until):
    """嘲讽锁定：当前时间仍在锁定期内则返回 True。"""
    return now < until


def in_los(angle, limit):
    """视线判定：目标偏离朝向的夹角在视野阈值内。"""
    return abs(angle) <= abs(limit)


def clear_on_death(alive):
    """死亡清表：存活为 False 时需要清除仇恨。"""
    return not alive


def dot_merge(ticks):
    """dot 合并：同一施法者的持续伤害跳数合并为一次仇恨。"""
    return sum(ticks)


def pet_owner(pet, owner):
    """宠物归属：宠物仇恨独立归属其当前主人。"""
    return owner


def taunt_stack(current, incoming):
    """嘲讽叠加：新增嘲讽在原有仇恨上累加，不清零。"""
    return current + incoming


def phase_keep(threat, ratio):
    """阶段保留：阶段切换时按比例保留仇恨。"""
    return threat * ratio


def decay(threat, rate, dt):
    """仇恨衰减：按速率与时长衰减，结果不低于 0。"""
    return max(0.0, threat * (1.0 - rate * dt))


def in_hardcut(elapsed, window):
    """硬切窗口：切换目标后的窗口期内仍允许嘲讽生效。"""
    return elapsed < window


def add_threat(a, b):
    """仇恨累加。"""
    return a + b


def top_threat(values):
    """最高仇恨：返回仇恨表中的最大值，空表返回 0。"""
    return max(values) if values else 0


def range_ok(distance, radius):
    """范围判定：距离不超过半径。"""
    return distance <= radius


def aggro_key(seed, index):
    """仇恨键：由种子与序号生成唯一键。"""
    return f"{seed}:{index}"


def reset_threat(value):
    """重置：清空仇恨。"""
    return 0
