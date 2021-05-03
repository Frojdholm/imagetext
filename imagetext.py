from PIL import ImageDraw, ImageFont


def split_text(text, font, target_width):
    words = text.split(" ")
    lines = [[]]
    for w in words:
        lines[-1].append(w)
        width = font.getlength(" ".join(lines[-1]))
        if width >= target_width:
            lines[-1].pop()
            lines.append([w])
    result = [" ".join(line) for line in lines]
    return "\n".join(result)


def draw_quote(
    image,
    text,
    author,
    font=None,
    fontsize=None,
    target_width=None,
    align="center"
):
    if font is None:
        font = ImageFont.load_default()
    elif isinstance(font, str):
        fontsize = fontsize or 12
        font = ImageFont.truetype(font, size=fontsize)

    im_width, im_height = image.size

    target_width = target_width or im_width * 0.6

    text = split_text(text, font, target_width)

    text_width, text_height = font.getsize_multiline(text)
    author_width, author_height = font.getsize(author)

    x = (im_width - text_width) / 2
    y = (im_height - (text_height + author_height)) / 2

    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, font=font, align=align)

    # Right align author line
    draw.text((x + (text_width - author_width), y + text_height), author, font=font)

    return image
