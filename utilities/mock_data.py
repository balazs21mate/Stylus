def image_generator(photo_number, resolution=[600,400]):
    photo_links=[]

    for i in range(photo_number):
        photo_links.append(f"https://source.unsplash.com/{resolution[0]}x{resolution[1]}/?nature,water{i + 1}")

    return photo_links