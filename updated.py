

import streamlit as st
import random
from datetime import datetime
import time

st.set_page_config(
    page_title="Happy Valentine's Day ❤️",
    page_icon="💕",
    layout="centered",
    initial_sidebar_state="expanded"
)




# ===================== VALENTINE ADD-ON START =====================

# Optional: Password Protection
password = st.text_input("Enter The Password -- (hint - the Month We First Saw Each other)💌", type="password")

if password == "" or password != "november":  # You can change love123
    st.stop()

# Dark Romantic Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Poppins:wght@300;400;500&display=swap');

.stApp {
    background: linear-gradient(135deg, #0f0f0f 0%, #1c1c1c 50%, #2a2a2a 100%);
}

/* Star overlay */
.stApp::before {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background-image: radial-gradient(white 1px, transparent 1px);
    background-size: 50px 50px;
    opacity: 0.05;
    pointer-events: none;
}

/* Headers */
h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #e0bfb8;
    text-align: center;
}

/* Text */
p {
    font-family: 'Poppins', sans-serif;
    color: #d6cfc7;
    line-height: 1.8;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #b76e79 0%, #e0bfb8 100%);
    color: black;
    border-radius: 25px;
    padding: 12px 30px;
    font-weight: 500;
    border: none;
    box-shadow: 0 0 15px rgba(224,191,184,0.4);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 25px rgba(224,191,184,0.7);
}

/* Floating Hearts */
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 20px;
    color: #e0bfb8;
    animation: floatUp 8s linear infinite;
    opacity: 0.7;
}

@keyframes floatUp {
    0% { transform: translateY(0) scale(1); opacity: 0.8; }
    100% { transform: translateY(-100vh) scale(1.5); opacity: 0; }
}

.heart:nth-child(1) { left: 10%; animation-duration: 7s; }
.heart:nth-child(2) { left: 25%; animation-duration: 9s; }
.heart:nth-child(3) { left: 40%; animation-duration: 6s; }
.heart:nth-child(4) { left: 60%; animation-duration: 10s; }
.heart:nth-child(5) { left: 80%; animation-duration: 8s; }

</style>

<div class="heart">❤</div>
<div class="heart">❤</div>
<div class="heart">❤</div>
<div class="heart">❤</div>
<div class="heart">❤</div>
""", unsafe_allow_html=True)

# Cinematic Welcome
st.markdown("""
<h1 style='font-size:55px;
text-shadow: 0 0 10px rgba(224,191,184,0.8),
             0 0 20px rgba(224,191,184,0.6),
             0 0 40px rgba(224,191,184,0.4);'>
Happy Valentine's Day ❤️
</h1>
<p style='text-align:center; font-size:18px;'>
A little universe I made just for you.
</p>
""", unsafe_allow_html=True)

# Secret Reveal Button
if st.button("Click for a Surprise 💖"):
    st.balloons()
    st.markdown("""
    <div style='background:#1f1f1f;
                padding:30px;
                border-radius:15px;
                text-align:center;
                box-shadow:0 0 20px rgba(224,191,184,0.2);'>
        <h2>You are my favorite person in this entire universe 🌌</h2>
        <p>No matter what happens, I choose you. Every single time.</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== VALENTINE ADD-ON END =====================




# ============================================================================
# DATA: ROMANTIC CONTENT
# ============================================================================

