def take_magic_damage(health, resist, amp, spell_power):
    print(health)
    magic_damage = (amp * spell_power) - resist
    print(magic_damage)
    health = health - magic_damage
    print(health)
    return health

def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    print("After xp: ", after_xp)
    alert = "Achievement Unlocked: " + ach_name
    print(alert)
    return after_xp, alert
