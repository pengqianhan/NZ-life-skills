---
name: travel-planner
description: >-
  Universal travel planning skill for multi-day road trips and city-hopping
  itineraries anywhere in the world. Use this whenever someone wants to plan a
  trip to any country or city, find accommodation (Airbnb or hotels) with
  real-time availability checking, build a day-by-day itinerary, research and
  book tours or activities, or get a complete clickable travel guide they can
  use to book everything. Triggers on any travel planning request such as
  "help me plan a trip to Japan", "road trip in Europe", "weekend in Sydney",
  "best things to do in Iceland", "find me an Airbnb in Barcelona", or Chinese
  requests like planning trips to Thailand, Japan, Australia, etc. Even if the
  user just describes destinations without asking explicitly for a plan, use
  this skill. Has deep built-in knowledge for New Zealand Northland
  (references/nz-northland.md) and accumulates examples from past plans.
metadata:
  author: Pengqian Han
  package: nz-life-skills
  bundle: extended
  geography: global
  audience:
    - travelers
    - trip-planners
  policy_sensitive: false
  official_sources_required: false
---

# Travel Planner

A skill for planning multi-day trips anywhere in the world — produces complete, clickable travel guides with real-time accommodation links, tour bookings, day-by-day itineraries, and budget breakdowns.

For trips with accumulated local knowledge, check the `references/` folder before starting. For inspiration on output format and planning process, see `examples/`.

---

## Workflow

### Step 1 — Clarify trip details

If not already provided, ask (or infer from context):

- **Destination(s)** — country, region, specific cities
- **Departure date + duration** (or return date)
- **Number of people** — adults / children
- **Accommodation budget** — total for the trip, and preferred currency
- **Must-see attractions or experiences** — check if user has a map, image, or list
- **Activity style** — adventure, culture, relaxation, food, family-friendly, etc.
- **Driving preference** — happy to self-drive long distances? Or prefer tours/transit?

If the user provides an image or map with marked attractions, extract all place names from it.

### Step 2 — Research the destination

Before planning, build a mental model of the geography and logistics:

1. **Check `references/` for this destination.** If a file like `references/nz-northland.md` exists, read it — it contains pre-researched routes, operators, and pricing that save research time.
2. **Identify the best base(s).** For linear routes (road trips), pick 1-2 central overnight stops. For city trips, one central base is usually best.
3. **Map the route logically** — order attractions to minimize backtracking, considering driving times.
4. **Note seasonal factors** — peak season pricing, closed attractions, weather.

For destinations not yet in `references/`, use web search to fill in: typical accommodation prices, top tour operators, key attractions, and transport options.

### Step 3 — Find accommodation (real-time browser check)

Use the Claude in Chrome browser tool to check **real-time availability** — static knowledge about specific listings is unreliable due to pricing and availability changes.

**Airbnb search approach:**

```
https://www.airbnb.[country-domain]/s/[City-Name]/homes?adults=N&checkin=YYYY-MM-DD&checkout=YYYY-MM-DD&price_max=XXX
```

Adjust the domain (`.com`, `.co.nz`, `.co.uk`, `.com.au`, etc.) and price_max based on the user's budget split across nights.

Screenshot the results and extract the top 3–5 listings with: total price, star rating, number of reviews, property type, and location notes. Then click into the top candidate to confirm availability for the exact dates.

If Airbnb doesn't yield good results (wrong location, budget too tight), also check:
- Booking.com — better for hotels and B&Bs
- Local booking platforms (e.g., Bookabach in NZ, Gîtes de France in France)

**Accommodation selection criteria (in priority order):**
1. Available for exact dates ✅
2. Within budget (aim for ~80% of budget on accommodation, leaving 20% buffer)
3. Central location relative to planned attractions
4. Strong reviews (4.8+ on Airbnb, 8.5+ on Booking.com)
5. Whole-place over shared — privacy matters for couples/families

### Step 4 — Plan the itinerary

Structure the days logically:

- **Day 1**: Travel day — schedule scenic stops en route, arrive and check in by late afternoon
- **Middle days**: The highlights — most physically demanding or logistically complex activities
- **Last day**: Lighter activities, check out, return journey with optional stops

For each day, build a time-based table:

| Time | Location | Activity | Travel time |
|------|----------|----------|-------------|

Include approximate driving times between stops. Be realistic about distances — a packed itinerary that looks good on paper but requires 10 hours of driving is not helpful.