# 25 Reasons I Love You
LOVE_REASONS = [
    "The way your eyes light up when you talk about something you're passionate about makes my heart skip a beat.",
    "Your laugh is the most beautiful sound in the world, and I'd do anything just to hear it one more time.",
    "You make even the most ordinary moments feel like magical adventures when we're together.",
    "The way you remember the little things I mention shows me how much you truly listen and care.",
    "Your kindness to everyone around you makes me fall in love with you over and over again.",
    "You're my safe place, my comfort zone, and the person I can always be myself around.",
    "The way you support my dreams and encourage me to be better inspires me every single day.",
    "Your hugs feel like coming home after a long journey—warm, safe, and exactly where I belong.",
    "You make me believe in love stories and fairy tales because ours feels like pure magic.",
    "The thoughtful little things you do remind me that love isn't just words, it's actions.",
    "Your smile has the power to turn my worst days into the best ones instantly.",
    "You challenge me to grow while loving me exactly as I am—that's the rarest gift.",
    "The way you hold my hand makes me feel like I could conquer anything with you by my side.",
    "Your patience with me, even when I'm being difficult, shows me the depth of your love.",
    "You're not just my boyfriend, you're my best friend, my confidant, and my favorite person.",
    "The way you look at me makes me feel like the most special person in the entire universe.",
    "Your ambition and drive inspire me to chase my own dreams fearlessly.",
    "You've taught me that love isn't perfect, but it's real, honest, and worth fighting for.",
    "The inside jokes we share and the memories we've created are treasures I'll cherish forever.",
    "You make me want to be a better person just by being the incredible person you are.",
    "Your voice is my favorite sound, whether you're laughing, talking, or just saying good morning.",
    "The way you care for me when I'm sick or sad shows me what true partnership looks like.",
    "You've shown me that vulnerability is strength and that it's okay to lean on someone.",
    "Every moment with you feels like a gift I never knew I needed but can't imagine living without.",
    "You are my today and all of my tomorrows—my forever person, my soulmate, my everything."
]

# Open When Letters Content
OPEN_WHEN_LETTERS = {
    "sad": """
    My dearest love,
    
    If you're reading this, I know your heart feels heavy right now. I wish I could wrap you in my arms and take away whatever pain you're feeling. But since I can't be there this exact moment, let these words be a gentle reminder:
    
    You are stronger than you know. This sadness is temporary, but your resilience is permanent. You've overcome so much already, and you'll overcome this too. I believe in you with every fiber of my being.
    
    Remember that it's okay to not be okay. Your feelings are valid, and you don't have to put on a brave face for anyone—including me. Let yourself feel, let yourself cry, let yourself be human.
    
    I'm here for you, always. Whether you need to talk, need silence, need distraction, or need a shoulder to cry on—I'm yours. You never have to face darkness alone because I'll be your light.
    
    This too shall pass, my love. And I'll be right here, holding your hand through it all.
    
    Forever yours,
    Lunaa❤️
    """,
    
    "miss": """
    To the one who holds my heart,
    
    Missing you is the strangest feeling—like a piece of me is somewhere else, walking around without me. Distance may separate our bodies, but nothing can separate our souls.
    
    Close your eyes and feel my love wrapping around you like a warm blanket. Every beat of my heart whispers your name. Every star in the sky is a reminder that we're looking at the same sky, thinking of each other.
    
    I miss your laugh that fills entire rooms with joy. I miss the way you scrunch your nose when you're concentrating. I miss our random 3 AM conversations about everything and nothing. I miss the simple act of existing in your presence.
    
    But here's what I know: the time we spend apart only makes our time together more precious. Every second of missing you is worth it for the moment I get to hold you again.
    
    Until then, carry my love with you. It's in every sunrise, every song, every gentle breeze. I'm never truly far when I'm always in your heart.
    
    Counting down the moments until I see you again,
    All my love ❤️
    """,
    
    "overthinking": """
    Hey you, my beautiful overthinker,
    
    I know that brilliant mind of yours is running in circles right now, analyzing every detail, playing out every scenario, worrying about things that might never happen. Take a deep breath with me. In... and out.
    
    Here's the truth: You are enough. Exactly as you are, right this moment. You don't need to have everything figured out. You don't need to be perfect. You just need to be you, and that's more than enough for me.
    
    That thing you're overthinking? It's probably not as big as it feels right now. Your anxiety is lying to you. It's magnifying your fears and minimizing your strength. But I see the real you—capable, resilient, and absolutely amazing.
    
    Remember: We're a team. Whatever you're facing, you're not facing it alone. We'll figure it out together, one step at a time. There's no rush, no pressure, no judgment.
    
    Let go of what you can't control. Trust in yourself the way I trust in you. And know that no matter what happens, my love for you isn't going anywhere.
    
    You've got this. We've got this.
    
    Believing in you always,
    Your biggest fan ❤️
    """,
    
    "achievement": """
    TO MY ABSOLUTE SUPERSTAR!
    
    I KNEW YOU COULD DO IT! From the moment you set this goal, I knew you had everything it takes to achieve it. And now look at you—absolutely crushing it!
    
    I am so incredibly proud of you. Not just for this achievement, but for every small step you took to get here. For every early morning, every late night, every moment of doubt you pushed through. You earned this.
    
    This is just the beginning, my love. You're capable of achieving anything you set your mind to. The world better watch out because you're unstoppable when you're determined.
    
    Take a moment to celebrate yourself. Seriously. Do a little dance, treat yourself to something special, and let yourself feel the pride you deserve. You worked hard for this, and you should enjoy every second of this victory.
    
    I hope you know how inspiring you are. Watching you chase your dreams motivates me to chase mine. You make me want to be better, do better, and reach higher.
    
    This achievement? It's just one of many in your incredible future. And I can't wait to celebrate every single one of them with you.
    
    Congratulations, my champion. I love you so much.
    
    Your proudest supporter,
    Forever and always ❤️
    """
}

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

