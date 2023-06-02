import os

cache: dict[str, str] = dict()


def get_item_from_cache(key: str) -> str | None:
    image_path = cache.get(key)

    if image_path is not None:
        if os.path.exists(image_path):
            return image_path

    return None


def save_bytes_as_img(file_name: str, img_bytes: bytes) -> str:
    if not os.path.exists(".cache"):
        os.makedirs(".cache")
    file_path = os.path.join(".cache", file_name)
    with open(file_path, "wb") as file:
        file.write(img_bytes)

    return file_path


def load_image_as_byte(file_path: str) -> bytes | None:
    with open(file_path, "rb") as file:
        image_bin = file.read()
        return image_bin
