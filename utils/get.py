def orta(sonlar):

    if len(sonlar) == 0:
        raise ValueError("Sonlar listi bo'sh bo'lmasligi kerak.")

    return sum(sonlar) / len(sonlar)
