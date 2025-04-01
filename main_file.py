import hashlib

data = {}  # In-memory dictionary


def generate_short_url(long_url):
    """Generate a short URL from a long URL using MD5 hashing."""
    hash_object = hashlib.md5(long_url.encode())
    short_code = hash_object.hexdigest()[:6]  # Take first 6 characters
    return f"http://short.ly/{short_code}"  # Return full shortened URL

def shorten_url():
    long_url = input("Enter the long URL: ").strip()
    if not long_url:  # Handling empty URL case
        print("Error: URL cannot be empty")
        return

    for short, url in data.items():
        if url == long_url:
            print(f"Short URL already exists: {short}")
            return
            
    short_url = generate_short_url(long_url)
    data[short_url] = long_url  # Store full shortened URL as key
    print(f"Short URL created: {short_url}")
    
def retrieve_url():
    """retrieving original URL."""
    short_url = input("Enter the short URL: ").strip()
    long_url = data.get(short_url)  # Direct lookup
    if long_url:
        print(f"Original URL: {long_url}")
    else:
        print("Short URL not found!")

def user_choice(choice):
    if choice == "1":
        shorten_url()
    elif choice == "2":
        retrieve_url()
    elif choice == "3":
        print("Exiting... Goodbye!")
        return
    else:
        print("Invalid choice! Try again.")

if __name__ == "__main__":
    while True:
        print("\nURL Shortener")
        print("1. Shorten a URL")
        print("2. Retrieve Original URL")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        user_choice(choice)
        if choice == "3":
            break