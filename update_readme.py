import datetime
import pytz

def update_readme():
    # Set IST timezone
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.datetime.now(ist)
    
    # Format the date and time
    weekday = now.strftime('%A')
    date = now.strftime('%d %B %Y')
    time = now.strftime('%I:%M:%S %p')
    
    # Create the formatted timestamp entry
    timestamp_entry = f"Weekday : {weekday:<10} | Date : {date:<20} | Time : {time} IST"
    
    # Read the README file
    try:
        with open('README.md', 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print("README.md not found. Creating new file...")
        content = "# Project README\n\n"
    
    # Check if the Last Updated section exists
    section_marker = "## 📅 Last Updated"
    
    if section_marker in content:
        # Find the section and append the new timestamp
        lines = content.split('\n')
        updated_lines = []
        found_section = False
        
        for i, line in enumerate(lines):
            updated_lines.append(line)
            if line.strip() == section_marker and not found_section:
                found_section = True
                # Add empty line if not present
                if i + 1 < len(lines) and lines[i + 1].strip() != '':
                    updated_lines.append('')
                # Skip to after the existing section header
                continue
        
        # Append the new timestamp
        if found_section:
            # Find where to insert (after the section header and empty line)
            insert_index = updated_lines.index(section_marker) + 1
            if insert_index < len(updated_lines) and updated_lines[insert_index].strip() == '':
                insert_index += 1
            updated_lines.insert(insert_index, f"- {timestamp_entry}")
        
        updated_content = '\n'.join(updated_lines)
    else:
        # Create new section at the end
        section_text = f"\n\n{section_marker}\n\n- {timestamp_entry}\n"
        updated_content = content.rstrip() + section_text
    
    # Write back to README
    with open('README.md', 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"✅ README.md updated successfully!")
    print(f"   Added: {timestamp_entry}")

if __name__ == "__main__":
    update_readme()