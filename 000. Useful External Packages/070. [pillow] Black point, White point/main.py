from PIL import Image

bl_negative = 64
bl_positive = 95
# 비관적으로 평균 64 이하, 낙관적으로 95 이하 정도가 블랙 포인트

wh_negative = 192
wh_positive = 156
# 비관적으로 평균 192 이상, 낙관적으로 156 이상 정도가 화이트 포인트

bl_strength = int(input('Black point strength(1~100) : '))
assert bl_strength > 0
assert bl_strength < 101
bl_strength = bl_strength * 0.45
# 완전히 새까맣게 되어버리는 걸 방지

wh_strength = int(input('White point strength(1~100) : '))
assert wh_strength > 0
assert wh_strength < 101
wh_strength = wh_strength * 0.6
# 완전히 새하얗게 되어버리는 걸 방지

# strength가 높을 수록 낙관적으로, 강하게 적용
img = Image.open('sample_image.jpg')
pixels = img.load()
width, height = img.size

chosen_bl = bl_negative + (bl_positive - bl_negative) / 100 * bl_strength
# 낙관적인 정도

chosen_wh = wh_negative - (wh_negative - wh_positive) / 100 * bl_strength
# 낙관적인 정도

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        rgb_avg = sum((r, g, b)) / 3
        # RGB의 평균

        if rgb_avg < chosen_bl:
            # 어두운 기준보다 더 어두울 때
            new_rgb = (int(r - r / 100 * bl_strength), int(g - g / 100 * bl_strength), int(b - b / 100 * bl_strength))
            pixels[i, j] = new_rgb
        elif rgb_avg > chosen_wh:
            # 밝은 기준보다 더 밝을 때
            new_rgb = (int(r + r / 100 * wh_strength), int(g + g / 100 * wh_strength), int(b + b / 100 * wh_strength))
            pixels[i, j] = new_rgb

img.save('new_image.jpg')