st.sidebar.markdown("<h2 style='text-align: center; color: #d4145a;'>💕 Our Journey 💕</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate to:",
    [
        "🏠 Welcome",
        "📖 Our Love Story",
        "💘 Love Quiz",
        "💝 Reasons I Love You",
        "🔒 Secret Letter",
        "💌 Open When Letters",
        "🌟 Future With Us",
        "🎁 Final Surprise"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; font-size: 12px; color: #8b3a62;'>Made with love, just for you ❤️</p>", unsafe_allow_html=True)

# ============================================================================
# PAGE 1: WELCOME
# ============================================================================

if page == "🏠 Welcome":
    st.markdown("<h1>💕 Welcome to Our Love Story 💕</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='welcome-box'>
            <h2 style='color: #d4145a; margin-bottom: 20px;'>Hello, My Love ❤️</h2>
            <p style='font-size: 18px; text-align: center;'>
                Happy Valentine's Day to the most incredible person I know! 
                I created this special place just for you, filled with all the love, 
                memories, and dreams we share together.
            </p>
            <p style='font-size: 16px; text-align: center; margin-top: 20px;'>
                Every page here is a piece of my heart, a reminder of why you mean 
                everything to me. Take your time exploring, smile at our memories, 
                and know that every word here is true.
            </p>
            <p style='font-size: 18px; text-align: center; margin-top: 25px; color: #d4145a; font-weight: 500;'>
                You are my forever. You are my always. You are my everything. 💕
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Start Our Journey ✨", use_container_width=True):
            st.balloons()
            st.success("Let the magic begin! 💖 Navigate through the pages using the sidebar →")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
  

# ============================================================================
# PAGE 2: OUR LOVE STORY
# ============================================================================

elif page == "📖 Our Love Story":
    st.markdown("<h1>📖 Our Beautiful Journey Together 📖</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 17px; color: #8b3a62;'>
            Every love story is beautiful, but ours is my favorite. Here are some of the 
            moments that made us... <i>us</i>. 💕
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Memory 1
    with st.expander("✨ The First Time We Met", expanded=False):
        st.markdown("""
            💞 Here’s Our Story

If this were a movie, it would start with something simple.

I came to my bestf's house that day — just another ordinary visit, or at least that’s what I thought. The door opened… and there you were.

For a few seconds, the world felt strangely quiet. Our eyes met. No background music. No dramatic dialogue. We didn’t say a single word to each other. Not even a proper hello. It was just a moment — soft, silent, almost forgettable.

At that time, there were no butterflies. No sudden realization. No love story beginning. Just two people standing in a doorway, completely unaware of what the future was quietly writing for them.

Later, I found out you had secretly made a small video of me sitting with my friends — without anyone knowing. And you got really scared. I didn’t know what to think. I didn’t understand you yet.

Back then, I only thought one thing — “He seems like a nice, confident guy.” That’s it. Nothing more.

But if this were truly a movie, that door opening scene would replay later. The camera would zoom in on that silent eye contact. And suddenly, it wouldn’t feel ordinary anymore. It would feel like the exact moment everything quietly began.

Because sometimes, love doesn’t start with fireworks.

Sometimes, it starts with a door…
a glance…
and a story waiting patiently to unfold.
            **That was the day my life got infinitely better.** 💫
        """)
        st.image("https://images.unsplash.com/photo-1518568814500-bf0f8d125f46?w=800", 
                 caption="The beginning of forever ❤️", use_container_width=True,
                 format="jpg")
        
    # Memory 1
    with st.expander("✨ Our First Hug", expanded=False):
        st.markdown("""
          🤍 Our First Hug

We met after eight whole months.

Eight months of calls.
Eight months of missing.
Eight months of “I wish you were here.”

And then finally… you were.

The house was full that day.
Everyone was there — in the hall, in the bedrooms, moving around, talking. It wasn’t some dramatic, empty movie scene.

It was normal. Loud. Real.

And somehow, that made it even more special.

I was standing in the kitchen, trying to act normal, trying to process the fact that you were actually in the same house as me — not on a screen, not on a call.

And then you came.

No big announcement. No warning.

You just walked up to me…
and hugged me.

That was it.

But that moment?

It felt like time paused.

After eight months of only talking… after months of imagining what it would feel like… we were finally close enough to hold each other.

I was in shock.

It didn’t feel real at first. It felt different. Warm. Safe. Familiar, yet completely new at the same time.

The first hug.

In a kitchen.
With everyone in the house.
In the most ordinary setting.

And yet… it was the most beautiful moment.

I still remember that feeling.

The way everything else faded.
The way my heart calmed down instantly.
The way it felt like, “Okay… I’m home.”

That hug wasn’t long.
It wasn’t dramatic.

But it was ours.

And it will always be one of the most special memories of my life. 🤍✨  
        """)
        st.image("https://images.unsplash.com/photo-1518568814500-bf0f8d125f46?w=800", 
                 caption="An Unforgatable Moment ❤️", use_container_width=True, format="jpg")    
    
    # Memory 2
    with st.expander("🌙 Our First Deep Conversation", expanded=False):
        st.markdown("""
            Do you remember staying up until 3 AM, talking about everything and nothing at all? 
            We discussed our dreams, our fears, our childhoods, our favorite memories. Hours passed 
            like minutes, and I didn't want it to end.
            
            That night, I realized you weren't just someone I wanted to know—you were someone I 
            *needed* to know. You understood me in ways no one else ever had. You listened, really 
            listened, and made me feel seen and heard.
            
            I fell in love with your mind that night, with the way you think, the way you see the world, 
            the depth of your soul. **You became my favorite conversation.** 🌟
        """)
        st.image("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=800", 
                 caption="Talking for hours, falling deeper 💕", use_container_width=True, format="jpg")
    
    # Memory 3
    with st.expander("💕 When I Knew You Were The One", expanded=False):
        st.markdown("""
            There wasn't one grand moment—it was a thousand little ones. The way you sent me all the money recieverd in cashback.
             The way you remembered the small things I mentioned in passing. 
            The way you made me laugh when I needed it most.
            
            It was in your patience during my worst moods. In your encouragement when I doubted myself. 
            In the way you loved me not despite my flaws, but with them, as if they made me more lovable.
            
            One ordinary Tuesday, I looked at you doing something completely mundane, and it hit me like 
            lightning: I want to do this forever. I want every ordinary Tuesday and every extraordinary 
            adventure with you. **You weren't just someone I loved—you were my person.** 💖
        """)
        st.image("https://images.unsplash.com/photo-1522673607710-24bc2c299d9d?w=800", 
                 caption="My person, my forever 💫", use_container_width=True, format="jpg")
    
    # Memory 4
    with st.expander("🎉 Our Favorite Adventure Together", expanded=False):
        st.markdown("""
         🌍 Our Greatest Adventure – Us

People think adventures mean mountains, road trips, or foreign countries.

But our biggest adventure?

It’s us.
It’s loving each other across distance.

Our LDR is the bravest, craziest, most emotional adventure I’ve ever been part of.

We’ve met so little. So, so little.
But jitka pn bhetloy… every single meeting feels like a whole movie compressed into a few minutes.

I still remember that day at the station.

I planned for hours. I cried just to take permission. My heart was racing the entire time. I had an exam after two days… I should’ve been studying, I should’ve been responsible.

But my love…

The eagerness to see you — even for five minutes — was stronger than everything else.

Not even five proper minutes.
Just a glimpse.
Just a presence.
Just knowing you were standing in front of me and not on a screen.

And you know what?

It was worth it.

Every second of stress.
Every tear.
Every heartbeat.

Worth it.

Because loving you has never felt like a burden.
It has always felt like courage.

Our adventure isn’t about places.
It’s about effort.
It’s about choosing each other even when it’s hard.
Even when distance tests us.

And honestly?

Every moment with you — even the short ones — is worth everything.

Because at the end of the day,
you are my favorite destination. 🤍✨
        """)
        st.image("https://images.unsplash.com/photo-1511895426328-dc8714191300?w=800", 
                 caption="Adventures are better with you 🗺️", use_container_width=True, format="jpg")

# ============================================================================
# PAGE 3: LOVE QUIZ
# ============================================================================

elif page == "💘 Love Quiz":
    st.markdown("<h1>💘 How Well Do You Know Us? 💘</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 17px; color: #8b3a62;'>
            Let's see how well you remember our special moments together! 💕
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Initialize score
    score = 0
    
    # Question 1
    st.markdown("### Question 1: What's my favorite thing about you?")
    q1 = st.radio(
        "",
        ["Your sense of humor", "Your kindness", "Everything about you"],
        key="q1",
        label_visibility="collapsed"
    )
    if q1 == "Everything about you":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Question 2
    st.markdown("### Question 2: What would be my ideal date with you?")
    q2 = st.radio(
        "",
        ["Fancy restaurant", "Cozy night in with movies and cuddles", "Adventure outdoors"],
        key="q2",
        label_visibility="collapsed"
    )
    if q2 == "Cozy night in with movies and cuddles":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Question 3
    st.markdown("### Question 3: What do I treasure most about our relationship?")
    q3 = st.radio(
        "",
        ["The fun times we have", "The deep connection we share", "The adventures we go on"],
        key="q3",
        label_visibility="collapsed"
    )
    if q3 == "The deep connection we share":
        score += 1
    
    st.markdown("<br><br>", unsafe_allow_html=True)


    # Question 4
    st.markdown("### Question 4: What is my favorite thing about you?")
    q2 = st.radio(
        "",
        ["Your smile","Your confidence","The way you care", "Everything"],
        key="q4",
        label_visibility="collapsed"
    )
    if q2 == "Everything":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)


    # Question 5
    st.markdown("### Question 5: What makes our love special?")
    q2 = st.radio(
        "",
        ["The distance","The effort","The deep connection","communication"],
        key="q5",
        label_visibility="collapsed"
    )
    if q2 == "The distance":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)


    # Question 6
    st.markdown("### Question 6: What do I value most in our relationship?")
    q2 = st.radio(
        "",
        ["Loyalty", "Effort", "Emotional connection","Us choosing each other every day"],
        key="q6",
        label_visibility="collapsed"
    )
    if q2 == "Us choosing each other every day":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)


    # Question 7
    st.markdown("### Question 7: How long did we wait for our first hug?")
    q2 = st.radio(
        "",
        ["6 months", "8 months", "7 months","9 months"],
        key="q7",
        label_visibility="collapsed"
    )
    if q2 == "8 months":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)


    # Question 8
    st.markdown("### Question 8: Where did our story technically begin?")
    q2 = st.radio(
        "",
        ["At the station", "in the kitchen", "At her house when the door opened","On a random late-night call/text"],
        key="q8",
        label_visibility="collapsed"
    )
    if q2 == "On a random late-night call/text":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)


    # Question 9
    st.markdown("### Question 9:What was my first impression of you?")
    q2 = st.radio(
        "",
        ["Mysterious", "Arrogant", "Nice and confident","Too quiet"],
        key="q9",
        label_visibility="collapsed"
    )
    if q2 == "Nice and confident":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)


    # Question 10
    st.markdown("### Question 10:Who gets more emotional during goodbyes?")
    q2 = st.radio(
        "",
        ["me", "you", "both equally","We pretend we’re strong"],
        key="q10",
        label_visibility="collapsed"
    )
    if q2 == "you":
        score += 1
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Submit button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💖 Submit My Answers 💖", use_container_width=True):
            if score >= 7:
                st.balloons()
                st.success(f"""
                    ### 🎉 Perfect Score: {score}/10! 🎉
                    
                    You know me so well! This is exactly why I love you—you pay attention to the little 
                    things, you understand my heart, and you *get* me in a way no one else does.
                    
                    Every answer you chose shows just how deeply you know my soul. We're connected in 
                    the most beautiful way, and I'm so grateful for that. You're my soulmate, and 
                    moments like this prove it. 💕
                """)
            else:
                st.warning(f"""
                    ### 😊 You got {score}/10... but that's okay!
                    
                    Hey, what matters isn't a quiz score—it's the fact that you're here, taking the time 
                    to celebrate our love. We're still learning about each other every single day, and 
                    that's what makes this journey so beautiful.
                    
                    Besides, I love you for who you are, not for how many quiz questions you get right! 
                    (But we might need more late-night deep talks so you can learn all my secrets 😉)
                    
                    Love you anyway, silly! ❤️
                """)

