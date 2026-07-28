import os
import cv2
import numpy as np

def generate_vector_svg(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} file not found!")
        return

    # 1. Image ko load karo aur grayscale me convert karo
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    # 2. Resize karo (taaki SVG bohot heavy na ho aur size perfect rahe)
    max_width = 240
    h, w = img.shape
    ratio = max_width / w
    new_w, new_h = int(w * ratio), int(h * ratio)
    img = cv2.resize(img, (new_w, new_h))

    # 3. Noise kam karne ke liye blur aur fir Canny Edge Detection (Lines nikalne ke liye)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, threshold1=40, threshold2=120)

    # 4. Lines (Contours) dhoondo
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # 5. Terminal ka size set karo
    term_w = new_w + 60
    term_h = new_h + 80

    svg_parts = []
    svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {term_w} {term_h}" width="100%" height="100%">')
    
    # --- CSS for Self-Drawing Animation ---
    svg_parts.append('  <style>')
    svg_parts.append('    .terminal-bg { fill: #0d1117; }')
    svg_parts.append('    .terminal-header { fill: #161b22; }')
    svg_parts.append('    .dot-red { fill: #ff5f56; }')
    svg_parts.append('    .dot-yellow { fill: #ffbd2e; }')
    svg_parts.append('    .dot-green { fill: #27c93f; }')
    svg_parts.append('    .text-title { font-family: "Courier New", Courier, monospace; font-size: 12px; fill: #8b949e; }')
    svg_parts.append('    .glow { filter: drop-shadow(0 0 3px rgba(88, 166, 255, 0.4)); }')
    svg_parts.append('    .drawing-path {')
    svg_parts.append('      fill: none;')
    svg_parts.append('      stroke: #58a6ff;')
    svg_parts.append('      stroke-width: 1.2;')
    svg_parts.append('      stroke-linecap: round;')
    svg_parts.append('      stroke-linejoin: round;')
    svg_parts.append('      stroke-dasharray: 3000;')
    svg_parts.append('      stroke-dashoffset: 3000;')
    svg_parts.append('      animation: draw 3.5s cubic-bezier(0.25, 1, 0.5, 1) forwards;')
    svg_parts.append('    }')
    svg_parts.append('    @keyframes draw { to { stroke-dashoffset: 0; } }')
    svg_parts.append('  </style>')

    # --- Terminal UI ---
    svg_parts.append('  <rect width="100%" height="100%" rx="8" class="terminal-bg"/>')
    svg_parts.append('  <rect width="100%" height="30" rx="8" class="terminal-header"/>')
    svg_parts.append('  <circle cx="20" cy="15" r="6" class="dot-red"/>')
    svg_parts.append('  <circle cx="40" cy="15" r="6" class="dot-yellow"/>')
    svg_parts.append('  <circle cx="60" cy="15" r="6" class="dot-green"/>')
    svg_parts.append(f'  <text x="{term_w // 2}" y="19" class="text-title" text-anchor="middle">mohit@portfolio: ~ (vector-portrait)</text>')

    # --- Group for Paths ---
    svg_parts.append('  <g transform="translate(30, 50)" class="glow">')

    # 6. Har line ko SVG Path me convert karo
    for contour in contours:
        # Chhoti noise lines ko ignore karo
        if len(contour) > 4:
            path_data = "M " + " L ".join([f"{pt[0][0]},{pt[0][1]}" for pt in contour])
            svg_parts.append(f'    <path class="drawing-path" d="{path_data}" />')

    svg_parts.append('  </g>')
    svg_parts.append('</svg>')

    # Variable name issue fixed here 👇
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts))
    print(f"Success! Vector animated SVG generated at: {output_path}")

if __name__ == "__main__":
    generate_vector_svg("assets/profile.jpg", "assets/portrait_animated.svg")