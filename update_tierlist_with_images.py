import os
import base64
import json
import html
import urllib.parse

games = [
    # --- ALREADY RELEASED HITS (80+ METACRITIC & 1M+ SALES, ORIGINAL 2026 RELEASES) ---
    {
        "id": "forza-horizon-6",
        "title": "Forza Horizon 6",
        "type": "hit",
        "meta": "91",
        "sales": "6.4M+",
        "status": "Вышла 19 мая 2026",
        "platforms": "PC, Xbox Series X/S",
        "lines": ["FORZA", "HORIZON 6"]
    },
    {
        "id": "resident-evil-requiem",
        "title": "Resident Evil Requiem",
        "type": "hit",
        "meta": "89",
        "sales": "6.0M+",
        "status": "Вышла 27 фев 2026",
        "platforms": "PC, PS5, XSX, Switch 2",
        "lines": ["RESIDENT", "EVIL", "REQUIEM"]
    },
    {
        "id": "007-first-light",
        "title": "007 First Light",
        "type": "hit",
        "meta": "87",
        "sales": "4.0M+",
        "status": "Вышла 26 мая 2026",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["007", "FIRST LIGHT"]
    },
    {
        "id": "pragmata",
        "title": "Pragmata",
        "type": "hit",
        "meta": "85",
        "sales": "2.5M+",
        "status": "Вышла 17 апр 2026",
        "platforms": "PC, PS5, XSX, Switch 2",
        "lines": ["PRAGMATA"]
    },
    {
        "id": "pokemon-pokopia",
        "title": "Pokémon Pokopia",
        "type": "hit",
        "meta": "89",
        "sales": "2.2M+",
        "status": "Вышла 5 мар 2026",
        "platforms": "Nintendo Switch 2",
        "lines": ["POKÉMON", "POKOPIA"]
    },
    {
        "id": "college-football-27",
        "title": "EA Sports College Football 27",
        "type": "hit",
        "meta": "84",
        "sales": "2.5M+",
        "status": "Вышла 9 июл 2026",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["EA SPORTS", "COLLEGE", "FOOTBALL 27"]
    },
    {
        "id": "lego-batman",
        "title": "LEGO Batman: Legacy of the Dark Knight",
        "type": "hit",
        "meta": "84",
        "sales": "1.2M+",
        "status": "Вышла 22 мая 2026",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["LEGO BATMAN", "LEGACY OF", "DARK KNIGHT"]
    },
    {
        "id": "halo-campaign-evolved",
        "title": "Halo: Campaign Evolved",
        "type": "hit",
        "meta": "81",
        "sales": "1.2M+",
        "status": "Вышла 28 июл 2026",
        "platforms": "PC, XSX, PS5",
        "lines": ["HALO", "CAMPAIGN", "EVOLVED"]
    },
    {
        "id": "marvel-tokon",
        "title": "MARVEL Tōkon: Fighting Souls",
        "type": "hit",
        "meta": "82",
        "sales": "1.0M+",
        "status": "Вышла 6 авг 2026",
        "platforms": "PC, PlayStation 5",
        "lines": ["MARVEL TŌKON", "FIGHTING SOULS"]
    },
    {
        "id": "nioh-3",
        "title": "Nioh 3",
        "type": "hit",
        "meta": "86",
        "sales": "1.0M+",
        "status": "Вышла 6 фев 2026",
        "platforms": "PC, PlayStation 5",
        "lines": ["NIOH 3"]
    },
    {
        "id": "mewgenics",
        "title": "Mewgenics",
        "type": "hit",
        "meta": "89",
        "sales": "1.0M+",
        "status": "Вышла 10 фев 2026",
        "platforms": "PC, PS5, XSX, Switch 2",
        "lines": ["MEWGENICS"]
    },
    {
        "id": "the-blood-of-dawnwalker",
        "title": "The Blood of Dawnwalker",
        "type": "hit",
        "meta": "83",
        "sales": "1.0M+",
        "status": "Вышла 3 сен 2026",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["THE BLOOD OF", "DAWNWALKER"]
    },
    {
        "id": "onimusha-way-of-the-sword",
        "title": "Onimusha: Way of the Sword",
        "type": "hit",
        "meta": "85",
        "sales": "1.0M+",
        "status": "Вышла 4 сен 2026",
        "platforms": "PC, PS5, XSX, Switch 2",
        "lines": ["ONIMUSHA", "WAY OF THE", "SWORD"]
    },
    {
        "id": "reanimal",
        "title": "Reanimal",
        "type": "hit",
        "meta": "80",
        "sales": "1.0M+",
        "status": "Вышла 13 фев 2026",
        "platforms": "PC, PS5, XSX, Switch 2",
        "lines": ["REANIMAL"]
    },

    # --- MOST ANTICIPATED & UPCOMING BLOCKBUSTERS OF 2026 (ORIGINAL GAMES) ---
    {
        "id": "gta-vi",
        "title": "Grand Theft Auto VI",
        "type": "anticipated",
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
        "meta": "HYPE 98",
        "sales": "15 Сентября 2026",
        "status": "Релиз 15 сентября 2026 (Insomniac)",
        "platforms": "PlayStation 5",
        "lines": ["MARVEL'S", "WOLVERINE"]
    },
    {
        "id": "control-resonant",
        "title": "Control Resonant",
        "type": "anticipated",
        "meta": "HYPE 94",
        "sales": "24 Сентября 2026",
        "status": "Релиз 24 сентября 2026 (Remedy)",
        "platforms": "PC, PS5, XSX, Mac",
        "lines": ["CONTROL", "RESONANT"]
    },
    {
        "id": "silent-hill-townfall",
        "title": "Silent Hill: Townfall",
        "type": "anticipated",
        "meta": "HYPE 93",
        "sales": "24 Сентября 2026",
        "status": "Релиз 24 сентября 2026 (Konami)",
        "platforms": "PC, PlayStation 5",
        "lines": ["SILENT HILL", "TOWNFALL"]
    },
    {
        "id": "ea-sports-fc-27",
        "title": "EA Sports FC 27",
        "type": "anticipated",
        "meta": "HYPE 92",
        "sales": "24 Сентября 2026",
        "status": "Релиз 24 сентября 2026 (EA)",
        "platforms": "PC, PS5, XSX, Switch 2",
        "lines": ["EA SPORTS", "FC 27"]
    },
    {
        "id": "ace-combat-8",
        "title": "Ace Combat 8: Wings of Theve",
        "type": "anticipated",
        "meta": "HYPE 91",
        "sales": "2 Октября 2026",
        "status": "Релиз 2 октября 2026 (Bandai Namco)",
        "platforms": "PC, PS5, Xbox Series X/S",
        "lines": ["ACE COMBAT 8", "WINGS OF THEVE"]
    },
    {
        "id": "gears-of-war-e-day",
        "title": "Gears of War: E-Day",
        "type": "anticipated",
        "meta": "HYPE 96",
        "sales": "6 Октября 2026",
        "status": "Релиз 6 октября 2026 (Xbox Studios)",
        "platforms": "PC, Xbox Series X/S",
        "lines": ["GEARS OF WAR", "E-DAY"]
    },
    {
        "id": "star-wars-galactic-racer",
        "title": "Star Wars: Galactic Racer",
        "type": "anticipated",
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
        "meta": "HYPE 92",
        "sales": "15 Октября 2026",
        "status": "Релиз 15 октября 2026 (Konami)",
        "platforms": "PC, PS5, XSX, Switch",
        "lines": ["CASTLEVANIA", "BELMONT'S", "CURSE"]
    },
    {
        "id": "cod-modern-warfare-4",
        "title": "Call of Duty: Modern Warfare 4",
        "type": "anticipated",
        "meta": "HYPE 95",
        "sales": "23 Октября 2026",
        "status": "Релиз 23 октября 2026 (Activision)",
        "platforms": "PC, PS5, XSX, Switch 2",
        "lines": ["CALL OF DUTY", "MODERN", "WARFARE 4"]
    },
    {
        "id": "phantom-blade-zero",
        "title": "Phantom Blade Zero",
        "type": "anticipated",
        "meta": "HYPE 94",
        "sales": "29 Октября 2026",
        "status": "Релиз 29 октября 2026 (S-Game)",
        "platforms": "PC, PlayStation 5",
        "lines": ["PHANTOM", "BLADE ZERO"]
    },
    {
        "id": "zelda-ocarina-of-time",
        "title": "The Legend of Zelda: Ocarina of Time (2026)",
        "type": "anticipated",
        "meta": "HYPE 99",
        "sales": "5 Ноября 2026",
        "status": "Релиз 5 ноября 2026 (Nintendo)",
        "platforms": "Nintendo Switch 2",
        "lines": ["ZELDA", "OCARINA OF", "TIME 2026"]
    },
    {
        "id": "warhammer-dawn-of-war-4",
        "title": "Warhammer 40,000: Dawn of War IV",
        "type": "anticipated",
        "meta": "HYPE 91",
        "sales": "3 Декабря 2026",
        "status": "Релиз 3 декабря 2026 (Sega / Relic)",
        "platforms": "PC",
        "lines": ["WARHAMMER", "DAWN OF", "WAR IV"]
    },
    {
        "id": "professor-layton-steam",
        "title": "Professor Layton & the New World of Steam",
        "type": "anticipated",
        "meta": "HYPE 90",
        "sales": "10 Декабря 2026",
        "status": "Релиз 10 декабря 2026 (Level-5)",
        "platforms": "Nintendo Switch 2, Switch",
        "lines": ["PROFESSOR", "LAYTON", "STEAM"]
    }
]