# ============================================================================
# PAGE 4: REASONS I LOVE YOU
# ============================================================================

elif page == "💝 Reasons I Love You":
    st.markdown("<h1>💝 Why I Love You 💝</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 17px; color: #8b3a62;'>
            There are countless reasons why I love you, but here are 25 that I've put into words. 
            Click the button below to discover a random reason! 💕
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💖 Show Me A Reason 💖", use_container_width=True):
            reason = random.choice(LOVE_REASONS)
            st.session_state.current_reason = reason
    
    # Display the reason if it exists
    if 'current_reason' in st.session_state:
        st.markdown(f"""
            <div class='love-reason'>
                <h3 style='color: #d4145a; margin-bottom: 15px;'>💕</h3>
                {st.session_state.current_reason}
                <h3 style='color: #d4145a; margin-top: 15px;'>💕</h3>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 Click the button as many times as you want to see different reasons!")

# ============================================================================
# PAGE 5: SECRET LETTER
# ============================================================================

elif page == "🔒 Secret Letter":
    st.markdown("<h1>🔒 Secret Love Letter 🔒</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 17px; color: #8b3a62;'>
            This letter is just for you. Enter our special date to unlock it... 💕
            <br><i>(Hint: Format: DDMMYYYY - our anniversary date)</i>
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Password input
    password = st.text_input("🔑 Enter the password:", type="password", max_chars=8)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Check password (Example: 02142023 for Feb 14, 2023 - customize this!)
    CORRECT_PASSWORD = "01032022"  # Change this to your actual anniversary date
    
    if password:
        if password == CORRECT_PASSWORD:
            st.balloons()
            st.success("✅ Access Granted! Welcome to your secret letter, my love.")
            
            st.markdown("""
                <div class='secret-letter'>
                    <h2 style='text-align: center; color: #d4145a; margin-bottom: 25px;'>
                        To The Love of My Life 💕
                    </h2>
                    
                    My Dearest Love,
                    
                    
                        If you're reading this, you've unlocked the most sacred part of this entire website—
                        the words I've kept closest to my heart, waiting for the perfect moment to share with you.
                        This isn't just a letter; it's a promise, a confession, and a celebration of everything 
                        we are together.
                   
                    
                   
                        From the moment you entered my life, everything changed. Colors became brighter, 
                        music sounded sweeter, and ordinary moments transformed into treasured memories. 
                        You didn't just walk into my life—you walked into my soul and made yourself at home there.
                        And I hope you never leave.
                   
                    
                    
                        I want you to know that loving you is the easiest and most natural thing I've ever done. 
                        It doesn't feel like a choice; it feels like breathing, like existing, like the most 
                        fundamental truth of who I am. I love you when you're happy and radiant. I love you when 
                        you're struggling and vulnerable. I love you in your strengths and in your weaknesses. 
                        I love every version of you that exists and every version yet to come.
                    
                    
                   
                        You've taught me what it means to be truly seen and truly loved. You've shown me that 
                        love isn't just about the grand gestures—it's in the quiet moments, the gentle touches, 
                        the inside jokes, the comfortable silences. It's in the way you know exactly what I need 
                        before I even ask. It's in the way you make me feel safe enough to be completely, 
                        authentically myself.
                   
                    
                    
                        I promise to love you fiercely and gently, passionately and patiently, today and always. 
                        I promise to be your safe place, your biggest cheerleader, your partner in crime, and 
                        your shoulder to lean on. I promise to choose you, every single day, in every single way.
                    
                    
                  
                        Thank you for being you. Thank you for choosing me. Thank you for this beautiful love 
                        we're building together. You are my greatest adventure, my sweetest comfort, my deepest 
                        love, and my brightest future.
                    
                    
                    
                        Happy Valentine's Day, my forever person. Here's to us, to our love, and to all the 
                        beautiful tomorrows we'll share together. 💕
                    
                    
                    
                    Forever and always yours,
                       Your Soulmate ❤️
                    
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Access Denied, Mister 😌")
            st.info("💭 Think about our special day... the day that changed everything! Try again.")

# ============================================================================
# PAGE 6: OPEN WHEN LETTERS
# ============================================================================

elif page == "💌 Open When Letters":
    st.markdown("<h1>💌 Open When... 💌</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 17px; color: #8b3a62;'>
            For every emotion, every moment, every time you need me—I'm here. 
            Open these letters whenever you need a reminder of my love. 💕
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Open When You're Sad
    with st.expander("💙 Open When You're Sad"):
        st.markdown(OPEN_WHEN_LETTERS["sad"])
    
    # Open When You Miss Me
    with st.expander("💜 Open When You Miss Me"):
        st.markdown(OPEN_WHEN_LETTERS["miss"])
    
    # Open When You're Overthinking
    with st.expander("💚 Open When You're Overthinking"):
        st.markdown(OPEN_WHEN_LETTERS["overthinking"])
    
    # Open When You Achieve Something
    with st.expander("💛 Open When You Achieve Something"):
        st.markdown(OPEN_WHEN_LETTERS["achievement"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💕 Remember: I'm always here for you, in every moment, through every emotion.")

# ============================================================================
# PAGE 7: FUTURE WITH US
# ============================================================================

elif page == "🌟 Future With Us":
    st.markdown("<h1>🌟 Our Future Together 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 17px; color: #8b3a62;'>
            I dream of a beautiful future with you. Check off the dreams you want to share with me! 💕
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dream checkboxes
    dream1 = st.checkbox("✈️ Travel the world together, exploring new places hand in hand")
    if dream1:
        st.success("""
            Imagine us in Paris, watching the sunset from the Eiffel Tower. In Tokyo, getting lost 
            in the streets and finding the best ramen. In Santorini, watching the sunrise together. 
            Every destination becomes magical when I'm with you. Let's make the world our playground! 🌍
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    dream2 = st.checkbox("👕 Wearing matching outfits (because we're adorable like that)")
    if dream2:
        st.success("""
            I can already see us being *that* couple—coordinating our outfits, being ridiculously 
            cute together, and not caring what anyone thinks because we're too busy being happy. 
            Matching hoodies? Matching shoes? Count me in! Let's be adorable together! 👫
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    dream3 = st.checkbox("🌙 Having deep late-night talks forever")
    if dream3:
        st.success("""
            I never want to stop having those 3 AM conversations with you. The ones where we talk about 
            everything—our dreams, our fears, the meaning of life, or absolutely nothing at all. 
            Your voice is my favorite sound, and your thoughts are my favorite stories. Let's never 
            stop talking, never stop sharing, never stop connecting on the deepest level. 💫
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    dream4 = st.checkbox("🏡 Building a cozy home filled with love and laughter")
    if dream4:
        st.success("""
            Our home won't be perfect, but it'll be ours. It'll have our photos on the walls, 
            our favorite books on the shelves, and our laughter echoing through the rooms. 
            It'll smell like your favorite coffee and my cooking experiments. It'll be our sanctuary, 
            our safe place, our piece of heaven on earth. I can't wait to build that with you! 🏠
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    dream5 = st.checkbox("👴👵 Growing old together, still madly in love")
    if dream5:
        st.success("""
            I want to grow old with you. I want to see your hair turn gray, watch wrinkles form 
            from years of smiling and laughing together. I want to hold your hand when we're 80 
            the same way I hold it now. I want our love story to be the kind that lasts forever, 
            the kind that inspires others, the kind that proves soulmates are real. 
            Because you're mine, and I'm yours, for all of time. 💕
        """)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style='text-align: center; font-size: 18px; color: #d4145a; font-weight: 500;'>
            Every dream is sweeter when I'm dreaming it with you. 💖
        </p>
    """, unsafe_allow_html=True)

# ============================================================================
# PAGE 8: FINAL SURPRISE
# ============================================================================

elif page == "🎁 Final Surprise":
    st.markdown("<h1>🎁 One Last Thing... 🎁</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Trigger balloons immediately
    st.balloons()
    
    st.markdown("""
        <div style='text-align: center; padding: 40px 20px;'>
            <h2 style='color: #d4145a; font-size: 32px; margin-bottom: 30px;'>
                You Are My Everything 💕
            </h2>
            
            
                Thank you for being my person.
                Thank you for loving me.
                Thank you for existing.
                Thank you for being you.
            
                Happy Valentine's Day, My Love ❤️
            
                I love you more than words can express,
                more than this website can show,
                and more than you'll ever know.
            
                Forever yours, 💕
                Always and Completely ❤️
          
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    

    
    # One more balloon burst!
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💖 Celebrate Our Love 💖", use_container_width=True):
            st.balloons()
            st.success("Here's to us, to our love, and to forever! 🥂❤️")

   

st.markdown("### A Letter For You 💌")

letter = """
From the moment you entered my life,
everything became brighter.
You are my comfort,
my happiness,
and my favorite notification.
"""

placeholder = st.empty()
typed = ""

for char in letter:
    typed += char
    placeholder.markdown(f"<p style='font-size:18px;'>{typed}</p>", unsafe_allow_html=True)
    time.sleep(0.03)

        

