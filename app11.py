import streamlit as st
from datetime import date
import uuid

st.set_page_config(
    page_title="GharSeva India",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f4f8ff, #ffffff);
}
[data-testid="stSidebar"] {
    background: #102b46;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.hero {
    background: linear-gradient(120deg, #123b5d, #147d78);
    padding: 28px;
    border-radius: 18px;
    color: white;
    margin-bottom: 22px;
}
.hero h1, .hero p {
    color: white !important;
}
.price {
    color: #087f5b;
    font-size: 22px;
    font-weight: 800;
}
div.stButton > button {
    border-radius: 10px;
    min-height: 42px;
    font-weight: 650;
}
[data-testid="stImage"] img {
    border-radius: 12px;
    object-fit: cover;
}
.success-panel {
    text-align: center;
    padding: 25px;
    border-radius: 18px;
    background: #e8fff1;
    border: 1px solid #75d99a;
}
</style>
""", unsafe_allow_html=True)


def money(value):
    return f"₹{value:,.0f}"


def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


# -------------------- PROPERTY DATA --------------------

PROPERTIES = [
    {
        "id": 1, "title": "Modern Family House",
        "city": "Hyderabad", "area": "Miyapur",
        "kind": "House", "deal": "Rent", "price": 18000,
        "unit": "/month", "size": "1500 sq.ft",
        "details": "3 bedrooms · 2 bathrooms · Parking",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 2, "title": "Comfortable City Flat",
        "city": "Vijayawada", "area": "Benz Circle",
        "kind": "Flat", "deal": "Rent", "price": 14000,
        "unit": "/month", "size": "1100 sq.ft",
        "details": "2 bedrooms · Lift · Family friendly",
        "image": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 3, "title": "Premium Independent House",
        "city": "Visakhapatnam", "area": "Madhurawada",
        "kind": "House", "deal": "Rent", "price": 22000,
        "unit": "/month", "size": "1800 sq.ft",
        "details": "3 bedrooms · Parking · Garden",
        "image": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 4, "title": "Residential Plot",
        "city": "Guntur", "area": "Amaravathi Road",
        "kind": "Land", "deal": "Sale", "price": 1800000,
        "unit": " total", "size": "10 cents",
        "details": "Road access · Residential area",
        "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 5, "title": "Independent House for Sale",
        "city": "Visakhapatnam", "area": "Madhurawada",
        "kind": "House", "deal": "Sale", "price": 6500000,
        "unit": " total", "size": "2200 sq.ft",
        "details": "3 bedrooms · Family home · Parking",
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 6, "title": "Open Agricultural Land",
        "city": "Guntur", "area": "Tenali",
        "kind": "Land", "deal": "Sale", "price": 2500000,
        "unit": " total", "size": "20 cents",
        "details": "Road access · Verify land documents",
        "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 7, "title": "Modern City Apartment",
        "city": "Hyderabad", "area": "Kukatpally",
        "kind": "Flat", "deal": "Sale", "price": 7200000,
        "unit": " total", "size": "1450 sq.ft",
        "details": "3 bedrooms · Lift · Security",
        "image": "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=900&q=85"
    },
    {
        "id": 8, "title": "Commercial Building",
        "city": "Vijayawada", "area": "Main Road",
        "kind": "Building", "deal": "Sale", "price": 12000000,
        "unit": " total", "size": "3200 sq.ft",
        "details": "Commercial use · Main-road location",
        "image": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=900&q=85"
    }
]


# -------------------- WORKER AND TOOL DATA --------------------

worker_seed = [
    (
        "Ravi Kumar", "Plumber", 700, 4000, 14000,
        "Tap leaks, pipe repair, sink fitting and bathroom plumbing.",
        "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=900&q=85",
        [
            ("Pipe Wrench", 850, "Adjustable wrench for pipe fitting",
             "https://images.unsplash.com/photo-1586864387967-d02ef85d93e8"),
            ("Basin Wrench", 650, "Tool for basin and sink connections",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c"),
            ("Plier Set", 550, "Heavy-duty plumbing pliers",
             "https://images.unsplash.com/photo-1530124566582-a618bc2615dc"),
            ("Teflon Tape", 120, "Thread sealing tape",
             "https://images.unsplash.com/photo-1581092160607-ee22621dd758")
        ]
    ),
    (
        "Suresh Babu", "Carpenter", 900, 5200, 18000,
        "Door repair, furniture work, shelves and wood fitting.",
        "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?auto=format&fit=crop&w=900&q=85",
        [
            ("Wood Hammer", 450, "Professional carpenter hammer",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c"),
            ("Hand Saw", 750, "Fine-tooth wood cutting saw",
             "https://images.unsplash.com/photo-1530124566582-a618bc2615dc"),
            ("Screwdriver Set", 600, "Multiple-size screwdriver set",
             "https://images.unsplash.com/photo-1586864387967-d02ef85d93e8"),
            ("Measuring Tape", 250, "5 metre measuring tape",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c")
        ]
    ),
    (
        "Imran Ali", "Painter", 1000, 6000, 21000,
        "Interior walls, exterior painting and finishing work.",
        "https://images.unsplash.com/photo-1562259949-e8e7689d7828?auto=format&fit=crop&w=900&q=85",
        [
            ("Paint Roller", 350, "Wall paint roller",
             "https://images.unsplash.com/photo-1562259949-e8e7689d7828"),
            ("Paint Brush Set", 299, "Different-size painting brushes",
             "https://images.unsplash.com/photo-1513364776144-60967b0f800f"),
            ("Paint Tray", 220, "Paint roller tray",
             "https://images.unsplash.com/photo-1562259949-e8e7689d7828"),
            ("Scraper", 180, "Wall preparation scraper",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c")
        ]
    ),
    (
        "Kiran", "Cleaner", 500, 2800, 9500,
        "Bathroom, kitchen, floor and complete home cleaning.",
        "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=900&q=85",
        [
            ("Cleaning Brush Set", 299, "Multi-purpose cleaning brushes",
             "https://images.unsplash.com/photo-1581578731548-c64695cc6952"),
            ("Floor Mop", 450, "Microfiber floor mop",
             "https://images.unsplash.com/photo-1581578731548-c64695cc6952"),
            ("Cleaning Bucket", 250, "Strong plastic cleaning bucket",
             "https://images.unsplash.com/photo-1581578731548-c64695cc6952"),
            ("Rubber Gloves", 150, "Protective cleaning gloves",
             "https://images.unsplash.com/photo-1581578731548-c64695cc6952")
        ]
    ),
    (
        "Arjun Singh", "Electrician", 800, 4500, 15500,
        "Switches, wiring, lights, fans and electrical repairs.",
        "https://images.unsplash.com/photo-1621905251918-48416bd8575a?auto=format&fit=crop&w=900&q=85",
        [
            ("Digital Multimeter", 850, "Voltage and current testing meter",
             "https://images.unsplash.com/photo-1581092160607-ee22621dd758"),
            ("Wire Stripper", 450, "Wire cutting and stripping tool",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c"),
            ("Voltage Tester", 180, "Electrical voltage tester",
             "https://images.unsplash.com/photo-1530124566582-a618bc2615dc"),
            ("Insulated Screwdriver Set", 650, "Electrical insulated screwdrivers",
             "https://images.unsplash.com/photo-1586864387967-d02ef85d93e8")
        ]
    ),
    (
        "Manoj Reddy", "Mechanic", 900, 5200, 18000,
        "Two-wheeler and basic vehicle repair and maintenance.",
        "https://images.unsplash.com/photo-1487754180451-c456f719a1fc?auto=format&fit=crop&w=900&q=85",
        [
            ("Spanner Set", 950, "Combination spanner set",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c"),
            ("Socket Set", 1250, "Vehicle maintenance socket kit",
             "https://images.unsplash.com/photo-1530124566582-a618bc2615dc"),
            ("Pliers", 350, "Heavy-duty mechanic pliers",
             "https://images.unsplash.com/photo-1586864387967-d02ef85d93e8"),
            ("Torque Wrench", 1800, "Torque control wrench",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c")
        ]
    ),
    (
        "Ramesh Kumar", "Welder", 1100, 6500, 23000,
        "Metal gates, grills, frames and welding repairs.",
        "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?auto=format&fit=crop&w=900&q=85",
        [
            ("Welding Machine", 6500, "Compact welding machine",
             "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122"),
            ("Welding Helmet", 950, "Protective welding helmet",
             "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122"),
            ("Welding Gloves", 450, "Heat-resistant gloves",
             "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122"),
            ("Angle Grinder", 2400, "Metal cutting and grinding tool",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c")
        ]
    ),
    (
        "Deepak Yadav", "Mason", 1000, 6000, 21000,
        "Brickwork, plastering, tiles and small construction repairs.",
        "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=900&q=85",
        [
            ("Brick Trowel", 280, "Masonry brick laying trowel",
             "https://images.unsplash.com/photo-1503387762-592deb58ef4e"),
            ("Spirit Level", 450, "Level checking tool",
             "https://images.unsplash.com/photo-1503387762-592deb58ef4e"),
            ("Plastering Trowel", 350, "Wall plaster finishing tool",
             "https://images.unsplash.com/photo-1503387762-592deb58ef4e"),
            ("Mason Hammer", 500, "Brick and masonry hammer",
             "https://images.unsplash.com/photo-1503387762-592deb58ef4e")
        ]
    ),
    (
        "Vijay Rao", "Gardener", 600, 3400, 11500,
        "Garden cleaning, pruning, planting and lawn maintenance.",
        "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&w=900&q=85",
        [
            ("Garden Shears", 550, "Plant pruning shears",
             "https://images.unsplash.com/photo-1416879595882-3373a0480b5b"),
            ("Hand Trowel", 220, "Small garden planting tool",
             "https://images.unsplash.com/photo-1416879595882-3373a0480b5b"),
            ("Garden Gloves", 180, "Protective garden gloves",
             "https://images.unsplash.com/photo-1416879595882-3373a0480b5b"),
            ("Watering Can", 350, "Garden watering can",
             "https://images.unsplash.com/photo-1416879595882-3373a0480b5b")
        ]
    ),
    (
        "Rahul Das", "AC Technician", 900, 5200, 18000,
        "AC service, cleaning, installation and basic repairs.",
        "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?auto=format&fit=crop&w=900&q=85",
        [
            ("AC Manifold Gauge", 1800, "AC pressure testing gauge",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c"),
            ("Digital Clamp Meter", 1200, "Electrical testing clamp meter",
             "https://images.unsplash.com/photo-1581092160607-ee22621dd758"),
            ("Fin Cleaning Brush", 250, "Air-conditioner fin cleaning brush",
             "https://images.unsplash.com/photo-1581578731548-c64695cc6952"),
            ("Tool Bag", 850, "Technician tool carrying bag",
             "https://images.unsplash.com/photo-1504148455328-c376907d081c")
        ]
    )
]


WORKERS = []

for i, item in enumerate(worker_seed):
    tools = []

    for tool in item[7]:
        image = tool[3]

        if "?" not in image:
            image += "?auto=format&fit=crop&w=700&q=85"

        tools.append((tool[0], tool[1], tool[2], image))

    WORKERS.append({
        "id": i + 1,
        "name": item[0],
        "job": item[1],
        "daily": item[2],
        "weekly": item[3],
        "monthly": item[4],
        "description": item[5],
        "image": item[6],
        "tools": tools
    })


# -------------------- SESSION STATE --------------------

defaults = {
    "worker_bookings": [],
    "property_requests": [],
    "tool_orders": [],
    "cart": [],
    "selected_worker": None,
    "selected_property": None,
    "last_success": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def find_worker(worker_id):
    return next(
        (worker for worker in WORKERS if worker["id"] == worker_id),
        None
    )


# -------------------- HORIZONTAL PROPERTY CARD --------------------

def property_card(item, key_prefix):
    with st.container(border=True):
        st.image(item["image"], use_container_width=True)
        st.markdown(f"### {item['title']}")
        st.caption(f"📍 {item['area']}, {item['city']}")

        st.markdown(
            f'<div class="price">{money(item["price"])}'
            f'{item["unit"]}</div>',
            unsafe_allow_html=True
        )

        st.write(f"**{item['deal']} · {item['kind']}**")
        st.write(f"**Area:** {item['size']}")
        st.write(item["details"])

        if st.button(
            "View / Request Property",
            key=f"{key_prefix}_{item['id']}",
            use_container_width=True
        ):
            st.session_state.selected_property = item["id"]
            st.rerun()


# -------------------- HORIZONTAL WORKER CARD --------------------

def worker_card(worker):
    with st.container(border=True):
        st.image(worker["image"], use_container_width=True)
        st.markdown(f"### {worker['job']}")
        st.write(f"**Worker:** {worker['name']}")
        st.write(worker["description"])

        c1, c2, c3 = st.columns(3)

        c1.metric("Daily", money(worker["daily"]))
        c2.metric("Weekly", money(worker["weekly"]))
        c3.metric("Monthly", money(worker["monthly"]))

        if st.button(
            "Select Worker",
            key=f"worker_{worker['id']}",
            use_container_width=True
        ):
            st.session_state.selected_worker = worker["id"]
            st.rerun()


# -------------------- SIDEBAR --------------------

st.sidebar.title("🏡 GharSeva India")
st.sidebar.caption("Your home, your services, one place.")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🏘️ Rent Houses",
        "🏷️ Sale Houses & Land",
        "🧰 Book a Worker",
        "🛒 Tools Shop",
        "🧾 Checkout",
        "✅ My Requests"
    ]
)

st.sidebar.divider()
st.sidebar.info(
    "Demo application. Listings, workers and prices are sample data."
)


# -------------------- HOME PAGE --------------------

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🏡 GharSeva India</h1>
        <p>Find a home, book a worker and shop useful tools.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Explore Our Services")

    cols = st.columns(3)

    with cols[0]:
        st.image(PROPERTIES[0]["image"], use_container_width=True)
        st.markdown("### 🏠 Find a Home")
        st.write("Explore properties for rent and sale.")

    with cols[1]:
        st.image(WORKERS[0]["image"], use_container_width=True)
        st.markdown("### 🧰 Book a Worker")
        st.write("Find a plumber, electrician, carpenter and more.")

    with cols[2]:
        st.image(WORKERS[1]["tools"][0][3], use_container_width=True)
        st.markdown("### 🛒 Shop Tools")
        st.write("Purchase tools for home maintenance.")

    st.divider()
    st.subheader("⭐ Featured Properties")

    cols = st.columns(3)

    for i, item in enumerate(PROPERTIES[:3]):
        with cols[i % 3]:
            property_card(item, "home")

    st.divider()
    st.subheader("👷 Popular Workers")

    cols = st.columns(3)

    for i, worker in enumerate(WORKERS[:3]):
        with cols[i % 3]:
            worker_card(worker)


# -------------------- RENT PAGE --------------------

elif page == "🏘️ Rent Houses":

    st.title("🏘️ Houses for Rent")

    rent_items = [
        p for p in PROPERTIES if p["deal"] == "Rent"
    ]

    city = st.selectbox(
        "Filter by city",
        ["All Cities"] + sorted({p["city"] for p in rent_items})
    )

    filtered = [
        p for p in rent_items
        if city == "All Cities" or p["city"] == city
    ]

    cols = st.columns(3)

    for i, item in enumerate(filtered):
        with cols[i % 3]:
            property_card(item, "rent")

    selected = next(
        (p for p in rent_items
         if p["id"] == st.session_state.selected_property),
        None
    )

    if selected:
        st.divider()
        st.subheader("📅 Request a Property Visit")

        with st.form("rent_form"):
            name = st.text_input("Your name")
            phone = st.text_input("10-digit phone number")
            visit = st.date_input(
                "Preferred visit date",
                min_value=date.today()
            )

            submitted = st.form_submit_button(
                "Confirm Property Request",
                use_container_width=True
            )

        if submitted:
            if not name.strip() or not valid_phone(phone):
                st.error("Enter your name and a valid 10-digit phone number.")
            else:
                st.session_state.property_requests.append({
                    "property": selected["title"],
                    "deal": "Rent",
                    "price": selected["price"],
                    "name": name,
                    "phone": phone,
                    "date": str(visit)
                })

                request_id = uuid.uuid4().hex[:8].upper()

                st.session_state.last_success = {
                    "title": "Property request submitted",
                    "message": "Your property visit request has been saved.",
                    "id": request_id
                }

                st.success("Property request submitted successfully!")


# -------------------- SALE PAGE --------------------

elif page == "🏷️ Sale Houses & Land":

    st.title("🏷️ Houses & Land for Sale")

    sale_items = [
        p for p in PROPERTIES if p["deal"] == "Sale"
    ]

    kind = st.selectbox(
        "Filter by property type",
        ["All", "House", "Flat", "Land", "Building"]
    )

    filtered = [
        p for p in sale_items
        if kind == "All" or p["kind"] == kind
    ]

    cols = st.columns(3)

    for i, item in enumerate(filtered):
        with cols[i % 3]:
            property_card(item, "sale")

    selected = next(
        (p for p in sale_items
         if p["id"] == st.session_state.selected_property),
        None
    )

    if selected:
        st.divider()
        st.subheader("📅 Request a Property Visit")

        with st.form("sale_form"):
            name = st.text_input("Buyer name")
            phone = st.text_input("10-digit phone number")
            visit = st.date_input(
                "Preferred visit date",
                min_value=date.today()
            )

            submitted = st.form_submit_button(
                "Confirm Property Request",
                use_container_width=True
            )

        if submitted:
            if not name.strip() or not valid_phone(phone):
                st.error("Enter your name and a valid 10-digit phone number.")
            else:
                st.session_state.property_requests.append({
                    "property": selected["title"],
                    "deal": "Sale",
                    "price": selected["price"],
                    "name": name,
                    "phone": phone,
                    "date": str(visit)
                })

                request_id = uuid.uuid4().hex[:8].upper()

                st.session_state.last_success = {
                    "title": "Property request submitted",
                    "message": "Your property visit request has been saved.",
                    "id": request_id
                }

                st.success("Property request submitted successfully!")


# -------------------- WORKER BOOKING PAGE --------------------

elif page == "🧰 Book a Worker":

    st.title("🧰 Book a Home-Service Worker")
    st.write("Select a worker and choose the service period.")

    job_filter = st.selectbox(
        "Worker type",
        ["All Workers"] + [w["job"] for w in WORKERS]
    )

    workers = [
        w for w in WORKERS
        if job_filter == "All Workers" or w["job"] == job_filter
    ]

    cols = st.columns(3)

    for i, worker in enumerate(workers):
        with cols[i % 3]:
            worker_card(worker)

    worker = find_worker(st.session_state.selected_worker)

    if worker:
        st.divider()
        st.header(f"📋 Book {worker['job']} — {worker['name']}")
        st.write(worker["description"])

        with st.form(f"booking_form_{worker['id']}"):

            period = st.radio(
                "Service period",
                ["Daily", "Weekly", "Monthly"],
                horizontal=True
            )

            price = {
                "Daily": worker["daily"],
                "Weekly": worker["weekly"],
                "Monthly": worker["monthly"]
            }[period]

            st.markdown(
                f'<div class="price">Service price: {money(price)}</div>',
                unsafe_allow_html=True
            )

            booking_date = st.date_input(
                "Service start date",
                min_value=date.today()
            )

            customer = st.text_input("Customer name")
            phone = st.text_input("10-digit phone number")
            address = st.text_area("Service address")

            payment = st.radio(
                "Payment method",
                ["Cash payment", "Online payment (demo)"],
                horizontal=True
            )

            submitted = st.form_submit_button(
                "Confirm Worker Booking",
                use_container_width=True
            )

        if submitted:
            if (
                not customer.strip()
                or not valid_phone(phone)
                or not address.strip()
            ):
                st.error(
                    "Enter your name, valid phone number and service address."
                )
            else:
                booking_id = uuid.uuid4().hex[:8].upper()

                st.session_state.worker_bookings.append({
                    "id": booking_id,
                    "worker": worker["name"],
                    "job": worker["job"],
                    "period": period,
                    "price": price,
                    "date": str(booking_date),
                    "name": customer,
                    "phone": phone,
                    "address": address,
                    "payment": payment,
                    "status": "Confirmed"
                })

                st.session_state.last_success = {
                    "title": "Worker booking successful",
                    "message": f"{worker['job']} booking confirmed.",
                    "id": booking_id
                }

                st.success("Worker booking confirmed!")
                st.balloons()

        st.divider()
        st.subheader(f"🛠️ Tools used by {worker['job']}")

        cols = st.columns(4)

        for i, tool in enumerate(worker["tools"]):
            name, price, description, image = tool

            with cols[i % 4]:
                with st.container(border=True):
                    st.image(image, use_container_width=True)
                    st.markdown(f"### {name}")
                    st.write(description)

                    st.markdown(
                        f'<div class="price">{money(price)}</div>',
                        unsafe_allow_html=True
                    )

                    qty = st.number_input(
                        "Quantity",
                        min_value=1,
                        max_value=10,
                        value=1,
                        key=f"worker_qty_{worker['id']}_{i}"
                    )

                    if st.button(
                        "🛒 Add to Cart",
                        key=f"worker_add_{worker['id']}_{i}",
                        use_container_width=True
                    ):
                        st.session_state.cart.append({
                            "name": name,
                            "price": price,
                            "quantity": qty,
                            "worker_job": worker["job"]
                        })

                        st.success("Added to cart!")


# -------------------- TOOLS SHOP PAGE --------------------

elif page == "🛒 Tools Shop":

    st.title("🛒 Tools Shop")

    selected_job = st.selectbox(
        "Show tools for",
        ["All Workers"] + [w["job"] for w in WORKERS]
    )

    all_tools = []

    for worker in WORKERS:
        if (
            selected_job != "All Workers"
            and worker["job"] != selected_job
        ):
            continue

        for tool in worker["tools"]:
            all_tools.append({
                "name": tool[0],
                "price": tool[1],
                "description": tool[2],
                "image": tool[3],
                "job": worker["job"]
            })

    st.write(f"Available tools: {len(all_tools)}")

    cols = st.columns(3)

    for i, tool in enumerate(all_tools):

        with cols[i % 3]:
            with st.container(border=True):

                st.image(tool["image"], use_container_width=True)
                st.markdown(f"### {tool['name']}")
                st.caption(f"Related worker: {tool['job']}")
                st.write(tool["description"])

                st.markdown(
                    f'<div class="price">{money(tool["price"])}</div>',
                    unsafe_allow_html=True
                )

                qty = st.number_input(
                    "Quantity",
                    min_value=1,
                    max_value=10,
                    value=1,
                    key=f"shop_qty_{i}"
                )

                if st.button(
                    "🛒 Add to Cart",
                    key=f"shop_add_{i}",
                    use_container_width=True
                ):
                    st.session_state.cart.append({
                        "name": tool["name"],
                        "price": tool["price"],
                        "quantity": qty,
                        "worker_job": tool["job"]
                    })

                    st.success("Added to cart!")

    st.info("Open Checkout to review your cart and place your order.")


# -------------------- CHECKOUT PAGE --------------------

elif page == "🧾 Checkout":

    st.title("🧾 Checkout")

    if not st.session_state.cart:
        st.info("Your cart is empty. Add tools before checkout.")

    else:
        total = sum(
            item["price"] * item["quantity"]
            for item in st.session_state.cart
        )

        st.subheader("1. Order Summary")

        for i, item in enumerate(st.session_state.cart):

            c1, c2, c3, c4 = st.columns([3, 1, 1, 1])

            c1.write(f"**{item['name']}**")
            c2.write(f"Qty: {item['quantity']}")
            c3.write(money(item["price"] * item["quantity"]))

            if c4.button("Remove", key=f"remove_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()

        st.divider()

        st.markdown(f"## Total Amount: {money(total)}")

        st.subheader("2. Delivery Details")

        with st.form("checkout_form"):

            customer = st.text_input("Customer name")
            phone = st.text_input("10-digit phone number")
            address = st.text_area("Delivery address")

            payment = st.radio(
                "Choose payment method",
                ["Cash on Delivery", "Online Payment (Demo)"],
                horizontal=True
            )

            if payment == "Online Payment (Demo)":
                st.info(
                    "Demo payment only. No real money is collected."
                )

            submitted = st.form_submit_button(
                "Place Order",
                use_container_width=True
            )

        if submitted:

            if (
                not customer.strip()
                or not valid_phone(phone)
                or not address.strip()
            ):
                st.error(
                    "Enter your name, valid phone number and delivery address."
                )

            else:
                order_id = uuid.uuid4().hex[:8].upper()

                st.session_state.tool_orders.append({
                    "id": order_id,
                    "customer": customer,
                    "phone": phone,
                    "address": address,
                    "items": list(st.session_state.cart),
                    "total": total,
                    "payment": payment,
                    "date": str(date.today()),
                    "status": "Confirmed"
                })

                st.session_state.cart = []

                st.session_state.last_success = {
                    "title": "Order placed successfully",
                    "message": f"Payment method: {payment}",
                    "id": order_id
                }

                st.success("Your order has been placed successfully!")
                st.balloons()

                st.markdown("""
                <div class="success-panel">
                    <h1>✅ Order Successful</h1>
                    <p>Thank you for shopping with GharSeva India.</p>
                </div>
                """, unsafe_allow_html=True)


# -------------------- MY REQUESTS PAGE --------------------

elif page == "✅ My Requests":

    st.title("✅ My Requests")

    success = st.session_state.last_success

    if success:
        st.markdown(f"""
        <div class="success-panel">
            <h1>✅ {success['title']}</h1>
            <p>{success['message']}</p>
            <p><b>Reference ID:</b> {success['id']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("🏠 Property Requests")

    if st.session_state.property_requests:

        for item in reversed(st.session_state.property_requests):
            with st.container(border=True):
                c1, c2, c3 = st.columns(3)

                c1.write(f"**Property:** {item['property']}")
                c2.write(f"**Type:** {item['deal']}")
                c3.write(f"**Price:** {money(item['price'])}")

                c1.write(f"**Customer:** {item['name']}")
                c2.write(f"**Visit date:** {item['date']}")

    else:
        st.info("No property requests yet.")

    st.divider()
    st.subheader("🧰 Worker Bookings")

    if st.session_state.worker_bookings:

        for item in reversed(st.session_state.worker_bookings):
            with st.container(border=True):

                c1, c2, c3 = st.columns(3)

                c1.write(f"**Worker:** {item['worker']}")
                c2.write(f"**Job:** {item['job']}")
                c3.write(f"**Period:** {item['period']}")

                c1.write(f"**Price:** {money(item['price'])}")
                c2.write(f"**Date:** {item['date']}")
                c3.write(f"**Payment:** {item['payment']}")

                st.write(f"**Reference ID:** {item['id']}")
                st.write(f"**Customer:** {item['name']}")
                st.write(f"**Phone:** {item['phone']}")
                st.write(f"**Address:** {item['address']}")

    else:
        st.info("No worker bookings yet.")

    st.divider()
    st.subheader("🛒 Tool Orders")

    if st.session_state.tool_orders:

        for order in reversed(st.session_state.tool_orders):

            with st.container(border=True):

                st.success("✅ Order confirmed")

                c1, c2, c3 = st.columns(3)

                c1.write(f"**Order ID:** {order['id']}")
                c2.write(f"**Customer:** {order['customer']}")
                c3.write(f"**Date:** {order['date']}")

                c1.write(f"**Phone:** {order['phone']}")
                c2.write(f"**Payment:** {order['payment']}")
                c3.write(f"**Total:** {money(order['total'])}")

                st.write(f"**Address:** {order['address']}")

                for item in order["items"]:
                    st.write(
                        f"- {item['name']} × {item['quantity']} "
                        f"= {money(item['price'] * item['quantity'])}"
                    )

    else:
        st.info("No tool orders yet.")


# -------------------- FOOTER --------------------

st.divider()

st.caption(
    "GharSeva India | Python + Streamlit demo | "
    "Sample property listings, workers and prices."
)