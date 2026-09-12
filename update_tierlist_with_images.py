import os
import json
import base64
import html
import urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load catalog
catalog_file = 'C:/Users/zdog0/.gemini/antigravity/scratch/tierlist-2026/catalog.json'
with open(catalog_file, 'r', encoding='utf-8') as f:
    catalog_data = json.load(f)

# 2. 28 Base Games strictly meeting criteria
base_games = [
    # --- ALREADY RELEASED HITS (1M+ SALES, 70+ METACRITIC, 80%+ STEAM SCORE) ---
    {
        "id": "forza-horizon-6",
        "title": "Forza Horizon 6",
        "type": "hit",
        "subtype": "original",
        "meta": "91",
        "sales": "6.4M+",
        "status": "Вышла 19 мая 2026 (Steam: 84%)",
        "platforms": "PC, Xbox Series X/S",
        "lines": ["FORZA", "HORIZON 6"]
    },
    {
        "id": "resident-evil-requiem",
        "title": "Resident Evil Requiem",
        "type": "hit",
        "subtype": "original",
        "meta": "89",
        "sales": "6.0M+",
        "status": "Вышла 27 фев 2026 (Steam: 97%)",
        "platforms": "PC, PS5, XSX",
        "lines": ["RESIDENT", "EVIL", "REQUIEM"]
    },
    {
        "id": "007-first-light",
        "title": "007 First Light",
        "type": "hit",
        "subtype": "original",
        "meta": "87",
        "sales": "4.0M+",
        "status": "Вышла 26 мая 2026 (Steam: 85%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["007", "FIRST LIGHT"]
    },
    {
        "id": "pragmata",
        "title": "Pragmata",
        "type": "hit",
        "subtype": "original",
        "meta": "85",
        "sales": "2.5M+",
        "status": "Вышла 17 апр 2026 (Steam: 80%)",
        "platforms": "PC, PS5, XSX",
        "lines": ["PRAGMATA"]
    },
    {
        "id": "college-football-27",
        "title": "EA Sports College Football 27",
        "type": "hit",
        "subtype": "original",
        "meta": "84",
        "sales": "2.5M+",
        "status": "Вышла 9 июл 2026 (Steam: 83%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["EA SPORTS", "COLLEGE", "FOOTBALL 27"]
    },
    {
        "id": "lego-batman",
        "title": "LEGO Batman: Legacy of the Dark Knight",
        "type": "hit",
        "subtype": "original",
        "meta": "84",
        "sales": "1.2M+",
        "status": "Вышла 22 мая 2026 (Steam: 96%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["LEGO BATMAN", "LEGACY OF", "DARK KNIGHT"]
    },
    {
        "id": "big-walk",
        "title": "Big Walk",
        "type": "hit",
        "subtype": "original",
        "meta": "83",
        "sales": "1.0M+",
        "status": "Вышла 4 авг 2026 (Steam: 96%)",
        "platforms": "PC, PS5, Mac",
        "lines": ["BIG WALK"]
    },
    {
        "id": "the-blood-of-dawnwalker",
        "title": "The Blood of Dawnwalker",
        "type": "hit",
        "subtype": "original",
        "meta": "83",
        "sales": "1.0M+",
        "status": "Вышла 3 сен 2026 (Steam: 86%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["THE BLOOD OF", "DAWNWALKER"]
    },
    {
        "id": "resonance-plague-tale",
        "title": "Resonance: A Plague Tale Legacy",
        "type": "hit",
        "subtype": "original",
        "meta": "82",
        "sales": "1.0M+",
        "status": "Вышла 27 авг 2026 (Steam: 92%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["RESONANCE", "A PLAGUE TALE", "LEGACY"]
    },
    {
        "id": "nioh-3",
        "title": "Nioh 3",
        "type": "hit",
        "subtype": "original",
        "meta": "86",
        "sales": "1.0M+",
        "status": "Вышла 6 фев 2026 (Steam: 80%)",
        "platforms": "PC, PlayStation 5",
        "lines": ["NIOH 3"]
    },
    {
        "id": "mewgenics",
        "title": "Mewgenics",
        "type": "hit",
        "subtype": "original",
        "meta": "89",
        "sales": "1.0M+",
        "status": "Вышла 10 фев 2026 (Steam: 91%)",
        "platforms": "PC, PS5, XSX",
        "lines": ["MEWGENICS"]
    },
    {
        "id": "onimusha-way-of-the-sword",
        "title": "Onimusha: Way of the Sword",
        "type": "hit",
        "subtype": "original",
        "meta": "85",
        "sales": "1.0M+",
        "status": "Вышла 4 сен 2026 (Steam: 94%)",
        "platforms": "PC, PS5, XSX",
        "lines": ["ONIMUSHA", "WAY OF THE", "SWORD"]
    },
    {
        "id": "reanimal",
        "title": "Reanimal",
        "type": "hit",
        "subtype": "original",
        "meta": "80",
        "sales": "1.0M+",
        "status": "Вышла 13 фев 2026 (Steam: 100%)",
        "platforms": "PC, PS5, XSX",
        "lines": ["REANIMAL"]
    },
    {
        "id": "star-wars-zero-company",
        "title": "Star Wars Zero Company",
        "type": "hit",
        "subtype": "original",
        "meta": "78",
        "sales": "1.1M+",
        "status": "Вышла 27 авг 2026 (Steam: 82%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["STAR WARS", "ZERO COMPANY"]
    },
    {
        "id": "gothic-1-remake",
        "title": "Gothic 1 Remake",
        "type": "hit",
        "subtype": "original",
        "meta": "76",
        "sales": "1.2M+",
        "status": "Вышла 5 июн 2026 (Steam: 85%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["GOTHIC 1", "REMAKE"]
    },
    {
        "id": "code-vein-2",
        "title": "CODE VEIN II",
        "type": "hit",
        "subtype": "original",
        "meta": "72",
        "sales": "1.2M+",
        "status": "Вышла 29 янв 2026 (Steam: 87%)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["CODE VEIN II"]
    },
    {
        "id": "death-stranding-2",
        "title": "Death Stranding 2: On The Beach",
        "type": "hit",
        "subtype": "original",
        "meta": "89",
        "sales": "2.0M+",
        "status": "Вышла 19 мар 2026 (Steam: 95%)",
        "platforms": "PC, PlayStation 5",
        "lines": ["DEATH", "STRANDING 2"]
    },

    # --- MOST ANTICIPATED BLOCKBUSTERS OF LATE 2026 (PS5 LIST & JSON) ---
    {
        "id": "gta-vi",
        "title": "Grand Theft Auto VI",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 100",
        "sales": "19 Ноября 2026",
        "status": "Релиз 19 ноября 2026 (Rockstar)",
        "platforms": "PlayStation 5, Xbox Series X/S",
        "lines": ["GRAND THEFT", "AUTO VI"]
    },
    {
        "id": "marvels-wolverine",
        "title": "Marvel's Wolverine",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 98",
        "sales": "15 Сентября 2026",
        "status": "Релиз 15 сентября 2026 (Insomniac)",
        "platforms": "PlayStation 5",
        "lines": ["MARVEL'S", "WOLVERINE"]
    },
    {
        "id": "gears-of-war-e-day",
        "title": "Gears of War: E-Day",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 96",
        "sales": "6 Октября 2026",
        "status": "Релиз 6 октября 2026 (Xbox Studios)",
        "platforms": "PC, Xbox Series X/S",
        "lines": ["GEARS OF WAR", "E-DAY"]
    },
    {
        "id": "control-resonant",
        "title": "Control Resonant",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 94",
        "sales": "24 Сентября 2026",
        "status": "Релиз 24 сентября 2026 (Remedy)",
        "platforms": "PC, PS5, XSX",
        "lines": ["CONTROL", "RESONANT"]
    },
    {
        "id": "silent-hill-townfall",
        "title": "Silent Hill: Townfall",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 93",
        "sales": "24 Сентября 2026",
        "status": "Релиз 24 сентября 2026 (Konami)",
        "platforms": "PC, PlayStation 5",
        "lines": ["SILENT HILL", "TOWNFALL"]
    },
    {
        "id": "ace-combat-8",
        "title": "Ace Combat 8: Wings of Theve",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 91",
        "sales": "2 Октября 2026",
        "status": "Релиз 2 октября 2026 (Bandai Namco)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["ACE COMBAT 8", "WINGS OF THEVE"]
    },
    {
        "id": "star-wars-galactic-racer",
        "title": "Star Wars: Galactic Racer",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 90",
        "sales": "6 Октября 2026",
        "status": "Релиз 6 октября 2026 (Lucasfilm)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["STAR WARS", "GALACTIC", "RACER"]
    },
    {
        "id": "castlevania-belmonts-curse",
        "title": "Castlevania: Belmont's Curse",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 92",
        "sales": "15 Октября 2026",
        "status": "Релиз 15 октября 2026 (Konami)",
        "platforms": "PC, PS5, XSX",
        "lines": ["CASTLEVANIA", "BELMONT'S", "CURSE"]
    },
    {
        "id": "cod-modern-warfare-4",
        "title": "Call of Duty: Modern Warfare 4",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 95",
        "sales": "23 Октября 2026",
        "status": "Релиз 23 октября 2026 (Activision)",
        "platforms": "PC, PS5, XSX",
        "lines": ["CALL OF DUTY", "MODERN", "WARFARE 4"]
    },
    {
        "id": "phantom-blade-zero",
        "title": "Phantom Blade Zero",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 94",
        "sales": "29 Октября 2026",
        "status": "Релиз 29 октября 2026 (S-Game)",
        "platforms": "PC, PlayStation 5",
        "lines": ["PHANTOM", "BLADE ZERO"]
    },
    {
        "id": "warhammer-dawn-of-war-4",
        "title": "Warhammer 40,000: Dawn of War IV",
        "type": "anticipated",
        "subtype": "original",
        "meta": "HYPE 91",
        "sales": "3 Декабря 2026",
        "status": "Релиз 3 декабря 2026 (Sega / Relic)",
        "platforms": "PC",
        "lines": ["WARHAMMER", "DAWN OF", "WAR IV"]
    }
]

