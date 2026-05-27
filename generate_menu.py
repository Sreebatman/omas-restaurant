import re
import os

# Menu Data Structure
menu = [
    {
        "category_id": "salads-soups",
        "category_name": "Salads",
        "items": [
            ("Green Salad (M)", "120"), ("Green Salad (L)", "180"), ("Arabic Salad", "200"), ("Cutfruits Salad", "200"), ("Hammus", "150")
        ]
    },
    {
        "category_id": "salads-soups",
        "category_name": "Soups",
        "items": [
            ("Lemon Coriander Chicken Soup", "150"), ("Lemon Coriander Chicken Soup ½", "200"), ("Lemon Coriander Soup Veg", "130"), ("Lemon Coriander Soup Veg ½", "180"),
            ("Chicken Clear Soup", "120"), ("Chicken Clear Soup ½", "160"), ("Veg Clear Soup", "90"), ("Veg Clear Soup ½", "140"),
            ("Mutton Hot & Sour Soup", "160"), ("Mutton Hot & Sour Soup ½", "240"), ("Chicken Hot & Sour Soup", "120"), ("Chicken Hot & Sour Soup ½", "160"),
            ("Veg Hot & Sour Soup", "100"), ("Veg Hot & Sour Soup ½", "140"), ("Mushroom Hot & Sour Soup", "120"), ("Mushroom Hot & Sour Soup ½", "160"),
            ("Chicken Manchow Soup", "140"), ("Chicken Manchow Soup ½", "200"), ("Veg Manchow Soup", "100"), ("Veg Manchow Soup ½", "140"),
            ("Chicken Noodles Soup", "120"), ("Chicken Noodles Soup ½", "160"), ("Veg Noodles Soup", "100"), ("Veg Noodles Soup ½", "140"),
            ("Naadan Mutton Soup", "160"), ("Naadan Mutton Soup ½", "240"), ("Cream of Chicken Soup", "150"), ("Cream of Chicken Soup ½", "200"),
            ("Cream of Tomato Soup", "100"), ("Cream of Tomato Soup ½", "140"), ("Cream of Mashroom Soup", "140"), ("Cream of Mashroom Soup ½", "200"),
            ("Sweet Corn Chicken Soup", "140"), ("Sweet Corn Chicken Soup ½", "200"), ("Sweet Corn Veg Soup", "110"), ("Sweet Corn Veg Soup ½", "150")
        ]
    },
    {
        "category_id": "starters",
        "category_name": "Veg Starter",
        "items": [("Mashroom 65Dry", "190"), ("Paneer Grilled Pepper", "260")]
    },
    {
        "category_id": "starters",
        "category_name": "Starters Seafood Fish",
        "items": [("Prawns Dryfry", "seasonal"), ("Thai Grilled Thawa Fish", "seasonal"), ("Thai Grilled Thawa Prawns", "seasonal"), ("Lemon Pepper Grilled Fish", "seasonal"), ("Lemon Pepper Grilled Prawns", "seasonal")]
    },
    {
        "category_id": "starters",
        "category_name": "Starters Chicken",
        "items": [
            ("Chicken Lollipop", "280/540"), ("Injipuli Chicken Lollipop", "300/560"), ("Injipuli Chicken Wings", "280/540"), ("Chicken 65", "160/300/580"),
            ("Omas Special Chicken Wings", "300"), ("Thai Grilled Chicken Tawa", "390"), ("Lemon Pepper Grilled Chicken", "390"), ("Dragon Chicken", "370"),
            ("Crispy Honey Chicken Dry", "390"), ("Kanthari Chicken Thawa", "390")
        ]
    },
    {
        "category_id": "starters",
        "category_name": "Starters Beef",
        "items": [("Beef Dry Fry (Half/Full)", "320/610")]
    },
    {
        "category_id": "maincourse",
        "category_name": "Main Courses Chicken",
        "items": [
            ("Chicken Curry", "150/290/560"), ("Chilli Chicken", "160/300/560"), ("Pepper Chicken", "160/300/560"), ("Chicken Roast", "160/300/560"),
            ("Garlic Chicken", "300/580"), ("Ginger Chicken", "300/580"), ("Kanthari Chicken Curry", "380"), ("Chicken Stew", "380"),
            ("Chicken Kondattam", "380"), ("Chicken Varattiyathu", "380"), ("Puthiyapla Chicken", "390/700"), ("Butter Chicken", "340/660"),
            ("Chicken Nirvana", "380"), ("Chicken Kolhapuri", "380")
        ]
    },
    {
        "category_id": "maincourse",
        "category_name": "Main Course Beef",
        "items": [
            ("Beef Fry", "140/280/520"), ("Beef Roast", "150/300/540"), ("Beef Curry", "150/300/540"), ("Beef Chilli", "160/300/580"),
            ("Beef Pepper", "300/580"), ("Beef Garlic", "300/580"), ("Beef Ginger", "300/580"), ("Beef Varattiyathu", "340/640"),
            ("Beef Kondattam", "340/640"), ("Beef Coconut Fry", "340/640"), ("Beef Ribs", "190/380/740"), ("Beef Ribs Varattu", "230/460/890")
        ]
    },
    {
        "category_id": "maincourse",
        "category_name": "Main Course Mutton",
        "items": [
            ("Mutton Kuruma", "360/700"), ("Mutton Pepper Roast", "360/700"), ("Mutton Stew", "370/720"), ("Mutton Chops", "360/700"),
            ("Mutton Kadai", "360/800"), ("Mutton Varattiyath", "360/700"), ("Mutton Rogan Josh", "360/800")
        ]
    },
    {
        "category_id": "maincourse",
        "category_name": "Main Course Veg",
        "items": [
            ("Baji Curry", "50"), ("Kadala Curry", "50"), ("Cherupayar Curry", "50"), ("Veg Stew", "50/70"), ("Veg Masala", "50/70"),
            ("Veg Kuruma", "120"), ("Greenpeace Masala", "120"), ("Chana Masala", "130"), ("Paneer Butter Masala", "230"), ("Paneer Chilli", "240"),
            ("Paneer 65", "240"), ("Paneer Pepper", "210"), ("Paneer Kadai", "210"), ("Dal fry", "100"), ("Dal Tadka", "120"), ("Dal Kolhapuri", "120"),
            ("Gobi Manjurian", "160/260"), ("Gobi Chilli", "180"), ("Gobi 65", "190"), ("Mushroom Chilli", "190"), ("Mushroom Manchurian", "170"),
            ("Mushroom Kadai", "210"), ("Mushroom Masala", "210"), ("Mix Veg Kuruma", "140"), ("Paneer Manchurian", "220"), ("Paneer Tikka Masala", "280"),
            ("Paneer Tikka", "260"), ("Garlic Paneer", "240")
        ]
    },
    {
        "category_id": "maincourse",
        "category_name": "Main Course Fish",
        "items": [
            ("Ayila Curry", "seasonal"), ("Ayakkoora Curry", "seasonal"), ("Fish Tawa", "seasonal"), ("Ayakkoora Masala", "seasonal"),
            ("Koonthal Pepper Roast", "seasonal"), ("Koonthal Fry", "seasonal"), ("Prawns Stick Fry", "seasonal"), ("Prawns Roast", "seasonal"),
            ("Prawns Dry Fry", "280"), ("Fish Nirvana", "490"), ("Fish Molly", "390"), ("Fish Mango Curry", "390")
        ]
    },
    {
        "category_id": "maincourse",
        "category_name": "Main Course Duck",
        "items": [("Duck Mappas", "460"), ("Duck Varattiyath", "470"), ("Duck Kanthari", "480")]
    },
    {
        "category_id": "rice-biriyani",
        "category_name": "Biriyani Items",
        "items": [
            ("Chicken Biriyani", "160/190"), ("Beef Biriyani", "180/220"), ("Mutton Biriyani", "330"), ("Egg Biriyani", "150"),
            ("Veg Biriyani", "160"), ("Prawns Biriyani", "320"), ("Kada Biriyani", "240"), ("Fish Biriyani", "seasonal"), ("Bucket Biriyani", "890")
        ]
    },
    {
        "category_id": "rice-biriyani",
        "category_name": "Omas Special Kizhi Biriyani",
        "items": [
            ("Kizhi Chicken Biriyani", "230"), ("Kizhi Beef Biriyani", "260"), ("Kizhi Mutton Biriyani", "370"), ("Kizhi Egg Biriyani", "190"),
            ("Kizhi Prawns Biriyani", "360"), ("Kizhi Kada Biriyani", "280"), ("Fish Kizhi Biriyani", "seasonal"), ("Pallichore Kizhi Biriyani", "240")
        ]
    },
    {
        "category_id": "rice-biriyani",
        "category_name": "Rice Items",
        "items": [("Biriyani Rice", "130"), ("Ghee Rice", "110"), ("Jeera Rice", "130"), ("Mandi Rice", "130/250/460")]
    },
    {
        "category_id": "rice-biriyani",
        "category_name": "Omas Special Rice",
        "items": [("Ghee Rice Chatty Combo", "340"), ("Chicken Pallikett", "289"), ("Beef Pallikett", "289")]
    },
    {
        "category_id": "rice-biriyani",
        "category_name": "Traditional Meals",
        "items": [("Chatty Choor", "280"), ("Thali Meals", "130")]
    },
    {
        "category_id": "mandi-shawai",
        "category_name": "Mandi",
        "items": [
            ("Chicken Mandi", "210/400/790"), ("Arabic Alfam Mandi", "240/450/880"), ("Peri Peri Alfam Mandi", "260/490/920"),
            ("Green Pepper Alfaham Mandi", "260/490/920"), ("Kanthari Alfahm Mandi", "260/490/920"), ("Honey Alfaham Mandi", "260/490/920"),
            ("Peri Peri Honey Alfaham Mandi", "260/490/920"), ("Alfaham Varattiyathu Mandi", "270/540/1060"), ("Fish Alfaham Mandi", "seasonal"),
            ("Fish Pollichat Mandi", "seasonal"), ("Beef Ribs Mandi", "280/550/1090"), ("Beef Ribs Varattiyath Mandi", "300/600/1190"),
            ("Puthiyappila Chicken Mandi", "660/1090"), ("Alfaham Butter Pepper Garlic Mandi", "270/540/1060"), ("Alfaham Kondattam Mandi", "270/540/1060"),
            ("Alfaham Schezwan Garlic Mandi", "270/540/1060"), ("Alfaham Kaju Mandi", "270/540/1060")
        ]
    },
    {
        "category_id": "mandi-shawai",
        "category_name": "Shawai",
        "items": [("Masala Shawai", "150/290/550"), ("Honey Chilli Shawai", "160/300/560")]
    },
    {
        "category_id": "noodles-friedrice",
        "category_name": "Fried Rice",
        "items": [
            ("Chicken Fried Rice", "200"), ("Egg Fried Rice", "180"), ("Veg Fried Rice", "160"), ("Beef Fried Rice", "210"),
            ("Mixed Fried Rice", "300"), ("Prawn Fried Rice", "310"), ("Mutton Fried Rice", "320"), ("Chicken Shezwan Fried Rice", "280"),
            ("Egg Shezwan Fried Rice", "240"), ("Mutton Shezwan Fried Rice", "340"), ("Veg Shezwan Fried Rice", "200"), ("Paneer Fried Rice", "240"),
            ("Omas Special Fried Rice", "280"), ("American Chop Suey", "380")
        ]
    },
    {
        "category_id": "noodles-friedrice",
        "category_name": "Noodles",
        "items": [
            ("Chicken Hakka Noodles", "240"), ("Egg Noodles", "190"), ("Veg noodles", "180"), ("Omas Special Noodles", "260"),
            ("Chicken Noodles", "220"), ("Mutton Noodles", "300"), ("Prawns Noodles", "300"), ("Mixed Noodles", "320"),
            ("Shezwan Veg Noodles", "210"), ("Shezwan Chicken Noodles", "240"), ("Shezwan Mutton Noodles", "320"),
            ("Shezwan Mix Noodles", "340"), ("Paneer Noodles", "260"), ("Egg Shezwan Noodles", "220")
        ]
    },
    {
        "category_id": "specialties",
        "category_name": "Kizhi Porotta",
        "items": [("Chicken Kizhi Porotta", "249"), ("Beef Kizhi Porotta", "249")]
    },
    {
        "category_id": "specialties",
        "category_name": "Omas Special Paalkappa",
        "items": [
            ("Paal kappa with Beef Ribs Varattiyath", "360"), ("Paal kappa with Beef curry", "260"), ("Paal kappa with Ayakkoora curry", "seasonal"),
            ("Paal kappa with Fish Tawa Roast", "seasonal"), ("Paal kappa with Chicken Varattiyath", "330")
        ]
    },
    {
        "category_id": "specialties",
        "category_name": "Omas Special Paalporotta",
        "items": [("Paalporotta with Chicken", "360"), ("Paalporotta with Beef", "360")]
    },
    {
        "category_id": "specialties",
        "category_name": "Seafood Bucket",
        "items": [("Seafood Bucket (S) 2 pcs", "1000"), ("Seafood Bucket (M) 4 pcs", "1900"), ("Seafood Bucket (L) 8 pcs", "3700")]
    },
    {
        "category_id": "specialties",
        "category_name": "Platers",
        "items": [
            ("Alfaham Platers 4 Person", "849"), ("Platers 2 Person", "720"), ("Platers 4 Person", "1390"),
            ("Chicken Grill Plater 8 Person", "2199"), ("Platers 8 Person", "2899"), ("Platers Mixed 8 Person", "2199")
        ]
    },
    {
        "category_id": "breads",
        "category_name": "Breakfast Items",
        "items": [("Masala Dosha", "80"), ("Ney Roast", "75")]
    },
    {
        "category_id": "breads",
        "category_name": "Bread Items",
        "items": [("Porotta", "14"), ("Wheat Porotta", "18"), ("Chapathi", "14"), ("Kuboos", "9"), ("Appam", "16"), ("Neypathal", "15"), ("Poori", "14"), ("Puttu", "14")]
    },
    {
        "category_id": "breads",
        "category_name": "Tandoori Bread Items",
        "items": [
            ("Rotti", "25"), ("Butter Rotti", "30"), ("Plain Naan", "30"), ("Butter Naan", "35"), ("Cheese Naan", "45"),
            ("Garlic Naan", "40"), ("Cheese Garlic Naan", "50"), ("Kulcha", "30"), ("Butter Kulcha", "35"), ("Rumali Roti", "40")
        ]
    },
    {
        "category_id": "tandoori-grills",
        "category_name": "Fish Alfam Items",
        "items": [("Fish Alfam", "seasonal"), ("Fish Pollichathu", "seasonal")]
    },
    {
        "category_id": "tandoori-grills",
        "category_name": "Tandoori Items",
        "items": [("Tandoori Chicken", "150/290/580"), ("Tandoori Choice", "160"), ("Afghani Chicken", "160/300/590"), ("Afghani Choice", "170")]
    },
    {
        "category_id": "tandoori-grills",
        "category_name": "Kababs",
        "items": [
            ("Chicken Kabab", "160/320/600"), ("Chicken Tikka", "160/320/600"), ("Arabic Kabab", "320"), ("Kandari Kabab", "320"),
            ("Rashmi Kabab", "320"), ("Nooreni Kabab", "320"), ("Afghani Kabab", "320"), ("Malai Kabab", "320"), ("Pahad Kabab", "320"), ("Nawab Tikka", "320")
        ]
    },
    {
        "category_id": "tandoori-grills",
        "category_name": "Alfahm Items",
        "items": [
            ("Arabic Alfahm", "150/290/560"), ("Kanthari Alfahm", "160/300/570"), ("Peri Peri Alfahm", "160/300/570"),
            ("Peri Peri Honey Alfahm", "170/310/580"), ("Green Pepper Alfahm", "160/300/570"), ("Honey Alfahm", "160/300/570"),
            ("Alfahm Kajoo", "190/360/700"), ("Butter Pepper Garlic", "190/360/700"), ("Alfahm Kondattam", "190/360/700"),
            ("Alfahm Shezwan Garlic", "190/360/700"), ("Alfahm Varattiyath", "190/360/700"), ("Alfahm Sukka", "190/360/700")
        ]
    },
    {
        "category_id": "fastfood",
        "category_name": "Fried Chicken Combos",
        "items": [
            ("Snak Meal", "179", "2 Pcs Chicken, 1 Bun, Mayo, Kechup"),
            ("Dinner Meal", "289", "3 Pcs Chicken, 1 Bun, Mayo, Kechup, Fries, Soft Drinks 250ml"),
            ("Couple Meal", "409", "4 Pcs Chicken, 2 Bun, Mayo, Kechup, Fries, Soft Drinks 750ml"),
            ("Omas Delight", "649", "6 Pcs Chicken, 3 Bun, Mayo (L), Kechup, Coleslaw, Fries (M), Soft Drinks 750ml"),
            ("Family Delight", "799", "8 Pcs Chicken, 4 Bun, Mayo (L), Kechup, Coleslaw, Fries (M), Soft Drinks 750ml"),
            ("Mini Bucket", "999", "10 Pcs Chicken, 5 Bun, Mayo (L), Kechup, Coleslaw, Fries (M), Soft Drinks 1Ltr"),
            ("Family Special", "1099", "12 Pcs Chicken, 6 Bun, Mayo (2L), Kechup, Coleslaw (2), Fries (L), Soft Drinks 1Ltr"),
            ("Bucket Meal", "1699", "18 Pcs Chicken, 9 Bun, Mayo (3L), Kechup, Coleslaw (3L), Fries (L), Soft Drinks 2Ltr"),
            ("King Meal", "1799", "20 Pcs Chicken, 10 Bun, Mayo (3L), Kechup, Coleslaw (3L), Fries (L), Soft Drinks 2Ltr")
        ]
    },
    {
        "category_id": "fastfood",
        "category_name": "Burgers",
        "items": [
            ("Beef Patty Burger", "150"), ("Crispy Burger", "110"), ("Zinger Burger", "130"), ("Veg Royal Burger", "120"),
            ("Zinger Burger Double", "160"), ("Chicken Patty Burger", "120"), ("Chicken Patty Burger Double", "150"), ("Mini Burger", "60")
        ]
    },
    {
        "category_id": "fastfood",
        "category_name": "Value Meal",
        "items": [
            ("Value Meal A1", "229", "Chicken 1 Piece, Burger 1, Mayonnaise, Fries, Ketchup, Pepsi 250ml"),
            ("Value Meal A2", "439", "Chicken 2 Piece, Burger 1, Mayonnaise, Fries, Ketchup, Pepsi 500ml, Crispy Roll")
        ]
    },
    {
        "category_id": "fastfood",
        "category_name": "Wrap Items",
        "items": [
            ("Shawarma Roll", "90"), ("Shawarma Plate", "120"), ("Poori Shawarma", "120"), ("Zinger Chicken Wrap", "120"),
            ("Chicken Tikka Wrap", "140"), ("Chicken Kabab Wrap", "140"), ("Beef Porotta Wrap", "140"),
            ("Crispy Shawarma Porotta Wrap", "100"), ("Paneer Tikka Wrap", "140"), ("Crispy Roll Kuboos", "90")
        ]
    },
    {
        "category_id": "starters",
        "category_name": "Crispy Starters",
        "items": [("Chicken Strips (6pcs/12pcs)", "230/440"), ("Chicken Pop", "199"), ("French Fry (M/C)", "90/140"), ("1 PC Fried Chicken", "70/80"), ("Chicken Nuggets (5 pcs)", "129"), ("Mayonnaise", "30"), ("Bun", "15"), ("Coleslaw", "30")]
    },
    {
        "category_id": "beverages",
        "category_name": "Shake with Ice Cream Scoops",
        "items": [
            ("Apple shake with ice cream", "120"), ("Cherry shake with ice cream", "110"), ("Tender Coconut with ice cream", "110"),
            ("Mango shake with ice cream", "110"), ("Chikku shake with ice cream", "110"), ("Badam shake with ice cream", "120"),
            ("Anar shake with ice cream", "120"), ("Pista shake with ice cream", "120"), ("Arabic Dates shake with ice cream", "120"),
            ("Oreo shake with ice cream", "120"), ("Banana shake with ice cream", "100"), ("Dryfruit shake with ice cream", "150"),
            ("Fig with ice cream", "120"), ("Strawberry shake with ice cream", "110")
        ]
    },
    {
        "category_id": "beverages",
        "category_name": "Omas Special Shake",
        "items": [("Dryfruit with fresh fruit shake", "180")]
    },
    {
        "category_id": "beverages",
        "category_name": "Falooda",
        "items": [
            ("Royal Falooda", "160"), ("Omas Special Falooda", "180"), ("Dryfruit Falooda", "190"), ("Fruit salad with ice Cream", "120"),
            ("Fruit salad without ice Cream", "100"), ("Tender Ice cream falooda", "190"), ("In House falooda", "140"), ("Family special falooda", "299")
        ]
    },
    {
        "category_id": "beverages",
        "category_name": "Mojitos",
        "items": [
            ("Blue Curacao", "110"), ("Mojito Mint", "110"), ("Watermelon", "110"), ("Green Apple", "110"),
            ("Lemon Mint", "110"), ("Passionfruit", "110"), ("Strawberry", "110"), ("Pineapple", "110"),
            ("Mango", "110"), ("Orange", "110"), ("Blueberry", "110"), ("Kiwi", "110")
        ]
    },
    {
        "category_id": "beverages",
        "category_name": "Juice Items",
        "items": [
            ("Lemon Juice", "25"), ("Mint Lime", "30"), ("Pineapple Lime", "35"), ("Ginger Lime", "35"), ("Grape Lime", "35"),
            ("Musambi Juice", "70"), ("Pineapple Juice", "80"), ("Orange Juice", "70"), ("Mango Juice", "90"), ("Chikku Juice", "80"),
            ("Apple Jucie", "90"), ("Shamam Juice", "80"), ("Anar Juice", "90"), ("Pappaya Juice", "80"), ("Watermelon Juice", "70"),
            ("Guava Cocktail", "80"), ("Grape Juice", "80"), ("Omas Mix", "90")
        ]
    },
    {
        "category_id": "beverages",
        "category_name": "Hot Items",
        "items": [
            ("Tea", "15"), ("Black Tea", "13"), ("Lime Tea", "17"), ("Green Tea", "17"), ("Lemonmint tea", "17"),
            ("Brue Coffee", "20"), ("Black Coffee", "15"), ("Horlicks", "25"), ("Boost", "25")
        ]
    },
    {
        "category_id": "beverages",
        "category_name": "Ice Cream Scoop (Single/Double)",
        "items": [
            ("Tender Coconut", "50/90"), ("Vanilla", "40/70"), ("Strawberry", "50/80"), ("Pista", "50/90"),
            ("Butterscotch", "50/90"), ("Jackfruit", "60/100"), ("Chocolate", "50/90"), ("Spanish Delight", "60/100"), ("Blueberry", "60/100")
        ]
    },
    {
        "category_id": "beverages",
        "category_name": "Shakes Items",
        "items": [
            ("Cherry Shake", "90"), ("Tender Coconut", "80"), ("Apple Shake", "100"), ("Mango Shake", "90"),
            ("Chikku Shake", "90"), ("Badam Shake", "100"), ("Anar Shake", "100"), ("Shamam Shake", "80"),
            ("Pappaya Shake", "90"), ("Kiwi Shake", "120"), ("Sharja Shake", "90"), ("Vanila Shake", "90"),
            ("Strawberry Shake", "90"), ("Pista Shake", "100"), ("Chocolate Shake", "100"), ("Banana Shake", "80"),
            ("Arabic Dates Shake", "100"), ("Grape Shake", "100"), ("Oreo Shake", "100"), ("Dryfruits Mixed Shake", "130"), ("Fig Shake", "100")
        ]
    }
]

