import random
import webbrowser


def open_random_website():
    websites = [
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.github.com",
        "https://www.python.org",
    ]
    chosen = random.choice(websites)
    print(f"Opening: {chosen}")
    webbrowser.open(chosen)


if __name__ == "__main__":
    open_random_website()