images_dir = "C:/Users/zdog0/.gemini/antigravity/scratch/tierlist-2026/images"
custom_covers = {}

matched_count = 0
for g in games:
    gid = g["id"]
    for ext in [".jpg", ".png", ".webp", ".jpeg"]:
        img_path = os.path.join(images_dir, f"{gid}{ext}")
        if os.path.exists(img_path):
            with open(img_path, "rb") as f:
                data = f.read()
                mime = "image/png" if data[:8] == b"\x89PNG\r\n\x1a\n" else "image/jpeg"
                b64 = base64.b64encode(data).decode("utf-8")
                custom_covers[gid] = f"data:{mime};base64,{b64}"
                matched_count += 1
                break

print(f"Matched {matched_count} of {len(games)} images!")

def make_svg(game):
    lines = game["lines"]
    line_count = len(lines)
    start_y = 118 - (line_count - 1) * 13
    text_tspans = ""
    for i, line in enumerate(lines):
        y = start_y + i * 25
        text_tspans += f'<text x="80" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="900" fill="#000000" text-anchor="middle" letter-spacing="0.2">{html.escape(line)}</text>\\n'

    is_hit = game.get("type") == "hit"
    top_badge_bg = "#f2f2f2" if is_hit else "#fef3c7"
    top_badge_color = "#444444" if is_hit else "#b45309"
    top_badge_text = "★ 2026 HIT ★" if is_hit else "🔥 ANTICIPATED"

    bottom_bg = "#000000" if is_hit else "#1e3a8a"
    sub1 = f"META: {game['meta']}" if is_hit else "COMING SOON"
    sub2 = f"{game['sales']} COPIES" if is_hit else f"{game['sales']}"
    sub2_color = "#4ade80" if is_hit else "#fbbf24"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="240" viewBox="0 0 160 240">
  <rect width="160" height="240" fill="#ffffff"/>
  <rect x="4" y="4" width="152" height="232" fill="#ffffff" stroke="#000000" stroke-width="2.5" rx="3"/>
  <rect x="8" y="8" width="144" height="22" fill="{top_badge_bg}" rx="2"/>
  <text x="80" y="23" font-family="Arial, Helvetica, sans-serif" font-size="9" font-weight="900" fill="{top_badge_color}" text-anchor="middle" letter-spacing="1">{top_badge_text}</text>
  
  {text_tspans}
  
  <rect x="8" y="196" width="144" height="34" fill="{bottom_bg}" rx="3"/>
  <text x="80" y="211" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">{sub1}</text>
  <text x="80" y="224" font-family="Arial, Helvetica, sans-serif" font-size="9" font-weight="bold" fill="{sub2_color}" text-anchor="middle">{sub2}</text>
