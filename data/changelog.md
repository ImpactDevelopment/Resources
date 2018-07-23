# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) ~~and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).~~

## 4.4
### Fixed
- Fixed uncommon crash caused by GuiTextContainingLinks

## 4.3

### Added
- Button to open Click GUI from the Impact menu
- Ability to open chat while Click GUI is open
- "Main Menu" entry in Click GUI's Render section
  - Toggle using Impact's custom main menu
  - Toggle using Impact's replacement menu wallpaper
- Clickable links and line-wrapping in the MOTD header
- Colored sign text exploit
- Movement speed widget in the HUD
- Customization for suffixes in module list
- Pause option for Click GUI
- Opacity option for Click GUI
- Option to blur background of Click GUI frames
- Option to save logout positions in Log Position
- Rank option for Nametags to show team prefix and suffix
- Catch Delay option for AutoFish (might help with fussy servers)
- Jump option for the strafe speed mode
- Skylight option for light module to prevent skylight lag machines from working
- Totem counter option to Auto Totem
- Auto Break option for nuker
- Origin option for nuker to choose the break origin
- Target option for nuker to choose the blocks targetted
- Filter option for nuker to use the nuker ID list
- Crosshair prioritization mode for Kill Aura
- Swing option for Scaffold
- Shulker Tooltip option for Inventory to change the tooltip length
- Shulker Coallate option for Inventory to group item stacks together in the tooltip
- Option to only shoot when scoped for Minestrike module
- Option to ignore attacking friends for Minestrike module
- Support for offhand in Scaffold
  - Added option to prioritize offhand which is on by default
- Swing option for breaker to show breaking on the client side
- "Reconnect" command that quickly disconnects and reconnects the user from their current server

### Changed
- Use player's team color in Nametags
- AutoFish options should be clearer now
- AutoFish AutoCast is now off by default
- Automatically focus the username field when creating an Alt
- Alts are now stored in a json format to enable future fanciness
- Significantly improve scaffold in all movement directions
- Improve jitter on Auto Clicker
- Added mineplex support for team check
- Freecam is now always in first person view
- Moved Inventory to the Misc category, updated its description and made move an option
- Click GUI menus now stay on the screen at all times
- Click GUI menus are now easier to navigate
  - Clicking the arrows next to modules will open the submen
  - Double clicking the menus will open them (like right click)
  - Move menus around by dragging anywhere within them (hold `Ctrl` or use middle mouse)
- Click GUI's keybind widget now has a tooltip and is easier to use
  - Left click to modify the bind
  - Clicking again (or pressing `Esc` will cancel)
  - Right click to delete/reset the bind
- `.set` command can now use option id as an alternative to name
- Removed all server-side changes (should make singleplayer more stable)

### Removed
- Mode option for nuker

### Fixed
- Absorption not being shown by Nametags
- `.set` command not finding nested options
- Fixed incorrect angle calculations in combat modules
- Incorrect murderer detection on Hypixel's Murder Mystery
- Incorrect murderer detection on PlayMCM
- No Fall Bucket mode getting stuck on the collection stage
- Dolphin Jesus jumping while in GUIs, even when out of water
- Xray GUI arrows not displaying with a transparent background
- Not being able to toggle mods or open Click GUI after toggling fullscreen mode
- Click GUI not always being saved on shutdown
- Issues caused when disabling the Click GUI
- Click GUI not rendering closed menus correctly until they are re-closed
- drop command not targetting correct slots
- Chams affecting models in the alt manager
- Smooth aim targetting incorrect positions
- Friends GUI causing a crash
- Alt GUI having transparent background while in-game
- Some vertical spacing problems with the HUD
- Cycler boxes in Click GUI not properly encasing children
- Freecam causing weird behavior while riding entities
- ChestStealer not functioning as expected
- Forge and Optifine support ~~(probably)~~
- AntiAFK "jump" option not working when a GUI is open
- AutoTool not applying to Nuker
- Fixed Riding "Entity Speed" not applying to boats
- Fixed Scaffold not placing glass blocks
