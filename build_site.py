"""Builds the static pages of itsahmadonai.github.io/jarvis-app (shared nav + footer)."""
import json
import os

OUT = os.path.dirname(os.path.abspath(__file__))
FORM = "https://docs.google.com/forms/d/e/1FAIpQLScqDjqnsNxoVrz9v8gEmZezJogX1aKm2vPyD3jjPqovd2WQjw/viewform"
CHOICE = 1533219292
SITE = "https://itsahmadonai.github.io/jarvis-app/"
AUTHOR = {"@type": "Person", "name": "Ahmad", "url": "https://github.com/itsAhmadOnAI"}
PAGES = []   # (file, priority) for the sitemap


def form(choice):
    return f"{FORM}?usp=pp_url&amp;entry.{CHOICE}={choice.replace(' ', '+')}"


ICONS = {
    "person": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    "wave": '<path d="M3 12h2M7 8v8M11 5v14M15 8v8M19 11v2"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "screen": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
}


def icon(name):
    return (f'<div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg></div>')


def page(file, title, desc, body, current="", og="og-home", ld=(), priority="0.8", hero=""):
    url = SITE + ("" if file == "index.html" else file)
    PAGES.append((file, priority))

    def link(href, text, cls=""):
        cur = ' aria-current="page"' if href == current else ""
        c = f' class="{cls}"' if cls else ""
        return f'<a href="{href}"{c}{cur}>{text}</a>'
    data = "".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in ld)
    pre = f'<link rel="preload" as="image" href="{hero}" fetchpriority="high">' if hero else ""
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="Ahmad">
<meta name="theme-color" content="#0D1117">
<meta name="color-scheme" content="dark">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Jarvis">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}img/{og}.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}img/{og}.jpg">
{pre}<link rel="stylesheet" href="style.css">{data}</head><body>
<a class="skip" href="#main">Skip to content</a>
<nav aria-label="Main"><div class="wrap"><a class="logo" href="./" aria-label="Jarvis home"><span class="dot"></span>Jarvis</a>
<div class="links">{link("early-access.html", "Early access")}{link("build.html", "The build")}{link("work-with-me.html", "Shopify", "hide-sm")}</div></div></nav>
<main id="main">
{body}
</main>
<footer><div class="wrap"><span>A Jarvis-like personal assistant, in development. Not affiliated with Marvel.</span>
<span><a href="./">Home</a> · <a href="early-access.html">Early access</a> · <a href="build.html">The build</a> · <a href="work-with-me.html">Work with me</a> · <a href="privacy.html">Privacy</a></span></div></footer>
</body></html>
"""
    open(os.path.join(OUT, file), "w").write(html)


SIZES = {"home": (1600, 1000), "phone": (780, 1688)}


def row(tag, title, text, ticks, img, alt, flip=False):
    lis = "".join(f"<li>{t}</li>" for t in ticks)
    return f"""<div class="row{' flip' if flip else ''}"><div class="text"><span class="tag">{tag}</span><h3>{title}</h3>
<p>{text}</p><ul class="ticks">{lis}</ul></div>
<div class="pic"><img src="img/{img}.webp" alt="{alt}" width="{SIZES.get(img, (762, 1280))[0]}" height="{SIZES.get(img, (762, 1280))[1]}" loading="lazy" decoding="async"></div></div>"""


# ---------------------------------------------------------------- home
home = f"""
<header class="hero"><div class="wrap">
<span class="eyebrow">A Jarvis-like assistant · in development</span>
<h1>Your very own <em>personal assistant.</em></h1>
<p class="lead">Talk to it like a person. It knows your day, remembers what matters to you and gets real work done
on your own computer, asking first before anything risky.</p>
<div class="ctas"><a class="btn primary" href="early-access.html">Get early access</a><a class="btn" href="build.html">Watch it being built</a></div>
<img class="shot" src="img/home.webp" width="1600" height="1000" fetchpriority="high" alt="The assistant's home screen: a glowing orb in the middle, the workspace on the left with a running job, and a conversation on the right">
</div></header>

