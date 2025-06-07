# 🎨 My Hyprland Rice Dotfiles

Welcome to my dotfiles for my Hyprland Gruvbox Rice! This setup is designed to be minimalistic, functional, and aesthetically pleasing, with a focus on productivity.  
**Note: This configuration is still under development.**

---

## 🖥️ Preview

![Preview](https://github.com/user-attachments/assets/09e0a4f9-b2f6-4a6f-9388-0e51952864fa)

---

## 📦 Required Programs

Before using these dotfiles, ensure you have the following programs installed on your system:

- **Kitty** (or **Alacritty**)
- **Dunst** 
- **Elkowar Wacky Widgets**
- **Fastfetch** (or **Neofetch**) 
- **Hypridle**
- **Hyprland**
- **Hyprpaper**
- **Spicetify**
- **Vencord**
- **Waybar**
- **Wofi**

---

## 🔤 Fonts Used

- [JetBrains Mono Nerd Font](https://www.nerdfonts.com/font-downloads#jetbrainsmono)
- [Symbols Nerd Fonts](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/NerdFontsSymbolsOnly.zip)
- [Iosevka](https://typeof.net/Iosevka/)
- [FiraCode Nerd Font](https://www.nerdfonts.com/font-downloads#firacode)

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/dotfiles.git ~/dotfiles
   ```

2. **Install the required programs**  
   Use your preferred package manager (e.g., `pacman`, `apt`, `nix`, `paru`, etc.) to install the dependencies listed above.

3. **Copy the configuration files:**
   ```bash
   cp -r ~/dotfiles/.config/ ~/.config/
   ```

4. **Restart your system** or re-login to apply the changes.

---

## ⌨️ Keybinds

All keybinds use the **Super (Windows)** key as the main modifier.

### Application Shortcuts
| Keybind | Action |
|---------|--------|
| `Super + Return` | Open terminal (Kitty) |
| `Super + D` | Open application launcher (Wofi) |
| `Super + E` | Open file manager (Thunar) |
| `Super + Shift + F` | Open file manager |
| `Super + B` | Open browser (Zen Browser) |
| `Super + Print` | Take screenshot (selection) |

### Window Management
| Keybind | Action |
|---------|--------|
| `Super + Q` | Kill active window |
| `Super + M` | Exit Hyprland |
| `Super + V` | Toggle floating mode |
| `Super + P` | Toggle pseudotile (dwindle) |
| `Super + J` | Toggle split direction (dwindle) |

### Focus Movement
| Keybind | Action |
|---------|--------|
| `Super + ←` | Move focus left |
| `Super + →` | Move focus right |
| `Super + ↑` | Move focus up |
| `Super + ↓` | Move focus down |

### Workspace Navigation
| Keybind | Action |
|---------|--------|
| `Super + 1-9` | Switch to workspace 1-9 |
| `Super + 0` | Switch to workspace 10 |
| `Super + Scroll Up` | Previous workspace |
| `Super + Scroll Down` | Next workspace |

### Window-to-Workspace Movement
| Keybind | Action |
|---------|--------|
| `Super + Shift + 1-9` | Move window to workspace 1-9 |
| `Super + Shift + 0` | Move window to workspace 10 |

### Special Workspace (Scratchpad)
| Keybind | Action |
|---------|--------|
| `Super + S` | Toggle special workspace |
| `Super + Shift + S` | Move window to special workspace |

### Window Manipulation
| Keybind | Action |
|---------|--------|
| `Super + Left Click + Drag` | Move window |
| `Super + Right Click + Drag` | Resize window |

---

## 📝 Notes

- These dotfiles were tested on **Arch Linux** but should work on other distros with minor adjustments.
- The setup is designed for **Wayland**; some X11 applications may require `xwayland` wrappers.  
  **Warning:** You may need to set desktop rules for apps like Discord or Spotify to make them run natively on Wayland.
- I get my wallpapers from: [gruvbox-wallpapers.pages.dev](https://gruvbox-wallpapers.pages.dev/).

---

## 📸 Gallery

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/09e0a4f9-b2f6-4a6f-9388-0e51952864fa" alt="Gallery 1" style="max-width: 45%; height: auto;">
  <img src="https://github.com/user-attachments/assets/10298e11-1dba-4596-b5e3-aabb5f42d44f" alt="Gallery 2" style="max-width: 45%; height: auto;">
  <img src="https://github.com/user-attachments/assets/4c7b5ea5-7e86-41b0-bd4a-e83becc39030" alt="Gallery 3" style="max-width: 45%; height: auto;">
  <img src="https://github.com/user-attachments/assets/af5f65f0-af08-4cfe-aba8-1f1c15bda0da" alt="Gallery 4" style="max-width: 45%; height: auto;">
</div>

*All themes and color schemes across the programs remain consistent. The bar keeps being the same as the one in the first printsc.*

---

## 📁 Repository Structure

```bash
.config/
├── alacritty/
├── kitty/
├── dunst/
├── fastfetch/
├── neofetch/
├── hypr/
├── hypridle/
├── hyprpaper/
├── spicetify/
├── vencord/
├── waybar/
└── wofi/
.bashrc                   # Bash startup file
LICENSE
README.md
midnight_gruvbox.theme.css  # Discord theme
```

---

## 🔐 License

These dotfiles are licensed under the MIT License.  
Feel free to use, modify, and distribute them—with or without credit.
