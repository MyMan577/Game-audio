#!/usr/bin/env python3
"""
Obby Builder V8 - AI Level Generator
Generates detailed obstacle course levels based on game mechanics analysis.
Runs asynchronously via GitHub Actions.
"""

import json
import random
import math
from datetime import datetime

# ============================================================================
# GAME KNOWLEDGE BASE (Extracted from ObbyBuilderV8_with_audio.html)
# ============================================================================

BLOCK_TYPES = {
    # Basic Blocks
    'solid': {'color': '#6f7b9b', 'danger': False, 'skill': 'platforming'},
    'spike': {'color': '#f25f5c', 'danger': True, 'skill': 'timing'},
    'spring': {'color': '#7cdbff', 'danger': False, 'skill': 'momentum'},
    'mover': {'color': '#ffd166', 'danger': False, 'skill': 'timing'},
    'ice': {'color': '#9ad9ff', 'danger': False, 'skill': 'control'},
    'bouncer': {'color': '#9cff9a', 'danger': False, 'skill': 'aiming'},
    'goal': {'color': '#ffe66d', 'danger': False, 'skill': 'completion'},
    
    # Advanced Movement
    'angledSpring': {'color': '#ff9f43', 'danger': False, 'skill': 'trajectory'},
    'dashRefill': {'color': '#4ade80', 'danger': False, 'skill': 'resource'},
    'wind': {'color': '#a4b0be', 'danger': False, 'skill': 'resistance'},
    'crumble': {'color': '#8d6e63', 'danger': True, 'skill': 'speed'},
    'checkpoint': {'color': '#f1c40f', 'danger': False, 'skill': 'progress'},
    'teleport': {'color': '#e056fd', 'danger': False, 'skill': 'positioning'},
    
    # Puzzle Elements
    'key': {'color': '#ffd700', 'danger': False, 'skill': 'exploration'},
    'door1': {'color': '#cd7f32', 'danger': False, 'skill': 'key-management'},
    'door2': {'color': '#c0c0c0', 'danger': False, 'skill': 'key-management'},
    'door4': {'color': '#ffd700', 'danger': False, 'skill': 'key-management'},
    'laser': {'color': '#ff0044', 'danger': True, 'skill': 'timing'},
    'plate': {'color': '#555555', 'danger': False, 'skill': 'puzzle'},
    
    # Combat/Challenge
    'breakable': {'color': '#5d4037', 'danger': False, 'skill': 'combat'},
    'saw': {'color': '#c0c0c0', 'danger': True, 'skill': 'dodging'},
    'speedBoost': {'color': '#00e5ff', 'danger': False, 'skill': 'control'},
    'speedSlow': {'color': '#ff6b35', 'danger': False, 'skill': 'patience'},
    
    # Special Mechanics
    'sticky': {'color': '#a3e635', 'danger': False, 'skill': 'wall-cling'},
    'conveyor': {'color': '#f59e0b', 'danger': False, 'skill': 'counter-movement'},
    'conveyor_l': {'color': '#d97706', 'danger': False, 'skill': 'counter-movement'},
    'lava': {'color': '#ff4500', 'danger': True, 'skill': 'avoidance'},
    'trampoline': {'color': '#e879f9', 'danger': False, 'skill': 'vertical'},
    'phantom': {'color': '#7c3aed', 'danger': False, 'skill': 'patience'},
    'gravity': {'color': '#06b6d4', 'danger': False, 'skill': 'orientation'},
    'thorn': {'color': '#22c55e', 'danger': True, 'skill': 'approach'},
    'warp': {'color': '#f43f5e', 'danger': False, 'skill': 'teleportation'},
    'cloud': {'color': '#e2e8f0', 'danger': False, 'skill': 'landing'},
    'bumper': {'color': '#fb923c', 'danger': False, 'skill': 'deflection'},
    
    # Expert Blocks
    'mirror': {'color': '#a8d8ea', 'danger': False, 'skill': 'momentum-control'},
    'sand': {'color': '#d4a853', 'danger': False, 'skill': 'descent'},
    'magnet': {'color': '#e74c3c', 'danger': False, 'skill': 'attraction'},
    'portal_l': {'color': '#8e44ad', 'danger': False, 'skill': 'portal'},
    'portal_r': {'color': '#2980b9', 'danger': False, 'skill': 'portal'},
    'drillable': {'color': '#7f8c8d', 'danger': False, 'skill': 'persistence'},
    'zipline': {'color': '#f39c12', 'danger': False, 'skill': 'riding'},
    'pulse': {'color': '#16a085', 'danger': False, 'skill': 'rhythm'},
    'oily': {'color': '#2c3e50', 'danger': False, 'skill': 'slippery'},
    'frozen': {'color': '#74b9ff', 'danger': False, 'skill': 'timing'},
    'repulsor': {'color': '#6c5ce7', 'danger': False, 'skill': 'repulsion'},
    'mushroom': {'color': '#d63031', 'danger': False, 'skill': 'bounce'},
    'bridge': {'color': '#a0522d', 'danger': False, 'skill': 'resource-management'},
    'noclip': {'color': '#00b894', 'danger': False, 'skill': 'ghost'},
    
    # Chaos Blocks
    'roulette': {'color': '#c084fc', 'danger': True, 'skill': 'adaptability'},
    'faker': {'color': '#64748b', 'danger': True, 'skill': 'caution'},
    'inverter': {'color': '#f472b6', 'danger': False, 'skill': 'reverse-control'},
    'bomber': {'color': '#ef4444', 'danger': True, 'skill': 'quick-reaction'},
    'acidpit': {'color': '#84cc16', 'danger': True, 'skill': 'escape'},
    'blackhole': {'color': '#1e1b4b', 'danger': True, 'skill': 'avoidance'},
    'shrink': {'color': '#a78bfa', 'danger': False, 'skill': 'size-manipulation'},
    'cursed': {'color': '#78350f', 'danger': False, 'skill': 'restriction'},
    
    # Directional Blocks
    'half': {'color': '#94a3b8', 'danger': False, 'skill': 'precision'},
    'oneWayL': {'color': '#fb7185', 'danger': False, 'skill': 'directional'},
    'oneWayR': {'color': '#38bdf8', 'danger': False, 'skill': 'directional'},
    'oneWayD': {'color': '#4ade80', 'danger': False, 'skill': 'directional'},
}