<section><div class="wrap center">
<h2>Not a chatbot. <em>An assistant.</em></h2>
<p class="sub">Six things that make it feel less like software and more like someone working with you.</p>
<div class="grid" style="text-align:left">
<div class="card">{icon("person")}<h3>Yours, and only yours</h3><p>It learns your habits, your clients and your day. It has a personality, a calm British voice and a dry sense of humour, sir.</p></div>
<div class="card">{icon("wave")}<h3>Feels like a real conversation</h3><p>No button to hold. Just talk. Interrupt it mid-sentence, and it knows when you've finished speaking.</p></div>
<div class="card">{icon("lock")}<h3>Runs on your laptop</h3><p>It hears you on your own machine. Simple commands never leave it. Your memories, chats and files stay yours.</p></div>
<div class="card">{icon("bolt")}<h3>Does real work</h3><p>Background jobs while you keep talking: store sections built and checked, videos made, mail drafted, reminders kept.</p></div>
<div class="card">{icon("screen")}<h3>Controls your desktop</h3><p>Apps, windows, music, volume, screenshots. It types for you and can look at your screen when you ask.</p></div>
<div class="card">{icon("shield")}<h3>Powerful, never reckless</h3><p>Anything risky waits for your OK. It writes email drafts but never sends them. You stay in charge.</p></div>
</div></div></section>

<section class="alt"><div class="wrap">
<h2>A look inside</h2>
<p class="sub">Real screens from the app, filled with demo data.</p>
{row("Your workspace", "Everything it's doing, at a glance",
     "Ask for something big and it becomes a job that runs in the background. You see every step as it happens, and you can keep chatting.",
     ["Live progress, step by step", "Pause, resume or talk about any job", "Screenshots of the result before you approve"], "overview",
     "The workspace showing a running design job with its steps and a preview screenshot")}
{row("Your day", "Calendar and reminders in one timeline",
     "Your meetings and your reminders, side by side. It nags you gently until it's done, and tells you about your day the first time you say hello.",
     ["A morning brief, by voice", "Reminders that repeat", "Add or move events by just asking"], "tasks",
     "The tasks tab with calendar events and reminders grouped by day", flip=True)}
{row("Your inbox", "It reads your mail, so you don't have to",
     "It picks out the emails that need a reply, reads them out, and drafts the answer. Sending is always your click.",
     ["Needs-reply first, newsletters out of the way", "Drafts in your own Gmail", "Never sends on its own"], "mail",
     "The inbox tab listing three emails that need a reply, each with Draft a reply and Read it out buttons")}
{row("Your memory", "It remembers what you tell it",
     "Your preferences and the people and projects in your life. You can see, edit or delete every memory, and it stays on your laptop.",
     ["Remembers on its own, tells you when it does", "Search, edit, forget", "Learns the words it mishears"], "memory",
     "The memory tab listing facts the assistant remembers", flip=True)}
</div></section>

<section><div class="wrap center">
<h2>How it works</h2>
<p class="sub">Simple on the outside. A lot of care on the inside.</p>
<div class="steps" style="text-align:left">
<div class="card"><h3>You talk</h3><p>It listens on your laptop, cancels its own voice and hears you even in a noisy room.</p></div>
<div class="card"><h3>It thinks</h3><p>Quick questions get a quick answer. Hard ones go to a stronger brain. Simple commands need no AI at all.</p></div>
<div class="card"><h3>It acts</h3><p>It does the work itself or hands it to the best tool for the job, then shows you what it did.</p></div>
<div class="card"><h3>You decide</h3><p>Anything that matters waits for your OK. Nothing is published, sent or deleted behind your back.</p></div>
</div></div></section>