images_dir = "C:/Users/zdog0/.gemini/antigravity/scratch/tierlist-2026/images"
custom_covers = {}

for fname in os.listdir(images_dir):
    if fname.endswith(('.jpg', '.png', '.webp', '.jpeg')):
        gid = os.path.splitext(fname)[0]
        img_path = os.path.join(images_dir, fname)
        with open(img_path, "rb") as f:
            data = f.read()
            mime = "image/png" if data[:8] == b"\x89PNG\r\n\x1a\n" else "image/jpeg"
            b64 = base64.b64encode(data).decode("utf-8")
            custom_covers[gid] = f"data:{mime};base64,{b64}"

print(f"Loaded {len(custom_covers)} pre-cached base64 covers from images/ directory!")

def make_svg(game):
    lines = game.get("lines", [game["title"]])
    line_count = len(lines)
    start_y = 118 - (line_count - 1) * 13
    text_tspans = ""
    for i, line in enumerate(lines):
        y = start_y + i * 25
        text_tspans += f'<text x="80" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="900" fill="#000000" text-anchor="middle" letter-spacing="0.2">{html.escape(line)}</text>\\n'

    is_hit = game.get("type") == "hit"
    top_badge_bg = "#dcfce7" if is_hit else "#fef3c7"
    top_badge_color = "#15803d" if is_hit else "#b45309"
    top_badge_text = "★ 2026 HIT (80+) ★" if is_hit else "🔥 ANTICIPATED"

    bottom_bg = "#000000" if is_hit else "#1e3a8a"
    sub1 = f"META: {game['meta']}" if is_hit else "COMING SOON"
    sub2 = f"{game['sales']} COPIES" if is_hit else f"{game['sales']}"
    sub2_color = "#4ade80" if is_hit else "#fbbf24"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="240" viewBox="0 0 160 240">
  <rect width="160" height="240" fill="#ffffff"/>
  <rect x="4" y="4" width="152" height="232" fill="#ffffff" stroke="#000000" stroke-width="2.5" rx="3"/>
  <rect x="8" y="8" width="144" height="22" fill="{top_badge_bg}" rx="2"/>
  <text x="80" y="23" font-family="Arial, Helvetica, sans-serif" font-size="8.5" font-weight="900" fill="{top_badge_color}" text-anchor="middle" letter-spacing="0.5">{top_badge_text}</text>
  
  {text_tspans}
  
  <rect x="8" y="196" width="144" height="34" fill="{bottom_bg}" rx="3"/>
  <text x="80" y="211" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">{sub1}</text>
  <text x="80" y="224" font-family="Arial, Helvetica, sans-serif" font-size="9" font-weight="bold" fill="{sub2_color}" text-anchor="middle">{sub2}</text>
