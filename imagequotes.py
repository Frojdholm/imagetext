import random
import json

from PIL import Image, ImageEnhance

from imagetext import draw_quote


def load_quote(path):
    with open(path) as f:
        quotes = json.load(f)

    quote = random.choice(quotes)
    return quote["text"], quote["author"]


def main(quote_path, image_path, result_path=None, dim=None, font=None, fontsize=None):
    text, author = load_quote(quote_path)
    with Image.open(image_path) as image:
        if dim is not None:
            brightness = ImageEnhance.Brightness(image)
            image = brightness.enhance(dim)
        image = draw_quote(
            image,
            text,
            author,
            font=font,
            fontsize=fontsize
        )

        if result_path:
            image.save(result_path)
        else:
            image.save(image_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("quotefile")
    parser.add_argument("image")
    parser.add_argument("output")
    parser.add_argument("--dim", type=int)
    parser.add_argument("--font", type=str)
    parser.add_argument("--fontsize", type=int)

    args = parser.parse_args()

    main(
        args.quotefile,
        args.image,
        args.output,
        dim=args.dim,
        font=args.font,
        fontsize=args.fontsize
     )