<section class="alt"><div class="wrap center">
<h2>Where do you fit in?</h2>
<p class="sub">Three ways to follow along.</p>
<div class="grid" style="text-align:left">
<a class="card" href="early-access.html"><h3>I want one</h3><p>Join the waitlist and be first to try it.</p><span class="go">Early access →</span></a>
<a class="card" href="build.html"><h3>I want to watch</h3><p>Follow the build in public, episode by episode.</p><span class="go">The build →</span></a>
<a class="card" href="work-with-me.html"><h3>I run a Shopify store</h3><p>Get sections built fast and checked on every screen.</p><span class="go">Work with me →</span></a>
</div></div></section>
"""
page("index.html", "Jarvis: an AI voice assistant that runs on your laptop",
     "A Jarvis-like personal AI assistant you talk to like a person. It remembers you, runs on your own laptop and does real work: calendar, email, desktop and more.",
     home, og="og-home", priority="1.0", hero="img/home.webp", ld=[
         {"@context": "https://schema.org", "@type": "WebSite", "name": "Jarvis", "url": SITE,
          "description": "A Jarvis-like personal AI voice assistant, built in public.", "author": AUTHOR},
         {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Jarvis",
          "applicationCategory": "UtilitiesApplication", "operatingSystem": "Linux", "url": SITE,
          "image": SITE + "img/og-home.jpg", "screenshot": SITE + "img/home.webp", "author": AUTHOR,
          "description": "A personal AI voice assistant: hands-free conversation, memory, calendar, email drafts, desktop control and background jobs, running on your own laptop.",
          "featureList": ["Hands-free voice conversation with interruptions", "Memory you can see and edit",
                          "Calendar, reminders and a morning brief", "Reads email and writes drafts, never sends",
                          "Desktop control: apps, windows, media, screenshots, typing", "Background jobs while you talk",
                          "Asks before anything risky"]}])

# ---------------------------------------------------------------- early access
FAQ = [("When can I try it?", "There's no date yet. Waitlist members hear first, before anyone else."),
       ("Which computers will it run on?", "It runs on Linux laptops today. Other systems come later. Tell me yours on the form."),
       ("What will it cost?", "Not decided yet. Waitlist members get the first offer."),
       ("Is my data safe?", "Your memories, chats and files stay on your own computer.")]
early = f"""
<header class="hero"><div class="wrap">
<span class="eyebrow">Early access</span>
<h1>Be one of the <em>first</em> to have one.</h1>
<p class="lead">The assistant already runs every day on its first laptop. The next step is yours. Join the waitlist
and you'll hear first when it's ready to try.</p>
<div class="ctas"><a class="btn primary" href="{form('Early access')}">Join the waitlist</a></div>
</div></header>

<section><div class="wrap">
<h2 class="center">Built around you</h2>
{row("What you get", "An assistant that's actually yours",
     "Not a chat window in a browser tab. A presence on your computer that you talk to, that knows your day and does the work.",
     ["Hands-free conversation, with interruptions", "Your calendar, mail and reminders in one place",
      "Background jobs while you keep talking", "Your data on your machine"], "home", "The assistant's main screen")}
{row("On the go", "Looks good on any screen",
     "The same calm interface on a big screen or a small one.",
     ["One clear status: listening, thinking, speaking", "Every action visible and reversible"], "phone",
     "The assistant on a phone-sized screen", flip=True)}
</div></section>

<section class="alt"><div class="wrap prose">
<h2 style="margin-top:0">Questions</h2>
{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)}
<p>More on the <a href="privacy.html">privacy page</a>.</p>
</div></section>

<section><div class="wrap"><div class="cta-band">
<h2>Want in?</h2><p class="sub" style="margin-inline:auto">It takes 20 seconds. No spam, just the news that matters.</p>
<a class="btn primary" href="{form('Early access')}">Join the waitlist</a></div></div></section>
"""
page("early-access.html", "Early access: a Jarvis-like AI personal assistant",
     "Join the waitlist for a hands-free AI voice assistant that knows your day, remembers what matters and works on your own computer.",
     early, "early-access.html", og="og-early-access", ld=[{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
         {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}])

# ---------------------------------------------------------------- the build
build = f"""
<header class="hero"><div class="wrap">
<span class="eyebrow">Building in public</span>
<h1>I'm building my own <em>Jarvis.</em> Follow along.</h1>
<p class="lead">One person, one laptop and a lot of AI. Every feature, every bug and every "it finally works" moment,
shared as it happens.</p>
<div class="ctas"><span class="btn" aria-disabled="true">YouTube channel: coming soon</span><a class="btn primary" href="{form('Updates on the build')}">Get updates</a></div>
</div></header>

