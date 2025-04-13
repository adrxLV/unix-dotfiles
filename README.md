# 🎨 My Hyprland Rice Dotfiles

Welcome to my dotfiles for my Hyprland Gruvbox Rice. This setup is designed to be "minimalistic", functional, and aesthetically pleasing focusing on productivity. **It is still in development**.

---

## 🖥️ Preview



![20250413_02h03m48s_grim](https://github.com/user-attachments/assets/e422f9e9-af22-4d11-bac8-fe0f38bc2085) ![20250413_02h07m48s_grim](https://github.com/user-attachments/assets/91f344c2-b9b0-43ae-a639-a2901e09ea5d)


---

## 📦 Required Programs

Before using these dotfiles, make sure to have these programs installed on your system:

- **Kitty** (or **Alacritty**) – A fast and highly configurable terminal.  
- **Dunst** – A simple and efficient notification manager.  
- **Elkowar Wacky Widgets** – widgets client to enhance aesthetics.  
- **Fastfetch** (or **Neofetch**) – A system information tool for the terminal. I personally prefer **Fastfetch**.  
- **Hypridle** – Idle manager for Hyprland.  
- **Hyprland** – The Wayland compositor that serves as the base for the setup.  
- **Hyprpaper** – Wallpaper setter for Hyprland environments.  
- **Spicetify** – Tool to customize Spotify.  
- **Vencord** – Tool to customize Discord.  
- **Waybar** – Status bar for Wayland.  
- **Wofi** – Lightweight application launcher for Wayland.

---

## ⚙️ Installation Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/dotfiles.git ~/dotfiles
```

2. **Install the required programs listed above.**  
   (You can use your preferred package manager, such as `pacman`, `apt`, `nix`, `paru`, etc.)

3. **Copy the files to the appropriate location:**

```bash
cp -r ~/dotfiles/* ~/.config/
```

4. **Restart your system.**

---

## 📝 Notes

- This setup has been tested on **Arch Linux** (it should work on others with slight adjustments).
- I use **Wayland**, so some X11 programs may not work properly without wrappers like `xwayland`. **WARNING**: u might need to add desktop rules to make progrmas as discord or spotify run in native wayland.

---

## 📸 Gallery

<div style="display: flex; flex-wrap: wrap; gap: 10px;"> <img src="https://github.com/user-attachments/assets/8b460b98-7231-4b1d-8c97-208a48498eed" alt="Gallery 1" style="max-width: 45%; height: auto;"> <img src="https://github.com/user-attachments/assets/10298e11-1dba-4596-b5e3-aabb5f42d44f" alt="Gallery 2" style="max-width: 45%; height: auto;"> <img src="https://github.com/user-attachments/assets/4c7b5ea5-7e86-41b0-bd4a-e83becc39030" alt="Gallery 3" style="max-width: 45%; height: auto;"> <img src="https://github.com/user-attachments/assets/af5f65f0-af08-4cfe-aba8-1f1c15bda0da" alt="Gallery 4" style="max-width: 45%; height: auto;"> </div>

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
```

---

## 💬 Feedback

If you'd like to suggest improvements or just have a chat about customizations, feel free to send a message or open an issue!

---

## 🔐 License

These dotfiles are licensed under the MIT License. Feel free to use, modify, and distribute as you like — with or without credit.