</svg>'''
    
    encoded = urllib.parse.quote(svg)
    return f"data:image/svg+xml;utf8,{encoded}"

for g in games:
    g["image"] = make_svg(g)

hits_count = sum(1 for g in games if g["type"] == "hit")
antic_count = sum(1 for g in games if g["type"] == "anticipated")
total_count = len(games)

covers_json = json.dumps(custom_covers)
games_json = json.dumps(games, ensure_ascii=False)

html_template = f'''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Games TierList 2026 (Hits & Most Anticipated) - TierMaker</title>
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

        /* TIER LIST TABLE */
        #tier-wrap {{
            width: 100%;
            background: #000;
            border: 2px solid #333;
            border-radius: 4px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            margin-bottom: 25px;
        }}

        .tier-row {{
            display: flex;
            min-height: 122px;
            border-bottom: 1px solid #333;
            background-color: #1a1a1a;
            position: relative;
        }}

        .tier-row:last-child {{
            border-bottom: none;
        }}

        .label-holder {{
            width: 105px;
            min-width: 105px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 8px;
            font-weight: 800;
            font-size: 18px;
            color: #000;
            cursor: pointer;
            outline: none;
            user-select: none;
            word-break: break-word;
            transition: filter 0.15s;
        }}
        .label-holder:hover {{
            filter: brightness(1.05);
        }}

        .tier-dropzone {{
            flex-grow: 1;
            display: flex;
            flex-wrap: wrap;
            align-content: flex-start;
            padding: 4px;
            gap: 4px;
            min-height: 122px;
            background: #141414;
            transition: background-color 0.2s;
        }}

        .tier-dropzone.drag-over {{
            background-color: #242424;
            outline: 2px dashed #7fbfff;
            outline-offset: -2px;
        }}

        .row-controls {{
            width: 44px;
            background: #202020;
            border-left: 1px solid #333;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            align-items: center;
            padding: 6px 0;
            user-select: none;
        }}

        .row-btn {{
            background: none;
            border: none;
            color: #888;
            cursor: pointer;
            font-size: 13px;
            padding: 4px;
            border-radius: 4px;
            transition: 0.15s;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 28px;
            height: 28px;
        }}

        .row-btn:hover {{
            color: #fff;
            background: #333;
        }}

        /* GAME CARDS */
        .character {{
            width: 80px;
            height: 120px;
            border-radius: 3px;
            overflow: hidden;
            cursor: grab;
            user-select: none;
            background-color: #111;
            position: relative;
            box-shadow: 0 2px 6px rgba(0,0,0,0.5);
            transition: transform 0.12s, box-shadow 0.12s;
            flex-shrink: 0;
        }}

        .character:active {{
            cursor: grabbing;
        }}

        .character:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.8);
        }}

        .character.dragging {{
            opacity: 0.35;
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
            font-size: 9px;
            padding: 3px 4px;
            text-align: center;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            opacity: 0;
            transition: opacity 0.2s;
            pointer-events: none;
        }}
        .character:hover .card-tooltip {{
            opacity: 1;
        }}

        /* FILTER TABS */
        .filter-tabs {{
            display: flex;
            gap: 8px;
            margin-bottom: 12px;
        }}
        .filter-tab {{
            background: #242222;
            color: #bbb;
            border: 1px solid #444;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 12px;
            cursor: pointer;
            transition: 0.2s;
        }}
        .filter-tab.active, .filter-tab:hover {{
            background: #3a5795;
            color: #fff;
            border-color: #7fbfff;
        }}

        /* POOL AREA */
        #pool-container {{
            background: #1a1a1a;
            border: 1px solid #333;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 25px;
        }}

        .pool-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid #2a2a2a;
        }}

        .pool-title {{
            font-size: 15px;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .pool-count {{
            background: #333;
            color: #aaa;
            font-size: 12px;
            padding: 2px 8px;
            border-radius: 10px;
        }}

        #unranked-pool {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            min-height: 130px;
            background: #111;
            padding: 10px;
            border-radius: 4px;
            border: 1px dashed #444;
            align-content: flex-start;
        }}

        #unranked-pool.drag-over {{
            background: #1e1e1e;
            border-color: #7fbfff;
        }}

        /* BUTTONS */
        .actions-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            justify-content: center;
            margin: 15px 0 35px;
        }}

        .btn-action {{
            background: #242222;
            color: #fff;
            border: 1px solid #666;
            padding: 10px 22px;
            font-size: 15px;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }}
        .btn-action:hover {{
            background: #333;
            border-color: #888;
        }}
        .btn-action.primary {{
            background: #3a5795;
            border-color: #4a6bb5;
        }}
        .btn-action.primary:hover {{
            background: #476bb8;
        }}
        .btn-action.danger {{
            background: #7f1d1d;
            border-color: #991b1b;
        }}
        .btn-action.danger:hover {{
            background: #991b1b;
        }}

        /* MODAL */
        #modal-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0,0,0,0.8);
            display: none;
            justify-content: center;
            align-items: center;
            z-index: 2000;
            backdrop-filter: blur(2px);
        }}

        #modal-box {{
            background: #242323;
            border: 1px solid #555;
            border-radius: 8px;
            padding: 24px;
            width: 90%;
            max-width: 450px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8);
            position: relative;
        }}

        #modal-close {{
            position: absolute;
            top: 15px;
            right: 18px;
            background: none;
            border: none;
            color: #fff;
            font-size: 20px;
            cursor: pointer;
        }}

        .color-palette {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 8px;
            margin: 14px 0;
        }}

        .color-swatch {{
            width: 100%;
            height: 36px;
            border-radius: 4px;
            cursor: pointer;
            border: 2px solid transparent;
            transition: transform 0.12s;
        }}
        .color-swatch:hover {{
            transform: scale(1.08);
            border-color: #fff;
        }}

        .modal-input {{
            width: 100%;
            padding: 10px 12px;
            background: #181818;
            border: 1px solid #555;
            color: #fff;
            font-size: 15px;
            border-radius: 4px;
            margin: 10px 0 18px 0;
        }}

        .modal-footer {{
            display: flex;
            gap: 8px;
            justify-content: flex-end;
        }}

        /* TABLE */
        .info-panel {{
            background: #1c1c1c;
            border: 1px solid #333;
            border-radius: 6px;
            padding: 20px;
            margin-top: 20px;
        }}
        .info-panel h3 {{
            color: #fff;
            font-size: 18px;
            margin-bottom: 12px;
        }}
        .info-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}
        .info-table th, .info-table td {{
            padding: 9px 12px;
            text-align: left;
            border-bottom: 1px solid #2a2a2a;
        }}
        .info-table th {{
            color: #fff;
            background: #242424;
        }}
        .info-table td {{
            color: #ccc;
        }}
        .info-table tr:hover {{
            background: #222;
        }}
    </style>
