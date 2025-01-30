import os

def print_directory_structure(path='.', exclude_dirs=['.venv', '.git', '.idea', '__pycache__']):
    for root, dirs, files in os.walk(path):
        # Zorg ervoor dat we de .venv en .git mappen niet opnemen
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        # Bereken de indents op basis van de diepte van de directory
        level = root.replace(path, '').count(os.sep)
        indent = '│   ' * level  # Gebruik "│" om een duidelijke hiërarchie weer te geven
        print(f"{indent}├── {os.path.basename(root)}/")  # Print de mapnaam

        # Print de bestanden in de huidige directory
        subindent = '│   ' * (level + 1)
        for f in files:
            print(f"{subindent}├── {f}")  # Toon bestand met bijpassende indent

# Verander de path naar jouw projectmap als je wilt
print_directory_structure()
