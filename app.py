
import streamlit as st

st.set_page_config(
    page_title="AI Question Generator",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #ffffff;
    color: #17172b;
}

header[data-testid="stHeader"] {
    background: #ffffff;
    border-bottom: 1px solid #ececf4;
}

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #ececf4;
    min-width: 300px;
    max-width: 300px;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 0.7rem;
}

.block-container {
    padding: 1.2rem 2.3rem 2.5rem 2.3rem;
    max-width: 1500px;
}

/* Header */
.app-brand {
    display:flex;
    align-items:center;
    gap:14px;
    padding: 4px 0 18px 0;
}
.brand-mark {
    width:52px;
    height:52px;
    border-radius:14px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:#5429f5;
    font-size:31px;
    font-weight:800;
    border:2px solid #5429f5;
    background:#faf8ff;
}
.brand-title {font-size:25px;font-weight:800;line-height:1.1;}
.brand-subtitle {font-size:16px;color:#25253a;margin-top:5px;}

.topbar {
    height:74px;
    border-bottom:1px solid #ececf4;
    display:flex;
    align-items:center;
    justify-content:flex-end;
    gap:26px;
    margin: -18px -36px 26px -36px;
    padding:0 30px;
}
.help {font-size:16px;font-weight:600;}
.teacher {
    display:flex;
    align-items:center;
    gap:10px;
    font-weight:700;
}
.avatar {
    width:42px;height:42px;border-radius:50%;
    display:flex;align-items:center;justify-content:center;
    color:#fff;background:#4c1fe8;font-weight:700;
}
.chev {font-size:14px;margin-left:4px;}

/* Sidebar */
.side-item {
    height:48px;
    display:flex;
    align-items:center;
    gap:16px;
    padding:0 14px;
    margin:4px 0;
    border-radius:9px;
    color:#25253a;
    font-size:16px;
    font-weight:500;
}
.side-item.active {
    background:linear-gradient(90deg,#f3efff,#faf8ff);
    color:#4b22ee;
    font-weight:700;
}
.side-icon {width:28px;text-align:center;font-size:22px;color:#5a5b70;}
.side-item.active .side-icon {color:#4b22ee;}
.premium {
    margin-top:62px;
    border:1px solid #e8e4f4;
    border-radius:11px;
    padding:18px;
    background:#fff;
}
.premium-title {color:#4b22ee;font-weight:800;font-size:16px;display:flex;gap:12px;align-items:center;}
.crown {
    width:34px;height:34px;border-radius:50%;background:#f0ebff;
    display:flex;align-items:center;justify-content:center;
}
.premium hr {border:0;border-top:1px solid #ececf4;margin:15px 0;}
.usage-label {font-size:14px;color:#44455b;}
.usage {font-size:17px;font-weight:800;margin-top:6px;}
.progress {height:6px;background:#e8e8f1;border-radius:20px;margin:13px 0 22px;}
.progress > div {width:25%;height:100%;background:#5b2af3;border-radius:20px;}
.upgrade {
    border:1px solid #6a45ff;color:#4b22ee;border-radius:7px;
    text-align:center;padding:11px;font-weight:700;
}

/* Main */
.page-title {font-size:28px;font-weight:800;margin:0;}
.page-subtitle {font-size:15px;color:#4d4e66;margin-top:6px;margin-bottom:18px;}

.panel {
    border:1px solid #e5e5ee;
    border-radius:13px;
    padding:20px;
    margin-bottom:16px;
    box-shadow: 0 1px 1px rgba(30,30,70,.02);
}
.step-head {display:flex;align-items:center;gap:17px;margin-bottom:18px;}
.step-number {
    width:32px;height:32px;border-radius:50%;
    background:#4e22ef;color:#fff;
    display:flex;align-items:center;justify-content:center;
    font-weight:700;font-size:16px;
}
.step-title {font-size:18px;font-weight:800;}
.step-sub {font-size:14px;color:#515269;margin-top:5px;}

.topic-card {
    border:1px solid #e4e4ed;
    border-radius:11px;
    min-height:155px;
    padding:18px;
    text-align:center;
}
.topic-card.selected {
    border:1.5px solid #6337ff;
    background:linear-gradient(180deg,#fcfaff,#fff);
    box-shadow:0 0 0 1px rgba(99,55,255,.03);
}
.topic-icon {font-size:39px;line-height:1;margin:3px 0 13px;}
.topic-name {font-size:16px;font-weight:800;}
.topic-desc {font-size:14px;color:#4d4e66;line-height:1.55;margin-top:7px;}

.info {
    background:#f3f5ff;
    border-radius:8px;
    padding:12px 16px;
    color:#4c4e67;
    font-size:15px;
    margin-bottom:14px;
}
.info b {color:#4f22ee;}

.select-all {
    border:1px solid #e5e5ed;border-radius:9px;padding:12px 14px;
    margin-bottom:12px;
}
.select-all-title {color:#4c22ee;font-weight:700;}
.select-all-sub {font-size:12px;color:#65667a;margin-top:4px;}

[data-testid="stCheckbox"] {
    border:1px solid #e5e5ed;
    border-radius:8px;
    padding:7px 10px;
    min-height:42px;
    background:#fff;
}
[data-testid="stCheckbox"] label p {
    font-size:13px;
    color:#3f4055;
}
[data-testid="stCheckbox"] > div {
    gap: 8px;
}

/* Buttons */
div.stButton > button {
    border-radius:8px;
    min-height:44px;
    font-weight:700;
}
.generate-btn button {
    background:#5425ef !important;
    color:#fff !important;
    border:0 !important;
    font-size:17px !important;
}
.clear-btn button {
    background:#fff !important;
    color:#5425ef !important;
    border:1px solid #7655ff !important;
}

.bottom-row {margin-top:2px;}

@media (max-width: 1000px) {
    [data-testid="stSidebar"] {min-width:250px;max-width:250px;}
    .block-container {padding-left:1rem;padding-right:1rem;}
}
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("""
    <div class="app-brand">
        <div class="brand-mark">✣</div>
        <div>
            <div class="brand-title">AI Question Generator</div>
            <div class="brand-subtitle">CBSE Class XII Computer Science</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    items = [
        ("⌂", "Dashboard", False),
        ("✣", "Generate Questions", True),
        ("▤", "Question Bank", False),
        ("▧", "Question Papers", False),
        ("▦", "Blueprints", False),
        ("▥", "Reports", False),
        ("☆", "Favorites", False),
        ("⚙", "Settings", False),
        ("?", "Help & Guide", False),
    ]
    for icon, label, active in items:
        st.markdown(
            f'<div class="side-item {"active" if active else ""}">'
            f'<div class="side-icon">{icon}</div><div>{label}</div></div>',
            unsafe_allow_html=True
        )

    st.markdown("""
    <div class="premium">
        <div class="premium-title"><span class="crown">♛</span> Premium Plan</div>
        <hr>
        <div class="usage-label">Questions Generated</div>
        <div class="usage">1,248 / 5,000</div>
        <div class="progress"><div></div></div>
        <div class="upgrade">Upgrade Plan</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Top bar ----------
st.markdown("""
<div class="topbar">
    <div class="help">ⓘ &nbsp; Help</div>
    <div style="font-size:24px;">♧</div>
    <div class="teacher"><div class="avatar">TS</div> Teacher <span class="chev">⌄</span></div>
</div>
""", unsafe_allow_html=True)

# ---------- Main content ----------
st.markdown('<div class="page-title">Generate Questions</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Select topic and subtopic to generate questions.</div>', unsafe_allow_html=True)

# Topic selection
st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown("""
<div class="step-head">
    <div class="step-number">1</div>
    <div>
        <div class="step-title">Select Topic</div>
        <div class="step-sub">Choose a main topic from the syllabus.</div>
    </div>
</div>
""", unsafe_allow_html=True)

if "topic" not in st.session_state:
    st.session_state.topic = "Python"

topic_cols = st.columns(4, gap="medium")
topics = [
    ("Python", "Python Programming<br>(Basic to Advanced)", "‹/›"),
    ("Database Concepts", "Database Concepts<br>and SQL", "▤"),
    ("Computer Networks", "Computer Networks", "◎"),
    ("Societal Impacts", "of IT", "♧"),
]

for col, (name, desc, icon) in zip(topic_cols, topics):
    with col:
        selected = st.session_state.topic == name
        if st.button(
            f"{'◉' if selected else '○'}\n\n{icon}\n{name}\n\n{desc.replace('<br>', ' ')}",
            key=f"topic_{name}",
            use_container_width=True,
        ):
            st.session_state.topic = name
            st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Subtopics
subtopics_by_topic = {
    "Python": [
        "1.1 Basics of Python", "1.2 Data Types", "1.3 Operators", "1.4 Expressions",
        "1.5 Input / Output", "1.6 Control Statements", "1.7 Functions", "1.8 String Manipulation",
        "1.9 Lists", "1.10 Tuples", "1.11 Dictionaries", "1.12 File Handling",
        "1.13 Exception Handling", "1.14 Modules",
    ],
    "Database Concepts": [
        "2.1 Database Basics", "2.2 SQL Commands", "2.3 DDL Commands", "2.4 DML Commands",
        "2.5 Constraints", "2.6 Functions", "2.7 Grouping & Aggregation", "2.8 Joins",
    ],
    "Computer Networks": [
        "3.1 Network Basics", "3.2 Network Devices", "3.3 Protocols", "3.4 IP Addressing",
        "3.5 Network Security", "3.6 Web & Internet", "3.7 Transmission Media", "3.8 Topologies",
    ],
    "Societal Impacts": [
        "4.1 Digital Footprint", "4.2 Cyber Ethics", "4.3 Intellectual Property", "4.4 E-Waste",
        "4.5 Cyber Safety", "4.6 Digital Society",
    ],
}

defaults = {
    "Python": {"1.3 Operators", "1.5 Input / Output", "1.7 Functions"},
    "Database Concepts": set(),
    "Computer Networks": set(),
    "Societal Impacts": set(),
}

st.markdown('<div class="panel">', unsafe_allow_html=True)
st.markdown("""
<div class="step-head">
    <div class="step-number">2</div>
    <div>
        <div class="step-title">Select Subtopic(s)</div>
        <div class="step-sub">Choose one or more subtopics from the selected topic.</div>
    </div>
</div>
""", unsafe_allow_html=True)

topic = st.session_state.topic
st.markdown(f'<div class="info">ⓘ &nbsp; Topic Selected: <b>{topic}</b></div>', unsafe_allow_html=True)

# Select all / clear
all_key = f"all_{topic}"
if all_key not in st.session_state:
    st.session_state[all_key] = False

c1, c2 = st.columns([1, 4])
with c1:
    select_all = st.checkbox(
        "Select All",
        value=st.session_state[all_key],
        key=f"select_all_checkbox_{topic}",
    )
    if select_all != st.session_state[all_key]:
        st.session_state[all_key] = select_all
        for item in subtopics_by_topic[topic]:
            st.session_state[f"sub_{topic}_{item}"] = select_all
        st.rerun()
    st.markdown('<div class="select-all-sub">Select all subtopics</div>', unsafe_allow_html=True)

with c2:
    subs = subtopics_by_topic[topic]
    for row_start in range(0, len(subs), 4):
        cols = st.columns(4, gap="small")
        for col, item in zip(cols, subs[row_start:row_start+4]):
            key = f"sub_{topic}_{item}"
            if key not in st.session_state:
                st.session_state[key] = item in defaults.get(topic, set())
            with col:
                st.checkbox(item, key=key)

st.markdown('<div class="bottom-row">', unsafe_allow_html=True)
b1, b2 = st.columns([1, 1])
with b1:
    st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
    if st.button("♲  Clear Selection", use_container_width=True):
        for item in subtopics_by_topic[topic]:
            st.session_state[f"sub_{topic}_{item}"] = False
        st.session_state[all_key] = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

with b2:
    st.markdown('<div style="height:0"></div>', unsafe_allow_html=True)
    if st.button("✣  Generate", type="primary", use_container_width=True):
        selected = [
            item for item in subtopics_by_topic[topic]
            if st.session_state.get(f"sub_{topic}_{item}", False)
        ]
        if not selected:
            st.warning("Please select at least one subtopic before generating questions.")
        else:
            st.success(
                f"Ready to generate questions for {topic}: "
                + ", ".join(selected)
            )

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
