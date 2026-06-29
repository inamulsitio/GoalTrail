# === Stage 32: Add pagination helpers for long console output ===
# Project: GoalTrail
from rich.console import Console, Group
from rich.table import Table
from rich.text import Text
from typing import List, Any, Optional
import math

def paginate_output(lines: List[str], max_lines: int = 20) -> None:
    """Renders a list of lines with pagination controls for long console output."""
    if not lines:
        return
    
    total_pages = math.ceil(len(lines) / max_lines)
    current_page = 1
    
    while current_page <= total_pages:
        start_idx = (current_page - 1) * max_lines
        end_idx = min(start_idx + max_lines, len(lines))
        
        page_content = lines[start_idx:end_idx]
        
        # Create a header for the current page
        header_text = Text()
        header_text.append(f"Page {current_page}/{total_pages}\n", style="bold cyan")
        header_text.append("-" * 40, style="dim")
        
        console = Console()
        console.print(Group(header_text))
        
        # Print the content of this page
        for line in page_content:
            if isinstance(line, str):
                console.print(line)
            else:
                console.print(line)
        
        # Add navigation footer
        footer_text = Text()
        footer_text.append("\n[Navigation]\n", style="bold yellow")
        footer_text.append("Press 'q' to quit\n", style="yellow")
        if current_page > 1:
            footer_text.append(f"Press '{current_page - 2}' for previous page\n", style="green")
        if current_page < total_pages:
            footer_text.append(f"Press '{current_page + 1}' for next page\n", style="green")
        
        console.print(footer_text)
