import os from datetime
import datetime, timezone

os.makedirs("public", exist_ok=True)
html_content = f"""<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <title>CI/CD Sandbox Dashboard</title> <style> body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 40px; background: #f6f8fa; }} 
.card {{ background: white; padding: 24px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }} h1 {{ color: #0969da; }}
 .status {{ display: inline-block; padding: 4px 12px; background: #dafbe1; color: #1a7f37; border-radius: 20px; font-weight: bold; }} 
 </style> </head> <body> <div class="card"> <h1>Deployment Verification Dashboard</h1> <p><span class="status">Pipeline Active</span></p> 
 <p>This page was generated and deployed automatically via GitHub Actions.</p> 
 <p><strong>Deployment Timestamp:</strong> {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}</p> </div> </body> </html> 
 """
with open("public/index.html", "w") as f:
    f.write(html_content)
    print("Documentation dashboard generated inside public/index.html")