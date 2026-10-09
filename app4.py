import streamlit as st
from datetime import date
import random
import uuid

st.set_page_config(
    page_title="GharSeva India",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f4f8ff, #fff7f0);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #102a43, #176b68);
}
[data-testid="stSidebar"] * {
    color: white;
}
.hero {
    padding: 30px;
    border-radius: 20px;
    color: white;
    background: linear-gradient(120deg, #123b5d, #008f87);
    margin-bottom: 22px;
}
.hero h1, .hero p {
    color: white;
}
.price {
    color: #087f5b;
    font-size: 22px;
    font-weight: bold;
}
div.stButton > button {
    border-radius: 10px;
    min-height: 40px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


def money(amount):
    return f"₹{amount:,.0f}"


def make_reference():
    return uuid.uuid4().hex[:8].upper()


def photo(photo_id, width=800):
    return (
        f"https://images.unsplash.com/{photo_id}"
        f"?auto=format&fit=crop&w={width}&q=80"
    )


def show_card(title, image, description, price=None):
    with st.container(border=True):
        st.image(image, use_container_width=True)
        st.markdown(f"### {title}")
        st.write(description)

        if price is not None:
            st.markdown(
                f'<div class="price">{money(price)}</div>',
                unsafe_allow_html=True
            )


# -------------------- PROPERTY DATA --------------------

PROPERTIES = [
    {
        "id": "P01",
        "name": "Modern Family House",
        "city": "Hyderabad",
        "kind": "House",
        "deal": "Rent",
        "price": 18000,
        "image": "photo-1600585154340-be6161a56a0c"
    },
    {
        "id": "P02",
        "name": "City Apartment",
        "city": "Vijayawada",
        "kind": "Flat",
        "deal": "Rent",
        "price": 14000,
        "image": "photo-1600607687920-4e2a09cf159d"
    },
    {
        "id": "P03",
        "name": "Garden Villa",
        "city": "Visakhapatnam",
        "kind": "House",
        "deal": "Rent",
        "price": 22000,
        "image": "photo-1600566753190-17f0baa2a6c3"
    },
    {
        "id": "P04",
        "name": "Comfortable Family Flat",
        "city": "Guntur",
        "kind": "Flat",
        "deal": "Rent",
        "price": 12000,
        "image": "photo-1494526585095-c41746248156"
    },
    {
        "id": "P05",
        "name": "Premium Rental Home",
        "city": "Hyderabad",
        "kind": "House",
        "deal": "Rent",
        "price": 25000,
        "image": "photo-1600047509807-ba8f99d2cdde"
    },
    {
        "id": "P06",
        "name": "Small City Apartment",
        "city": "Guntur",
        "kind": "Flat",
        "deal": "Rent",
        "price": 9500,
        "image": "photo-1600210492486-724fe5c67fb0"
    },
    {
        "id": "P07",
        "name": "Bright Modern House",
        "city": "Tenali",
        "kind": "House",
        "deal": "Rent",
        "price": 11000,
        "image": "photo-1600607687939-ce8a6c25118c"
    },
    {
        "id": "P08",
        "name": "Luxury Apartment",
        "city": "Hyderabad",
        "kind": "Flat",
        "deal": "Rent",
        "price": 30000,
        "image": "photo-1600566753086-00f18fb6b3ea"
    },
    {
        "id": "P09",
        "name": "Residential Plot",
        "city": "Guntur",
        "kind": "Land",
        "deal": "Sale",
        "price": 1800000,
        "image": "photo-1500382017468-9049fed747ef"
    },
    {
        "id": "P10",
        "name": "Independent House for Sale",
        "city": "Visakhapatnam",
        "kind": "House",
        "deal": "Sale",
        "price": 6500000,
        "image": "photo-1600607687939-ce8a6c25118c"
    },
    {
        "id": "P11",
        "name": "Open Agricultural Land",
        "city": "Tenali",
        "kind": "Land",
        "deal": "Sale",
        "price": 2500000,
        "image": "photo-1472396961693-142e6e269027"
    },
    {
        "id": "P12",
        "name": "Modern Apartment for Sale",
        "city": "Hyderabad",
        "kind": "Flat",
        "deal": "Sale",
        "price": 7200000,
        "image": "photo-1600607687920-4e2a09cf159d"
    },
    {
        "id": "P13",
        "name": "Commercial Building",
        "city": "Vijayawada",
        "kind": "Building",
        "deal": "Sale",
        "price": 12000000,
        "image": "photo-1486406146926-c627a92ad1ab"
    },
    {
        "id": "P14",
        "name": "Family Villa for Sale",
        "city": "Guntur",
        "kind": "House",
        "deal": "Sale",
        "price": 5500000,
        "image": "photo-1600585154340-be6161a56a0c"
    },
    {
        "id": "P15",
        "name": "Office Property",
        "city": "Hyderabad",
        "kind": "Building",
        "deal": "Sale",
        "price": 15000000,
        "image": "photo-1497366754035-f200968a6e72"
    }
]


# -------------------- WORKERS AND TOOLS --------------------

WORKER_DATA = [
    ("Ravi Kumar", "Plumber", 700,
     "photo-1621905252507-b35492cc74b4",
     ["Pipe Wrench", "Basin Wrench", "Plier Set", "Teflon Tape"]),

    ("Suresh Babu", "Carpenter", 900,
     "photo-1621905251189-08b45d6a269e",
     ["Wood Hammer", "Hand Saw", "Screwdriver Set", "Measuring Tape"]),

    ("Imran Ali", "Painter", 1000,
     "photo-1562259949-e8e7689d7828",
     ["Paint Roller", "Brush Set", "Paint Tray", "Wall Scraper"]),

    ("Kiran", "Cleaner", 500,
     "photo-1581578731548-c64695cc6952",
     ["Cleaning Brushes", "Floor Mop", "Bucket", "Rubber Gloves"]),

    ("Arjun Singh", "Electrician", 800,
     "photo-1621905251918-48416bd8575a",
     ["Multimeter", "Wire Stripper", "Voltage Tester",
      "Insulated Screwdriver"]),

    ("Manoj Reddy", "Mechanic", 900,
     "photo-1487754180451-c456f719a1fc",
     ["Spanner Set", "Socket Set", "Pliers", "Torque Wrench"]),

    ("Ramesh Kumar", "Welder", 1100,
     "photo-1504917595217-d4dc5ebe6122",
     ["Welding Machine", "Welding Helmet", "Welding Gloves",
      "Angle Grinder"]),

    ("Deepak Yadav", "Mason", 1000,
     "photo-1503387762-592deb58ef4e",
     ["Brick Trowel", "Spirit Level", "Plastering Trowel",
      "Mason Hammer"]),

    ("Vijay Rao", "Gardener", 600,
     "photo-1416879595882-3373a0480b5b",
     ["Garden Shears", "Hand Trowel", "Garden Gloves",
      "Watering Can"]),

    ("Rahul Das", "AC Technician", 900,
     "photo-1581092160607-ee22621dd758",
     ["AC Gauge", "Clamp Meter", "Cleaning Brush", "Tool Bag"])
]

TOOL_PHOTOS = [
    "photo-1586864387967-d02ef85d93e8",
    "photo-1504148455328-c376907d081c",
    "photo-1530124566582-a618bc2615dc",
    "photo-1581092160607-ee22621dd758",
    "photo-1504917595217-d4dc5ebe6122",
    "photo-1503387762-592deb58ef4e",
    "photo-1416879595882-3373a0480b5b",
    "photo-1586864387967-d02ef85d93e8",
    "photo-1530124566582-a618bc2615dc",
    "photo-1581092160607-ee22621dd758"
]

WORKERS = []
TOOLS = []
tool_number = 0

for index, data in enumerate(WORKER_DATA):
    worker_name, job, daily_price, worker_image, tool_names = data

    worker = {
        "id": index + 1,
        "name": worker_name,
        "job": job,
        "daily": daily_price,
        "weekly": daily_price * 5,
        "monthly": daily_price * 20,
        "image": worker_image,
        "description": f"Home-service professional for {job.lower()} tasks."
    }

    WORKERS.append(worker)

    for tool_name in tool_names:
        tool = {
            "id": f"T{tool_number + 1:03d}",
            "name": tool_name,
            "price": 200 + tool_number * 75,
            "image": TOOL_PHOTOS[tool_number % len(TOOL_PHOTOS)],
            "job": job,
            "description": f"{tool_name} for {job.lower()} work."
        }

        TOOLS.append(tool)
        tool_number += 1


# -------------------- SESSION STATE --------------------

defaults = {
    "cart": [],
    "pending_properties": [],
    "pending_bookings": [],
    "property_requests": [],
    "bookings": [],
    "orders": [],
    "last_result": None,
    "discount": 0,
    "discount_spun": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# -------------------- SHARED FUNCTIONS --------------------

def add_property(item):
    existing = [
        p["id"] for p in st.session_state.pending_properties
    ]

    if item["id"] in existing:
        st.warning("This property is already in your checkout.")
        return

    st.session_state.pending_properties.append({
        **item,
        "reference": make_reference()
    })
    st.success("Property added to checkout!")


def add_tool(tool, quantity):
    for item in st.session_state.cart:
        if item["id"] == tool["id"]:
            item["quantity"] += quantity
            st.success("Tool quantity updated in your cart!")
            return

    st.session_state.cart.append({
        **tool,
        "quantity": quantity
    })
    st.success("Tool added to your cart!")


def add_booking(worker, period, service_date, customer,
                phone, address, payment):
    prices = {
        "Daily": worker["daily"],
        "Weekly": worker["weekly"],
        "Monthly": worker["monthly"]
    }

    st.session_state.pending_bookings.append({
        "id": make_reference(),
        "worker": worker["name"],
        "job": worker["job"],
        "period": period,
        "date": str(service_date),
        "customer": customer.strip(),
        "phone": phone.strip(),
        "address": address.strip(),
        "payment": payment,
        "price": prices[period],
        "reference": make_reference()
    })


def checkout_total():
    property_total = sum(
        p["price"] for p in st.session_state.pending_properties
    )

    worker_total = sum(
        b["price"] for b in st.session_state.pending_bookings
    )

    tool_total = sum(
        t["price"] * t["quantity"] for t in st.session_state.cart
    )

    return property_total + worker_total + tool_total


def validate_customer(name, phone, address=""):
    if not name.strip():
        return "Please enter your name."

    if not phone.isdigit() or len(phone) != 10:
        return "Enter a valid 10-digit mobile number."

    if address is not None and not address.strip():
        return "Please enter your address."

    return None


# -------------------- SIDEBAR --------------------

st.sidebar.title("🏡 GharSeva India")
st.sidebar.caption("Your home, your services")

pages = [
    "🏠 Home",
    "🏘️ Rent Houses",
    "🏷️ Property Sales",
    "🧰 Workers",
    "🛒 Tools Shop",
    "🧾 Checkout",
    "🎁 Spin & Offers",
    "✅ Final Confirmation",
    "📋 My Requests"
]

page = st.sidebar.radio("Choose a page", pages)

st.sidebar.divider()

cart_count = sum(
    item["quantity"] for item in st.session_state.cart
)

st.sidebar.metric("Tools in cart", cart_count)
st.sidebar.metric(
    "Items awaiting checkout",
    len(st.session_state.pending_properties)
    + len(st.session_state.pending_bookings)
    + len(st.session_state.cart)
)

st.sidebar.info(
    "Demo application. Listings, providers and prices are examples."
)


# -------------------- HOME --------------------

if page == "🏠 Home":
    st.markdown("""
    <div class="hero">
        <h1>🏡 Welcome to GharSeva India</h1>
        <p>Find properties, book home-service workers and shop for tools.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(photo("photo-1600585154340-be6161a56a0c"))
        st.subheader("🏠 Find a Home")
        st.write("Browse available sample properties.")

    with col2:
        st.image(photo("photo-1621905252507-b35492cc74b4"))
        st.subheader("🧰 Book a Worker")
        st.write("Choose a home-service professional.")

    with col3:
        st.image(photo("photo-1586864387967-d02ef85d93e8"))
        st.subheader("🛠️ Shop Tools")
        st.write("Browse tools for different jobs.")

    st.divider()
    st.subheader("⭐ Featured Properties")

    cols = st.columns(3)

    for i, item in enumerate(PROPERTIES[:6]):
        with cols[i % 3]:
            show_card(
                item["name"],
                photo(item["image"]),
                f'{item["city"]} · {item["kind"]} · {item["deal"]}',
                item["price"]
            )

            if st.button("Add to Checkout", key=f"home_{item['id']}"):
                add_property(item)

    st.info("Your selected items can be reviewed on the Checkout page.")


# -------------------- RENT HOUSES --------------------

elif page == "🏘️ Rent Houses":
    st.title("🏘️ Homes and Flats for Rent")

    city_options = ["All Cities"] + sorted({
        p["city"] for p in PROPERTIES if p["deal"] == "Rent"
    })

    city = st.selectbox("Choose city", city_options)

    max_rent = max(
        p["price"] for p in PROPERTIES if p["deal"] == "Rent"
    )

    rent_limit = st.slider(
        "Maximum monthly rent",
        min_value=5000,
        max_value=max_rent,
        value=max_rent,
        step=500
    )

    items = [
        p for p in PROPERTIES
        if p["deal"] == "Rent"
        and (city == "All Cities" or p["city"] == city)
        and p["price"] <= rent_limit
    ]

    st.write(f"Found {len(items)} rental properties.")

    cols = st.columns(3)

    for i, item in enumerate(items):
        with cols[i % 3]:
            show_card(
                item["name"],
                photo(item["image"]),
                f'{item["city"]} · {item["kind"]} · Monthly rent',
                item["price"]
            )

            if st.button(
                "Select Property",
                key=f"rent_select_{item['id']}"
            ):
                add_property(item)

    if not items:
        st.warning("No properties match your filters.")


# -------------------- PROPERTY SALES --------------------

elif page == "🏷️ Property Sales":
    st.title("🏷️ Properties for Sale")

    kinds = ["All Types", "House", "Flat", "Land", "Building"]
    kind = st.selectbox("Property category", kinds)

    cities = ["All Cities"] + sorted({
        p["city"] for p in PROPERTIES if p["deal"] == "Sale"
    })
    city = st.selectbox("Property city", cities)

    items = [
        p for p in PROPERTIES
        if p["deal"] == "Sale"
        and (kind == "All Types" or p["kind"] == kind)
        and (city == "All Cities" or p["city"] == city)
    ]

    cols = st.columns(3)

    for i, item in enumerate(items):
        with cols[i % 3]:
            show_card(
                item["name"],
                photo(item["image"]),
                f'{item["city"]} · {item["kind"]} · For sale',
                item["price"]
            )

            if st.button(
                "Select Property",
                key=f"sale_select_{item['id']}"
            ):
                add_property(item)

    if not items:
        st.warning("No properties match your filters.")


# -------------------- WORKERS --------------------

elif page == "🧰 Workers":
    st.title("🧰 Home-Service Workers")
    st.write("Select a worker and add a booking to your checkout.")

    job_options = ["All Workers"] + [
        w["job"] for w in WORKERS
    ]

    job = st.selectbox("Choose worker type", job_options)

    shown_workers = [
        w for w in WORKERS
        if job == "All Workers" or w["job"] == job
    ]

    cols = st.columns(2)

    for i, worker in enumerate(shown_workers):
        with cols[i % 2]:
            show_card(
                worker["job"],
                photo(worker["image"]),
                f'{worker["name"]} · {worker["description"]}',
                worker["daily"]
            )

            st.caption(
                f'Weekly: {money(worker["weekly"])} · '
                f'Monthly: {money(worker["monthly"])}'
            )

            if st.button(
                "Book This Worker",
                key=f"worker_{worker['id']}"
            ):
                st.session_state["booking_worker_id"] = worker["id"]

    selected_id = st.session_state.get("booking_worker_id")

    worker = next(
        (w for w in WORKERS if w["id"] == selected_id),
        None
    )

    if worker:
        st.divider()
        st.subheader(f"📋 Booking details: {worker['name']}")

        with st.form(f"booking_form_{worker['id']}"):
            period = st.radio(
                "Service period",
                ["Daily", "Weekly", "Monthly"],
                horizontal=True
            )

            service_date = st.date_input(
                "Service date",
                min_value=date.today()
            )

            customer = st.text_input("Your name")
            phone = st.text_input("10-digit mobile number")
            address = st.text_area("Service address")

            payment = st.radio(
                "Payment method",
                ["Cash", "Online Payment (Demo)"],
                horizontal=True
            )

            prices = {
                "Daily": worker["daily"],
                "Weekly": worker["weekly"],
                "Monthly": worker["monthly"]
            }

            st.write(f"Service price: **{money(prices[period])}**")

            submitted = st.form_submit_button(
                "Add Booking to Checkout"
            )

        if submitted:
            error = validate_customer(customer, phone, address)

            if error:
                st.error(error)
            else:
                add_booking(
                    worker,
                    period,
                    service_date,
                    customer,
                    phone,
                    address,
                    payment
                )
                st.success(
                    "Booking added! Open Checkout to review or remove it."
                )

        st.divider()
        st.subheader(f"🛠️ Tools for {worker['job']}")

        related_tools = [
            t for t in TOOLS if t["job"] == worker["job"]
        ]

        tool_cols = st.columns(4)

        for i, tool in enumerate(related_tools):
            with tool_cols[i % 4]:
                show_card(
                    tool["name"],
                    photo(tool["image"], 600),
                    tool["description"],
                    tool["price"]
                )

                quantity = st.number_input(
                    "Quantity",
                    min_value=1,
                    max_value=10,
                    value=1,
                    key=f"worker_qty_{tool['id']}"
                )

                if st.button(
                    "Add Tool",
                    key=f"worker_tool_{tool['id']}"
                ):
                    add_tool(tool, quantity)


# -------------------- TOOLS SHOP --------------------

elif page == "🛒 Tools Shop":
    st.title("🛒 Home-Service Tools Shop")

    job_options = ["All Workers"] + [
        w["job"] for w in WORKERS
    ]

    job = st.selectbox("Filter tools by worker", job_options)

    search = st.text_input("Search for a tool")

    tools = [
        t for t in TOOLS
        if (job == "All Workers" or t["job"] == job)
        and search.lower() in t["name"].lower()
    ]

    cols = st.columns(3)

    for i, tool in enumerate(tools):
        with cols[i % 3]:
            show_card(
                tool["name"],
                photo(tool["image"], 600),
                f'{tool["job"]} · {tool["description"]}',
                tool["price"]
            )

            quantity = st.number_input(
                "Quantity",
                min_value=1,
                max_value=10,
                value=1,
                key=f"shop_qty_{tool['id']}"
            )

            if st.button(
                "Add to Cart",
                key=f"shop_add_{tool['id']}"
            ):
                add_tool(tool, quantity)

    if not tools:
        st.info("No tools found for this search.")


# -------------------- CHECKOUT --------------------

elif page == "🧾 Checkout":
    st.title("🧾 Checkout")
    st.write(
        "Review everything you selected. Remove unwanted items "
        "before confirming."
    )

    st.subheader("🏠 Selected Properties")

    if st.session_state.pending_properties:
        for item in st.session_state.pending_properties[:]:
            with st.container(border=True):
                left, right = st.columns([4, 1])

                with left:
                    st.write(f'**{item["name"]}**')
                    st.write(
                        f'{item["deal"]} · {item["city"]} · '
                        f'{item["kind"]}'
                    )
                    st.write(f'Price: {money(item["price"])}')

                with right:
                    if st.button(
                        "Remove",
                        key=f"remove_property_{item['id']}"
                    ):
                        st.session_state.pending_properties = [
                            p for p in st.session_state.pending_properties
                            if p["id"] != item["id"]
                        ]
                        st.rerun()
    else:
        st.info("No properties selected.")

    st.divider()
    st.subheader("🧰 Worker Bookings")

    if st.session_state.pending_bookings:
        for booking in st.session_state.pending_bookings[:]:
            with st.container(border=True):
                left, right = st.columns([4, 1])

                with left:
                    st.write(
                        f'**{booking["worker"]} — {booking["job"]}**'
                    )
                    st.write(
                        f'{booking["period"]} · {booking["date"]}'
                    )
                    st.write(f'Customer: {booking["customer"]}')
                    st.write(f'Payment: {booking["payment"]}')
                    st.write(f'Price: {money(booking["price"])}')

                with right:
                    if st.button(
                        "Remove",
                        key=f"remove_booking_{booking['id']}"
                    ):
                        st.session_state.pending_bookings = [
                            b for b in st.session_state.pending_bookings
                            if b["id"] != booking["id"]
                        ]
                        st.rerun()
    else:
        st.info("No worker bookings selected.")

    st.divider()
    st.subheader("🛒 Tools Cart")

    if st.session_state.cart:
        for item in st.session_state.cart[:]:
            with st.container(border=True):
                left, middle, right = st.columns([3, 2, 1])

                with left:
                    st.write(f'**{item["name"]}**')
                    st.caption(item["job"])
                    st.write(f'Price each: {money(item["price"])}')

                with middle:
                    new_quantity = st.number_input(
                        "Quantity",
                        min_value=1,
                        max_value=10,
                        value=item["quantity"],
                        key=f"checkout_qty_{item['id']}"
                    )

                    if new_quantity != item["quantity"]:
                        item["quantity"] = new_quantity

                with right:
                    st.write(
                        money(item["price"] * item["quantity"])
                    )

                    if st.button(
                        "Remove",
                        key=f"remove_tool_{item['id']}"
                    ):
                        st.session_state.cart = [
                            t for t in st.session_state.cart
                            if t["id"] != item["id"]
                        ]
                        st.rerun()
    else:
        st.info("Your tools cart is empty.")

    st.divider()

    total = checkout_total()

    st.markdown(f"## Total: {money(total)}")

    if st.button("🗑️ Clear All Selections", use_container_width=True):
        st.session_state.pending_properties = []
        st.session_state.pending_bookings = []
        st.session_state.cart = []
        st.success("All pending selections removed.")
        st.rerun()

    has_items = (
        st.session_state.pending_properties
        or st.session_state.pending_bookings
        or st.session_state.cart
    )

    if has_items:
        st.success("Your selections are ready for review.")
        st.info(
            "When you are ready, open Final Confirmation "
            "to enter your details and confirm."
        )
    else:
        st.warning("Add a property, worker booking or tool before checkout.")


# -------------------- SPIN & OFFERS --------------------

elif page == "🎁 Spin & Offers":
    st.title("🎁 Spin & Offers")

    st.markdown("""
    <div class="hero">
        <h1>🎡 Lucky Home-Service Wheel</h1>
        <p>Try your luck with a sample discount.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "### 🟢 5%   🔵 10%   🟡 15%   🟣 20%   🎉 FREE"
    )

    if not st.session_state.discount_spun:
        if st.button("🎡 SPIN NOW", use_container_width=True):
            st.session_state.discount = random.choice([5, 10, 15, 20])
            st.session_state.discount_spun = True
            st.rerun()
    else:
        st.success(
            f'🎉 You received a demo offer of '
            f'{st.session_state.discount}%!'
        )

        st.caption(
            "This is a demonstration offer. It is not a real discount "
            "unless your application implements a validated pricing system."
        )

        if st.button("Spin Again"):
            st.session_state.discount = random.choice([5, 10, 15, 20])
            st.rerun()


# -------------------- FINAL CONFIRMATION --------------------

elif page == "✅ Final Confirmation":
    st.title("✅ Final Confirmation")

    st.write(
        "Review your selected properties, bookings and tools "
        "before submitting your request."
    )

    has_items = (
        st.session_state.pending_properties
        or st.session_state.pending_bookings
        or st.session_state.cart
    )

    if not has_items:
        st.info(
            "Nothing to confirm yet. Select items from Rent Houses, "
            "Property Sales, Workers or Tools Shop."
        )
    else:
        st.subheader("Your Selected Items")

        for item in st.session_state.pending_properties:
            st.write(
                f'🏠 {item["name"]} — {money(item["price"])}'
            )

        for booking in st.session_state.pending_bookings:
            st.write(
                f'🧰 {booking["worker"]} ({booking["period"]}) — '
                f'{money(booking["price"])}'
            )

        for item in st.session_state.cart:
            st.write(
                f'🛒 {item["name"]} × {item["quantity"]} — '
                f'{money(item["price"] * item["quantity"])}'
            )

        st.divider()

        total = checkout_total()

        discount_percent = (
            st.session_state.discount
            if st.session_state.discount_spun else 0
        )

        discount_amount = round(total * discount_percent / 100)
        final_total = max(0, total - discount_amount)

        st.write(f"Subtotal: **{money(total)}**")

        if discount_percent:
            st.write(
                f"Demo discount ({discount_percent}%): "
                f"**−{money(discount_amount)}**"
            )

        st.markdown(f"## Final total: {money(final_total)}")

        st.divider()
        st.subheader("Customer Details")

        with st.form("final_confirmation_form"):
            customer = st.text_input("Full name")
            phone = st.text_input("10-digit mobile number")
            address = st.text_area("Address")

            payment = st.radio(
                "Payment method",
                ["Cash", "Online Payment (Demo)"],
                horizontal=True
            )

            agreed = st.checkbox(
                "I have reviewed my selected items and details."
            )

            submitted = st.form_submit_button(
                "✅ Confirm All Selections",
                use_container_width=True
            )

        if submitted:
            error = validate_customer(customer, phone, address)

            if error:
                st.error(error)
            elif not agreed:
                st.error("Please confirm that you reviewed your selections.")
            else:
                reference = make_reference()

                result = {
                    "reference": reference,
                    "customer": customer.strip(),
                    "phone": phone.strip(),
                    "address": address.strip(),
                    "payment": payment,
                    "subtotal": total,
                    "discount_percent": discount_percent,
                    "discount_amount": discount_amount,
                    "amount": final_total,
                    "properties": list(
                        st.session_state.pending_properties
                    ),
                    "bookings": list(
                        st.session_state.pending_bookings
                    ),
                    "items": list(st.session_state.cart),
                    "date": str(date.today())
                }

                st.session_state.orders.append(result)
                st.session_state.last_result = result

                st.session_state.property_requests.extend(
                    result["properties"]
                )
                st.session_state.bookings.extend(
                    result["bookings"]
                )

                st.session_state.pending_properties = []
                st.session_state.pending_bookings = []
                st.session_state.cart = []

                st.session_state.discount = 0
                st.session_state.discount_spun = False

                st.session_state.confirmed_result = result

                st.rerun()

    result = st.session_state.get("confirmed_result")

    if result:
        st.divider()
        st.markdown("""
        <div style="
            text-align:center;
            padding:30px;
            border-radius:20px;
            background:#e8fff1;
            border:2px solid #20a464;">
            <div style="
                width:90px;
                height:90px;
                margin:auto;
                border-radius:50%;
                background:#20a464;
                color:white;
                font-size:60px;
                line-height:90px;">✓</div>
            <h1 style="color:#137847;">Successfully Submitted!</h1>
            <p style="color:#137847;">
                Your request has been recorded in this demo session.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write(f'**Reference number:** {result["reference"]}')
        st.write(f'**Customer:** {result["customer"]}')
        st.write(f'**Payment option:** {result["payment"]}')
        st.write(f'**Final total:** {money(result["amount"])}')

        st.success(
            "Your selections have been saved. Open My Requests to review them."
        )

        st.caption(
            "Online payment is a demo only. No real payment has been processed."
        )


# -------------------- MY REQUESTS --------------------

elif page == "📋 My Requests":
    st.markdown("""
    <div class="hero">
        <h1>📋 My Requests</h1>
        <p>Review confirmed bookings, property requests and orders.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🏠 Property Requests")

    if st.session_state.property_requests:
        for item in reversed(st.session_state.property_requests):
            with st.container(border=True):
                st.write(f'**Property:** {item["name"]}')
                st.write(f'**Type:** {item["deal"]}')
                st.write(f'**City:** {item["city"]}')
                st.write(f'**Price:** {money(item["price"])}')
    else:
        st.info("No property requests yet.")

    st.divider()
    st.subheader("🧰 Worker Bookings")

    if st.session_state.bookings:
        for booking in reversed(st.session_state.bookings):
            with st.container(border=True):
                st.write(f'**Worker:** {booking["worker"]}')
                st.write(f'**Service:** {booking["job"]}')
                st.write(f'**Period:** {booking["period"]}')
                st.write(f'**Date:** {booking["date"]}')
                st.write(f'**Price:** {money(booking["price"])}')
                st.write(f'**Payment:** {booking["payment"]}')
    else:
        st.info("No worker bookings yet.")

    st.divider()
    st.subheader("🛒 Confirmed Orders")

    if st.session_state.orders:
        for order in reversed(st.session_state.orders):
            with st.container(border=True):
                st.success("✓ Order confirmed")
                st.write(f'**Reference:** {order["reference"]}')
                st.write(f'**Customer:** {order["customer"]}')
                st.write(f'**Date:** {order["date"]}')
                st.write(f'**Subtotal:** {money(order["subtotal"])}')
                st.write(f'**Final total:** {money(order["amount"])}')
                st.write(f'**Payment:** {order["payment"]}')

                if order["properties"]:
                    st.write("**Properties:**")
                    for item in order["properties"]:
                        st.write(f'- {item["name"]}')

                if order["bookings"]:
                    st.write("**Worker bookings:**")
                    for booking in order["bookings"]:
                        st.write(
                            f'- {booking["worker"]} — {booking["period"]}'
                        )

                if order["items"]:
                    st.write("**Tools:**")
                    for item in order["items"]:
                        st.write(
                            f'- {item["name"]} × {item["quantity"]}'
                        )
    else:
        st.info("No confirmed orders yet.")


# -------------------- FOOTER --------------------

st.divider()

st.caption(
    "GharSeva India | Built with Python and Streamlit. "
    "Sample listings and prices only. Requests are stored in the "
    "current session; permanent storage and real payment integration "
    "require a database and payment provider."
)