<section><div class="wrap" style="display:grid;gap:48px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))">
<div><h2>So far</h2><p class="sub">What already works, every day.</p>
<ol class="timeline">
<li><b>It listens and talks</b><span>Hands-free conversation, its own voice cancelled out, interruptions welcome.</span></li>
<li><b>It works on your desktop</b><span>Apps, windows, media, screenshots and typing, by voice.</span></li>
<li><b>It knows your day</b><span>Calendar, inbox, reminders and a morning brief.</span></li>
<li><b>It remembers you</b><span>A memory you can see and edit.</span></li>
<li><b>It does client work</b><span>Shopify sections built, tested on every screen and handed over for review.</span></li>
<li><b>It makes videos</b><span>From idea to script, voice, visuals and final cut.</span></li>
<li><b>It got a personality</b><span>A British voice, "sir", and a dry wit.</span></li>
</ol></div>
<div><h2>Next</h2><p class="sub">What's being built now.</p>
<ol class="timeline">
<li class="next"><b>Knowing who's talking</b><span>Telling your voice apart from everyone else's.</span></li>
<li class="next"><b>A voice with a little "AI" in it</b><span>Just enough effect to feel like the films.</span></li>
<li class="next"><b>More of your apps</b><span>Docs, Sheets, Drive and more.</span></li>
<li class="next"><b>Early access</b><span>Getting it onto computers other than mine.</span></li>
</ol></div>
</div></section>

<section class="alt"><div class="wrap">
{row("Behind the scenes", "Real screens, real progress",
     "No mock-ups, no promises. Every episode shows what the assistant actually does, including when it gets things wrong.",
     ["Honest build logs", "What worked, what didn't", "How the AI is put to work"], "overview", "The workspace with a job in progress")}
</div></section>

<section><div class="wrap"><div class="cta-band">
<h2>Don't miss an episode</h2><p class="sub" style="margin-inline:auto">The channel launches soon. Leave your email and I'll tell you when.</p>
<a class="btn primary" href="{form('Updates on the build')}">Get updates</a></div></div></section>
"""
page("build.html", "Building a real-life Jarvis AI assistant, in public",
     "Follow one developer building a Jarvis-like AI voice assistant: what already works, what's next and every lesson along the way.",
     build, "build.html", og="og-build")

# ---------------------------------------------------------------- work with me
work = f"""
<header class="hero"><div class="wrap">
<span class="eyebrow">For Shopify stores</span>
<h1>New store sections, <em>built fast</em> and checked on every screen.</h1>
<p class="lead">Tell me what you need. My AI assistant builds it on a private copy of your theme, tests it like a
shopper on phone, tablet and desktop, and I review every detail before you see it.</p>
<div class="ctas"><a class="btn primary" href="{form('A Shopify project')}">Start a project</a></div>
</div></header>

<section><div class="wrap center">
<h2>How a project runs</h2>
<p class="sub">Your live store is never touched until you say so.</p>
<div class="steps" style="text-align:left">
<div class="card"><h3>Your brief</h3><p>What you need, plus a screenshot or a site you like.</p></div>
<div class="card"><h3>Built on a copy</h3><p>Work happens on an unpublished copy of your theme, never your live store.</p></div>
<div class="card"><h3>Checked like a shopper</h3><p>Screenshots on phone, tablet and desktop. Buttons, variants and Add to cart, clicked.</p></div>
<div class="card"><h3>You approve</h3><p>You see the preview. It goes live only when you say yes.</p></div>
</div></div></section>

<section class="alt"><div class="wrap">
{row("Every section", "Fully responsive. Fully customizable.",
     "Every section is built to edit in the theme editor: text, images, colours and layout, with no code needed after handover.",
     ["Phone, tablet and desktop, checked every time", "Editable in the Shopify theme editor",
      "Theme check with no new errors", "Fits your theme's own style"], "clients", "The client list with a project in progress")}
{row("Transparent", "Watch your project move",
     "Every step is logged, from download to theme check to preview, with screenshots of each round.",
     ["Step-by-step progress", "Screenshots of every round", "Questions asked, not guessed"], "overview",
     "A design job's stages and a preview of the store", flip=True)}
</div></section>

<section><div class="wrap center">
<h2>What I can build</h2>
<div class="grid" style="text-align:left">
<div class="card"><h3>New sections</h3><p>Heroes, banners, product highlights, testimonials, FAQs. Built from your brief or a screenshot.</p></div>
<div class="card"><h3>Page copies</h3><p>A page you love, rebuilt in your theme, your way.</p></div>
<div class="card"><h3>Fixes and text changes</h3><p>A bug on a page, or wording that needs to change, found and fixed.</p></div>
</div></div></section>

