// ── Obby Builder V8 - Constants & Configuration ────────────────────────────────

export const GRID = 40;
export const WORLD_W = 400;
export const WORLD_H = 72;
export const TILE = GRID;

// Color Palette for blocks and entities
export const PALETTE = {
  solid: '#6f7b9b', spike: '#f25f5c', spring: '#7cdbff',
  mover: '#ffd166', ice: '#9ad9ff', bouncer: '#9cff9a',
  goal: '#ffe66d', player: '#ffffff', dashCharge: '#ff6b9d',
  angledSpring: '#ff9f43', dashRefill: '#4ade80',
  wind: '#a4b0be', crumble: '#8d6e63', checkpoint: '#f1c40f', teleport: '#e056fd',
  key: '#ffd700', door1: '#cd7f32', door2: '#c0c0c0', door4: '#ffd700',
  laser: '#ff0044', plate: '#555555', plateActive: '#00ff00',
  breakable: '#5d4037', saw: '#c0c0c0',
  speedBoost: '#00e5ff', speedSlow: '#ff6b35',
  sticky: '#a3e635', conveyor: '#f59e0b', conveyor_l: '#d97706',
  lava: '#ff4500', trampoline: '#e879f9', phantom: '#7c3aed',
  gravity: '#06b6d4', thorn: '#22c55e', warp: '#f43f5e',
  cloud: '#e2e8f0', bumper: '#fb923c',
  mirror: '#a8d8ea', charSign: '#f5deb3', sand: '#d4a853',
  magnet: '#e74c3c', portal_l: '#8e44ad', portal_r: '#2980b9',
  drillable: '#7f8c8d', zipline: '#f39c12', pulse: '#16a085',
  coin: '#f1c40f', hpPickup: '#ff6b9d', oily: '#2c3e50',
  frozen: '#74b9ff', repulsor: '#6c5ce7', mushroom: '#d63031',
  bridge: '#a0522d', noclip: '#00b894',
  roulette: '#c084fc', faker: '#64748b', inverter: '#f472b6',
  bomber: '#ef4444', acidpit: '#84cc16', blackhole: '#1e1b4b',
  shrink: '#a78bfa', cursed: '#78350f',
  half: '#94a3b8', oneWayL: '#fb7185', oneWayR: '#38bdf8', oneWayD: '#4ade80',
  // Enemy colors
  enemy_walker: '#e11d48', enemy_jumper: '#16a34a', enemy_flyer: '#7c3aed',
  enemy_shooter: '#b45309', enemy_charger: '#9f1239', enemy_shielder: '#1d4ed8',
  enemy_bouncer: '#d97706', enemy_ghost: '#6d28d9', enemy_bomber: '#dc2626',
  enemy_boss: '#111827', enemy_necromancer: '#6d28d9', enemy_titan: '#374151',
  enemy_vampire: '#7f1d1d', enemy_trickster: '#d97706', enemy_oracle: '#0891b2',
  enemy_berserker: '#b91c1c', enemy_phantom_mk2: '#312e81'
};

// Character definitions
export const CHARACTERS = [
  { id: 'classic', name: 'Classic', color: '#ffffff' },
  { id: 'pyro', name: 'Pyro', color: '#ff6b35' },
  { id: 'frost', name: 'Frost', color: '#7cb9e8' },
  { id: 'shadow', name: 'Shadow', color: '#4a3b6e' },
  { id: 'phantom', name: 'Phantom', color: '#b19cd9' },
  { id: 'wisp', name: 'Wisp', color: '#ffd93d' },
  { id: 'nomad', name: 'Nomad', color: '#d4a853' },
  { id: 'wraith', name: 'Wraith', color: '#6b7c8a' },
  { id: 'jolt', name: 'Jolt', color: '#facc15' },
  { id: 'prophet', name: 'Prophet', color: '#8b5cf6' },
  { id: 'brute', name: 'Brute', color: '#dc2626' },
  { id: 'shade', name: 'Shade', color: '#312e81' },
  { id: 'herald', name: 'Herald', color: '#fbbf24' },
  { id: 'trickster', name: 'Trickster', color: '#d97706' },
  { id: 'dawnblade', name: 'Dawnblade', color: '#fb923c' },
  { id: 'abyssal', name: 'Abyssal', color: '#1e3a8a' },
  { id: 'riftwalker', name: 'Riftwalker', color: '#a855f7' },
  { id: 'ironclad', name: 'Ironclad', color: '#6b7280' },
  { id: 'stormcaller', name: 'Stormcaller', color: '#3b82f6' },
  { id: 'operator', name: 'Operator', color: '#10b981' },
  { id: 'swordsman', name: 'Swordsman', color: '#ef4444' }
];

// Enemy type definitions
export const ENEMY_TYPES = [
  'walker', 'jumper', 'flyer', 'shooter', 'charger', 'shielder',
  'bouncer', 'ghost', 'bomber', 'boss', 'necromancer', 'titan',
  'vampire', 'trickster', 'oracle', 'berserker', 'phantom_mk2'
];
