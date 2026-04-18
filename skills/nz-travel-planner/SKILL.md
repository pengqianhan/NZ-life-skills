---
name: nz-travel-planner
description: New Zealand travel planning skill — use this whenever someone wants to plan a road trip or multi-day trip in New Zealand, especially in the Auckland Northland / Bay of Islands region. Triggers when the user mentions visiting NZ attractions (Cape Reinga, Bay of Islands, Paihia, Kerikeri, Whangarei, Matakana, Ninety Mile Beach, Te Paki Sand Dunes, Waitangi, etc.), asks for NZ accommodation recommendations or Airbnb searches, wants a NZ itinerary or travel guide, or asks about booking tours and activities in New Zealand. Even if the user just says "help me plan a trip to New Zealand" or "I'm going to Auckland and want to explore north", use this skill.
metadata:
  author: Pengqian Han
  package: nz-life-skills
  bundle: extended
  geography: nz
  audience:
    - travelers
    - visitors
  policy_sensitive: false
  official_sources_required: false
---

# NZ Travel Planner — Auckland Northland Route

A skill for planning multi-day road trips in New Zealand, with deep expertise in the Auckland → Northland / Bay of Islands corridor. Produces complete, clickable travel guides with accommodation links, tour bookings, itineraries, and budget breakdowns.

---

## Workflow Overview

1. **Clarify trip details** — dates, group size, budget, must-see attractions
2. **Find and verify accommodation** — use browser to check real-time Airbnb availability
3. **Plan the itinerary** — structure stops logically along the route
4. **Research tour operators** — find reputable tours for key activities
5. **Compile the guide** — create a single Markdown file with all clickable links

---

## Step 1: Clarify Trip Details

Before searching, confirm these details with the user (if not already provided):

- **Departure date and return date** (or number of nights)
- **Number of people** (adults/children)
- **Accommodation budget** (total for the trip, in NZD)
- **Key attractions / places** the user wants to visit
- **Activity preferences** (adventure, culture, nature, food, etc.)
- **Driving preference** — comfortable with long drives? (Cape Reinga is ~5h from Auckland)

If the user mentions a map or image with attractions, extract all place names from it.

---

## Step 2: Find Accommodation via Browser

Use the Claude in Chrome browser tool to check **real-time availability** — don't guess or use static knowledge, as prices and availability change.

### Airbnb Search Strategy

1. Open Airbnb with URL parameters for the target area:
   ```
   https://www.airbnb.co.nz/s/Kerikeri--New-Zealand/homes?adults=2&checkin=YYYY-MM-DD&checkout=YYYY-MM-DD&price_max=XXX
   ```
   Adjust location, dates, and price_max based on user's budget.

2. **Best base for Northland trips**: **Kerikeri** — central location, ~20 min from Paihia, 2.5h from Cape Reinga.

3. Screenshot and extract the top 3–5 listings with:
   - Price per night and total
   - Star rating and number of reviews
   - Property type (whole place vs. private room)
   - Distance to key attractions
   - Any special notes (pet-friendly, min nights, etc.)

4. Click into the top candidate to verify availability for exact dates before recommending.

5. If budget is tight, try **Paihia** or **Whangarei** as alternative bases. Always compare April vs. other months — peak season (Dec–Jan) is significantly more expensive.

### Accommodation Tips for Northland

| Location | Pros | Best For |
|----------|------|----------|
| Kerikeri | Central, peaceful, near Stone Store & Rainbow Falls | Couples, nature lovers |
| Paihia | Waterfront, tours depart from here | Easy access to Bay of Islands cruises |
| Whangarei | City amenities, 1h to Paihia | Budget-conscious travelers |

---

## Step 3: Plan the Itinerary

### Auckland → Northland Route (Standard 3-Day Trip)

**Day 1: Auckland → Kerikeri (via scenic stops)**

Key stops southward → north:
- **Matakana** (~45 min from Auckland): artisan market, boutique cafes, Ascension Wine Estate
- **Eutopia Cafe** (near Kaiwaka, ~45 min from Matakana): photogenic hillside cafe, good coffee
- **Whangarei** (~45 min): Town Basin waterfront lunch, Whangarei Falls (short walk)
- **Kawakawa** (~20 min): Famous Hundertwasser public toilet (quirky art landmark, free to see)
- **Paihia** (~30 min): Bay of Islands atmosphere, waterfront walk
- **Kerikeri** (~20 min): Check in, dinner at local restaurants

Total driving without stops: ~3 hours. With stops: plan 7–8 hours.

**Day 2: Cape Reinga Full Day Tour (the highlight)**

This is the unmissable day. Book a guided tour — self-driving is possible but tours offer beach driving, sandboarding equipment, and local knowledge.