filters_html = """            <div class="menu-filters">
                <button class="filter-btn active" data-filter="all">All Items</button>
                <button class="filter-btn" data-filter="starters">Starters & Soups</button>
                <button class="filter-btn" data-filter="maincourse">Main Courses</button>
                <button class="filter-btn" data-filter="rice-biriyani">Biriyani & Rice</button>
                <button class="filter-btn" data-filter="mandi-shawai">Mandi & Shawai</button>
                <button class="filter-btn" data-filter="noodles-friedrice">Noodles & Rice</button>
                <button class="filter-btn" data-filter="specialties">Specialties</button>
                <button class="filter-btn" data-filter="breads">Breads & Breakfast</button>
                <button class="filter-btn" data-filter="tandoori-grills">Tandoori & Grills</button>
                <button class="filter-btn" data-filter="fastfood">Fast Food</button>
                <button class="filter-btn" data-filter="beverages">Beverages & Desserts</button>
            </div>"""

menu_html = '<div class="menu-categories-wrapper">\n'

# Group categories together by ID so it forms one section per filter
grouped = {}
for m in menu:
    if m["category_id"] not in grouped:
        grouped[m["category_id"]] = []
    grouped[m["category_id"]].append(m)

for cat_id, sections in grouped.items():
    menu_html += f'            <div class="menu-category-group" data-category="{cat_id}">\n'
    for sec in sections:
        menu_html += f'                <section class="menu-category">\n'
        menu_html += f'                    <h3>{sec["category_name"]}</h3>\n'
        menu_html += f'                    <ul class="menu-list">\n'
        for item in sec["items"]:
            if len(item) == 3:
                name, price, desc = item
                if price == "seasonal":
                    price_str = "Seasonal"
                else:
                    price_str = f"₹{price}"
                menu_html += f'                        <li class="menu-item"><span class="menu-item-name">{name}</span><span class="menu-item-desc">{desc}</span> <strong class="menu-item-price">{price_str}</strong></li>\n'
            else:
                name, price = item
                if price == "seasonal":
                    price_str = "Seasonal"
                else:
                    price_str = f"₹{price}"
                menu_html += f'                        <li class="menu-item"><span class="menu-item-name">{name}</span> <strong class="menu-item-price">{price_str}</strong></li>\n'
        menu_html += f'                    </ul>\n'
        menu_html += f'                </section>\n'
    menu_html += f'            </div>\n'

menu_html += '        </div>'

# Now read the original HTML and replace
html_path = r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('{{MENU_PLACEHOLDER}}', filters_html + '\n' + menu_html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu generation complete. Wrote massive menu structure to menu.html.")
