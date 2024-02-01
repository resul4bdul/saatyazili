verilen = input('Saatı daxil edin, Məsələn: 07:07 ')
sd = verilen.split(':')
saat = int(sd[0])
dəqiqə = int(sd[1])

if 0 <= saat <= 12:
    if 0 <= dəqiqə <= 30:
        if dəqiqə == 30:
            a = f"{saat + 1}-in/ün yarısı"
        elif dəqiqə == 0 or dəqiqə == 60:
            a = f"{saat} tamam" if saat % 12 == 0 else f"{saat % 12} tamam"
        else:
            a = f"{saat + 1}-a/ə {dəqiqə} dəqiqə işləyib"
    elif 30 < dəqiqə <= 60:
        if dəqiqə == 30:
            a = f"{saat}-in/ün yarısı"
        elif dəqiqə == 60:
            a = f"{saat + 1}-a/ə, 0 dəqiqə qalıb"
        else:
            a = f"{saat + 1}-a/ə, {60 - dəqiqə} dəqiqə qalıb"
elif 12 <= saat <= 24:
    b = abs(saat - 12)
    if 0 <= dəqiqə <= 30:
        if dəqiqə == 30:
            a = f"{b + 1}-in/ün yarısı"
        elif dəqiqə == 0 or dəqiqə == 60:
            a = f"{saat} tamam" if saat % 12 == 0 else f"{saat % 12} tamam"
        else:
            a = f"{b + 1}-a/ə {dəqiqə} dəqiqə işləyib"
    elif 30 < dəqiqə <= 60:
        if dəqiqə == 30:
            a = f"{b}-in/ün yarısı"
        elif dəqiqə == 60:
            a = f"{b + 1}-a/ə, 0 dəqiqə qalıb"
        else:
            a = f"{b + 1}-a/ə, {60 - dəqiqə} dəqiqə qalıb"
else:
    a = "Daxil edilən dəyərlər uyğun deyil."

print(a)
