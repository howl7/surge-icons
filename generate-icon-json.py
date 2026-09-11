#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Surge / Loon 策略组图标库 JSON 自动构建脚本
自动扫描 icons/ 目录下的分类与 PNG 文件，生成标准 surge-icon.json。
"""

import os
import json
import argparse

def generate_surge_icon_json(icons_dir, repo, branch, name, description, out_path, use_cdn=True):
    icons_list = []
    
    # 按照目录字母序排序分类
    categories = sorted([d for d in os.listdir(icons_dir) if os.path.isdir(os.path.join(icons_dir, d)) and not d.startswith(".")])
    
    # 如果没有子目录，则直接扫描 icons_dir 根目录，分类默认 General
    if not categories:
        categories = ["General"]
        scan_map = {"General": icons_dir}
    else:
        scan_map = {c: os.path.join(icons_dir, c) for c in categories}
        
    for cat, dir_path in scan_map.items():
        files = sorted([f for f in os.listdir(dir_path) if f.lower().endswith(".png") and not f.startswith(".")])
        for filename in files:
            icon_name = os.path.splitext(filename)[0]
            rel_path = f"icons/{cat}/{filename}" if cat != "General" and dir_path != icons_dir else f"icons/{filename}"
            
            if use_cdn:
                url = f"https://cdn.jsdelivr.net/gh/{repo}@{branch}/{rel_path}"
            else:
                url = f"https://raw.githubusercontent.com/{repo}/{branch}/{rel_path}"
                
            icons_list.append({
                "name": icon_name,
                "category": cat,
                "url": url
            })
            
    payload = {
        "name": name,
        "description": description,
        "icons": icons_list
    }
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
        
    print(f"✅ 成功生成图标库配置文件: {out_path}")
    print(f"   总收录图标: {len(icons_list)} 个，涵盖分类: {len(categories)} 个")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate surge-icon.json for Surge / Loon icon set")
    parser.add_argument("--repo", default="howl/surge-icons", help="GitHub repo in format username/reponame")
    parser.add_argument("--branch", default="main", help="Git branch (default: main)")
    parser.add_argument("--name", default="Custom-Surge-Icons", help="Icon set display name")
    parser.add_argument("--desc", default="个人定制高精 Retina 正圆策略组图标库", help="Icon set description")
    parser.add_argument("--icons-dir", default="icons", help="Path to icons directory")
    parser.add_argument("--out", default="surge-icon.json", help="Output JSON path")
    parser.add_argument("--raw", action="store_true", help="Use GitHub raw url instead of jsDelivr CDN")
    
    args = parser.parse_args()
    generate_surge_icon_json(
        icons_dir=args.icons_dir,
        repo=args.repo,
        branch=args.branch,
        name=args.name,
        description=args.desc,
        out_path=args.out,
        use_cdn=not args.raw
    )