ENEMY_TYPES = {
    # Basic Enemies
    'enemy_walker': {'hp': 2, 'difficulty': 1, 'behavior': 'chase'},
    'enemy_jumper': {'hp': 2, 'difficulty': 2, 'behavior': 'jump'},
    'enemy_flyer': {'hp': 2, 'difficulty': 2, 'behavior': 'fly'},
    'enemy_shooter': {'hp': 3, 'difficulty': 3, 'behavior': 'ranged'},
    'enemy_charger': {'hp': 3, 'difficulty': 3, 'behavior': 'charge'},
    'enemy_shielder': {'hp': 4, 'difficulty': 4, 'behavior': 'defend'},
    'enemy_bouncer': {'hp': 2, 'difficulty': 2, 'behavior': 'bounce'},
    'enemy_ghost': {'hp': 2, 'difficulty': 3, 'behavior': 'phase'},
    'enemy_bomber': {'hp': 2, 'difficulty': 3, 'behavior': 'explode'},
    
    # Advanced Enemies
    'enemy_necromancer': {'hp': 6, 'difficulty': 5, 'behavior': 'summon'},
    'enemy_titan': {'hp': 14, 'difficulty': 6, 'behavior': 'smash'},
    'enemy_vampire': {'hp': 5, 'difficulty': 4, 'behavior': 'dash'},
    'enemy_trickster': {'hp': 5, 'difficulty': 5, 'behavior': 'decoy'},
    'enemy_oracle': {'hp': 6, 'difficulty': 5, 'behavior': 'predict'},
    'enemy_berserker': {'hp': 8, 'difficulty': 5, 'behavior': 'enrage'},
    
    # Boss Enemies
    'enemy_brute': {'hp': 65, 'difficulty': 8, 'behavior': 'boss-slam'},
    'enemy_glacier': {'hp': 35, 'difficulty': 7, 'behavior': 'boss-freeze'},
    'enemy_tempest': {'hp': 30, 'difficulty': 7, 'behavior': 'boss-storm'},
    'enemy_serpent': {'hp': 45, 'difficulty': 8, 'behavior': 'boss-lunge'},
    'enemy_lich': {'hp': 38, 'difficulty': 8, 'behavior': 'boss-magic'},
    'enemy_dreadscorpion': {'hp': 120, 'difficulty': 9, 'behavior': 'boss-burrow'},
    'enemy_voidwalker': {'hp': 90, 'difficulty': 9, 'behavior': 'boss-blink'},
    'enemy_eye': {'hp': 110, 'difficulty': 9, 'behavior': 'boss-gaze'},
    'enemy_ember_drake': {'hp': 150, 'difficulty': 10, 'behavior': 'boss-breath'},
}

