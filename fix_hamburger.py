# -*- coding: utf-8 -*-
import os, re

# New CSS: hamburger menu for mobile, horizontal nav for desktop
NEW_MOBILE_CSS = """
        /* Hamburger menu - hidden on desktop */
        .hamburger { display: none; background: none; border: none; font-size: 1.8rem; cursor: pointer; color: #2c3e50; padding: 4px 10px; }
        /* Mobile responsive */
        @media (max-width: 768px) {
            .header-inner { flex-direction: row; justify-content: space-between; align-items: center; position: relative; }
            .hamburger { display: block; }
            .nav { display: none; flex-direction: column; position: absolute; top: 100%; right: 0; left: 0; background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); padding: 1rem; gap: 0.5rem; z-index: 100; border-radius: 0 0 12px 12px; }
            .nav.open { display: flex; }
            .nav a { margin-left: 0; text-align: center; padding: 10px; width: 100%; }
            .hero h1 { font-size: 1.8rem !important; }
            .hero p { font-size: 0.95rem !important; }
            .features-grid, .topics-grid { grid-template-columns: 1fr !important; }
            .community-stats { flex-wrap: wrap; gap: 1rem !important; }
            .stat-num { font-size: 1.5rem !important; }
            .container { padding: 0 12px !important; }
        }"""

# JavaScript for hamburger toggle
HAMBURGER_JS = """
    <script>
        function toggleMenu() {
            document.querySelector('.nav').classList.toggle('open');
        }
    </script>
</body>
</html>"""

files = ['index.html', 'community.html', 'ai-check.html']
for fname in files:
    fpath = os.path.join('D:\\temp\\pet-five', fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old mobile CSS (between </style> and the </style> tag, remove everything from /* Mobile responsive to end)
    content = re.sub(r'\n        /\* Mobile responsive.*?</style>', '\n    </style>', content, flags=re.DOTALL)
    
    # Add new mobile CSS before </style>
    content = content.replace('    </style>', NEW_MOBILE_CSS + '\n    </style>')
    
    # Add hamburger button in header (before nav)
    # The pattern: <nav class="nav">
    content = content.replace('<nav class="nav">', '<button class="hamburger" onclick="toggleMenu()">&#9776;</button>\n                <nav class="nav">')
    
    # Replace closing </body></html> with script + closing tags
    content = re.sub(r'</body>\s*</html>\s*$', HAMBURGER_JS, content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"OK: {fname} - hamburger menu added")

print("\nDone! All 3 files now have working hamburger menu.")