</head>
<body>

    <div id="header">
        <div id="inner-header">
            <a href="#" class="logo-container">
                <span class="logo-badge">TIER</span>
                <span class="logo-text">MAKER</span>
                <span class="header-tag">2026 EDITION</span>
            </a>
            <div class="header-nav">
                <span id="header-save-indicator" style="font-size: 12px; color: #4ade80; display: inline-flex; align-items: center; gap: 5px; background: rgba(74,222,128,0.1); border: 1px solid rgba(74,222,128,0.25); padding: 4px 10px; border-radius: 6px;">
                    <span style="display:inline-block; width:7px; height:7px; border-radius:50%; background:#4ade80; box-shadow: 0 0 5px #4ade80;"></span>
                    Автосохранение
                </span>
                <button class="btn-header" onclick="resetAllToPool()">Вернуть в пул</button>
                <button class="btn-header" style="background:#10b981;" onclick="exportTierList()">📸 Скачать PNG</button>
            </div>
        </div>
    </div>

    <div id="main-container">
        
        <div id="breadcrumbs">
            <a href="#">Video Games</a> / <span>Video Games TierList (2026: Original Hits & Most Anticipated)</span> /
        </div>

        <h1>Video Games TierList 2026 (Original Releases & Anticipated Blockbusters)</h1>
        <p class="description">
            Интерактивный Tier List главных оригинальных релизов 2026 года (все переиздания и порты исключены). 
            Включает вышедшие суперхиты (80+ Metacritic и 1M+ продаж) и самые ожидаемые новинки от ведущих игровых студий.
        </p>

        <div class="criteria-badges">
            <span class="badge green">🏆 Вышедшие хиты 2026 года: 80+ Metacritic и 1M+ продаж</span>
            <span class="badge blue">🔥 Самые ожидаемые новые игры конца 2026</span>
            <span class="badge">🚫 Без портов с предыдущих лет / консолей</span>
        </div>

        <!-- TIER LIST BOARD -->
        <div id="tier-wrap">
            <div id="tier-container">

                <div class="tier-row" data-row-id="s-plus">
                    <div class="label-holder" contenteditable="true" style="background-color: #FF7F7F;">S+</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

                <div class="tier-row" data-row-id="s">
                    <div class="label-holder" contenteditable="true" style="background-color: #FFBF7F;">S</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

                <div class="tier-row" data-row-id="a">
                    <div class="label-holder" contenteditable="true" style="background-color: #FFDF7F;">A</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

                <div class="tier-row" data-row-id="b">
                    <div class="label-holder" contenteditable="true" style="background-color: #FFFF7F;">B</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

                <div class="tier-row" data-row-id="c">
                    <div class="label-holder" contenteditable="true" style="background-color: #BFFF7F;">C</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

                <div class="tier-row" data-row-id="d">
                    <div class="label-holder" contenteditable="true" style="background-color: #7FFF7F;">D</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

                <div class="tier-row" data-row-id="wanna-play">
                    <div class="label-holder" contenteditable="true" style="background-color: #7F7FFF;">Wanna Play</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

                <div class="tier-row" data-row-id="dont-know">
                    <div class="label-holder" contenteditable="true" style="background-color: #FF7FFF;">Dont Know</div>
                    <div class="tier-dropzone"></div>
                    <div class="row-controls">
                        <button class="row-btn" onclick="openRowSettings(this)" title="Настройки">⚙️</button>
                        <button class="row-btn" onclick="moveRowUp(this)" title="Вверх">▲</button>
                        <button class="row-btn" onclick="moveRowDown(this)" title="Вниз">▼</button>
                    </div>
                </div>

            </div>
        </div>

        <!-- UNRANKED POOL -->
        <div id="pool-container">
            <div class="pool-header">
                <div class="pool-title">
                    <span>🎮 Доступные игры (в пуле):</span>
                    <span class="pool-count" id="unranked-count">{total_count} игр</span>
                    <span id="save-status-msg" style="font-size:12px; color:#4ade80; margin-left:12px; opacity:0; transition:opacity 0.3s; font-weight:normal;">💾 Позиции сохранены в браузере</span>
                </div>
                <div style="display:flex; gap:10px; align-items:center;">
                    <button class="btn-action" style="padding: 4px 12px; font-size: 12px;" onclick="resetAllToPool()">Вернуть все в пул</button>
                </div>
            </div>

            <div class="filter-tabs">
                <button class="filter-tab active" onclick="filterCards('all', this)">Все ({total_count})</button>
                <button class="filter-tab" onclick="filterCards('hit', this)">🏆 Вышедшие хиты ({hits_count})</button>
                <button class="filter-tab" onclick="filterCards('anticipated', this)">🔥 Самые ожидаемые ({antic_count})</button>
            </div>
            
            <div id="unranked-pool" class="tier-dropzone">
                <!-- CARDS INSERTED VIA JAVASCRIPT -->
            </div>
        </div>

        <!-- ACTION BUTTONS -->
        <div class="actions-bar">
            <button class="btn-action primary" onclick="exportTierList()">📸 Сохранить / Скачать изображение</button>
            <button class="btn-action" onclick="addNewRow()">➕ Добавить строку</button>
            <button class="btn-action" onclick="resetAllToPool()">🔄 Вернуть всё в пул</button>
            <button class="btn-action danger" onclick="resetToDefault()" style="background:#7f1d1d; border-color:#991b1b;">↺ Сбросить до начального вида</button>
        </div>

        <!-- INFO TABLE ABOUT THE GAMES -->
        <div class="info-panel">
            <h3>📊 Список всех {total_count} ключевых оригинальных игр 2026 года</h3>
            <table class="info-table">
                <thead>
                    <tr>
                        <th>Игра</th>
                        <th>Категория / Рейтинг</th>
                        <th>Статус / Продажи</th>
                        <th>Платформы</th>
                    </tr>
                </thead>
                <tbody id="games-table-body">
                    <!-- POPULATED VIA JS -->
                </tbody>
            </table>
        </div>

    </div>

    <!-- ROW SETTINGS MODAL -->
    <div id="modal-overlay" onclick="if(event.target===this) closeModal()">
        <div id="modal-box">
            <button id="modal-close" onclick="closeModal()">✕</button>
            <h3 style="color:#fff; margin-bottom:10px;">Настройка строки тира</h3>
            
            <p style="font-size:13px; color:#aaa; margin-bottom:6px;">Название тира:</p>
            <input type="text" id="modal-label-input" class="modal-input" placeholder="Название тира...">

            <p style="font-size:13px; color:#aaa; margin-bottom:6px;">Цвет фона ярлыка:</p>
            <div class="color-palette">
                <div class="color-swatch" style="background:#FF7F7F" onclick="setRowColor('#FF7F7F')"></div>
                <div class="color-swatch" style="background:#FFBF7F" onclick="setRowColor('#FFBF7F')"></div>
                <div class="color-swatch" style="background:#FFDF7F" onclick="setRowColor('#FFDF7F')"></div>
                <div class="color-swatch" style="background:#FFFF7F" onclick="setRowColor('#FFFF7F')"></div>
                <div class="color-swatch" style="background:#BFFF7F" onclick="setRowColor('#BFFF7F')"></div>
                <div class="color-swatch" style="background:#7FFF7F" onclick="setRowColor('#7FFF7F')"></div>
                <div class="color-swatch" style="background:#7FFFFF" onclick="setRowColor('#7FFFFF')"></div>
                <div class="color-swatch" style="background:#7FBFFF" onclick="setRowColor('#7FBFFF')"></div>
                <div class="color-swatch" style="background:#7F7FFF" onclick="setRowColor('#7F7FFF')"></div>
                <div class="color-swatch" style="background:#FF7FFF" onclick="setRowColor('#FF7FFF')"></div>
                <div class="color-swatch" style="background:#BF7FBF" onclick="setRowColor('#BF7FBF')"></div>
                <div class="color-swatch" style="background:#3B3B3B" onclick="setRowColor('#3B3B3B')"></div>
                <div class="color-swatch" style="background:#858585" onclick="setRowColor('#858585')"></div>
                <div class="color-swatch" style="background:#CFCFCF" onclick="setRowColor('#CFCFCF')"></div>
                <div class="color-swatch" style="background:#F7F7F7" onclick="setRowColor('#F7F7F7')"></div>
            </div>

            <div class="modal-footer" style="margin-top:20px;">
                <button class="btn-action danger" onclick="deleteCurrentRow()">Удалить строку</button>
                <button class="btn-action" onclick="clearCurrentRow()">Очистить строку</button>
                <button class="btn-action primary" onclick="saveRowSettings()">Сохранить</button>
            </div>
        </div>
    </div>

    <canvas id="export-canvas" style="display: none;"></canvas>

    <script>
        const GAMES_DATA = {games_json};
        const GAME_CUSTOM_COVERS = {covers_json};
        const STORAGE_KEY = 'video_games_tierlist_2026_save_v1';

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

            const threshold = 120; // px from top or bottom of viewport
            const maxSpeed = 22;   // max pixels to scroll per frame
            const vh = window.innerHeight;

            if (clientY >= 0 && clientY < threshold) {{
                // Closer to top -> faster scroll up
                const factor = Math.max(0.1, (threshold - clientY) / threshold);
                autoScrollSpeed = -Math.round(4 + factor * (maxSpeed - 4));
            }} else if (clientY > vh - threshold && clientY <= vh + 100) {{
                // Closer to bottom -> faster scroll down
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

        // --- HTML HELPER ---
        function escapeHtml(str) {{
            if (!str) return '';
            return String(str)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
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
                    version: 1,
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

                // Ensure any newly added games from site updates appear in pool
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
                const card = document.createElement('div');
                card.className = 'character';
                card.id = 'game-' + game.id;
                card.setAttribute('draggable', 'true');
                card.setAttribute('data-game-id', game.id);
                card.setAttribute('data-game-title', game.title);
                card.setAttribute('data-game-type', game.type);

                const imgSrc = GAME_CUSTOM_COVERS[game.id] || ('images/' + game.id + '.jpg');
                
                card.innerHTML = 
                    '<img src="' + imgSrc + '" data-id="' + game.id + '" data-fallback="' + game.image + '" onerror="this.onerror=null;this.src=this.dataset.fallback;" alt="' + escapeHtml(game.title) + '" id="img-' + game.id + '">' +
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

                pool.appendChild(card);

                const tr = document.createElement('tr');
                const isHit = game.type === 'hit';
                const tagColor = isHit ? '#4ade80' : '#60a5fa';
                const typeLabel = isHit ? ('★ ' + game.meta) : ('🔥 Ожидается (' + game.meta + ')');
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
                if (type === 'all' || cType === type) {{
                    card.style.display = 'block';
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

            for (const child of draggableElements) {{
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
            if (confirm('Сбросить весь тир-лист до начального вида? Все добавленные строки, переименования и расставленные позиции будут удалены из памяти браузера.')) {{
                try {{
                    localStorage.removeItem(STORAGE_KEY);
                }} catch(e) {{}}
                window.location.reload();
            }}
        }}

        function openRowSettings(btn) {{
            activeEditingRow = btn.closest('.tier-row');
            const labelHolder = activeEditingRow.querySelector('.label-holder');
            document.getElementById('modal-label-input').value = labelHolder.innerText.trim();
            document.getElementById('modal-overlay').style.display = 'flex';
        }}

        function closeModal() {{
            document.getElementById('modal-overlay').style.display = 'none';
            activeEditingRow = null;
        }}

        function setRowColor(color) {{
            if (activeEditingRow) {{
                const labelHolder = activeEditingRow.querySelector('.label-holder');
                labelHolder.style.backgroundColor = color;
                saveState();
            }}
        }}

        function saveRowSettings() {{
            if (activeEditingRow) {{
                const labelHolder = activeEditingRow.querySelector('.label-holder');
                const newText = document.getElementById('modal-label-input').value.trim();
                if (newText) {{
                    labelHolder.innerText = newText;
                }}
                saveState();
            }}
            closeModal();
        }}

        function deleteCurrentRow() {{
            if (activeEditingRow) {{
                const dropzone = activeEditingRow.querySelector('.tier-dropzone');
                const pool = document.getElementById('unranked-pool');
                dropzone.querySelectorAll('.character').forEach(card => {{
                    pool.appendChild(card);
                }});
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
                dropzone.querySelectorAll('.character').forEach(card => {{
                    pool.appendChild(card);
                }});
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
            ctx.fillText('VIDEO GAMES 2026 TIER LIST (Original Hits & Anticipated)', 20, 37);

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
            // Auto-scroll when dragging anywhere on the page
            document.addEventListener('dragover', function(e) {{
                if (draggedItem) {{
                    handleAutoScroll(e.clientY);
                }}
            }}, {{ capture: true }});

            window.addEventListener('dragend', stopAutoScroll);
            window.addEventListener('drop', stopAutoScroll);
            window.addEventListener('blur', stopAutoScroll);
            window.addEventListener('pointerup', stopAutoScroll);

            // Auto-save on label edit
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
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            initCards();
            loadState();
            setupDropzones();
            setupGlobalEvents();
        }});
    </script>
</body>
</html>'''

with open("C:/Users/zdog0/.gemini/antigravity/scratch/tierlist-2026/index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated index.html without ports! Total games: {total_count} ({hits_count} hits, {antic_count} anticipated). All {matched_count} images embedded.")
