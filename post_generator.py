# Use for generating the weekly update post

from random import randint, randrange
import time
from datetime import timedelta, datetime
import os

def check_for_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_all_days(start, end, target):
    start = datetime.strptime(start, '%Y-%m-%d').date()
    end = datetime.strptime(end, '%Y-%m-%d').date()
    dates = []
    for day in range((end - start).days + 1):
        if ((start + timedelta(days=day)).weekday() == time.strptime(target, '%A').tm_wday):
            dates.append(start + timedelta(days=day))

    return dates


def generate_post(path, date, index):
    index = str(index).zfill(2)
    filename = f"{date}-weekly-update-{index}"
    f = open(f"{path}\{filename}.md", "w+")

    hour = randint(11, 23)
    minute = randint(0, 59)
    second = randint(0, 59)

    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    second = str(second).zfill(2)

    lines = [
        "---",
        f"date: {date} {hour}:{minute}:{second}",
        "layout: post",
        f'title: "Weekly Update #{index}"',
        f'subtitle: "Weekly Update #{index}"',
        f'description: "Weekly Update #{index}"',
        "category: blog",
        "tags:",
        "   - Sem B",
        "   - Weekly Update",
        "author: Joe Siu",
        "paginate: true",
        "---",
        "To be update..."
    ]

    f.writelines(s + '\n' for s in lines)
    f.close()


def main():
    basePath = os.path.dirname(__file__)
    filePath = os.path.join(basePath, "_posts/temp")
    check_for_dir(filePath)
    # Sem A
    startingIndex = 1
    fridays = get_all_days("2021-09-01", "2021-12-31", "Saturday")
    # Sem B
    # startingIndex = 18
    # fridays = get_all_days("2022-01-01", "2022-04-30", "Saturday")

    for index in range(0, len(fridays)):
        generate_post(filePath, fridays[index], index + startingIndex)


if __name__ == "__main__":
    main()
