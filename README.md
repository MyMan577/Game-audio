# 🎮 Obby Builder V8 - Ultimate Platformer Level Creator

**A feature-rich, browser-based obby (platformer) level builder and player with extensive customization options.**

![Version](https://img.shields.io/badge/version-8.0-blue)
![Characters](https://img.shields.io/badge/characters-20+-green)
![Enemies](https://img.shields.io/badge/enemies-35+-red)
![Blocks](https://img.shields.io/badge/block%20types-50+-orange)

---

## 🌟 Key Features

### 🎭 20+ Unique Characters
Each with distinct abilities and playstyles:
- **Default** - Balanced stats
- **Speedster** - High movement speed
- **Jumper** - Enhanced jump height
- **Wall Jumper** - Can wall jump indefinitely
- **Double Jumper** - Mid-air double jump
- **Dash Master** - Quick dash ability
- **Grapple Knight** - Grapple hook mobility
- **Heavy** - High HP, slow movement
- **Ninja** - Wall jump + slash attack
- **Tank** - Maximum durability
- **Ghost** - Phase through obstacles
- **Archer** - Ranged attacks
- **Mage** - Magic projectiles
- **Berserker** - Rage mode combat
- **Parkour Master** - Enhanced movement combo
- **Shadow** - Stealth abilities
- **Phoenix** - Revive on death
- **Time Bender** - Slow motion ability
- **Cosmic** - Special cosmic powers
- **Shell Knight** - Defensive shell ability
- And more!

### 👾 35+ Enemy Types
From basic foes to complex bosses:
- **Basic Enemies**: Walker, Jumper, Flyer, Shooter, Charger
- **Special Enemies**: Shielder, Bouncer, Ghost, Bomber
- **Elite Enemies**: Necromancer, Titan, Vampire, Trickster, Oracle, Berserker
- **Bosses**: Boss, Phantom MK2, Brute, Glacier, Tidecaller
- **Advanced**: Lich, Webspinner, Golem, Pyromancer, Warlord
- **Legendary**: Dreadscorpion, Voidwalker, Eye of Malice, Ember Drake
- **Special**: Patrol variants (safe/hurt/kill), Training Dummy, Tempest, Serpent

### 🧱 50+ Block Types
Complete building toolkit:
- **Solids**: Stone, Grass, Dirt, Sand, Snow, Ice, Wood, Brick, Metal, Glass
- **Hazards**: Lava, Water, Spike, Crusher, Sawblade, Laser
- **Interactive**: Checkpoint, Finish Line, Bounce Pad, Speed Boost, Jump Boost
- **Technical**: Mover (horizontal/vertical/circular), Conveyor, Portal
- **Special**: Coin Block, Cosmic Coin, Invisible Block, One-Way Platform
- **Dynamic**: Disappearing Block, Moving Platform, Rotating Block
- **Environmental**: Cloud, Chain, Rope, Vine, Ladder
- **Ghost Zone**: Pass-through area for secrets

### 🎯 Advanced Gameplay Systems

#### Ghost Replay System 👻
- Record your best runs automatically
- Watch ghost replays of previous attempts after death
- Toggle recording on/off in build mode
- Clear saved ghosts anytime
- Perfect for learning difficult sections

#### Achievement & Milestone System 🏆
Track your progress with comprehensive milestones:
- Total jumps, wall jumps, dashes
- Enemies defeated by type
- Levels completed
- Time played
- Coins collected
- Deaths (and causes)
- Building statistics
- Character-specific achievements

#### Mobile Touch Controls 📱
Full mobile support with:
- Virtual directional buttons (left/right)
- Jump button with multi-touch support
- Action buttons (dash, grapple, slash, crouch, double jump)
- Responsive touch controls optimized for all screen sizes
- Auto-detects mobile devices
- Desktop mode hides touch controls automatically

#### Level Export/Import 📤📥
Share your creations easily:
- Export levels to JSON format
- Import levels from files or text
- Share level codes with friends
- Full level data preservation
- Compatible across sessions

#### Comprehensive Save System 💾
- Auto-save progress to localStorage
- Character unlocks and upgrades
- Coin collection (regular + cosmic)
- Achievement tracking
- Custom character configurations
- Build mode creations
- Settings and preferences

### 🎵 Audio System
Immersive sound experience:
- Background music for different game modes
- Sound effects for actions (jump, dash, attack, etc.)
- Enemy sound effects
- Environmental audio
- Volume controls
- Multiple audio tracks included

### 🛠️ Build Mode Editor
Powerful level creation tools:
- Grid-based placement system
- Camera pan/zoom controls
- Block selection palette
- Enemy placement tools
- Property editing for blocks/enemies
- Play test directly in editor
- Undo/redo functionality
- Layer management
- Size adjustment tools

---

## 🎮 Controls

### Desktop (Keyboard + Mouse)
| Action | Key(s) |
|--------|--------|
| Move Left/Right | `A` / `D` or Arrow Keys |
| Jump | `Space` or `W` or `↑` |
| Double Jump | `Space` (mid-air, if unlocked) |
| Wall Jump | Jump while touching wall |
| Dash | `Shift` or `F` |
| Grapple Hook | `G` or Right Click |
| Slash Attack | `J` or `K` |
| Shoot Projectile | `L` or Left Click |
| Crouch | `S` or `↓` |
| Pause Menu | `Esc` |
| Build Mode | `B` (in menu) |
| Delete Block | `Delete` (build mode) |
| Copy Block | `C` (build mode) |
| Paste Block | `V` (build mode) |

### Mobile (Touch)
- **Left/Right Buttons**: Character movement
- **Jump Button**: Jump / Double Jump / Wall Jump
- **Action Bar**: Dash, Grapple, Slash, Shoot, Crouch (context-sensitive)
- **Swipe Gestures**: Camera control in build mode
- **Tap**: Select/place blocks in build mode

---

## 🚀 Getting Started

### Playing Levels
1. Open `ObbyBuilderV8_with_audio.html` in a modern browser
2. Select your character from the roster
3. Choose a pre-made level or create your own
4. Reach the finish line while avoiding enemies and hazards
5. Collect coins and unlock new characters/upgrades

### Creating Levels
1. Enter **Build Mode** from the main menu
2. Select block types from the palette
3. Place blocks by clicking/tapping on the grid
4. Add enemies using the enemy selector
5. Configure properties (size, movement, etc.)
6. Set spawn point and finish line
7. **Play Test** your level instantly
8. **Save** or **Export** when finished

---

## 📁 File Structure

```
/workspace/
├── ObbyBuilderV8_with_audio.html    # Main game file (all-in-one)
├── README.md                         # This documentation
├── *.mp3, *.ogg, *.wav              # Audio assets
└── obby-builder-src/                 # Split source code (development)
    ├── index.html                    # Main HTML structure
    ├── css/                          # Stylesheets
    │   └── style.css
    ├── js/                           # JavaScript modules
    │   ├── constants.js              # Game constants
    │   └── game.js                   # Main game logic
    └── assets/                       # Asset references
```

---

## 🔧 Technical Details

### Engine
- **Rendering**: HTML5 Canvas 2D API
- **Physics**: Custom AABB collision detection
- **Input**: Keyboard, mouse, and touch event handlers
- **Storage**: localStorage for persistence
- **Audio**: Web Audio API + HTML5 Audio elements

### Performance
- Optimized render loop with delta time
- Object pooling for particles and projectiles
- Efficient collision broad-phase filtering
- Camera culling for off-screen objects
- Mobile-optimized touch controls

### Browser Compatibility
- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers (iOS Safari, Chrome Android)

---

## 🎯 Game Modes

### Campaign Mode
Progress through curated levels with increasing difficulty.

### Free Build
Create unlimited custom levels with all tools unlocked.

### Challenge Mode
Special levels with restrictions (no double jump, time limits, etc.).

### Practice Mode
Spawn anywhere, invincible, unlimited retries.

---

## 💰 Economy System

### Coins
- **Regular Coins**: Found in levels, used for basic upgrades
- **Cosmic Coins**: Rare currency, unlocks premium characters
- Earn by: completing levels, collecting coin blocks, achievements

### Upgrades
- Health increases
- Damage boosts
- Cooldown reductions
- Movement enhancements
- Character-specific abilities

### Cosmetics
- Alternate character skins
- Trail effects
- Victory animations
- Profile badges

---

## 🐛 Known Limitations

- Single-player only (no multiplayer/co-op)
- No procedural generation (all levels hand-crafted)
- No custom enemy behavior scripting
- No block animation editor
- No user audio upload (uses bundled assets)
- Level sharing requires manual file/code exchange

---

## 🛣️ Future Enhancement Ideas

Potential features for future versions:
- [ ] Multiplayer co-op mode
- [ ] Procedural level generation
- [ ] Custom enemy behavior creator
- [ ] Block animation timeline editor
- [ ] User audio upload support
- [ ] Advanced mover path editor
- [ ] Trigger/event scripting system
- [ ] Mini-map / level overview
- [ ] Screenshot/video capture
- [ ] Level rating and commenting system
- [ ] Cloud save synchronization

---

## 📄 License

This project is provided as-is for educational and entertainment purposes.

---

## 🙏 Credits

**Developer**: Obby Builder Community  
**Version**: 8.0  
**Built With**: HTML5, CSS3, Vanilla JavaScript  

Special thanks to the community for feedback, testing, and level creations!

---

## 📞 Support

For issues, suggestions, or level sharing:
- Check the in-game help menu
- Review the controls section above
- Ensure you're using a modern browser
- Clear localStorage if experiencing save issues

**Enjoy building and playing! 🎮✨**
