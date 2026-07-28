import os

def generate_terminal_svg(output_path):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 300" width="100%" height="100%">
  <style>
    .terminal-bg { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; }
    .terminal-header { fill: #161b22; border-bottom: 1px solid #30363d; }
    .dot-red { fill: #ff5f56; }
    .dot-yellow { fill: #ffbd2e; }
    .dot-green { fill: #27c93f; }
    .text-main { font-family: "Courier New", Courier, monospace; font-size: 15px; fill: #c9d1d9; }
    .text-cmd { fill: #58a6ff; font-weight: bold; }
    .text-prompt { fill: #7ee787; font-weight: bold; }
    .text-comment { fill: #8b949e; font-style: italic; }
    
    .line-1 { opacity: 0; animation: showLine 0.1s forwards 0.5s; }
    .line-2 { opacity: 0; animation: showLine 0.1s forwards 1.2s; }
    .line-3 { opacity: 0; animation: showLine 0.1s forwards 1.5s; }
    .line-4 { opacity: 0; animation: showLine 0.1s forwards 1.8s; }
    .line-5 { opacity: 0; animation: showLine 0.1s forwards 2.1s; }
    .line-6 { opacity: 0; animation: showLine 0.1s forwards 2.4s; }
    .cursor { opacity: 0; animation: blink 1s infinite 2.5s; font-weight: bold; fill: #c9d1d9; }

    @keyframes showLine { to { opacity: 1; } }
    @keyframes blink { 0%, 50% { opacity: 1; } 51%, 100% { opacity: 0; } }
  </style>

  <rect width="100%" height="100%" rx="8" class="terminal-bg"/>
  <rect width="100%" height="35" rx="8" class="terminal-header"/>
  
  <circle cx="25" cy="17" r="6" class="dot-red"/>
  <circle cx="45" cy="17" r="6" class="dot-yellow"/>
  <circle cx="65" cy="17" r="6" class="dot-green"/>
  <text x="410" y="23" font-family="'Courier New', Courier, monospace" font-size="13" fill="#8b949e" text-anchor="middle">mohit-sharma-001 bash</text>

  <g transform="translate(25, 75)">
    <g class="line-1">
      <text x="0" y="0" class="text-main"><tspan class="text-prompt">mohit-sharma-001:~$</tspan> ./fetch_profile.sh</text>
    </g>
    
    <!-- GitHub SVG fix: Changed > to &gt; -->
    <g class="line-2">
      <text x="0" y="35" class="text-main">&gt; IDENTITY     <tspan class="text-cmd">Mohit Sharma</tspan></text>
    </g>
    <g class="line-3">
      <text x="0" y="65" class="text-main">&gt; STATUS       <tspan class="text-cmd">Building Real-world Software</tspan></text>
    </g>
    <g class="line-4">
      <text x="0" y="95" class="text-main">&gt; EDUCATION    <tspan class="text-cmd">B.Tech CSE @ UTU, Dehradun</tspan></text>
    </g>
    <g class="line-5">
      <text x="0" y="125" class="text-main">&gt; CURRENT_GOAL <tspan class="text-cmd">Open Source Contributions &amp; Full Stack</tspan></text>
    </g>

    <g class="line-6">
      <text x="0" y="170" class="text-main"><tspan class="text-prompt">mohit-sharma-001:~$</tspan> <tspan class="cursor">_</tspan></text>
    </g>
  </g>
</svg>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Animated Terminal SVG generated at: {output_path}")

if __name__ == "__main__":
    generate_terminal_svg("assets/terminal.svg")