<section class="alt"><div class="wrap"><div class="cta-band">
<h2>Have a store that needs some love?</h2><p class="sub" style="margin-inline:auto">Tell me about it. I'll reply with how I'd do it.</p>
<a class="btn primary" href="{form('A Shopify project')}">Start a project</a></div></div></section>
"""
page("work-with-me.html", "Custom Shopify sections, built by AI and checked by hand",
     "Fully responsive, fully customizable Shopify sections: built on a copy of your theme, tested on phone, tablet and desktop, and live only when you approve.",
     work, "work-with-me.html", og="og-work", ld=[{"@context": "https://schema.org", "@type": "Service",
         "serviceType": "Shopify theme section development", "name": "Custom Shopify sections",
         "description": "Responsive, theme-editor-customizable Shopify sections built with an AI assistant on an unpublished copy of the theme, tested on every screen size and reviewed by hand before going live.",
         "provider": AUTHOR, "areaServed": "Worldwide", "url": SITE + "work-with-me.html"}])

# ---------------------------------------------------------------- privacy
privacy = """
<section><div class="wrap prose">
<h1 style="font-size:40px;margin:0 0 6px">Privacy policy</h1>
<p>Last updated: 8 November 2026</p>
<p>Jarvis is a personal assistant used only by its owner, on the owner's own laptop. This page explains what it does with Google data.</p>
<h2>What it accesses</h2>
<ul>
<li><b>Google Calendar</b> (calendar events): to show upcoming events, and to add, move or delete events when the owner asks and approves.</li>
<li><b>Gmail</b> (read-only and compose): to read and search the owner's email and to write drafts. Jarvis cannot send email.</li>
</ul>
<h2>Where the data goes</h2>
<ul>
<li>The sign-in token is stored only on the owner's laptop, in a private file.</li>
<li>To answer a request, parts of an email or an event may be sent to the AI model the owner uses (Anthropic's Claude API), only as part of that request.</li>
<li>Google data is never sold, never shared with anyone else and never used for advertising.</li>
</ul>
<h2>Google API Services User Data Policy</h2>
<p>Jarvis's use and transfer of information received from Google APIs adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data Policy</a>, including the Limited Use requirements.</p>
<h2>Contact forms</h2>
<p>If you fill in the contact form on this site, your name and email are used only to reply to you, and never shared.</p>
<h2>Removing access</h2>
<p>Access can be removed at any time with Disconnect in Jarvis's Settings, or at <a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>.</p>
</div></section>
"""
page("privacy.html", "Privacy policy | Jarvis",
     "How Jarvis, a personal AI assistant, handles Google Calendar and Gmail data: kept on the owner's laptop, never sold or shared.",
     privacy, "privacy.html", priority="0.3")

nf = """<section class="hero"><div class="wrap"><span class="eyebrow">404</span>
<h1>That page has <em>wandered off.</em></h1><p class="lead">Even a good assistant can't find everything.</p>
<div class="ctas"><a class="btn primary" href="/jarvis-app/">Back to home</a></div></div></section>"""
page("404.html", "Page not found | Jarvis", "This page doesn't exist.", nf, priority="")
html404 = open(os.path.join(OUT, "404.html")).read()
html404 = html404.replace('content="index,follow,max-image-preview:large"', 'content="noindex"')
html404 = html404.replace('href="', 'href="/jarvis-app/').replace('href="/jarvis-app/https://', 'href="https://').replace('href="/jarvis-app/./"', 'href="/jarvis-app/"').replace('href="/jarvis-app/#', 'href="#').replace('href="/jarvis-app//jarvis-app/', 'href="/jarvis-app/')
import re
html404 = re.sub(r'<link rel="canonical"[^>]*>\n?', '', html404)
open(os.path.join(OUT, "404.html"), "w").write(html404)

import datetime
today = datetime.date.today().isoformat()
urls = "".join(f"<url><loc>{SITE}{'' if f == 'index.html' else f}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>"
               for f, pr in PAGES if pr)
open(os.path.join(OUT, "sitemap.xml"), "w").write(
    f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
open(os.path.join(OUT, "site.webmanifest"), "w").write(json.dumps({
    "name": "Jarvis", "short_name": "Jarvis", "start_url": "/jarvis-app/", "scope": "/jarvis-app/", "display": "standalone",
    "background_color": "#0D1117", "theme_color": "#0D1117", "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=1))
print("built")
