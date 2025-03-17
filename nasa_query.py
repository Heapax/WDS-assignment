import requests
import csv

def get_nasa_assets(query="Ilan Ramon"):
    url = "https://images-api.nasa.gov/search"
    params = {"q": query, "media_type": "image"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["collection"]["items"]
    else:
        print("Failed to fetch data from NASA API", response.status_code)
        return []

def filter_large_images(items, min_size_kb=1000):
    large_images = []
    for item in items:
        nasa_id = item["data"][0]["nasa_id"]
        asset_url = f"https://images-assets.nasa.gov/image/{nasa_id}/{nasa_id}~orig.jpg"
        try:
            head_response = requests.head(asset_url)
            if head_response.status_code == 200:
                size_kb = int(head_response.headers.get("Content-Length", 0)) // 1024
                if size_kb > min_size_kb:
                    large_images.append((nasa_id, size_kb))
        except Exception as e:
            print(f"Error fetching image metadata for {nasa_id}: {e}")
    return large_images

def save_to_csv(data, filename="/data/nasa_images.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nasa_id", "kb"])
        writer.writerows(data)

if __name__ == "__main__":
    assets = get_nasa_assets()
    large_images = filter_large_images(assets)
    save_to_csv(large_images)
    print(f"Saved {len(large_images)} records to nasa_images.csv")