**Key scheduling considerations:**
- Tour departure times (many are early morning — 7am is common)
- Activity operating days (some don't run on weekdays or Mondays)
- Opening hours of attractions
- Meal stops — plan lunch around activity locations, not just convenience

### Step 5 — Research tours and activities

For major activities (guided tours, cruises, experiences):

1. **Identify 2-3 reputable operators** via web search ("[activity] [city] tour operator" + reviews)
2. **Check operating schedules** — especially important for seasonal activities or those with limited departure days
3. **Compare pricing** — look for online booking discounts (often 10%), early bird deals, or combo packages
4. **Note cancellation policies** — free cancellation 24-48h before is standard for good operators
5. **Flag scheduling conflicts** — e.g., if a cruise only runs on certain days, ensure the itinerary aligns

Present the best option(s) with direct booking URLs, pricing, and key logistics.

### Step 6 — Compile the travel guide

Create a `.md` file in the user's workspace. Match the language to the user (Chinese → Chinese, English → English, or bilingual if helpful).

**File naming convention:** `[城市/地区]旅游攻略.md` (Chinese) or `[destination]-travel-guide.md` (English)

**Required sections:**

```markdown
# [目的地] 旅游攻略 / Travel Guide
[出发日期 | 人数 | 天数]

## 🏠 住宿预订 / Accommodation
- Property: name, rating, price
- [Direct booking link with pre-filled dates and guest count]

## 🎫 活动预订 / Tour & Activity Bookings
For each activity:
- Name, operator, price, duration
- Key logistics (departure time, meeting point, included items)
- [Direct booking URL]
- ⚠️ Any scheduling warnings (operating days, capacity, etc.)

## 📅 完整行程 / Itinerary
Day-by-day tables with time | location | activity | travel time

## 💰 费用总结 / Budget Summary
Table: item | cost (2-person or per-person)
Total with / without optional activities

## ✅ 预订清单 / Booking Checklist
- [ ] Step 1: [Link]
- [ ] Step 2: [Link]
- [ ] Step 3 (optional): [Link]

## 📌 实用贴士 / Practical Tips
Driving routes, weather, packing list, local tips
```

**Link quality rules:**
- All links must be direct booking pages (not homepages)
- Pre-fill dates and group size in URLs where the platform supports it (Airbnb, Viator, GetYourGuide support this)
- No affiliate links or redirect wrappers needed

---

## Destination Reference Files

When planning for these destinations, read the corresponding reference file first:

| Destination | Reference File | Contains |
|-------------|---------------|---------|
| New Zealand — Northland / Bay of Islands | `references/nz-northland.md` | Route, operators, pricing, seasonal notes |

To add a new destination to the library: after completing a plan, extract the key reusable knowledge (routes, operators, prices, seasonal tips) and save as `references/[country-region].md`.

---

## Past Plan Examples

Browse `examples/` for complete worked plans. These show the expected output format and document the planning decisions made.

| Example | File |
|---------|------|
| New Zealand — Auckland → Northland 3日游（2026年4月，2人，NZD $350住宿预算） | `examples/nz-auckland-northland.md` |

When the user's trip is similar to an existing example, reference it explicitly: "I have a past plan for a similar trip — let me adapt it for your dates and group size."

---

## Language and Currency

- **Language**: Match the user's language throughout. If they wrote in Chinese, the entire guide is in Chinese. If they switch mid-conversation, follow.
- **Currency**: Always use the destination country's local currency as the primary unit. Add approximate conversions (RMB, USD) for Chinese users as a secondary reference.
- **Budget framing**: State budgets clearly — "2人两晚合计 NZD $355" not "NZD $177.50/人/晚" — total cost is easier to evaluate.

---

## Common Pitfalls to Avoid

- **Don't recommend specific Airbnb listings by name without browser verification** — listings come and go. Always check real-time availability.
- **Don't assume tour schedules** — operating days change seasonally. Check the actual booking page.
- **Don't underestimate driving time** — always add 30-50% buffer over Google Maps estimates to account for stops, photo opportunities, and rural speed limits.
- **Don't schedule optional activities on the last day** if the user has a flight — use last-day time for backup/flexibility.
- **Always check date-day conflicts** — a user who wants a "Tuesday dolphin cruise" on a Monday trip has a problem you need to flag and resolve before writing the guide.