# ============================================================================
# LEVEL GENERATION ALGORITHMS
# ============================================================================

class LevelGenerator:
    def __init__(self, difficulty='medium', length='medium', theme='mixed'):
        self.difficulty = difficulty  # easy, medium, hard, expert
        self.length = length  # short, medium, long
        self.theme = theme  # mixed, platforming, puzzle, combat, chaos
        
        # Difficulty settings
        self.diff_settings = {
            'easy': {'danger_ratio': 0.15, 'enemy_freq': 0.3, 'complexity': 1},
            'medium': {'danger_ratio': 0.3, 'enemy_freq': 0.5, 'complexity': 2},
            'hard': {'danger_ratio': 0.45, 'enemy_freq': 0.7, 'complexity': 3},
            'expert': {'danger_ratio': 0.6, 'enemy_freq': 0.9, 'complexity': 4},
        }
        
        # Length settings (in screens)
        self.length_settings = {
            'short': {'screens': 3, 'width': 120},
            'medium': {'screens': 6, 'width': 240},
            'long': {'screens': 10, 'width': 400},
        }
        
        self.ds = self.diff_settings[difficulty]
        self.ls = self.length_settings[length]
        
    def generate(self):
        """Generate a complete level with blocks, enemies, and spawn/goal."""
        level_data = {
            'blocks': [],
            'enemies': [],
            'spawn': {'x': 2, 'y': 10},
            'goal': {'x': self.ls['width'] - 5, 'y': 10},
            'metadata': {
                'difficulty': self.difficulty,
                'length': self.length,
                'theme': self.theme,
                'generated_at': datetime.now().isoformat(),
                'generator_version': '1.0'
            }
        }
        
        # Generate terrain based on theme
        if self.theme == 'mixed':
            level_data = self._generate_mixed(level_data)
        elif self.theme == 'platforming':
            level_data = self._generate_platforming(level_data)
        elif self.theme == 'puzzle':
            level_data = self._generate_puzzle(level_data)
        elif self.theme == 'combat':
            level_data = self._generate_combat(level_data)
        elif self.theme == 'chaos':
            level_data = self._generate_chaos(level_data)
        
        # Add floor
        level_data = self._add_floor(level_data)
        
        return level_data
    
    def _generate_mixed(self, level_data):
        """Generate a balanced mix of all elements."""
        sections = ['platforming', 'puzzle', 'combat', 'platforming', 'combat', 'puzzle']
        section_width = self.ls['width'] // len(sections)
        
        for i, section_type in enumerate(sections):
            start_x = 2 + (i * section_width)
            end_x = start_x + section_width - 10
            
            if section_type == 'platforming':
                level_data = self._section_platforming(level_data, start_x, end_x)
            elif section_type == 'puzzle':
                level_data = self._section_puzzle(level_data, start_x, end_x)
            elif section_type == 'combat':
                level_data = self._section_combat(level_data, start_x, end_x)
        
        return level_data
    
    def _generate_platforming(self, level_data):
        """Focus on jumping and movement challenges."""
        return self._section_platforming(level_data, 2, self.ls['width'] - 5)
    
    def _generate_puzzle(self, level_data):
        """Focus on keys, switches, and logic."""
        return self._section_puzzle(level_data, 2, self.ls['width'] - 5)
    
    def _generate_combat(self, level_data):
        """Focus on enemy encounters."""
        return self._section_combat(level_data, 2, self.ls['width'] - 5)
    
    def _generate_chaos(self, level_data):
        """Chaotic mix with roulette, blackholes, and unpredictable elements."""
        return self._section_chaos(level_data, 2, self.ls['width'] - 5)
    
    def _section_platforming(self, level_data, start_x, end_x):
        """Generate platforming section."""
        current_y = 10
        x = start_x
        
        while x < end_x:
            # Choose block type based on difficulty
            available_blocks = self._get_platforming_blocks()
            
            # Create platform patterns
            pattern = random.choice(['stairs', 'gaps', 'varied', 'moving'])
            
            if pattern == 'stairs':
                # Staircase pattern
                for i in range(4):
                    block_type = random.choice(available_blocks)
                    level_data['blocks'].append({
                        'type': block_type,
                        'x': x + i,
                        'y': current_y - i,
                        'w': 1,
                        'h': 1
                    })
                x += 4
                current_y -= 4
                
            elif pattern == 'gaps':
                # Gap jumps with platforms
                gap_size = random.randint(1, 2 + self.ds['complexity'])
                plat_width = random.randint(2, 4)
                
                # Gap
                x += gap_size
                
                # Platform
                for i in range(plat_width):
                    block_type = random.choice(available_blocks)
                    level_data['blocks'].append({
                        'type': block_type,
                        'x': x + i,
                        'y': current_y,
                        'w': 1,
                        'h': 1
                    })
                x += plat_width
                
            elif pattern == 'varied':
                # Varied height platforms
                height_change = random.randint(-2, 2)
                current_y = max(2, min(18, current_y + height_change))
                
                plat_width = random.randint(2, 5)
                for i in range(plat_width):
                    block_type = random.choice(available_blocks)
                    level_data['blocks'].append({
                        'type': block_type,
                        'x': x + i,
                        'y': current_y,
                        'w': 1,
                        'h': 1
                    })
                x += plat_width
                
            elif pattern == 'moving':
                # Moving blocks (if difficulty allows)
                if self.ds['complexity'] >= 2:
                    for i in range(3):
                        level_data['blocks'].append({
                            'type': 'mover',
                            'x': x + (i * 3),
                            'y': current_y,
                            'w': 1,
                            'h': 1,
                            'moveX': 2,
                            'moveY': 0
                        })
                    x += 9
        
        return level_data
    
    def _section_puzzle(self, level_data, start_x, end_x):
        """Generate puzzle section with keys and doors."""
        x = start_x
        current_y = 10
        
        # Place key
        key_x = x + random.randint(3, 8)
        level_data['blocks'].append({
            'type': 'key',
            'x': key_x,
            'y': current_y - 2,
            'w': 0.6,
            'h': 0.6
        })
        
        # Path to key with obstacles
        for i in range(key_x - x):
            if random.random() < 0.3:
                level_data['blocks'].append({
                    'type': random.choice(['spike', 'ice', 'phantom']),
                    'x': x + i,
                    'y': current_y,
                    'w': 1,
                    'h': 1
                })
        
        x = key_x + 5
        
        # Place door
        level_data['blocks'].append({
            'type': 'door1',
            'x': x,
            'y': current_y - 1,
            'w': 1,
            'h': 2
        })
        
        # Behind door: more puzzles
        x += 3
        if self.ds['complexity'] >= 2:
            # Laser and plate puzzle
            level_data['blocks'].append({
                'type': 'plate',
                'x': x,
                'y': current_y,
                'w': 1,
                'h': 1
            })
            level_data['blocks'].append({
                'type': 'laser',
                'x': x + 3,
                'y': current_y - 2,
                'w': 1,
                'h': 3,
                'triggeredBy': 'plate'
            })
        
        return level_data
    
    def _section_combat(self, level_data, start_x, end_x):
        """Generate combat section with enemies."""
        x = start_x
        current_y = 10
        
        # Create combat arenas
        arena_width = 15
        num_arenas = (end_x - start_x) // arena_width
        
        for arena_idx in range(num_arenas):
            arena_x = start_x + (arena_idx * arena_width)
            
            # Arena floor
            for i in range(arena_width - 2):
                level_data['blocks'].append({
                    'type': 'solid',
                    'x': arena_x + i,
                    'y': current_y,
                    'w': 1,
                    'h': 1
                })
            
            # Spawn enemies based on difficulty
            num_enemies = int(2 * self.ds['enemy_freq']) + random.randint(0, 2)
            enemies_to_spawn = self._get_enemy_pool()
            
            for i in range(num_enemies):
                if enemies_to_spawn:
                    enemy_type = random.choice(enemies_to_spawn)
                    enemy_x = arena_x + random.randint(3, arena_width - 4)
                    enemy_y = current_y - 1
                    
                    level_data['enemies'].append({
                        'type': enemy_type,
                        'x': enemy_x,
                        'y': enemy_y
                    })
            
            # Add some combat-friendly blocks
            if random.random() < 0.5:
                level_data['blocks'].append({
                    'type': 'breakable',
                    'x': arena_x + random.randint(2, arena_width - 3),
                    'y': current_y - 3,
                    'w': 1,
                    'h': 1
                })
        
        return level_data
    
    def _section_chaos(self, level_data, start_x, end_x):
        """Generate chaotic section with unpredictable elements."""
        x = start_x
        current_y = 10
        
        chaos_blocks = ['roulette', 'blackhole', 'bomber', 'acidpit', 'inverter', 'faker']
        
        while x < end_x:
            # Random chaos element
            block_type = random.choice(chaos_blocks)
            
            if block_type == 'roulette':
                # Line of roulette blocks
                for i in range(random.randint(2, 4)):
                    level_data['blocks'].append({
                        'type': 'roulette',
                        'x': x + i,
                        'y': current_y,
                        'w': 1,
                        'h': 1
                    })
                x += 4
                
            elif block_type == 'blackhole':
                level_data['blocks'].append({
                    'type': 'blackhole',
                    'x': x,
                    'y': current_y - 2,
                    'w': 1,
                    'h': 1
                })
                # Surround with safe blocks
                level_data['blocks'].append({
                    'type': 'solid',
                    'x': x - 2,
                    'y': current_y,
                    'w': 1,
                    'h': 1
                })
                level_data['blocks'].append({
                    'type': 'solid',
                    'x': x + 2,
                    'y': current_y,
                    'w': 1,
                    'h': 1
                })
                x += 5
                
            elif block_type == 'bomber':
                # Bomber gauntlet
                for i in range(3):
                    level_data['blocks'].append({
                        'type': 'bomber',
                        'x': x + (i * 2),
                        'y': current_y,
                        'w': 1,
                        'h': 1
                    })
                x += 6
        
        return level_data
    
    def _add_floor(self, level_data):
        """Add floor beneath all blocks."""
        floor_y = 20
        
        for x in range(0, self.ls['width'], 2):
            # Leave some gaps for challenge
            if random.random() > 0.1:
                level_data['blocks'].append({
                    'type': 'solid',
                    'x': x,
                    'y': floor_y,
                    'w': 2,
                    'h': 2
                })
        
        return level_data
    
    def _get_platforming_blocks(self):
        """Get appropriate blocks for platforming based on difficulty."""
        basic = ['solid', 'spring', 'bouncer', 'ice']
        intermediate = basic + ['mover', 'crumble', 'phantom', 'cloud']
        advanced = intermediate + ['gravity', 'trampoline', 'conveyor', 'magnet']
        expert = advanced + ['portal_l', 'portal_r', 'shrink', 'noclip']
        
        if self.ds['complexity'] == 1:
            return basic
        elif self.ds['complexity'] == 2:
            return intermediate
        elif self.ds['complexity'] == 3:
            return advanced
        else:
            return expert
    
    def _get_enemy_pool(self):
        """Get appropriate enemies based on difficulty."""
        basic = ['enemy_walker', 'enemy_jumper']
        intermediate = basic + ['enemy_flyer', 'enemy_charger', 'enemy_bouncer']
        advanced = intermediate + ['enemy_shooter', 'enemy_ghost', 'enemy_bomber']
        expert = advanced + ['enemy_necromancer', 'enemy_vampire', 'enemy_trickster']
        
        if self.ds['complexity'] == 1:
            return basic
        elif self.ds['complexity'] == 2:
            return intermediate
        elif self.ds['complexity'] == 3:
            return advanced
        else:
            return expert


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Generate level and output as JSON."""
    import sys
    
    # Parse arguments (from GitHub Actions)
    difficulty = sys.argv[1] if len(sys.argv) > 1 else 'medium'
    length = sys.argv[2] if len(sys.argv) > 2 else 'medium'
    theme = sys.argv[3] if len(sys.argv) > 3 else 'mixed'
    
    print(f"Generating level: difficulty={difficulty}, length={length}, theme={theme}")
    
    # Generate level
    generator = LevelGenerator(difficulty, length, theme)
    level_data = generator.generate()
    
    # Output JSON
    output_json = json.dumps(level_data, indent=2)
    
    # Write to file
    output_file = 'generated_level.json'
    with open(output_file, 'w') as f:
        f.write(output_json)
    
    print(f"Level generated successfully! Saved to {output_file}")
    print(f"Blocks: {len(level_data['blocks'])}, Enemies: {len(level_data['enemies'])}")
    
    return output_json


if __name__ == '__main__':
    main()