- Depart Paihia/Kerikeri early (7:00am pickup from Paihia)
- Stops: Kaitaia → 可口可乐湖 (Cola Lake / Tannin Lake) → Cape Reinga Lighthouse (NZ's northern tip, Pacific meets Tasman Sea) → Houhora (lunch) → Te Paki Sand Dunes (sandboarding!) → Ninety Mile Beach (bus drives along the beach)
- Return ~6pm

**Day 3: Bay of Islands → Return to Auckland**

Options depending on what's available:
- **Waitangi Treaty Grounds** — NZ founding document site, highly recommended (2–3 hours)
- **Hole in the Rock cruise** — iconic rock arch, see dolphins en route
- **Rainbow Falls & Stone Store** in Kerikeri (easy morning walk)
- Depart ~2pm for Auckland, arrive ~5pm

### Seasonal Notes

- **April (Autumn)**: Best season — warm (18–24°C), fewer crowds, good value
- **December–January**: Peak summer, crowded and expensive
- **June–August**: Winter, cooler, some tours reduce frequency

---

## Step 4: Research Tour Operators

### Cape Reinga Day Tours

**Must Do New Zealand** (mustdonewzealand.co.nz) — top-rated operator departing from Paihia.

| Feature | Details |
|---------|---------|
| Route | Paihia → 90-Mile Beach → Cape Reinga → Sand Dunes → Ninety Mile Beach |
| Duration | ~11 hours (7am–6pm) |
| Includes | Lunch at Houhora, sandboards, bus along beach |
| Price | ~NZD $195/person (book online for ~10% discount: ~$175.50) |
| Cancellation | 48h free cancellation |
| Booking URL | `https://mustdonewzealand.co.nz/tours/cape-reinga-90-mile-beach-tour-paihia/` |

**Combo Deal**: Cape Reinga + Hole in the Rock = ~$290/person (vs $365 separately). Look for "Combine your Day trip to Cape Reinga and a Hole in the Rock Cruise" on the same page.

### Bay of Islands Cruises / Dolphin Tours

**Explore Group NZ** (exploregroup.co.nz) — DOC-licensed operator, guarantee policy.

| Feature | Details |
|---------|---------|
| Tour | Dolphin Eco Cruise — Bay of Islands |
| Duration | 5.5 hours |
| Departs | Paihia Wharf, 11:30am |
| April schedule | Tues / Thurs / **Sat / Sun only** (not Mon or Wed) |
| Price | ~NZD $165/person |
| Guarantee | Free return trip if no marine wildlife spotted |
| Booking URL | `https://www.exploregroup.co.nz/bay-of-islands/dolphin-eco-cruise/` |

⚠️ **Important**: Always check the operating calendar for the specific travel dates. If the trip spans a Monday, the dolphin cruise won't run — suggest doing it on arrival day (if Saturday) or booking the Hole in the Rock combo instead.

---

## Step 5: Compile the Travel Guide

Create a `.md` file in the user's workspace folder with this structure:

```
# [标题] 旅游攻略 / NZ Travel Guide

## 🏠 住宿预订 / Accommodation
- Property name, star rating, price
- Direct Airbnb booking link with pre-filled dates

## 🎫 旅游团预订 / Tour Bookings
- Activity 1: name, price, link, key details
- Activity 2: ...

## 📅 完整行程 / Itinerary
- Day 1 table: time | location | activity | drive time
- Day 2 table
- Day 3 table

## 💰 费用总结 / Budget Summary
- Table: item | 2-person cost
- Total with/without optional activities

## ✅ 预订清单 / Booking Checklist
- [ ] Step 1: Book accommodation (link)
- [ ] Step 2: Book main tour (link)
- [ ] Step 3: Book optional activity (link)

## 📌 实用贴士 / Practical Tips
- Driving route, weather, packing, activity tips
```

**Language**: Match the user's language. If they wrote in Chinese, write the guide in Chinese. If bilingual labels help (like section headers), use both.

**Links**: All booking links must be direct and clickable (no affiliate redirects needed). Pre-fill dates and group size in URLs where possible.

---

## Budget Reference (2 People, Northland, April)

| Item | Typical Cost (NZD) |
|------|-------------------|
| Accommodation (2 nights, Kerikeri) | $300–$380 |
| Cape Reinga Day Tour × 2 | $351 (with 10% online discount) |
| Dolphin Cruise × 2 (optional) | $330 |
| Cape Reinga + Hole in the Rock Combo × 2 | $580 |
| Fuel (Auckland round trip + local, ~600km) | $100–$140 |
| Food (3 days, excluding included tour lunch) | $150–$200 |
| **Total without optional cruise** | **~$950–$1,050** |
| **Total with dolphin cruise** | **~$1,250–$1,400** |

---

## Key URLs Reference

| Resource | URL |
|----------|-----|
| Airbnb NZ search | `https://www.airbnb.co.nz/s/Kerikeri--New-Zealand/homes` |
| Must Do NZ (Cape Reinga) | `https://mustdonewzealand.co.nz/tours/cape-reinga-90-mile-beach-tour-paihia/` |
| Explore Group (Dolphin Cruise) | `https://www.exploregroup.co.nz/bay-of-islands/dolphin-eco-cruise/` |
| Waitangi Treaty Grounds | `https://www.waitangi.org.nz` |
| Eutopia Cafe | Search "Eutopia Cafe Kaiwaka" on Google Maps |
| Matakana Market | Saturdays 8am–1pm (mustdonewzealand.co.nz has info) |

---

*Skill created: 2026-04-03 | Based on Auckland Northland trip planning for 2 adults, April 2026*