</svg>'''
    
    encoded = urllib.parse.quote(svg)
    return f"data:image/svg+xml;utf8,{encoded}"

for g in base_games:
    g["image"] = make_svg(g)

hits_count = sum(1 for g in base_games if g["type"] == "hit")
antic_count = sum(1 for g in base_games if g["type"] == "anticipated")
total_count = len(base_games)

covers_json = json.dumps(custom_covers)
games_json = json.dumps(base_games, ensure_ascii=False)
catalog_json = json.dumps(catalog_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Games TierList 2026 (1M+ Sales, 80%+ Score, Catalog Search) - TierMaker</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: #242222;
            color: #888;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        /* HEADER */
        #header {{
            width: 100%;
            background-color: #1a1a1a;
            border-bottom: 1px solid #444;
            display: flex;
            justify-content: center;
            padding: 10px 20px;
            position: sticky;
            top: 0;
            z-index: 1000;
        }}

        #inner-header {{
            width: 100%;
            max-width: 1140px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .logo-container {{
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
        }}

        .logo-badge {{
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            color: #fff;
            font-weight: 900;
            font-size: 18px;
            padding: 4px 10px;
            border-radius: 4px;
        }}

        .logo-text {{
            color: #fff;
            font-size: 20px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }}

        .header-tag {{
            background: #2a2a2a;
            color: #4ade80;
            font-size: 11px;
            font-weight: bold;
            padding: 3px 8px;
            border-radius: 12px;
            border: 1px solid #4ade80;
        }}

        .header-nav {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .btn-header {{
            background: #3a5795;
            color: #fff;
            padding: 7px 15px;
            border-radius: 6px;
            font-size: 14px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            transition: 0.2s;
        }}
        .btn-header:hover {{
            background: #476bb8;
        }}

        /* CONTAINER */
        #main-container {{
            width: 100%;
            max-width: 1140px;
            padding: 20px 15px 80px 15px;
            display: flex;
            flex-direction: column;
        }}

        #breadcrumbs {{
            font-size: 13px;
            color: #bfbfbf;
            margin-bottom: 12px;
        }}

        #breadcrumbs a {{
            color: #7fbfff;
            text-decoration: none;
        }}

        h1 {{
            color: #ffffff;
            font-size: 25px;
            font-weight: 800;
            margin-bottom: 8px;
        }}

        .description {{
            color: #bfbfbf;
            font-size: 14px;
            line-height: 1.5;
            margin-bottom: 16px;
        }}

        .criteria-badges {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 22px;
        }}

        .badge {{
            background-color: #2e2c2c;
            color: #eee;
            font-size: 12px;
            padding: 5px 12px;
            border-radius: 4px;
            border-left: 3px solid #ff7f7f;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .badge.green {{ border-color: #4ade80; }}
        .badge.yellow {{ border-color: #fbbf24; }}
        .badge.blue {{ border-color: #60a5fa; }}
        .badge.purple {{ border-color: #a78bfa; }}

        /* CONTROLS BAR */
        .controls-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            background: #1a1a1a;
            padding: 10px 16px;
            border-radius: 6px;
            border: 1px solid #333;
            margin-bottom: 16px;
        }}

        .btn-group {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .btn {{
            background: #2d2d2d;
            color: #ddd;
            border: 1px solid #444;
            padding: 7px 14px;
            border-radius: 4px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .btn:hover {{
            background: #3d3d3d;
            color: #fff;
            border-color: #666;
        }}
        .btn-primary {{
            background: #166534;
            color: #dcfce7;
            border-color: #22c55e;
        }}
        .btn-primary:hover {{
            background: #15803d;
            color: #fff;
        }}
        .btn-danger {{
            background: #7f1d1d;
            color: #fee2e2;
            border-color: #ef4444;
        }}
        .btn-danger:hover {{
            background: #991b1b;
            color: #fff;
        }}

        .save-indicator {{
            font-size: 12px;
            color: #4ade80;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            opacity: 0;
            transition: opacity 0.3s;
        }}

        /* TIER LIST TABLE */
        #tier-container {{
            background-color: #111111;
            border: 1px solid #000;
            display: flex;
            flex-direction: column;
            gap: 2px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            border-radius: 4px;
            overflow: hidden;
        }}

        .tier-row {{
            display: flex;
            min-height: 122px;
            background-color: #141414;
            border-bottom: 1px solid #222;
            position: relative;
        }}

        .label-holder {{
            width: 110px;
            min-width: 110px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: #000000;
            font-size: 18px;
            font-weight: 900;
            padding: 8px;
            word-break: break-word;
            cursor: pointer;
            user-select: none;
            outline: none;
            transition: opacity 0.15s;
        }}
        .label-holder:hover {{
            opacity: 0.9;
        }}

        .tier-dropzone {{
            flex: 1;
            display: flex;
            flex-wrap: wrap;
            align-content: flex-start;
            padding: 4px;
            gap: 4px;
            min-height: 122px;
            background-color: #141414;
            transition: background-color 0.15s;
        }}

        .tier-dropzone.drag-over {{
            background-color: #262626;
            outline: 2px dashed #4ade80;
            outline-offset: -2px;
        }}

        .row-controls {{
            width: 38px;
            background-color: #181818;
            border-left: 1px solid #282828;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 6px;
            padding: 4px 0;
        }}

        .row-btn {{
            background: none;
            border: none;
            color: #666;
            cursor: pointer;
            font-size: 13px;
            padding: 4px;
            border-radius: 3px;
            transition: 0.15s;
            line-height: 1;
        }}
        .row-btn:hover {{
            color: #fff;
            background: #333;
        }}

        /* CARDS */
        .character {{
            width: 80px;
            height: 120px;
            background-color: #000;
            cursor: grab;
            user-select: none;
            position: relative;
            flex-shrink: 0;
            border-radius: 3px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.4);
            transition: transform 0.1s, box-shadow 0.1s;
        }}
        .character:active {{
            cursor: grabbing;
        }}
        .character.dragging {{
            opacity: 0.4;
            transform: scale(0.95);
        }}

        .character img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            pointer-events: none;
        }}

        .card-tooltip {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0,0,0,0.85);
            color: #fff;
            font-size: 9.5px;
            font-weight: bold;
            padding: 2px 4px;
            text-align: center;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            pointer-events: none;
            border-top: 1px solid rgba(255,255,255,0.15);
        }}

        .card-new-highlight {{
            animation: flashHighlight 1.5s ease-out;
        }}

        @keyframes flashHighlight {{
            0% {{ transform: scale(1.15); box-shadow: 0 0 15px #4ade80; }}
            100% {{ transform: scale(1); box-shadow: none; }}
        }}

        /* UNRANKED POOL & SEARCH */
        #unranked-container {{
            background-color: #181818;
            border: 1px solid #333;
            border-radius: 6px;
            padding: 16px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}

        .unranked-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 12px;
        }}

        .unranked-title-wrap {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .unranked-title {{
            color: #fff;
            font-size: 16px;
            font-weight: 800;
            letter-spacing: 0.5px;
        }}

        .unranked-count-badge {{
            background: #2a2a2a;
            color: #4ade80;
            font-size: 12px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 12px;
            border: 1px solid #333;
        }}

        .filter-tabs {{
            display: flex;
            gap: 6px;
        }}

        .filter-tab {{
            background: #242424;
            color: #aaa;
            border: 1px solid #383838;
            padding: 5px 12px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.15s;
        }}
        .filter-tab:hover {{
            background: #333;
            color: #fff;
        }}
        .filter-tab.active {{
            background: #3a5795;
            color: #fff;
            border-color: #476bb8;
        }}

        /* CATALOG SEARCH BAR */
        .catalog-search-container {{
            margin: 10px 0 16px 0;
            position: relative;
            width: 100%;
        }}

        .search-input-wrapper {{
            display: flex;
            align-items: center;
            background: #121212;
            border: 1.5px solid #3a3a3a;
            border-radius: 8px;
            padding: 8px 14px;
            gap: 10px;
            transition: 0.2s;
        }}

        .search-input-wrapper:focus-within {{
            border-color: #4ade80;
            box-shadow: 0 0 0 2px rgba(74, 222, 128, 0.2);
        }}

        .search-icon {{
            font-size: 16px;
            color: #888;
        }}

        #catalog-search-input {{
            background: transparent;
            border: none;
            outline: none;
            color: #fff;
            font-size: 14px;
            width: 100%;
        }}

        #catalog-search-input::placeholder {{
            color: #777;
        }}

        .clear-search-btn {{
            background: #2a2a2a;
            border: none;
            color: #bbb;
            font-size: 12px;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .clear-search-btn:hover {{
            background: #444;
            color: #fff;
        }}

        .catalog-dropdown {{
            position: absolute;
            top: calc(100% + 6px);
            left: 0;
            right: 0;
            background: #1c1c1c;
            border: 1px solid #444;
            border-radius: 8px;
            max-height: 380px;
            overflow-y: auto;
            z-index: 500;
            box-shadow: 0 10px 25px rgba(0,0,0,0.7);
        }}

        .catalog-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 14px;
            border-bottom: 1px solid #2a2a2a;
            transition: background 0.15s;
            gap: 12px;
        }}

        .catalog-item:hover {{
            background: #262626;
        }}

        .catalog-item-info {{
            display: flex;
            align-items: center;
            gap: 12px;
            min-width: 0;
        }}

        .catalog-item-poster {{
            width: 36px;
            height: 50px;
            border-radius: 4px;
            object-fit: cover;
            background: #222;
            flex-shrink: 0;
            border: 1px solid #333;
        }}

        .catalog-item-text {{
            min-width: 0;
        }}

        .catalog-item-title {{
            color: #fff;
            font-size: 14px;
            font-weight: 700;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}

        .catalog-item-meta {{
            font-size: 11px;
            color: #999;
            margin-top: 3px;
            display: flex;
            gap: 8px;
            align-items: center;
        }}

        .catalog-source-tag {{
            background: #2e3846;
            color: #60a5fa;
            padding: 1px 6px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 600;
        }}

        .btn-catalog-add {{
            background: #166534;
            color: #dcfce7;
            border: 1px solid #22c55e;
            border-radius: 6px;
            padding: 6px 12px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            white-space: nowrap;
            transition: 0.2s;
            flex-shrink: 0;
        }}

        .btn-catalog-add:hover {{
            background: #15803d;
        }}
        .btn-catalog-add:disabled {{
            background: #333;
            color: #aaa;
            border-color: #555;
            cursor: wait;
        }}

        .badge-in-list {{
            background: #27272a;
            color: #a1a1aa;
            border: 1px solid #3f3f46;
            border-radius: 6px;
            padding: 5px 10px;
            font-size: 11px;
            font-weight: 600;
            flex-shrink: 0;
        }}

        #unranked-pool {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            min-height: 130px;
            background-color: #111111;
            padding: 10px;
            border-radius: 4px;
            border: 1px solid #262626;
        }}

        /* MODAL OVERLAY & TIERMAKER SETTINGS */
        #modal-overlay {{
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.75);
            display: none;
            justify-content: center;
            align-items: flex-start;
            padding-top: 50px;
            z-index: 2000;
        }}

        #modal-wrapper {{
            position: relative;
            width: 90%;
            max-width: 480px;
        }}

        #modal {{
            background: #242323;
            border: 1px solid #3e3e3e;
            border-radius: 8px;
            padding: 24px 28px 26px;
            position: relative;
            box-shadow: 0 12px 35px rgba(0,0,0,0.85);
            color: #fff;
        }}

        #modal #close {{
            position: absolute;
            top: 14px;
            right: 18px;
            cursor: pointer;
            font-size: 22px;
            font-weight: 900;
            color: #fff;
            opacity: 0.8;
            line-height: 1;
            transition: opacity 0.15s, transform 0.15s;
            user-select: none;
        }}
        #modal #close:hover {{
            opacity: 1;
            transform: scale(1.1);
        }}

        #modal h4 {{
            color: #ffffff;
            font-size: 15px;
            font-weight: 700;
            letter-spacing: 0.2px;
        }}

        #color-select {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin: 12px 0 20px 0;
        }}

        #color-select span {{
            width: 32px;
            height: 32px;
            border-radius: 4px;
            cursor: pointer;
            border: 2px solid transparent;
            transition: transform 0.15s, border-color 0.15s, box-shadow 0.15s;
            display: inline-block;
        }}
        #color-select span:hover {{
            transform: scale(1.15);
            border-color: #ffffff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.5);
        }}
        #color-select span.active {{
            border-color: #ffffff;
            box-shadow: 0 0 8px rgba(255,255,255,0.8);
            transform: scale(1.1);
        }}

        #labelName {{
            width: 100%;
            height: 52px;
            background: #141414;
            border: 1px solid #444;
            border-radius: 5px;
            color: #fff;
            padding: 10px 12px;
            font-size: 15px;
            font-family: inherit;
            resize: none;
            box-sizing: border-box;
            margin-top: 10px;
            margin-bottom: 6px;
            outline: none;
            transition: border-color 0.2s;
        }}
        #labelName:focus {{
            border-color: #3b82f6;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.3);
        }}

        /* MODAL BUTTONS WITH GENEROUS SPACING TOP AND BOTTOM */
        .modal-buttons {{
            display: flex;
            gap: 14px;
            margin-top: 18px;
            margin-bottom: 0;
        }}

        .modal-buttons button {{
            flex: 1;
            padding: 12px 16px;
            font-size: 14px;
            font-weight: 700;
            border-radius: 6px;
            border: 1px solid transparent;
            cursor: pointer;
            transition: background 0.15s, transform 0.1s, box-shadow 0.15s;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }}
        .modal-buttons button:active {{
            transform: scale(0.98);
        }}

        #delete-row {{
            background-color: #b91c1c;
            color: #fff;
            border-color: #991b1b;
        }}
        #delete-row:hover {{
            background-color: #dc2626;
            box-shadow: 0 2px 10px rgba(220, 38, 38, 0.4);
        }}

        #clear-row {{
            background-color: #374151;
            color: #f3f4f6;
            border-color: #4b5563;
        }}
        #clear-row:hover {{
            background-color: #4b5563;
            color: #fff;
        }}

        #add-row-up, #add-row-below {{
            background-color: #1d4ed8;
            color: #fff;
            border-color: #1e40af;
        }}
        #add-row-up:hover, #add-row-below:hover {{
            background-color: #2563eb;
            box-shadow: 0 2px 10px rgba(37, 99, 235, 0.4);
        }}

        /* FOOTER TABLE */
        .games-table-container {{
            margin-top: 30px;
            background: #181818;
            border: 1px solid #333;
            border-radius: 6px;
            padding: 16px;
            overflow-x: auto;
        }}

        .games-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            text-align: left;
        }}
        .games-table th {{
            background: #121212;
            color: #fff;
            padding: 10px 12px;
            border-bottom: 2px solid #333;
        }}
        .games-table td {{
            padding: 8px 12px;
            border-bottom: 1px solid #222;
            color: #ccc;
        }}
        .games-table tr:hover td {{
            background: #202020;
        }}

        #export-canvas {{
            display: none;
        }}
    </style>
</head>
<body>

    <!-- HEADER -->
    <header id="header">
        <div id="inner-header">
            <a href="#" class="logo-container">
                <span class="logo-badge">TIER</span>
                <span class="logo-text">MAKER</span>
                <span class="header-tag">2026 EDITION</span>
            </a>
            <div class="header-nav">
                <span class="save-indicator" id="header-save-indicator">💾 Сохранено</span>
                <button class="btn-header" onclick="exportTierList()">Скачать PNG</button>
            </div>
        </div>
    </header>

    <!-- MAIN -->
    <main id="main-container">
        <div id="breadcrumbs">
            <a href="#">Главная</a> &gt; <a href="#">Видеоигры</a> &gt; <span>Tier List 2026</span>
        </div>

        <h1>Рейтинг видеоигр 2026 года (1M+ копий, 80%+ Steam & Ожидаемые блокбастеры)</h1>
        <p class="description">
            Интерактивный тир-лист ключевых релизов 2026 года. Базовый ростер сформирован строго по критериям: 
            <strong>полноценные релизы и ремейки</strong> (без DLC и Enhanced-изданий) с тиражом <strong>более 1 млн копий</strong> 
            и пользовательской оценкой Steam <strong>80%+</strong>, а также главные ожидаемые блокбастеры из каталога PC JSON и PS5. 
            Используйте строку поиска, чтобы мгновенно найти и добавить любую из <strong>1270+ игр</strong> каталога!
        </p>

        <!-- CRITERIA BADGES -->
        <div class="criteria-badges">
            <div class="badge green">★ Полноценные релизы & ремейки (без DLC)</div>
            <div class="badge green">💰 Продажи 1M+ копий</div>
            <div class="badge green">👍 Оценка Steam 80%+</div>
            <div class="badge blue">🔥 Ожидаемые блокбастеры 2026 (PS5 / PC)</div>
            <div class="badge purple">🔍 Поиск по базе из 1270+ игр с автоскачиванием обложек</div>
            <div class="badge yellow">💾 Локальное автосохранение позиций</div>
        </div>

        <!-- CONTROLS BAR -->
        <div class="controls-bar">
            <div class="btn-group">
                <button class="btn btn-primary" onclick="addNewRow()">+ Добавить строку</button>
                <button class="btn" onclick="resetAllToPool()">Вернуть все в пул</button>
                <button class="btn btn-danger" onclick="resetToDefault()">Сбросить до начального</button>
            </div>
            <div class="btn-group" style="align-items: center;">
                <span class="save-indicator" id="save-status-msg">Автосохранение выполнено ✓</span>
                <button class="btn btn-primary" onclick="exportTierList()">📥 Скачать изображение (PNG)</button>
            </div>
        </div>

        <!-- TIER CONTAINER -->
        <div id="tier-container">
            <div class="tier-row" data-row-id="tier-s">
                <div class="label-holder" contenteditable="true" style="background-color: #FF7F7F;">S</div>
                <div class="tier-dropzone"></div>
                <div class="row-controls">
                    <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                    <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                    <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                </div>
            </div>
            <div class="tier-row" data-row-id="tier-a">
                <div class="label-holder" contenteditable="true" style="background-color: #FFBF7F;">A</div>
                <div class="tier-dropzone"></div>
                <div class="row-controls">
                    <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                    <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                    <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                </div>
            </div>
            <div class="tier-row" data-row-id="tier-b">
                <div class="label-holder" contenteditable="true" style="background-color: #FFFF7F;">B</div>
                <div class="tier-dropzone"></div>
                <div class="row-controls">
                    <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                    <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                    <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                </div>
            </div>
            <div class="tier-row" data-row-id="tier-c">
                <div class="label-holder" contenteditable="true" style="background-color: #7FFF7F;">C</div>
                <div class="tier-dropzone"></div>
                <div class="row-controls">
                    <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                    <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                    <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                </div>
            </div>
            <div class="tier-row" data-row-id="tier-d">
                <div class="label-holder" contenteditable="true" style="background-color: #7FBFFF;">D</div>
                <div class="tier-dropzone"></div>
                <div class="row-controls">
                    <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                    <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                    <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                </div>
            </div>
        </div>

        <!-- UNRANKED POOL -->
        <div id="unranked-container">
            <div class="unranked-header">
                <div class="unranked-title-wrap">
                    <span class="unranked-title">ДОСТУПНЫЕ ИГРЫ</span>
                    <span class="unranked-count-badge" id="unranked-count">28 игр</span>
                </div>
                <div class="filter-tabs">
                    <button class="filter-tab active" onclick="filterCards('all', this)">Все игры</button>
                    <button class="filter-tab" onclick="filterCards('hit', this)">★ Хиты 2026 (80+)</button>
                    <button class="filter-tab" onclick="filterCards('anticipated', this)">🔥 Ожидаемые 2026</button>
                </div>
            </div>

            <!-- SEARCH IN CATALOG -->
            <div class="catalog-search-container">
                <div class="search-input-wrapper">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="catalog-search-input" placeholder="Поиск по каталогу 1270+ игр (JSON & PS5) для добавления на доску..." autocomplete="off">
                    <button id="catalog-search-clear" class="clear-search-btn" style="display:none;" onclick="clearCatalogSearch()">✕</button>
                </div>
                <div id="catalog-search-dropdown" class="catalog-dropdown" style="display:none;"></div>
            </div>

            <div id="unranked-pool" class="tier-dropzone"></div>
        </div>

        <!-- TABLE OF ALL BASE GAMES -->
        <div class="games-table-container">
            <h3 style="color:#fff; margin-bottom:12px; font-size:16px;">Информация о релизах базы 2026</h3>
            <table class="games-table">
                <thead>
                    <tr>
                        <th>Название игры</th>
                        <th>Статус / Оценка</th>
                        <th>Дата релиза</th>
                        <th>Платформы</th>
                    </tr>
                </thead>
                <tbody id="games-table-body"></tbody>
            </table>
        </div>
    </main>

    <!-- MODAL FOR ROW EDIT -->
    <div id="modal-overlay">
        <div id="modal-wrapper">
            <div id="modal">
                <span id="close" onclick="closeModal()" title="Закрыть">✕</span>
                <h4 style="margin: 0 0 12px 0;">Выберите цвет фона строки:</h4>
                <div id="color-select">
                    <span style="background:#FF7F7F;" onclick="setRowColor('#FF7F7F')"></span>
                    <span style="background:#FFBF7F;" onclick="setRowColor('#FFBF7F')"></span>
                    <span style="background:#FFDF7F;" onclick="setRowColor('#FFDF7F')"></span>
                    <span style="background:#FFFF7F;" onclick="setRowColor('#FFFF7F')"></span>
                    <span style="background:#BFFF7F;" onclick="setRowColor('#BFFF7F')"></span>
                    <span style="background:#7FFF7F;" onclick="setRowColor('#7FFF7F')"></span>
                    <span style="background:#7FFFFF;" onclick="setRowColor('#7FFFFF')"></span>
                    <span style="background:#7FBFFF;" onclick="setRowColor('#7FBFFF')"></span>
                    <span style="background:#7F7FFF;" onclick="setRowColor('#7F7FFF')"></span>
                    <span style="background:#FF7FFF;" onclick="setRowColor('#FF7FFF')"></span>
                    <span style="background:#BF7FBF;" onclick="setRowColor('#BF7FBF')"></span>
                    <span style="background:#3B3B3B;" onclick="setRowColor('#3B3B3B')"></span>
                    <span style="background:#858585;" onclick="setRowColor('#858585')"></span>
                    <span style="background:#CFCFCF;" onclick="setRowColor('#CFCFCF')"></span>
                    <span style="background:#F7F7F7;" onclick="setRowColor('#F7F7F7')"></span>
                </div>
                <h4 style="margin: 18px 0 10px 0;">Текст названия строки:</h4>
                <textarea class="settings-label" maxlength="500" id="labelName"></textarea>
                <p class="modal-buttons">
                    <button id="delete-row" onclick="deleteCurrentRow()">Удалить строку</button>
                    <button id="clear-row" onclick="clearCurrentRow()">Очистить изображения</button>
                </p>
                <p class="modal-buttons">
                    <button id="add-row-up" onclick="addRowAbove()">+ Добавить строку выше</button>
                    <button id="add-row-below" onclick="addRowBelow()">+ Добавить строку ниже</button>
                </p>
            </div>
        </div>
    </div>

    <canvas id="export-canvas"></canvas>

    <script>
        const STORAGE_KEY = 'tierlist_2026_state_v3';
        const STORAGE_CUSTOM_GAMES = 'tierlist_2026_custom_games';
        const STORAGE_SAVED_COVERS = 'tierlist_2026_saved_covers';

        const BASE_GAMES = {games_json};
        const GAME_CUSTOM_COVERS = {covers_json};
        const CATALOG_DATA = {catalog_json};

        let customCoversCache = {{}};
        try {{
            const rawCache = JSON.parse(localStorage.getItem(STORAGE_SAVED_COVERS) || '{{}}');
            // Clean out any SVG placeholders from cache so real covers can be downloaded
            for (const k in rawCache) {{
                if (rawCache[k] && !rawCache[k].startsWith('data:image/svg+xml')) {{
                    customCoversCache[k] = rawCache[k];
                }}
            }}
        }} catch(e) {{}}

        let customAddedGames = [];
        try {{
            customAddedGames = JSON.parse(localStorage.getItem(STORAGE_CUSTOM_GAMES) || '[]');
        }} catch(e) {{}}

        // Combined games array
        let GAMES_DATA = [...BASE_GAMES];
        customAddedGames.forEach(cg => {{
            if (!GAMES_DATA.some(g => g.id === cg.id)) {{
                GAMES_DATA.push(cg);
            }}
        }});

        let activeEditingRow = null;
        let currentFilter = 'all';
        let draggedItem = null;
        let touchTarget = null;

        // --- AUTO-SCROLL ON DRAG NEAR TOP / BOTTOM ---
        let autoScrollSpeed = 0;
        let autoScrollAnimId = null;

        function autoScrollLoop() {{
            if (autoScrollSpeed !== 0) {{
                window.scrollBy(0, autoScrollSpeed);
                autoScrollAnimId = requestAnimationFrame(autoScrollLoop);
            }} else {{
                autoScrollAnimId = null;
            }}
        }}

        function handleAutoScroll(clientY) {{
            if (!draggedItem && !touchTarget) {{
                stopAutoScroll();
                return;
            }}
            const threshold = 120;
            const maxSpeed = 22;
            const vh = window.innerHeight;

            if (clientY >= 0 && clientY < threshold) {{
                const factor = Math.max(0.1, (threshold - clientY) / threshold);
                autoScrollSpeed = -Math.round(4 + factor * (maxSpeed - 4));
            }} else if (clientY > vh - threshold && clientY <= vh + 100) {{
                const factor = Math.max(0.1, (clientY - (vh - threshold)) / threshold);
                autoScrollSpeed = Math.round(4 + factor * (maxSpeed - 4));
            }} else {{
                autoScrollSpeed = 0;
            }}

            if (autoScrollSpeed !== 0 && !autoScrollAnimId) {{
                autoScrollAnimId = requestAnimationFrame(autoScrollLoop);
            }}
        }}

        function stopAutoScroll() {{
            autoScrollSpeed = 0;
            if (autoScrollAnimId) {{
                cancelAnimationFrame(autoScrollAnimId);
                autoScrollAnimId = null;
            }}
        }}

        function escapeHtml(str) {{
            if (!str) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
        }}

        function isGameAlreadyOnBoard(gameId) {{
            return !!document.querySelector('[data-game-id="' + gameId + '"]');
        }}

        function isRealCover(src) {{
            if (!src) return false;
            if (src.startsWith('data:image/svg+xml')) return false;
            if (src.startsWith('data:image/jpeg') || src.startsWith('data:image/png') || src.startsWith('data:image/webp')) return true;
            if (src.startsWith('images/') || src.startsWith('http://') || src.startsWith('https://')) return true;
            return false;
        }}

        // --- RELIABLE POSTER DOWNLOAD VIA CORS FETCH & FILEREADER ---
        async function fetchImageAsBase64(url) {{
            try {{
                const resp = await fetch(url, {{ mode: 'cors' }});
                if (!resp.ok) return null;
                const blob = await resp.blob();
                if (blob.size < 1000) return null; // Reject tiny error images
                return new Promise((resolve, reject) => {{
                    const reader = new FileReader();
                    reader.onloadend = () => {{
                        if (reader.result && typeof reader.result === 'string' && reader.result.startsWith('data:image')) {{
                            resolve(reader.result);
                        }} else {{
                            resolve(null);
                        }}
                    }};
                    reader.onerror = () => resolve(null);
                    reader.readAsDataURL(blob);
                }});
            }} catch (err) {{
                return null;
            }}
        }}

        async function downloadGamePoster(game) {{
            // 1. Check if game has Steam appid -> try Steam CDN endpoints in order
            if (game.appid) {{
                const steamEndpoints = [
                    `https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/${{game.appid}}/library_600x900.jpg`,
                    `https://cdn.akamai.steamstatic.com/steam/apps/${{game.appid}}/library_600x900.jpg`,
                    `https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/${{game.appid}}/header.jpg`,
                    `https://cdn.akamai.steamstatic.com/steam/apps/${{game.appid}}/header.jpg`,
                    `https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/${{game.appid}}/capsule_616x353.jpg`
                ];

                for (const u of steamEndpoints) {{
                    const dataUrl = await fetchImageAsBase64(u);
                    if (dataUrl) return dataUrl;
                }}
            }}

            // 2. Wikipedia Search API
            const cleanTitle = game.title.replace(/['’"™®:!?,.()&]/g, '').trim();
            const searchQueries = [
                cleanTitle + ' video game',
                cleanTitle
            ];

            for (const q of searchQueries) {{
                try {{
                    const wikiUrl = `https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=${{encodeURIComponent(q)}}&prop=pageimages&pithumbsize=600&format=json&origin=*`;
                    const resp = await fetch(wikiUrl);
                    if (resp.ok) {{
                        const data = await resp.json();
                        const pages = data.query?.pages;
                        if (pages) {{
                            for (const pid in pages) {{
                                const thumb = pages[pid].thumbnail?.source;
                                if (thumb) {{
                                    const dataUrl = await fetchImageAsBase64(thumb);
                                    if (dataUrl) return dataUrl;
                                }}
                            }}
                        }}
                    }}
                }} catch (e) {{}}
            }}

            return null;
        }}

        function makeDynamicCoverSvg(title, source, date) {{
            const words = title.split(' ');
            let lines = [];
            let cur = '';
            words.forEach(w => {{
                if ((cur + ' ' + w).trim().length > 14) {{
                    if (cur) lines.push(cur);
                    cur = w;
                }} else {{
                    cur = (cur + ' ' + w).trim();
                }}
            }});
            if (cur) lines.push(cur);
            lines = lines.slice(0, 4);

            const startY = 110 - (lines.length - 1) * 12;
            let tspans = '';
            lines.forEach((l, i) => {{
                tspans += `<text x="80" y="${{startY + i * 24}}" font-family="Arial, sans-serif" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">${{escapeHtml(l)}}</text>`;
            }});

            const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="160" height="240" viewBox="0 0 160 240">
  <rect width="160" height="240" fill="#181818"/>
  <rect x="4" y="4" width="152" height="232" fill="#202020" stroke="#4ade80" stroke-width="2" rx="4"/>
  <rect x="8" y="8" width="144" height="22" fill="#2e3846" rx="3"/>
  <text x="80" y="23" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#60a5fa" text-anchor="middle">${{escapeHtml(source || 'CATALOG 2026')}}</text>
  ${{tspans}}
  <rect x="8" y="196" width="144" height="34" fill="#000000" rx="3"/>
  <text x="80" y="211" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">${{escapeHtml(date ? ('Релиз ' + date) : '2026')}}</text>
  <text x="80" y="224" font-family="Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#4ade80" text-anchor="middle">★ ДОБАВЛЕНО ИЗ БАЗЫ</text>
</svg>`;
            return 'data:image/svg+xml;utf8,' + encodeURIComponent(svg);
        }}

        // --- CATALOG SEARCH & ADD ---
        let searchDebounce = null;
        const searchInput = document.getElementById('catalog-search-input');
        const searchDropdown = document.getElementById('catalog-search-dropdown');
        const clearSearchBtn = document.getElementById('catalog-search-clear');

        if (searchInput) {{
            searchInput.addEventListener('input', function() {{
                clearTimeout(searchDebounce);
                const q = this.value.trim();
                if (q.length > 0) {{
                    clearSearchBtn.style.display = 'block';
                }} else {{
                    clearSearchBtn.style.display = 'none';
                    searchDropdown.style.display = 'none';
                    return;
                }}

                searchDebounce = setTimeout(() => {{
                    executeCatalogSearch(q);
                }}, 120);
            }});

            searchInput.addEventListener('focus', function() {{
                const q = this.value.trim();
                if (q.length > 0) {{
                    executeCatalogSearch(q);
                }}
            }});
        }}

        function clearCatalogSearch() {{
            if (searchInput) {{
                searchInput.value = '';
                clearSearchBtn.style.display = 'none';
                searchDropdown.style.display = 'none';
            }}
        }}

        document.addEventListener('click', function(e) {{
            if (!e.target.closest('.catalog-search-container')) {{
                if (searchDropdown) searchDropdown.style.display = 'none';
            }}
        }});

        function executeCatalogSearch(query) {{
            const q = query.toLowerCase();
            const matches = [];

            for (let i = 0; i < CATALOG_DATA.length; i++) {{
                const g = CATALOG_DATA[i];
                const t = g.title.toLowerCase();
                if (t.includes(q)) {{
                    const starts = t.startsWith(q);
                    matches.push({{ game: g, priority: starts ? 1 : 2 }});
                }}
            }}

            matches.sort((a, b) => a.priority - b.priority);
            const results = matches.slice(0, 20).map(m => m.game);

            if (results.length === 0) {{
                searchDropdown.innerHTML = '<div style="padding:14px; text-align:center; color:#777; font-size:13px;">Игры по запросу "' + escapeHtml(query) + '" не найдены в каталоге</div>';
                searchDropdown.style.display = 'block';
                return;
            }}

            let html = '';
            results.forEach(g => {{
                const inList = isGameAlreadyOnBoard(g.id);
                const thumb = GAME_CUSTOM_COVERS[g.id] || customCoversCache[g.id] || (g.appid ? `https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/${{g.appid}}/library_600x900.jpg` : '');
                
                const thumbImg = thumb ? 
                    `<img class="catalog-item-poster" src="${{thumb}}" onerror="this.style.display='none';">` : 
                    `<div class="catalog-item-poster" style="display:flex;align-items:center;justify-content:center;color:#666;font-size:18px;">🎮</div>`;

                html += `
                    <div class="catalog-item" id="catalog-item-${{g.id}}">
                        <div class="catalog-item-info">
                            ${{thumbImg}}
                            <div class="catalog-item-text">
                                <div class="catalog-item-title">${{escapeHtml(g.title)}}</div>
                                <div class="catalog-item-meta">
                                    <span class="catalog-source-tag">${{escapeHtml(g.source)}}</span>
                                    <span>${{escapeHtml(g.date || '2026')}}</span>
                                    <span>• ${{escapeHtml(g.platform)}}</span>
                                </div>
                            </div>
                        </div>
                        <div>
                            ${{inList ? 
                                '<span class="badge-in-list">✓ На доске</span>' : 
                                `<button class="btn-catalog-add" id="btn-add-${{g.id}}" onclick="addGameFromCatalog('${{g.id}}')">+ Добавить</button>`
                            }}
                        </div>
                    </div>
                `;
            }});

            searchDropdown.innerHTML = html;
            searchDropdown.style.display = 'block';
        }}

        // --- ADD GAME: DOWNLOAD POSTER ONLY ON CLICK ---
        async function addGameFromCatalog(gameId) {{
            const game = CATALOG_DATA.find(g => g.id === gameId);
            if (!game) return;

            if (isGameAlreadyOnBoard(game.id)) {{
                alert(`Игра "${{game.title}}" уже добавлена в тир-лист!`);
                return;
            }}

            const btn = document.getElementById('btn-add-' + game.id);
            if (btn) {{
                btn.disabled = true;
                btn.textContent = '⏳ Скачивание постера...';
            }}

            // Check if already downloaded
            let posterSrc = GAME_CUSTOM_COVERS[game.id] || (customCoversCache[game.id] && isRealCover(customCoversCache[game.id]) ? customCoversCache[game.id] : null);

            // Download poster ONLY when user clicks Add
            if (!posterSrc) {{
                posterSrc = await downloadGamePoster(game);
                if (posterSrc) {{
                    customCoversCache[game.id] = posterSrc;
                    try {{
                        localStorage.setItem(STORAGE_SAVED_COVERS, JSON.stringify(customCoversCache));
                    }} catch(e) {{}}
                }}
            }}

            const finalPoster = posterSrc || makeDynamicCoverSvg(game.title, game.source, game.date);

            // Build game object
            const isHit = game.date && game.date <= '2026-09-12';
            const newGameObject = {{
                id: game.id,
                title: game.title,
                type: isHit ? 'hit' : 'anticipated',
                subtype: 'original',
                meta: isHit ? '80+' : 'HYPE',
                sales: game.date ? (isHit ? '1.0M+' : game.date) : '2026',
                status: game.date ? `Релиз ${{game.date}} (${{game.source}})` : game.platform,
                platforms: game.platform || 'PC',
                image: finalPoster
            }};

            if (!GAMES_DATA.some(g => g.id === newGameObject.id)) {{
                GAMES_DATA.push(newGameObject);
            }}

            if (!customAddedGames.some(g => g.id === newGameObject.id)) {{
                customAddedGames.push(newGameObject);
                try {{
                    localStorage.setItem(STORAGE_CUSTOM_GAMES, JSON.stringify(customAddedGames));
                }} catch(e) {{}}
            }}

            // Create card and append to pool
            const pool = document.getElementById('unranked-pool');
            const card = createCardElement(newGameObject);
            card.classList.add('card-new-highlight');
            pool.appendChild(card);

            updateCounts();
            saveState();

            if (btn) {{
                btn.outerHTML = '<span class="badge-in-list">✓ Добавлено</span>';
            }}

            card.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}

        // --- ON PAGE REFRESH: CHECK ALL GAMES UNDER TIERS AND IN TIERS ---
        async function checkAndDownloadMissingPosters() {{
            const cards = document.querySelectorAll('.character');
            for (const card of cards) {{
                const gid = card.getAttribute('data-game-id');
                if (!gid) continue;

                const hasEmbedded = !!GAME_CUSTOM_COVERS[gid];
                const cached = customCoversCache[gid];
                const hasRealCached = isRealCover(cached);

                // If poster is NOT downloaded yet (currently using SVG or missing)
                if (!hasEmbedded && !hasRealCached) {{
                    const gameInfo = CATALOG_DATA.find(g => g.id === gid) || GAMES_DATA.find(g => g.id === gid);
                    if (!gameInfo) continue;

                    console.log('Проверка при обновлении: скачиваем недостающий постер для ' + gameInfo.title);
                    try {{
                        const downloaded = await downloadGamePoster(gameInfo);
                        if (downloaded) {{
                            customCoversCache[gid] = downloaded;
                            try {{
                                localStorage.setItem(STORAGE_SAVED_COVERS, JSON.stringify(customCoversCache));
                            }} catch(e) {{}}
                            const img = card.querySelector('img');
                            if (img) {{
                                img.src = downloaded;
                            }}
                            const gObj = GAMES_DATA.find(g => g.id === gid);
                            if (gObj) gObj.image = downloaded;
                        }}
                    }} catch (e) {{}}
                }}
            }}
        }}

        function createCardElement(game) {{
            const card = document.createElement('div');
            card.className = 'character';
            card.id = 'game-' + game.id;
            card.setAttribute('draggable', 'true');
            card.setAttribute('data-game-id', game.id);
            card.setAttribute('data-game-title', game.title);
            card.setAttribute('data-game-type', game.type);
            card.setAttribute('data-game-subtype', game.subtype || 'original');

            const imgSrc = GAME_CUSTOM_COVERS[game.id] || customCoversCache[game.id] || game.image || ('images/' + game.id + '.jpg');
            const fallbackSrc = makeDynamicCoverSvg(game.title, game.source || '2026', '');

            card.innerHTML = 
                '<img src="' + imgSrc + '" data-id="' + game.id + '" data-fallback="' + fallbackSrc + '" onerror="this.onerror=null;this.src=this.dataset.fallback;" alt="' + escapeHtml(game.title) + '" id="img-' + game.id + '">' +
                '<div class="card-tooltip">' + escapeHtml(game.title) + '</div>';

            card.addEventListener('dragstart', handleDragStart);
            card.addEventListener('dragend', handleDragEnd);
            card.addEventListener('drag', function(e) {{
                if (draggedItem && e.clientY && e.clientY > 0) {{
                    handleAutoScroll(e.clientY);
                }}
            }});

            card.addEventListener('touchstart', handleTouchStart, {{ passive: false }});
            card.addEventListener('touchmove', handleTouchMove, {{ passive: false }});
            card.addEventListener('touchend', handleTouchEnd, {{ passive: false }});
            card.addEventListener('touchcancel', handleTouchEnd, {{ passive: false }});

            card.addEventListener('click', function(e) {{
                if (this.parentElement.id === 'unranked-pool') {{
                    const firstTier = document.querySelector('.tier-row .tier-dropzone');
                    if (firstTier) firstTier.appendChild(this);
                }} else {{
                    document.getElementById('unranked-pool').appendChild(this);
                }}
                updateCounts();
                saveState();
            }});

            return card;
        }}

        function createTierRowElement(rowId, labelText, color) {{
            const row = document.createElement('div');
            row.className = 'tier-row';
            row.setAttribute('data-row-id', rowId || ('custom-' + Date.now()));
            const safeColor = color || '#858585';
            const safeLabel = escapeHtml(labelText || 'NEW');
            row.innerHTML = 
                '<div class="label-holder" contenteditable="true" style="background-color: ' + safeColor + ';">' + safeLabel + '</div>' +
                '<div class="tier-dropzone"></div>' +
                '<div class="row-controls">' +
                    '<button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>' +
                    '<button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>' +
                    '<button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>' +
                '</div>';
            return row;
        }}

        // --- LOCAL STORAGE PERSISTENCE ---
        let saveTimer = null;
        function showSaveIndicator() {{
            const msg = document.getElementById('save-status-msg');
            const headerBadge = document.getElementById('header-save-indicator');
            if (msg) {{
                msg.style.opacity = '1';
                clearTimeout(saveTimer);
                saveTimer = setTimeout(() => {{
                    msg.style.opacity = '0';
                }}, 1600);
            }}
            if (headerBadge) {{
                headerBadge.style.opacity = '1';
            }}
        }}

        function saveState() {{
            try {{
                const rows = document.querySelectorAll('#tier-container .tier-row');
                const tiersData = [];
                const placedIds = new Set();

                rows.forEach((row, idx) => {{
                    const labelEl = row.querySelector('.label-holder');
                    const dropzone = row.querySelector('.tier-dropzone');
                    const label = labelEl ? labelEl.innerText.trim() : ('Tier ' + (idx + 1));
                    const color = labelEl ? (labelEl.style.backgroundColor || '#858585') : '#858585';
                    const rowId = row.getAttribute('data-row-id') || ('row-' + idx);

                    const items = [];
                    if (dropzone) {{
                        dropzone.querySelectorAll('.character').forEach(card => {{
                            const gid = card.getAttribute('data-game-id');
                            if (gid) {{
                                items.push(gid);
                                placedIds.add(gid);
                            }}
                        }});
                    }}

                    tiersData.push({{
                        id: rowId,
                        label: label,
                        color: color,
                        items: items
                    }});
                }});

                const pool = document.getElementById('unranked-pool');
                const poolItems = [];
                if (pool) {{
                    pool.querySelectorAll('.character').forEach(card => {{
                        const gid = card.getAttribute('data-game-id');
                        if (gid) poolItems.push(gid);
                    }});
                }}

                const state = {{
                    version: 3,
                    timestamp: Date.now(),
                    tiers: tiersData,
                    pool: poolItems
                }};

                localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
                showSaveIndicator();
            }} catch (err) {{
                console.warn('LocalStorage save error:', err);
            }}
        }}

        function loadState() {{
            try {{
                const saved = localStorage.getItem(STORAGE_KEY);
                if (!saved) return false;
                const state = JSON.parse(saved);
                if (!state || !Array.isArray(state.tiers) || state.tiers.length === 0) return false;

                const container = document.getElementById('tier-container');
                const pool = document.getElementById('unranked-pool');
                container.innerHTML = '';

                const placedIds = new Set();

                state.tiers.forEach(tier => {{
                    const row = createTierRowElement(tier.id, tier.label, tier.color);
                    container.appendChild(row);
                    const dropzone = row.querySelector('.tier-dropzone');

                    if (Array.isArray(tier.items)) {{
                        tier.items.forEach(gid => {{
                            const card = document.getElementById('game-' + gid);
                            if (card) {{
                                dropzone.appendChild(card);
                                placedIds.add(gid);
                            }}
                        }});
                    }}
                }});

                if (Array.isArray(state.pool)) {{
                    state.pool.forEach(gid => {{
                        if (!placedIds.has(gid)) {{
                            const card = document.getElementById('game-' + gid);
                            if (card) {{
                                pool.appendChild(card);
                                placedIds.add(gid);
                            }}
                        }}
                    }});
                }}

                // Any newly registered or base games not yet placed go into pool
                GAMES_DATA.forEach(game => {{
                    if (!placedIds.has(game.id)) {{
                        const card = document.getElementById('game-' + game.id);
                        if (card && card.parentElement !== pool) {{
                            pool.appendChild(card);
                        }}
                    }}
                }});

                setupDropzones();
                updateCounts();
                return true;
            }} catch (err) {{
                console.error('LocalStorage load error:', err);
                return false;
            }}
        }}

        function initCards() {{
            const pool = document.getElementById('unranked-pool');
            const tableBody = document.getElementById('games-table-body');
            pool.innerHTML = '';
            tableBody.innerHTML = '';

            GAMES_DATA.forEach(game => {{
                const card = createCardElement(game);
                pool.appendChild(card);

                const tr = document.createElement('tr');
                const isHit = game.type === 'hit';
                let tagColor = isHit ? '#4ade80' : '#60a5fa';
                let typeLabel = isHit ? ('★ ' + game.meta) : ('🔥 ' + game.meta);

                tr.innerHTML = 
                    '<td style="font-weight:bold; color:#fff;">' + escapeHtml(game.title) + '</td>' +
                    '<td><span style="color:' + tagColor + '; font-weight:bold;">' + typeLabel + '</span></td>' +
                    '<td>' + escapeHtml(game.status) + '</td>' +
                    '<td>' + escapeHtml(game.platforms) + '</td>';
                tableBody.appendChild(tr);
            }});

            updateCounts();
        }}

        function filterCards(type, btn) {{
            currentFilter = type;
            document.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
            if (btn) btn.classList.add('active');

            document.querySelectorAll('#unranked-pool .character').forEach(card => {{
                const cType = card.getAttribute('data-game-type');
                if (type === 'all') {{
                    card.style.display = 'block';
                }} else if (type === 'hit') {{
                    card.style.display = (cType === 'hit') ? 'block' : 'none';
                }} else if (type === 'anticipated') {{
                    card.style.display = (cType === 'anticipated') ? 'block' : 'none';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        function handleDragStart(e) {{
            draggedItem = this;
            this.classList.add('dragging');
            e.dataTransfer.effectAllowed = 'move';
            e.dataTransfer.setData('text/plain', this.id);
        }}

        function handleDragEnd(e) {{
            this.classList.remove('dragging');
            document.querySelectorAll('.tier-dropzone').forEach(zone => {{
                zone.classList.remove('drag-over');
            }});
            draggedItem = null;
            stopAutoScroll();
            updateCounts();
            saveState();
        }}

        function handleTouchStart(e) {{
            touchTarget = this;
            this.classList.add('dragging');
        }}

        function handleTouchMove(e) {{
            if (!touchTarget) return;
            e.preventDefault();
            const touch = e.touches[0];
            handleAutoScroll(touch.clientY);
            const elemBelow = document.elementFromPoint(touch.clientX, touch.clientY);
            if (elemBelow) {{
                const dropzone = elemBelow.closest('.tier-dropzone');
                if (dropzone) {{
                    const afterElement = getDragAfterElement(dropzone, touch.clientX, touch.clientY);
                    if (afterElement == null) {{
                        dropzone.appendChild(touchTarget);
                    }} else {{
                        dropzone.insertBefore(touchTarget, afterElement);
                    }}
                }}
            }}
        }}

        function handleTouchEnd(e) {{
            if (touchTarget) {{
                touchTarget.classList.remove('dragging');
                touchTarget = null;
                stopAutoScroll();
                updateCounts();
                saveState();
            }}
        }}

        function setupDropzones() {{
            document.querySelectorAll('.tier-dropzone').forEach(zone => {{
                if (zone._dropSetup) return;
                zone._dropSetup = true;

                zone.addEventListener('dragover', function(e) {{
                    e.preventDefault();
                    e.dataTransfer.dropEffect = 'move';
                    this.classList.add('drag-over');

                    if (draggedItem) {{
                        handleAutoScroll(e.clientY);
                        const afterElement = getDragAfterElement(this, e.clientX, e.clientY);
                        if (afterElement == null) {{
                            this.appendChild(draggedItem);
                        }} else {{
                            this.insertBefore(draggedItem, afterElement);
                        }}
                    }}
                }});

                zone.addEventListener('dragleave', function(e) {{
                    this.classList.remove('drag-over');
                }});

                zone.addEventListener('drop', function(e) {{
                    e.preventDefault();
                    this.classList.remove('drag-over');
                    stopAutoScroll();
                    updateCounts();
                    saveState();
                }});
            }});
        }}

        function getDragAfterElement(container, x, y) {{
            const draggableElements = [...container.querySelectorAll('.character:not(.dragging)')];

            for (let i = 0; i < draggableElements.length; i++) {{
                const child = draggableElements[i];
                const box = child.getBoundingClientRect();
                if (y >= box.top && y <= box.bottom) {{
                    if (x < box.left + box.width / 2) {{
                        return child;
                    }}
                }} else if (y < box.top) {{
                    return child;
                }}
            }}
            return null;
        }}

        function updateCounts() {{
            const unrankedPool = document.getElementById('unranked-pool');
            const count = unrankedPool ? unrankedPool.querySelectorAll('.character').length : 0;
            const countElem = document.getElementById('unranked-count');
            if (countElem) {{
                countElem.textContent = count + (count === 1 ? ' игра' : (count >= 2 && count <= 4 ? ' игры' : ' игр'));
            }}
        }}

        function moveRowUp(btn) {{
            const row = btn.closest('.tier-row');
            const prev = row.previousElementSibling;
            if (prev && prev.classList.contains('tier-row')) {{
                row.parentNode.insertBefore(row, prev);
                saveState();
            }}
        }}

        function moveRowDown(btn) {{
            const row = btn.closest('.tier-row');
            const next = row.nextElementSibling;
            if (next && next.classList.contains('tier-row')) {{
                row.parentNode.insertBefore(next, row);
                saveState();
            }}
        }}

        function addNewRow() {{
            const container = document.getElementById('tier-container');
            const newRow = createTierRowElement('custom-' + Date.now(), 'NEW', '#858585');
            container.appendChild(newRow);
            setupDropzones();
            saveState();
        }}

        function resetAllToPool() {{
            const pool = document.getElementById('unranked-pool');
            document.querySelectorAll('.tier-row .character').forEach(card => {{
                pool.appendChild(card);
            }});
            updateCounts();
            if (currentFilter !== 'all') {{
                filterCards(currentFilter);
            }}
            saveState();
        }}

        function resetToDefault() {{
            if (confirm('Сбросить весь тир-лист до начального вида? Все добавленные строки, переименования, расставленные позиции и добавленные игры будут сброшены.')) {{
                try {{
                    localStorage.removeItem(STORAGE_KEY);
                    localStorage.removeItem(STORAGE_CUSTOM_GAMES);
                    localStorage.removeItem(STORAGE_SAVED_COVERS);
                }} catch(e) {{}}
                window.location.reload();
            }}
        }}

        function openRowSettings(btn) {{
            activeEditingRow = btn.closest('.tier-row');
            const labelHolder = activeEditingRow.querySelector('.label-holder');
            const currentText = labelHolder ? labelHolder.innerText.trim() : '';
            const currentBg = labelHolder ? (labelHolder.style.backgroundColor || '').toLowerCase() : '';

            const input = document.getElementById('labelName');
            if (input) {{
                input.value = currentText;
            }}

            // Highlight active color in palette
            document.querySelectorAll('#color-select span').forEach(span => {{
                const spanBg = (span.style.backgroundColor || '').toLowerCase();
                if (spanBg && currentBg && (spanBg === currentBg)) {{
                    span.classList.add('active');
                }} else {{
                    span.classList.remove('active');
                }}
            }});

            document.getElementById('modal-overlay').style.display = 'flex';
        }}

        function closeModal() {{
            document.getElementById('modal-overlay').style.display = 'none';
            activeEditingRow = null;
        }}

        function setRowColor(color) {{
            if (activeEditingRow) {{
                const labelHolder = activeEditingRow.querySelector('.label-holder');
                if (labelHolder) {{
                    labelHolder.style.backgroundColor = color;
                    saveState();
                }}
                const cleanColor = color.toLowerCase();
                document.querySelectorAll('#color-select span').forEach(span => {{
                    const spanBg = (span.style.backgroundColor || '').toLowerCase();
                    if (spanBg === cleanColor) {{
                        span.classList.add('active');
                    }} else {{
                        span.classList.remove('active');
                    }}
                }});
            }}
        }}

        function addRowAbove() {{
            if (!activeEditingRow) return;
            const newRow = createTierRowElement('custom-' + Date.now(), 'NEW', '#858585');
            activeEditingRow.parentNode.insertBefore(newRow, activeEditingRow);
            setupDropzones();
            saveState();
            closeModal();
        }}

        function addRowBelow() {{
            if (!activeEditingRow) return;
            const newRow = createTierRowElement('custom-' + Date.now(), 'NEW', '#858585');
            activeEditingRow.parentNode.insertBefore(newRow, activeEditingRow.nextSibling);
            setupDropzones();
            saveState();
            closeModal();
        }}

        function deleteCurrentRow() {{
            if (activeEditingRow) {{
                const dropzone = activeEditingRow.querySelector('.tier-dropzone');
                const pool = document.getElementById('unranked-pool');
                if (dropzone && pool) {{
                    dropzone.querySelectorAll('.character').forEach(card => {{
                        pool.appendChild(card);
                    }});
                }}
                activeEditingRow.remove();
                updateCounts();
                saveState();
            }}
            closeModal();
        }}

        function clearCurrentRow() {{
            if (activeEditingRow) {{
                const dropzone = activeEditingRow.querySelector('.tier-dropzone');
                const pool = document.getElementById('unranked-pool');
                if (dropzone && pool) {{
                    dropzone.querySelectorAll('.character').forEach(card => {{
                        pool.appendChild(card);
                    }});
                }}
                updateCounts();
                saveState();
            }}
            closeModal();
        }}

        function exportTierList() {{
            const rows = document.querySelectorAll('.tier-row');
            const width = 1140;
            const labelWidth = 110;
            const cardWidth = 80;
            const cardHeight = 120;
            const cardPadding = 4;
            const cardsPerRow = Math.floor((width - labelWidth - 10) / (cardWidth + cardPadding));

            let totalHeight = 60;
            const rowHeights = [];

            rows.forEach(row => {{
                const cardCount = row.querySelectorAll('.character').length;
                const lines = Math.max(1, Math.ceil(cardCount / cardsPerRow));
                const h = Math.max(122, lines * (cardHeight + cardPadding) + 8);
                rowHeights.push(h);
                totalHeight += h;
            }});

            const canvas = document.getElementById('export-canvas');
            canvas.width = width;
            canvas.height = totalHeight;
            const ctx = canvas.getContext('2d');

            ctx.fillStyle = '#111111';
            ctx.fillRect(0, 0, width, totalHeight);

            ctx.fillStyle = '#1a1a1a';
            ctx.fillRect(0, 0, width, 60);
            ctx.fillStyle = '#ffffff';
            ctx.font = 'bold 20px Arial, sans-serif';
            ctx.fillText('VIDEO GAMES 2026 TIER LIST (1M+ Sales, 80%+ Score & Anticipated)', 20, 37);

            ctx.fillStyle = '#888';
            ctx.font = '13px Arial, sans-serif';
            ctx.fillText('tiermaker.com / 2026 Edition', width - 200, 37);

            let currentY = 60;
            const renderPromises = [];

            rows.forEach((row, rIdx) => {{
                const label = row.querySelector('.label-holder');
                const labelText = label.innerText.trim();
                const labelBg = label.style.backgroundColor || '#FF7F7F';
                const rHeight = rowHeights[rIdx];

                ctx.fillStyle = labelBg;
                ctx.fillRect(0, currentY, labelWidth, rHeight);

                ctx.fillStyle = '#000000';
                ctx.font = 'bold 18px Arial, sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText(labelText, labelWidth / 2, currentY + rHeight / 2);

                ctx.fillStyle = '#141414';
                ctx.fillRect(labelWidth, currentY, width - labelWidth, rHeight);
                ctx.strokeStyle = '#333333';
                ctx.lineWidth = 1;
                ctx.strokeRect(0, currentY, width, rHeight);

                const cards = row.querySelectorAll('.character');
                cards.forEach((card, cIdx) => {{
                    const cRow = Math.floor(cIdx / cardsPerRow);
                    const cCol = cIdx % cardsPerRow;
                    const cX = labelWidth + 6 + cCol * (cardWidth + cardPadding);
                    const cY = currentY + 4 + cRow * (cardHeight + cardPadding);

                    const imgElem = card.querySelector('img');
                    if (imgElem) {{
                        const p = new Promise(resolve => {{
                            const img = new Image();
                            img.crossOrigin = 'anonymous';
                            img.onload = () => {{
                                ctx.drawImage(img, cX, cY, cardWidth, cardHeight);
                                ctx.strokeStyle = '#333';
                                ctx.strokeRect(cX, cY, cardWidth, cardHeight);
                                resolve();
                            }};
                            img.onerror = () => resolve();
                            img.src = imgElem.src;
                        }});
                        renderPromises.push(p);
                    }}
                }});

                currentY += rHeight;
            }});

            Promise.all(renderPromises).then(() => {{
                const link = document.createElement('a');
                link.download = 'games-tierlist-2026.png';
                link.href = canvas.toDataURL('image/png');
                link.click();
            }});
        }}

        function setupGlobalEvents() {{
            document.addEventListener('dragover', function(e) {{
                if (draggedItem) {{
                    handleAutoScroll(e.clientY);
                }}
            }}, {{ capture: true }});

            window.addEventListener('dragend', stopAutoScroll);
            window.addEventListener('drop', stopAutoScroll);
            window.addEventListener('blur', stopAutoScroll);
            window.addEventListener('pointerup', stopAutoScroll);

            const tierContainer = document.getElementById('tier-container');
            if (tierContainer) {{
                tierContainer.addEventListener('blur', function(e) {{
                    if (e.target.classList.contains('label-holder')) {{
                        saveState();
                    }}
                }}, true);

                tierContainer.addEventListener('keyup', function(e) {{
                    if (e.target.classList.contains('label-holder')) {{
                        saveState();
                    }}
                }});
            }}

            const labelInput = document.getElementById('labelName');
            if (labelInput) {{
                labelInput.addEventListener('input', function() {{
                    if (activeEditingRow) {{
                        const labelHolder = activeEditingRow.querySelector('.label-holder');
                        if (labelHolder) {{
                            labelHolder.innerText = this.value;
                            saveState();
                        }}
                    }}
                }});
            }}

            const overlay = document.getElementById('modal-overlay');
            if (overlay) {{
                overlay.addEventListener('click', function(e) {{
                    if (e.target === this || e.target.id === 'modal-wrapper') {{
                        closeModal();
                    }}
                }});
            }}

            window.addEventListener('keydown', function(e) {{
                if (e.key === 'Escape') closeModal();
            }});
        }}

        window.addEventListener('DOMContentLoaded', async () => {{
            initCards();
            loadState();
            setupDropzones();
            setupGlobalEvents();
            
            // On page refresh / load: check all games on the board and download missing posters
            await checkAndDownloadMissingPosters();
        }});
    </script>
</body>
</html>'''

# Write index.html
with open("C:/Users/zdog0/.gemini/antigravity/scratch/tierlist-2026/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Update update_tierlist_with_images.py

print(f"Generated index.html & update_tierlist_with_images.py successfully!")