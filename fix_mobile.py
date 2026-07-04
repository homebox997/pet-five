# -*- coding: utf-8 -*-
import os

# Mobile responsive CSS to add to all 3 HTML files
MOBILE_CSS = """
        /* Mobile responsive - stack header and make nav hamburger style */
        @media (max-width: 768px) {
            .header-inner { flex-direction: column; gap: 1rem; text-align: center; }
            .logo { font-size: 1.3rem; }
            .nav { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.5rem; width: 100%; }
            .nav a { margin-left: 0; font-size: 0.9rem; padding: 6px 12px; }
            .hero h1 { font-size: 1.8rem !important; }
            .hero p { font-size: 0.95rem !important; }
            .features-grid, .topics-grid { grid-template-columns: 1fr !important; }
            .community-stats { flex-wrap: wrap; gap: 1rem !important; }
            .stat-num { font-size: 1.5rem !important; }
            .container { padding: 0 12px !important; }
        }
        @media (max-width: 480px) {
            .logo { font-size: 1.1rem; }
            .nav a { font-size: 0.8rem; padding: 5px 10px; }
        }"""

files = ['index.html', 'community.html', 'ai-check.html']
for fname in files:
    fpath = os.path.join('D:\\temp\\pet-five', fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has mobile CSS
    if '@media (max-width: 768px)' in content:
        print(f"SKIP: {fname} already has mobile CSS")
        continue
    
    # Insert mobile CSS right before </style>
    new_content = content.replace('    </style>', MOBILE_CSS + '\n    </style>')
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"OK: {fname} - added mobile responsive CSS")

print("\nDone! All 3 files now have mobile responsive layout.")
