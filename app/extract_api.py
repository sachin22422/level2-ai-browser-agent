from fastapi import APIRouter

extract_router = APIRouter()

@extract_router.get("/extract")
async def extract_data():
    # Static mockup data to simulate product extraction
    return {
        "platform": "Amazon",
        "products": [
            {
                "title": "Apple iPhone 15 (128 GB) - Black",
                "price": "₹61,400",
                "rating": "4.5",
                "availability": "In stock"
            },
            {
                "title": "Apple iPhone 15 (128 GB) - Blue",
                "price": "₹61,790",
                "rating": "4.3",
                "availability": "In stock"
            }
        ],
        "note": "Static product data extracted after login and search"
    }
